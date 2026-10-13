"""Crée un projet vidéo prêt à remplir : python3 new_project.py <dossier> [durée_s]
Copie le kit (kit/), le gabarit (index.html), les fichiers HyperFrames et un sound.json de départ."""
import json, pathlib, shutil, sys

SKILL = pathlib.Path(__file__).resolve().parents[1]
dst = pathlib.Path(sys.argv[1]); total = sys.argv[2] if len(sys.argv) > 2 else "20"
name = dst.name
for d in ["kit", "audio", "docs", "out", "refs"]:
    (dst / d).mkdir(parents=True, exist_ok=True)
for f in ["motion-kit.css", "motion-kit.js"]:
    shutil.copy(SKILL / "kit" / f, dst / "kit" / f)
if not (dst / "index.html").exists():
    (dst / "index.html").write_text((SKILL / "templates" / "index.html").read_text(encoding="utf-8").replace("__TOTAL__", total), encoding="utf-8")
(dst / "hyperframes.json").write_text(json.dumps({"$schema": "https://hyperframes.heygen.com/schema/hyperframes.json", "registry": "https://raw.githubusercontent.com/heygen-com/hyperframes/main/registry", "paths": {"blocks": "compositions", "components": "compositions/components", "assets": "assets"}, "media": {"autoProxy": True}}, indent=2))
(dst / "meta.json").write_text(json.dumps({"id": name, "name": name}, indent=2))
(dst / "package.json").write_text(json.dumps({"name": name, "private": True, "type": "module", "scripts": {"check": "npx --yes hyperframes@0.8.150 check", "render": "npx --yes hyperframes@0.8.150 render"}}, indent=2))
if not (dst / "sound.json").exists():
    (dst / "sound.json").write_text(json.dumps({"total": float(total), "voice": {"file": "audio/voix.mp3", "start": 0.3}, "music": {"preset": "pulse", "bpm": 120, "sections": [[0, float(total), "full"]]}, "sfx": [], "out": "audio/mix.wav"}, indent=2, ensure_ascii=False))
print("Projet prêt :", dst)
