"""Bande-son générique d'une vidéo motion : musique synthétisée + bruitages + voix off, ducking, -14 LUFS.

Usage : python3 sound.py sound.json   (depuis le dossier du projet)
Dépendances : numpy, scipy, ffmpeg.

Exemple de sound.json :
{
  "total": 33.0,
  "voice": {"file": "audio/voix.mp3", "start": 0.4},
  "music": {"preset": "pulse", "bpm": 120, "root": 55.0,
            "sections": [[0, 8, "half"], [8, 30, "full"], [30, 33, "pad"]]},
  "sfx": [["whoosh", 1.2], ["pop", 2.0, -10, 0.3], ["typing", 0.1, -14, 0, 1.4]],
  "out": "audio/mix.wav"
}
- sections : "full" (kick + clap + hats + basse), "half" (kick + basse), "pad" (nappe seule), "off".
- preset "ambient" : nappe + arpège doux (les sections sont ignorées, sauf "off").
- sfx : [type, temps, gain_dB (défaut -12), pan -1..1 (défaut 0), durée (pour typing/riser/fire)].
  types : whoosh, whoosh_down, pop, pop_low, click, tick, thud, boom, glass, ding, chord, riser, typing, glitch, swoosh_big.
"""
import json, pathlib, subprocess, sys, wave
import numpy as np
from scipy import signal

cfg = json.loads(pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "sound.json").read_text(encoding="utf-8"))
SR = 48000
TOTAL = float(cfg["total"]); N = int(TOTAL * SR)
rng = np.random.default_rng(cfg.get("seed", 11))
mus = np.zeros((N, 2)); sfx = np.zeros((N, 2))


def db(g): return 10 ** (g / 20)
def tt(n): return np.arange(n) / SR
def norm(x): return x / (np.max(np.abs(x)) + 1e-9)
def lp(x, f): return signal.sosfilt(signal.butter(2, f, "low", fs=SR, output="sos"), x)
def hp(x, f): return signal.sosfilt(signal.butter(2, f, "high", fs=SR, output="sos"), x)


def put(buf, y, at, g=0.0, pan=0.0):
    s = int(at * SR)
    if s >= N or s + len(y) <= 0: return
    if s < 0: y = y[-s:]; s = 0
    y = y * db(g); e = min(N, s + len(y)); y = y[: e - s]
    buf[s:e, 0] += y * np.cos((pan + 1) * np.pi / 4) * 1.41; buf[s:e, 1] += y * np.sin((pan + 1) * np.pi / 4) * 1.41


# ---------- sons de base ----------
def sweep(d, f0, f1, shape="mid"):
    n = int(d * SR); src = rng.standard_normal(n); y = np.zeros(n); hop = 960
    for s0 in range(0, n, hop):
        fc = f0 * (f1 / f0) ** (s0 / n)
        seg = signal.sosfilt(signal.butter(2, [max(60, fc / 1.5), min(SR / 2 - 200, fc * 1.5)], "band", fs=SR, output="sos"), src[max(0, s0 - 2400): s0 + hop])[-hop:]
        seg = seg[: n - s0]; y[s0:s0 + len(seg)] = seg
    x = np.linspace(0, 1, n)
    env = {"up": x ** 2, "down": (1 - x) ** 1.6}.get(shape, np.sin(np.pi * x) ** 1.5)
    return norm(y * env)


def bell(f, d=0.8):
    n = int(d * SR); x = tt(n); y = np.zeros(n)
    for m, a, k in [(1, 1, 1), (2.76, .45, .6), (5.4, .2, .4)]: y += a * np.sin(2 * np.pi * f * m * x) * np.exp(-x / (d * k * 0.35))
    return norm(y * np.minimum(1, x / 0.002))


def pop(f0=1000, f1=300, d=0.12):
    n = int(d * SR); x = tt(n); f = f0 * (f1 / f0) ** (x / d)
    return norm(np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-x / 0.035))


def click(d=0.012, f=2500): n = int(d * SR); return norm(hp(rng.standard_normal(n), f) * np.exp(-tt(n) / 0.003))


def thud(f0=140, f1=50, d=0.3):
    n = int(d * SR); x = tt(n); f = f0 * (f1 / f0) ** (x / d)
    return norm(np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-x / 0.07) + lp(rng.standard_normal(n), 800) * np.exp(-x / 0.02) * 0.4)


def boom(d=1.4):
    n = int(d * SR); x = tt(n); f = 80 * (30 / 80) ** (x / d)
    return norm(np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-x / 0.5) + 0.7 * norm(lp(rng.standard_normal(n), 300)) * np.exp(-x / 0.18))


def glass(f=2200, d=1.2):
    n = int(d * SR); x = tt(n); y = np.zeros(n)
    for m, a in [(1, 1), (2.32, .5), (4.25, .25), (6.1, .12)]: y += a * np.sin(2 * np.pi * f * m * x) * np.exp(-x / (0.35 / m ** 0.5))
    return norm(y)


def chord(notes=(523.3, 659.3, 784.0, 1046.5), d=1.4):
    y = np.zeros(int((d + 0.04 * len(notes)) * SR))
    for k, f in enumerate(notes): b = bell(f, d); s = int(k * 0.035 * SR); y[s:s + len(b)] += b
    return norm(y)


def typing(d=1.0):
    y = np.zeros(int((d + 0.05) * SR)); t = 0.0
    while t < d:
        c = click(0.008, 1800 + rng.uniform(0, 2500)) * rng.uniform(0.5, 1); s = int(t * SR); y[s:s + len(c)] += c
        t += rng.uniform(0.05, 0.11)
    return norm(y)


def glitch(d=0.35):
    n = int(d * SR); x = tt(n); y = signal.square(2 * np.pi * 180 * x) * (np.sin(2 * np.pi * 37 * x) > 0) + hp(rng.standard_normal(n), 3000) * 0.5
    return norm(lp(y, 6000) * np.exp(-x / 0.15))


def riser(d=0.8):
    n = int(d * SR); x = tt(n)
    return norm(sweep(d, 600, 8000, "up") + 0.3 * np.sin(2 * np.pi * np.cumsum(200 * (8 ** (x / d))) / SR) * (x / d) ** 2)


SFX = {
    "whoosh": lambda d: sweep(d or 0.6, 300, 4500), "whoosh_down": lambda d: sweep(d or 0.6, 4500, 300),
    "swoosh_big": lambda d: sweep(d or 0.9, 200, 6000), "pop": lambda d: pop(), "pop_low": lambda d: pop(700, 200, 0.15),
    "click": lambda d: click(), "tick": lambda d: click(0.006, 3000), "thud": lambda d: thud(), "boom": lambda d: boom(d or 1.4),
    "glass": lambda d: glass(), "ding": lambda d: bell(1568, 1.0), "chord": lambda d: chord(), "riser": lambda d: riser(d or 0.8),
    "typing": lambda d: typing(d or 1.0), "glitch": lambda d: glitch(d or 0.35),
}

# ---------- musique ----------
def kick(): n = int(0.42 * SR); x = tt(n); f = 52 + 130 * np.exp(-x / 0.035); return norm(np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-x / 0.16))
def hat(o=False): n = int((0.2 if o else 0.06) * SR); return norm(hp(rng.standard_normal(n), 7000) * np.exp(-tt(n) / (0.06 if o else 0.012)))
def clap():
    n = int(0.25 * SR); x = tt(n); env = sum((x >= k) * np.exp(-np.clip(x - k, 0, None) / 0.012) for k in (0, 0.011, 0.022)) + (x >= 0.03) * np.exp(-np.clip(x - 0.03, 0, None) / 0.09) * 0.6
    return norm(signal.sosfilt(signal.butter(2, [900, 4000], "band", fs=SR, output="sos"), rng.standard_normal(n)) * env)
def bass(f, d): n = int(d * SR); x = tt(n); return norm(lp(np.sin(2 * np.pi * f * x) + 0.45 * signal.sawtooth(2 * np.pi * f * x), 420) * np.minimum(1, x / 0.005) * np.exp(-x / (d * 0.9)))
def pad(freqs, d):
    n = int(d * SR); x = tt(n); y = sum(signal.sawtooth(2 * np.pi * f * (1 + det / 100) * x + rng.uniform(0, 6)) for f in freqs for det in (-0.12, 0, 0.12))
    return norm(lp(y, 1100) * np.minimum(1, x / 0.6) * np.minimum(1, np.clip(d - x, 0, None) / 0.6))
def pluck(f, d=0.5): n = int(d * SR); x = tt(n); return norm((np.sin(2 * np.pi * f * x) + 0.3 * np.sin(4 * np.pi * f * x)) * np.exp(-x / 0.18) * np.minimum(1, x / 0.004))

M = cfg.get("music", {"preset": "ambient"})
root = M.get("root", 55.0)
PROG = [1.0, 0.794, 1.189, 0.891]  # i – VI – III – VII (en rapport de fréquence)
if M.get("preset") == "pulse":
    beat = 60.0 / M.get("bpm", 120)
    for t0, t1, mode in M.get("sections", [[0, TOTAL, "full"]]):
        t = t0
        while t < t1 - 1e-6:
            i = round((t - t0) / beat); r = root * PROG[int(t // (beat * 8)) % 4]
            if mode in ("full", "half"):
                put(mus, kick(), t, -4)
                for k in (0, 0.5): put(mus, bass(r, beat * 0.45), t + k * beat, -9)
            if mode == "full":
                if i % 2 == 1: put(mus, clap(), t, -12)
                for k in range(4): put(mus, hat(o=(k == 2)), t + k * beat / 4, -20 + (0 if k % 2 else -5), 0.25 * (-1) ** k)
            if mode in ("full", "half", "pad") and i % 8 == 0: put(mus, pad([r * 4, r * 5, r * 6], beat * 8), t, -16)
            t += beat
else:
    chords = [(174.6, 220.0, 261.6, 329.6), (220.0, 261.6, 329.6, 392.0), (146.8, 174.6, 220.0, 261.6), (130.8, 164.8, 196.0, 246.9)]
    for k in range(int(TOTAL // 3) + 1):
        c = chords[k % 4]; put(mus, pad(c, 3.6), k * 3.0, -6)
        for j in range(12): put(mus, pluck(c[j % 4] * 2), k * 3.0 + j * 0.25, -20 - (j % 3) * 2, (-0.4, 0.4)[j % 2])

for item in cfg.get("sfx", []):
    kind, t = item[0], float(item[1]); g = item[2] if len(item) > 2 else -12; pan = item[3] if len(item) > 3 else 0.0; d = item[4] if len(item) > 4 else None
    put(sfx, SFX[kind](d), t, g, pan)

# ---------- voix + mixage ----------
voice = np.zeros(N)
V = cfg.get("voice")
if V:
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", V["file"], "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"], check=True, capture_output=True).stdout
    v = np.frombuffer(raw, dtype=np.int16).astype(np.float64) / 32768
    s0 = int(V.get("start", 0.3) * SR); v = v[: max(0, N - s0)]; voice[s0:s0 + len(v)] = v
fr = int(0.02 * SR); env = np.repeat([np.sqrt(np.mean(voice[k:k + fr] ** 2)) for k in range(0, N, fr)], fr)[:N]
duck = signal.sosfiltfilt(signal.butter(1, 3, "low", fs=SR, output="sos"), np.where(env > db(-40), db(cfg.get("duck", -8)), 1.0))
mix = np.stack([voice, voice], 1) + norm(mus) * db(M.get("gain", -13)) * duck[:, None] + norm(sfx) * db(cfg.get("sfx_gain", -10)) * duck[:, None]
fade = int(0.5 * SR); mix[-fade:] *= np.linspace(1, 0, fade)[:, None]
mix = mix / (np.max(np.abs(mix)) + 1e-9) * 0.9
out = pathlib.Path(cfg.get("out", "audio/mix.wav")); out.parent.mkdir(parents=True, exist_ok=True)
brut = out.with_name("mix-brut.wav")
with wave.open(str(brut), "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mix * 32767).astype(np.int16).tobytes())
subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(brut), "-af", f"loudnorm=I={cfg.get('lufs', -14)}:TP=-1.0:LRA=9", "-ar", "48000", str(out)], check=True)
brut.unlink(); print("OK", out)
