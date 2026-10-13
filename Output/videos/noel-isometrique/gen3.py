"""Version finale calée sur la prise unique ElevenLabs (voix-prise-unique/elevenlabs-paulk.mp3).

La prise n'est jamais accélérée ni ralentie : on insère seulement de courtes respirations
dans ses silences naturels (changements de scène), puis l'animation est recalée sur les mots.
Usage : python3 gen3.py (voix calée) puis python3 mix3.py, puis python3 gen3.py --build
"""
import json, pathlib, re, shutil, subprocess, sys, wave
import numpy as np
import gen

ICI = pathlib.Path(__file__).resolve().parent
PRISE = ICI / "voix-prise-unique" / "elevenlabs-paulk.mp3"
SR = 48000
V0 = 0.3  # début de la voix dans la vidéo
# (instant de coupe dans la prise, durée de respiration ajoutée) — coupes dans des silences
RESPIRATIONS = [(13.1, 1.4), (16.25, 0.6), (16.95, 0.2), (17.7, 0.35), (18.65, 1.3), (22.68, 0.5)]
FIN_VOIX = 27.59


def S(t):
    """Instant dans la vidéo d'un instant t de la prise."""
    return V0 + t + sum(g for c, g in RESPIRATIONS if c < t)


TOTAL = round(S(FIN_VOIX) + 1.1, 2)
# (temps d'origine de l'animation, mot de la prise sur lequel il tombe)
KP = [(0, 0)] + [(o, round(S(m), 3)) for o, m in [
    (0.35, 0.03),    # Vingt-quatre décembre
    (5.15, 4.47),    # Au pôle Nord
    (11.75, 11.03),  # Minuit pile
    (13.0, 12.18),   # décollage
    (16.45, 13.32),  # Son secret
    (18.4, 15.67),   # Tokyo
    (20.6, 16.32),   # Paris
    (21.8, 17.01),   # Cotonou
    (23.6, 17.76),   # New York
    (27.9, 19.01),   # cheminée
    (28.7, 19.91),   # sapin
    (29.5, 20.86),   # cadeau
    (33.35, 22.88),  # Joyeux Noël (titre final)
]] + [(37.0, TOTAL)]


def T(t):
    for (a, A), (b, B) in zip(KP, KP[1:]):
        if t <= b:
            return A + (t - a) * (B - A) / (b - a)
    return KP[-1][1]


def voix():
    brut = subprocess.run(["ffmpeg", "-v", "error", "-i", str(PRISE), "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"],
                          check=True, capture_output=True).stdout
    x = np.frombuffer(brut, dtype=np.int16).astype(np.float64) / 32768
    morceaux, prec = [np.zeros(int(V0 * SR))], 0
    for c, g in RESPIRATIONS:
        k = int(c * SR); m = x[prec:k].copy(); f = int(0.01 * SR)
        m[-f:] *= np.linspace(1, 0, f)
        if prec: m[:f] *= np.linspace(0, 1, f)
        morceaux += [m, np.zeros(int(g * SR))]; prec = k
    m = x[prec:].copy(); m[:int(0.01 * SR)] *= np.linspace(0, 1, int(0.01 * SR)); morceaux.append(m)
    y = np.concatenate(morceaux); y = np.pad(y, (0, max(0, int(TOTAL * SR) - len(y))))[: int(TOTAL * SR)]
    out = ICI / "audio" / "voix-calee-11labs.wav"; out.parent.mkdir(exist_ok=True)
    with wave.open(str(out), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(y, -1, 1) * 32767).astype(np.int16).tobytes())
    return out


def html():
    src = (ICI / "index.html").read_text(encoding="utf-8")
    remap = re.sub(r"const KP = \[.*?\];", lambda m: "const KP = " + json.dumps(KP) + ";", gen.REMAP_JS, flags=re.S)
    h = src.replace('      const tl = gsap.timeline({ paused: true });\n', remap)
    h = h.replace('window.__timelines["main"] = tl;\n      tl.seek(0);', 'window.__timelines["main"] = _tl;\n      _tl.seek(0);')
    gen.T, gen.TOTAL = T, TOTAL  # gen.clips() utilise ces deux globales
    h = gen.clips(h)
    audio = f'      <audio id="mix" src="mix.wav" data-start="0" data-duration="{TOTAL}" data-track-index="10"></audio>\n    </div>\n\n    <script>'
    return h.replace('    </div>\n\n    <script>', audio, 1)


def build(nom, h):
    d = ICI / nom; d.mkdir(exist_ok=True)
    for f in ["package.json", "hyperframes.json"]:
        shutil.copy(ICI / f, d / f)
    (d / "meta.json").write_text(json.dumps({"id": f"noel-{nom}", "name": f"noel-{nom}"}), encoding="utf-8")
    (d / "index.html").write_text(h, encoding="utf-8")
    shutil.copy(ICI / "audio" / "mix3.wav", d / "mix.wav")


if __name__ == "__main__":
    if "--build" in sys.argv:
        h = html(); build("build-h3", h); build("build-v3", gen.vertical(h))
        print("OK build-h3/ build-v3/, durée", TOTAL)
    else:
        print("voix :", voix(), "durée", TOTAL)
        for (a, A), (b, B) in zip(KP, KP[1:]):
            print(f"{a:6.2f}-{b:6.2f} -> {A:6.2f}-{B:6.2f}  vitesse x{(b - a) / (B - A):.2f}")
