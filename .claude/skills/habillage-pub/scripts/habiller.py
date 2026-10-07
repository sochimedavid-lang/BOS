#!/usr/bin/env python3
"""Habille une pub finie : phrase d'accroche animée en haut au début + carte de fin CTA.

Usage :
    python habiller.py habillage.json            # rendu complet -> "out" du fichier de config
    python habiller.py habillage.json --preview  # seulement 2 images de contrôle (accroche + carte), pas de vidéo

Le fichier de config (voir ../config.example.json) donne la vidéo source, le texte de l'accroche et le contenu
de la carte de fin. Les chemins sont relatifs au fichier de config.

Étapes : lit la vidéo (taille, fps, durée) -> extrait la dernière image -> génère deux compositions HyperFrames
(accroche transparente .mov, carte de fin .mp4) -> les rend -> un seul encodage ffmpeg : accroche posée sur le
début de la vidéo + carte de fin collée à la suite (son de la vidéo conservé, silence sous la carte).

Besoins : Node.js 22+, ffmpeg/ffprobe, et la CLI HyperFrames (npx hyperframes, téléchargée au premier lancement ;
le premier rendu télécharge aussi Chrome Headless : `npx hyperframes browser ensure`).
"""
import json
import shutil
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
TEMPLATES = SKILL / "templates"
FONTS = SKILL / "assets" / "fonts"


def run(cmd, **kw):
    print("  $", " ".join(str(c) for c in cmd))
    r = subprocess.run([str(c) for c in cmd], **kw)
    if r.returncode != 0:
        sys.exit(f"Échec de la commande ({r.returncode}) : {cmd[0]}")
    return r


def npx():
    exe = shutil.which("npx") or shutil.which("npx.cmd")
    if not exe:
        sys.exit("npx introuvable : installe Node.js 22+ (https://nodejs.org).")
    return exe


def probe(video):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "stream=codec_type,width,height,r_frame_rate:format=duration",
         "-of", "json", str(video)], capture_output=True, text=True, check=True).stdout
    data = json.loads(out)
    v = next(s for s in data["streams"] if s["codec_type"] == "video")
    has_audio = any(s["codec_type"] == "audio" for s in data["streams"])
    return {
        "w": int(v["width"]), "h": int(v["height"]), "fps": v["r_frame_rate"],
        "duration": float(data["format"]["duration"]), "has_audio": has_audio,
    }


def make_project(name, template, work, info, cfg, duration, extra_assets=()):
    proj = work / name
    if proj.exists():
        shutil.rmtree(proj)
    (proj / "assets" / "fonts").mkdir(parents=True)
    for f in FONTS.iterdir():
        if f.suffix.lower() in (".ttf", ".otf"):
            shutil.copy(f, proj / "assets" / "fonts" / f.name)
    for src, dst_name in extra_assets:
        shutil.copy(src, proj / "assets" / dst_name)
    page_cfg = dict(cfg)
    page_cfg["scale"] = info["w"] / 1080
    page_cfg["duration"] = duration
    html = (TEMPLATES / template).read_text(encoding="utf-8")
    html = (html.replace("__W__", str(info["w"])).replace("__H__", str(info["h"]))
            .replace("__DURATION__", f"{duration:.3f}")
            .replace("__CONFIG__", json.dumps(page_cfg, ensure_ascii=False)))
    (proj / "index.html").write_text(html, encoding="utf-8")
    (proj / "meta.json").write_text(json.dumps({"id": name, "name": name}), encoding="utf-8")
    return proj


def has_qsv():
    try:
        enc = subprocess.run(["ffmpeg", "-hide_banner", "-encoders"], capture_output=True, text=True).stdout
        if "h264_qsv" not in enc:
            return False
        test = subprocess.run(["ffmpeg", "-v", "error", "-f", "lavfi", "-i", "color=s=256x256:d=0.2", "-c:v", "h264_qsv",
                               "-f", "null", "-"], capture_output=True)
        return test.returncode == 0
    except OSError:
        return False


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    cfg_path = Path(sys.argv[1]).resolve()
    preview = "--preview" in sys.argv
    base = cfg_path.parent
    cfg = json.loads(cfg_path.read_text(encoding="utf-8"))

    video = (base / cfg["video"]).resolve()
    out = (base / cfg.get("out", Path(cfg["video"]).stem + "-habillee.mp4")).resolve()
    work = base / "habillage-build"
    work.mkdir(exist_ok=True)

    info = probe(video)
    ratio = info["w"] / info["h"]
    if abs(ratio - 9 / 16) > 0.02:
        print(f"Attention : la vidéo fait {info['w']}x{info['h']}, pas du 9:16 ; la mise en page est prévue pour du 9:16.")
    fps = str(Fraction(info["fps"]).limit_denominator(1001))
    print(f"Vidéo : {info['w']}x{info['h']}, {fps} i/s, {info['duration']:.2f} s, son : {'oui' if info['has_audio'] else 'non'}")

    hook = cfg.get("hook")
    end = cfg.get("endcard")
    hook_dur = None
    if hook:
        hook.setdefault("end", 3.0)
        hook_dur = min(hook["end"] + 0.1, info["duration"])
    end_dur = float(end.get("duration", 3.0)) if end else 0

    # Dernière image de la vidéo = fond flouté de la carte de fin
    last = work / "last-frame.jpg"
    run(["ffmpeg", "-v", "error", "-y", "-sseof", "-0.1", "-i", video, "-frames:v", "1", "-update", "1", "-q:v", "2", last])

    hf = npx()
    hook_mov = work / "accroche.mov"
    end_mp4 = work / "carte-fin.mp4"

    if hook:
        proj = make_project("accroche", "hook.html", work, info, cfg, hook_dur)
        if preview:
            run([hf, "hyperframes", "snapshot", proj, "--at", f"{min(hook_dur - 0.5, 1.5):.2f}"])
        else:
            run([hf, "hyperframes", "render", proj, "-o", hook_mov, "--format", "mov", "--fps", fps])
    if end:
        assets = [(last, "last-frame.jpg")]
        if end.get("product_image"):
            img = (base / end["product_image"]).resolve()
            assets.append((img, img.name))
            end = dict(end, product_image=img.name)
            cfg = dict(cfg, endcard=end)
        proj = make_project("carte-fin", "endcard.html", work, info, cfg, end_dur, assets)
        if preview:
            run([hf, "hyperframes", "snapshot", proj, "--at", f"{end_dur - 0.4:.2f}"])
        else:
            run([hf, "hyperframes", "render", proj, "-o", end_mp4, "--fps", fps])

    if preview:
        print(f"\nAperçus : {work / 'accroche' / 'snapshots'} et {work / 'carte-fin' / 'snapshots'}")
        return

    # Un seul encodage : accroche par-dessus le début, carte de fin collée à la suite
    inputs = ["-i", video]
    idx = 1
    hook_i = end_i = None
    if hook:
        inputs += ["-i", hook_mov]
        hook_i = idx
        idx += 1
    if end:
        inputs += ["-i", end_mp4]
        end_i = idx
        idx += 1
        inputs += ["-f", "lavfi", "-t", f"{end_dur:.3f}", "-i", "anullsrc=r=48000:cl=stereo"]
        sil_i = idx
        idx += 1
    if not info["has_audio"]:
        inputs += ["-f", "lavfi", "-t", f"{info['duration']:.3f}", "-i", "anullsrc=r=48000:cl=stereo"]
        main_a = f"{idx}:a"
        idx += 1
    else:
        main_a = "0:a"

    W, H = info["w"], info["h"]
    f = [f"[0:v]setsar=1,format=yuv420p[v0]"]
    vmain = "v0"
    if hook:
        f.append(f"[{hook_i}:v]setsar=1[hk]")
        f.append(f"[v0][hk]overlay=0:0:eof_action=pass:format=auto,format=yuv420p[v1]")
        vmain = "v1"
    f.append(f"[{main_a}]aresample=48000,aformat=channel_layouts=stereo[a0]")
    if end:
        f.append(f"[{end_i}:v]scale={W}:{H},setsar=1,fps={fps},format=yuv420p[ve]")
        f.append(f"[{sil_i}:a]aformat=channel_layouts=stereo[ae]")
        f.append(f"[{vmain}][a0][ve][ae]concat=n=2:v=1:a=1[vout][aout]")
    else:
        f.append(f"[{vmain}]null[vout]")
        f.append("[a0]anull[aout]")

    if has_qsv():
        venc = ["-c:v", "h264_qsv", "-global_quality", "18"]
    else:
        venc = ["-c:v", "libx264", "-crf", "17", "-preset", "medium", "-pix_fmt", "yuv420p"]
    run(["ffmpeg", "-v", "error", "-stats", "-y", *inputs, "-filter_complex", ";".join(f),
         "-map", "[vout]", "-map", "[aout]", *venc, "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out])

    total = info["duration"] + end_dur
    print(f"\nTerminé : {out}  ({total:.1f} s)")
    print("À vérifier : l'accroche ne couvre ni visage ni produit, la carte de fin est lisible, le son s'arrête proprement"
          f" à {info['duration']:.1f} s.")


if __name__ == "__main__":
    main()
