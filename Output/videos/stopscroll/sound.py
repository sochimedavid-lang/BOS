"""Bande-son STOPSCROLL : beat minimal synthétisé à 120 BPM + bruitages calés sur l'image.
Sortie : audio/soundtrack.wav (48 kHz stéréo, -14 LUFS). Déterministe (graine fixe).
"""
import pathlib, subprocess, wave
import numpy as np
from scipy import signal

ICI = pathlib.Path(__file__).resolve().parent
SR, TOTAL, BEAT = 48000, 24.0, 0.5
N = int(TOTAL * SR)
rng = np.random.default_rng(42)
out = np.zeros((N, 2))


def db(g): return 10 ** (g / 20)
def tt(n): return np.arange(n) / SR
def lp(x, f, o=2): return signal.sosfilt(signal.butter(o, f, "low", fs=SR, output="sos"), x)
def hp(x, f, o=2): return signal.sosfilt(signal.butter(o, f, "high", fs=SR, output="sos"), x)
def norm(x): return x / (np.max(np.abs(x)) + 1e-9)


def put(y, at, g=0.0, pan=0.0):
    s = int(at * SR)
    if s >= N or s + len(y) <= 0: return
    y = y * db(g); e = min(N, s + len(y)); y = y[: e - s]
    out[s:e, 0] += y * np.cos((pan + 1) * np.pi / 4) * 1.41
    out[s:e, 1] += y * np.sin((pan + 1) * np.pi / 4) * 1.41


# ---------- instruments ----------
def kick(d=0.42):
    n = int(d * SR); x = tt(n); f = 52 + 130 * np.exp(-x / 0.035)
    y = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-x / 0.16)
    y[: int(0.004 * SR)] += hp(rng.standard_normal(int(0.004 * SR)), 2000) * 0.4
    return norm(y)


def hat(d=0.06, o=False):
    n = int((0.22 if o else d) * SR); x = tt(n)
    return norm(hp(rng.standard_normal(n), 7000) * np.exp(-x / (0.07 if o else 0.012)))


def clap(d=0.25):
    n = int(d * SR); x = tt(n); env = np.zeros(n)
    for k in (0, 0.011, 0.022): env += (x >= k) * np.exp(-np.clip(x - k, 0, None) / 0.012)
    env += (x >= 0.03) * np.exp(-np.clip(x - 0.03, 0, None) / 0.09) * 0.6
    return norm(signal.sosfilt(signal.butter(2, [900, 4000], "band", fs=SR, output="sos"), rng.standard_normal(n)) * env)


def bass(f, d):
    n = int(d * SR); x = tt(n)
    y = np.sin(2 * np.pi * f * x) + 0.45 * signal.sawtooth(2 * np.pi * f * x)
    y = lp(y, 420) * np.minimum(1, x / 0.005) * np.exp(-x / (d * 0.9))
    return norm(y)


def bell(f, d=0.8):
    n = int(d * SR); x = tt(n); y = np.zeros(n)
    for m, a, k in [(1, 1, 1), (2.76, .45, .6), (5.4, .2, .4)]:
        y += a * np.sin(2 * np.pi * f * m * x) * np.exp(-x / (d * k * 0.35))
    return norm(y * np.minimum(1, x / 0.002))


def chord(notes, d=1.6, gap=0.03):
    y = np.zeros(int((d + gap * len(notes)) * SR))
    for k, f in enumerate(notes):
        b = bell(f, d); s = int(k * gap * SR); y[s:s + len(b)] += b
    return norm(y)


def noise_sweep(d, f0, f1, shape="up"):
    n = int(d * SR); src = rng.standard_normal(n); y = np.zeros(n); hop = 960
    for s in range(0, n, hop):
        fc = f0 * (f1 / f0) ** (s / n)
        sos = signal.butter(2, [max(60, fc / 1.5), min(SR / 2 - 200, fc * 1.5)], "band", fs=SR, output="sos")
        seg = signal.sosfilt(sos, src[max(0, s - 2400): s + hop])[-hop:] if s >= 2400 else signal.sosfilt(sos, src[: s + hop])[-hop:]
        seg = seg[: n - s]; y[s:s + len(seg)] = seg
    x = np.linspace(0, 1, n)
    env = x ** 2 if shape == "up" else (1 - x) ** 1.6 if shape == "down" else np.sin(np.pi * x) ** 1.5
    return norm(y * env)


def whoosh(d=0.5, up=True): return noise_sweep(d, 300 if up else 5000, 5000 if up else 300, "mid")
def riser(d=0.8): return norm(noise_sweep(d, 600, 8000, "up") + 0.3 * np.sin(2 * np.pi * np.cumsum(200 * (8 ** (tt(int(d * SR)) / d))) / SR) * (tt(int(d * SR)) / d) ** 2)


def pop(f0=1100, f1=300, d=0.12):
    n = int(d * SR); x = tt(n); f = f0 * (f1 / f0) ** (x / d)
    return norm(np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-x / 0.035))


def tick(): n = int(0.01 * SR); return norm(hp(rng.standard_normal(n), 3000) * np.exp(-tt(n) / 0.0025))
def thud(f0=140, f1=50, d=0.3):
    n = int(d * SR); x = tt(n); f = f0 * (f1 / f0) ** (x / d)
    return norm(np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-x / 0.07) + lp(rng.standard_normal(n), 800) * np.exp(-x / 0.02) * 0.4)


def boom(d=1.4):
    n = int(d * SR); x = tt(n); f = 80 * (30 / 80) ** (x / d)
    return norm(np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-x / 0.5) + 0.7 * norm(lp(rng.standard_normal(n), 300)) * np.exp(-x / 0.18))


def buzz(d=0.35):
    n = int(d * SR); x = tt(n)
    return norm(lp(signal.square(2 * np.pi * 92 * x) * np.exp(-x / 0.18), 1500))


# ---------- musique (grille de 120 BPM) ----------
def beat_section(t0, t1, kick_g=-4, hat_g=-20, clap_g=-12, bass_g=-9, roots=(55.0,), full=True):
    t = t0
    while t < t1 - 1e-6:
        i = round((t - t0) / BEAT)
        put(kick(), t, kick_g)
        if full and i % 2 == 1: put(clap(), t, clap_g)
        for k in range(4 if full else 2):
            h = t + k * (BEAT / (4 if full else 2))
            if h < t1: put(hat(o=(k == 2 and full)), h, hat_g + (0 if k % 2 else -5), 0.25 * (-1) ** k)
        root = roots[int((t - t0) // 2.0) % len(roots)]
        for k in (0, 0.25):
            if t + k < t1: put(bass(root, 0.24), t + k, bass_g)
        t += BEAT


# A : accroche, ça défile (0–1)
beat_section(0.0, 1.0, hat_g=-17, roots=(55.0,))
for k in range(10): put(tick(), k * 0.1, -10, 0.3 if k % 2 else -0.3)
put(noise_sweep(1.0, 400, 3000, "up"), 0.0, -22)
# gel (1,0)
put(boom(), 1.0, -2); put(thud(180, 45), 1.0, -6); put(chord((440.0, 659.3), 0.9), 1.0, -22)
# B : titre + photo fixe (2–7)
beat_section(2.0, 7.0, kick_g=-7, hat_g=-24, clap_g=-16, bass_g=-12, roots=(55.0, 55.0, 43.65), full=False)
put(whoosh(0.6), 1.85, -16); put(thud(), 2.25, -16); put(thud(), 2.5, -18); put(whoosh(0.45, False), 3.7, -18)
put(whoosh(0.7), 3.9, -16); put(thud(110, 45), 4.6, -14); put(tick(), 5.4, -14); put(tick(), 5.65, -16)
put(whoosh(0.4), 5.85, -6, 0.3); put(thud(160, 50), 6.2, -8); put(buzz(), 6.2, -16)
# C : la question (7–8)
put(pop(900, 400), 7.0, -14)
for k in range(10): put(tick(), 7.1 + k * 0.03, -20)
put(riser(0.6), 7.4, -10)
# D : la pub vivante (8–14)
beat_section(8.0, 14.0, roots=(55.0, 43.65, 65.41))
put(boom(), 8.0, -4); put(whoosh(0.6), 8.0, -14, -0.2); put(whoosh(0.7), 8.35, -16, 0.3)
put(noise_sweep(0.8, 2000, 9000, "mid"), 9.0, -22, -0.5); put(noise_sweep(0.8, 2000, 9000, "mid"), 11.5, -22, 0.5)
put(pop(1300, 500), 8.9, -18)
put(thud(150, 60), 10.0, -10); put(pop(900, 250), 10.0, -12)
put(pop(1200, 600), 10.5, -12, -0.3); put(pop(1500, 700), 11.0, -12, 0.3)
put(pop(1000, 300), 9.0, -16); put(pop(1000, 300), 10.5, -16); put(pop(1000, 300), 12.5, -16)
put(whoosh(0.5), 12.3, -20, 0.5)
put(tick(), 12.95, -4); put(pop(700, 200, 0.08), 13.0, -8); put(chord((1046.5, 1318.5, 1568.0, 2093.0), 1.4), 13.05, -12)
# E : retour dans le flux + résultats (14–17,6)
put(whoosh(0.5, False), 13.9, -12); put(noise_sweep(1.1, 3000, 300, "down"), 14.0, -18)
beat_section(14.0, 17.5, kick_g=-6, hat_g=-21, roots=(55.0, 43.65), full=True)
put(thud(), 14.25, -16); put(thud(), 14.5, -18); put(whoosh(0.5), 15.5, -12)
for t, f in [(15.75, 523.3), (16.0, 659.3), (16.5, 784.0), (17.0, 1046.5)]:
    put(pop(1100, 400), t, -14); put(bell(f, 0.7), t + 0.05, -20)
put(chord((523.3, 659.3, 784.0, 1046.5), 1.0), 17.0, -18)
put(riser(0.35), 17.65, -8)
# F : marque + fin (18–24)
put(boom(), 18.0, -3); put(thud(200, 60), 18.05, -8)
for k in range(4): put(tick(), 18.25 + k * 0.05, -14)
for k in range(6): put(tick(), 18.5 + k * 0.05, -14)
put(pop(800, 300), 19.0, -14)
beat_section(18.5, 23.0, kick_g=-6, hat_g=-22, clap_g=-14, bass_g=-11, roots=(55.0, 43.65, 65.41), full=True)
for t in (19.0, 20.0): put(tick(), t, -8)
put(whoosh(0.6), 20.65, -14); put(thud(), 21.25, -16); put(thud(), 21.5, -18)
put(pop(900, 300), 22.0, -10); put(chord((440.0, 554.4, 659.3, 880.0), 2.2), 22.0, -16)
for t in (22.5, 23.0, 23.5): put(pop(1300, 600, 0.08), t, -20)
put(kick(), 23.0, -6); put(boom(1.0), 23.0, -12)

# fin : fondu court
fade = int(0.35 * SR); out[-fade:] *= np.linspace(1, 0, fade)[:, None]
mix = out / (np.max(np.abs(out)) + 1e-9) * 0.9
(ICI / "audio").mkdir(exist_ok=True)
brut = ICI / "audio" / "soundtrack-brut.wav"
with wave.open(str(brut), "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mix * 32767).astype(np.int16).tobytes())
subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(brut), "-af", "loudnorm=I=-14:TP=-1.0:LRA=9", "-ar", "48000", "-t", str(TOTAL), str(ICI / "audio" / "soundtrack.wav")], check=True)
brut.unlink()
print("OK audio/soundtrack.wav")
