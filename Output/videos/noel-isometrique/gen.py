"""Génère les versions avec voix off (horizontale et verticale) à partir de index.html.

- Les animations sont recalées sur la voix grâce à une table « ancien temps -> nouveau temps ».
- La voix off est assemblée à partir de voix/ligne-N.wav aux instants choisis ci-dessous.
Usage : python3 gen.py  (crée build-h/ et build-v/)
"""
import json, pathlib, re, shutil, subprocess

ICI = pathlib.Path(__file__).resolve().parent
SRC = (ICI / "index.html").read_text(encoding="utf-8")

# Début de chaque phrase dans la nouvelle vidéo (s)
VO = [0.3, 7.6, 17.8, 23.3, 36.6, 45.6]
TOTAL = 53.9
# Points de calage (temps d'origine, nouveau temps), synchronisés sur les mots de la voix
KP = [
    (0, 0), (0.3, 0.55), (0.9, 2.6), (2.4, 4.8), (3.7, 6.3), (5.0, 7.5),
    (11.4, 17.5), (12.4, 19.0), (13.0, 20.1), (16.4, 23.1),
    (18.4, 28.75), (20.6, 30.05), (21.8, 31.05), (23.6, 32.25), (25.4, 34.0),
    (27.6, 36.4), (27.9, 36.85), (28.7, 38.4), (29.5, 39.8), (30.9, 41.0), (31.4, 44.6),
    (33.35, 45.75), (33.9, 47.85), (34.8, 50.4), (37.0, TOTAL),
]


def T(t):
    for (a, A), (b, B) in zip(KP, KP[1:]):
        if t <= b:
            return A + (t - a) * (B - A) / (b - a)
    return KP[-1][1]


REMAP_JS = """
      const KP = %s;
      function T(t) { for (let i = 0; i < KP.length - 1; i++) { const [a, A] = KP[i], [b, B] = KP[i + 1]; if (t <= b) return A + (t - a) * (B - A) / (b - a); } return KP[KP.length - 1][1]; }
      function adj(v, p) { v = Object.assign({}, v); if (v.duration != null) { const d = T(p + v.duration) - T(p); const k = v.duration ? d / v.duration : 1; v.duration = d; if (typeof v.stagger === "number") v.stagger *= k; } return v; }
      const _tl = gsap.timeline({ paused: true });
      const tl = { to: (t, v, p) => _tl.to(t, adj(v, p), T(p)), fromTo: (t, f, v, p) => _tl.fromTo(t, f, adj(v, p), T(p)), set: (t, v, p) => _tl.set(t, v, T(p)) };
""" % json.dumps(KP)


def clips(html):
    def rep(m):
        s, d = float(m.group(1)), float(m.group(2))
        if s == 0 and d == 37:
            return f'data-start="0" data-duration="{TOTAL}"'
        ns, ne = T(s), T(s + d)
        return f'data-start="{ns:.3f}" data-duration="{ne - ns:.3f}"'
    return re.sub(r'data-start="([\d.]+)" data-duration="([\d.]+)"', rep, html)


def commun(html):
    html = html.replace('      const tl = gsap.timeline({ paused: true });\n', REMAP_JS)
    html = html.replace('window.__timelines["main"] = tl;\n      tl.seek(0);', 'window.__timelines["main"] = _tl;\n      _tl.seek(0);')
    html = clips(html)
    audio = f'      <audio id="vo" src="voix-off.wav" data-start="0" data-duration="{TOTAL}" data-track-index="10"></audio>\n    </div>\n    <script>'
    html = html.replace('    </div>\n\n    <script>', audio, 1)
    return html


def vertical(html):
    html = html.replace('data-resolution="landscape"', 'data-resolution="portrait"')
    html = html.replace('content="width=1920, height=1080"', 'content="width=1080, height=1920"')
    html = html.replace("html, body { width: 1920px; height: 1080px;", "html, body { width: 1080px; height: 1920px;")
    html = html.replace("#root { position: relative; width: 1920px; height: 1080px;", "#root { position: relative; width: 1080px; height: 1920px;")
    html = html.replace("svg.stage { position: absolute; inset: 0; width: 1920px; height: 1080px;", "svg.stage { position: absolute; inset: 0; width: 1080px; height: 1920px;")
    html = html.replace('data-width="1920" data-height="1080"', 'data-width="1080" data-height="1920"')
    # cadrage de chaque scène (largeur visible, centre vertical)
    def vb(w, cy):
        h = w * 16 / 9
        return f'viewBox="{-w / 2:.0f} {cy - h / 2:.0f} {w:.0f} {h:.0f}"'
    cad = {"cam12": (1350, 60), "cam3": (1750, -80), "cam4": (1450, 40), "cam5a": (1300, 0), "cam5b": (1350, -40), "cam6": (1250, 160)}
    for cam, (w, cy) in cad.items():
        html = re.sub(r'viewBox="-960 -540 1920 1080"(><g id="%s")' % cam, vb(w, cy) + r"\1", html)
    html = html.replace('id="skySvg" viewBox="-960 -540 1920 1080"', 'id="skySvg" viewBox="-540 -960 1080 1920"')
    html = html.replace('id="snowSvg" viewBox="-960 -540 1920 1080"', 'id="snowSvg" viewBox="-540 -960 1080 1920"')
    # ciel, lune, étoiles, neige
    for a, b in [("cx: 640, cy: -330", "cx: 340, cy: -850"), ("cx: 610, cy: -350", "cx: 310, cy: -870"), ("cx: 670, cy: -300", "cx: 370, cy: -820")]:
        html = html.replace(a, b)
    html = html.replace("cx: -960 + rnd() * 1920, cy: -540 + rnd() * 760", "cx: -540 + rnd() * 1080, cy: -960 + rnd() * 1250")
    html = html.replace("const wrapY = gsap.utils.wrap(-600, 600);", "const wrapY = gsap.utils.wrap(-1000, 1000);")
    html = html.replace("x = -960 + rnd() * 1920, y0 = -600 + rnd() * 1200", "x = -540 + rnd() * 1080, y0 = -1000 + rnd() * 2000")
    # textes
    css = """
      #t1k { top: 330px; } #t1a { top: 390px; font-size: 128px; } #t1b { top: 560px; font-size: 50px; padding: 0 60px; }
      #counter { left: 70px; top: 170px; } #counter .num { font-size: 84px; }
      #clock { top: 210px; } #t4 { left: 70px; top: 200px; } #t4 .h { font-size: 70px; }
      .word { font-size: 80px; } #w1 { left: 80px; top: 230px; } #w2 { left: 80px; top: 330px; } #w3 { left: 80px; top: 430px; }
      #endT { top: 290px; padding: 0 70px; } #endT .h { font-size: 140px; } #endT .s { font-size: 42px; }
      #grain { background: radial-gradient(1000px 1700px at 50% 45%, transparent 60%, rgba(3,5,15,.7) 100%) !important; }
      #tag { bottom: 170px; } #tag .pill { flex-direction: column; gap: 8px; padding: 20px 40px; border-radius: 30px; } #tag .sep { display: none; }
    </style>"""
    html = html.replace("    </style>", css, 1)
    return html


def projet(nom, html):
    d = ICI / nom
    d.mkdir(exist_ok=True)
    for f in ["package.json", "hyperframes.json"]:
        shutil.copy(ICI / f, d / f)
    (d / "meta.json").write_text(json.dumps({"id": f"noel-{nom}", "name": f"noel-{nom}"}), encoding="utf-8")
    (d / "index.html").write_text(html, encoding="utf-8")
    shutil.copy(ICI / "voix" / "voix-off-calee.wav", d / "voix-off.wav")


def voix():
    lignes = [ICI / "voix" / f"ligne-{i}.wav" for i in range(1, 7)]
    cmd = ["ffmpeg", "-y", "-v", "error"]
    for f in lignes:
        cmd += ["-i", str(f)]
    filt = [f"[{k}:a]adelay={int(s * 1000)}|{int(s * 1000)}[a{k}]" for k, s in enumerate(VO)]
    filt.append("".join(f"[a{k}]" for k in range(6)) + f"amix=inputs=6:normalize=0,loudnorm=I=-16:TP=-1.5:LRA=11,apad,atrim=0:{TOTAL}[o]")
    cmd += ["-filter_complex", ";".join(filt), "-map", "[o]", "-ar", "48000", "-ac", "2", str(ICI / "voix" / "voix-off-calee.wav")]
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    voix()
    base = commun(SRC)
    projet("build-h", base)
    projet("build-v", vertical(base))
    print("OK : build-h/ et build-v/ ; durée", TOTAL, "s")
