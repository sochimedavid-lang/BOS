"""Bande-son : nappe douce + arpège discret + bruitages de verre et d'interface + voix ElevenLabs (prise choisie).
Usage : python3 sound.py [numéro de prise, défaut 2]. Sortie : audio/mix.wav (48 kHz stéréo, -14 LUFS).
"""
import pathlib, subprocess, sys, wave
import numpy as np
from scipy import signal

ICI = pathlib.Path(__file__).resolve().parent
SR, TOTAL, V0 = 48000, 24.6, 0.3
N = int(TOTAL * SR)
rng = np.random.default_rng(7)
mus = np.zeros((N, 2)); sfx = np.zeros((N, 2))


def db(g): return 10 ** (g / 20)
def tt(n): return np.arange(n) / SR
def norm(x): return x / (np.max(np.abs(x)) + 1e-9)
def lp(x, f): return signal.sosfilt(signal.butter(2, f, "low", fs=SR, output="sos"), x)
def hp(x, f): return signal.sosfilt(signal.butter(2, f, "high", fs=SR, output="sos"), x)


def put(buf, y, at, g=0.0, pan=0.0):
    s = int(at * SR)
    if s >= N: return
    y = y * db(g); e = min(N, s + len(y)); y = y[: e - s]
    buf[s:e, 0] += y * np.cos((pan + 1) * np.pi / 4) * 1.41; buf[s:e, 1] += y * np.sin((pan + 1) * np.pi / 4) * 1.41


def pad(freqs, d):
    n = int(d * SR); x = tt(n); y = np.zeros(n)
    for f in freqs:
        for det in (-0.12, 0.0, 0.12):
            y += signal.sawtooth(2 * np.pi * f * (1 + det / 100) * x + rng.uniform(0, 6))
    y = lp(y, 1100); env = np.minimum(1, x / 0.8) * np.minimum(1, (d - x) / 0.9)
    return norm(y * env)


def pluck(f, d=0.6):
    n = int(d * SR); x = tt(n)
    return norm((np.sin(2 * np.pi * f * x) + 0.3 * np.sin(4 * np.pi * f * x)) * np.exp(-x / 0.18) * np.minimum(1, x / 0.004))


def sub(f, d):
    n = int(d * SR); x = tt(n); return norm(np.sin(2 * np.pi * f * x) * np.minimum(1, x / 0.05) * np.minimum(1, (d - x) / 0.3))


def whoosh(d=0.6, up=True):
    n = int(d * SR); src = rng.standard_normal(n); y = np.zeros(n); hop = 960
    for s0 in range(0, n, hop):
        fc = (300 * (14 ** (s0 / n))) if up else (4200 * (1 / 14) ** (s0 / n))
        seg = signal.sosfilt(signal.butter(2, [max(60, fc / 1.5), min(20000, fc * 1.5)], "band", fs=SR, output="sos"), src[max(0, s0 - 2400): s0 + hop])[-hop:]
        seg = seg[: n - s0]; y[s0:s0 + len(seg)] = seg
    xx = np.linspace(0, 1, n); return norm(y * np.sin(np.pi * xx) ** 1.5)


def glass(f=2200, d=1.2):
    n = int(d * SR); x = tt(n); y = np.zeros(n)
    for m, a in [(1, 1), (2.32, .5), (4.25, .25), (6.1, .12)]:
        y += a * np.sin(2 * np.pi * f * m * x) * np.exp(-x / (0.35 / m ** 0.5))
    return norm(y)


def click(): n = int(0.012 * SR); return norm(hp(rng.standard_normal(n), 2500) * np.exp(-tt(n) / 0.003))
def pop(f0=900, f1=300, d=0.1):
    n = int(d * SR); x = tt(n); f = f0 * (f1 / f0) ** (x / d)
    return norm(np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-x / 0.03))


# ---------- musique : Fmaj7 – Am7 – Dm7 – Cmaj7, 3 s par accord ----------
CH = [(174.6, 220.0, 261.6, 329.6), (220.0, 261.6, 329.6, 392.0), (146.8, 174.6, 220.0, 261.6), (130.8, 164.8, 196.0, 246.9)]
for k in range(9):
    t0 = k * 3.0; c = CH[k % 4]
    put(mus, pad(c, 3.6), t0, -6, 0.0)
    put(mus, sub(c[0] / 2, 3.0), t0, -8)
    for j in range(12):
        put(mus, pluck(c[j % 4] * 2, 0.5), t0 + j * 0.25, -20 - (j % 3) * 2, (-0.4, 0.4)[j % 2])

# ---------- bruitages (instants de la vidéo) ----------
for t, up in [(0.95, True), (2.45, False), (6.6, True), (8.15, True), (9.7, True), (10.85, True), (14.6, True), (19.9, False), (21.35, True), (21.9, True)]:
    put(sfx, whoosh(0.6, up), t - 0.1, -12, 0.3 if up else -0.3)
for t, f in [(1.3, 1800), (13.05, 2400), (18.75, 2000), (20.3, 2600)]:
    put(sfx, glass(f), t, -14)
for t in (7.25, 7.7): put(sfx, click(), t, -6); put(sfx, pop(700, 200), t + 0.05, -12)
for i in range(5): put(sfx, pop(1200, 600, 0.08), 10.45 + i * 0.09, -16, 0.5)
for i in range(5): put(sfx, pop(900, 500, 0.08), 11.8 + i * 0.12, -16, -0.5)
put(sfx, pop(600, 150, 0.2), 16.4, -6); put(sfx, pop(600, 150, 0.2), 16.7, -6)
put(sfx, pop(1000, 300), 5.5, -12)
put(sfx, glass(3200, 0.8), 24.0 - 1.6, -16)

# ---------- voix ----------
prise = sys.argv[1] if len(sys.argv) > 1 else "2"
raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(ICI / "audio" / f"prise-{prise}.mp3"), "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"], check=True, capture_output=True).stdout
v = np.frombuffer(raw, dtype=np.int16).astype(np.float64) / 32768
voice = np.zeros(N); s0 = int(V0 * SR); voice[s0:s0 + len(v)] = v[: N - s0]

# ducking de la musique sous la voix
fr = int(0.02 * SR); env = np.repeat([np.sqrt(np.mean(voice[k:k + fr] ** 2)) for k in range(0, N, fr)], fr)[:N]
duck = signal.sosfiltfilt(signal.butter(1, 3, "low", fs=SR, output="sos"), np.where(env > db(-40), db(-9), 1.0))
mix = np.stack([voice, voice], 1) * 1.0 + norm(mus) * 0.22 * duck[:, None] + norm(sfx) * 0.32 * duck[:, None]
fade = int(0.6 * SR); mix[-fade:] *= np.linspace(1, 0, fade)[:, None]
mix = mix / (np.max(np.abs(mix)) + 1e-9) * 0.9
brut = ICI / "audio" / "mix-brut.wav"
with wave.open(str(brut), "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mix * 32767).astype(np.int16).tobytes())
subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(brut), "-af", "loudnorm=I=-14:TP=-1.0:LRA=9", "-ar", "48000", str(ICI / "audio" / "mix.wav")], check=True)
brut.unlink(); print("OK audio/mix.wav (prise", prise + ")")
