"""Bruitages (instants d'origine recalés via gen3.T) + prise unique ElevenLabs calée + mixage final.
Entrée : audio/voix-calee-11labs.wav (python3 gen3.py). Sortie : audio/mix3.wav (48 kHz stéréo, -14 LUFS).
"""
import pathlib, subprocess, tempfile, wave
import numpy as np
from scipy import signal
from gen3 import T, TOTAL

ICI = pathlib.Path(__file__).resolve().parent
SR = 48000
N = int(TOTAL * SR)
rng = np.random.default_rng(2026)


def db(g): return 10 ** (g / 20)
def t(n): return np.arange(n) / SR


# ---------- briques sonores ----------
def bell(f, dur=0.8, amp=1.0):
    n = int(dur * SR); x = t(n); y = np.zeros(n)
    for k, (m, a, d) in enumerate([(1, 1, 1), (2.76, .5, .6), (5.4, .25, .4), (8.93, .12, .25)]):
        y += a * np.sin(2 * np.pi * f * m * x + k) * np.exp(-x / (dur * d * 0.35))
    y *= np.minimum(1, x / 0.002)
    return amp * y / np.max(np.abs(y))


def bandnoise(dur, f0, f1, order=2):
    n = int(dur * SR); src = rng.standard_normal(n + SR // 10); out = np.zeros(n)
    hop = 960; win = np.hanning(2 * hop)
    for s in range(0, n, hop):
        fc = f0 * (f1 / f0) ** (s / max(1, n))
        lo, hi = max(40, fc / 1.6), min(SR / 2 - 100, fc * 1.6)
        sos = signal.butter(order, [lo, hi], btype="band", fs=SR, output="sos")
        seg = signal.sosfilt(sos, src[s: s + 2 * hop + 2400])[2400:2400 + 2 * hop]
        seg = np.pad(seg, (0, 2 * hop - len(seg)))
        e = min(n, s + 2 * hop); out[s:e] += (seg * win)[: e - s]
    return out / (np.max(np.abs(out)) + 1e-9)


def whoosh(dur=0.8, up=True, peak=0.65):
    f0, f1 = (300, 4500) if up else (4500, 300)
    y = bandnoise(dur, f0, f1); x = np.linspace(0, 1, len(y))
    env = np.where(x < peak, (x / peak) ** 2, ((1 - x) / (1 - peak)) ** 1.5)
    return y * env


def pop(f0=900, f1=220, dur=0.14):
    n = int(dur * SR); x = t(n); f = f0 * (f1 / f0) ** (x / dur)
    y = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-x / 0.045)
    y[:int(0.003 * SR)] += rng.standard_normal(int(0.003 * SR)) * 0.3
    return y


def click(dur=0.012, hp=2000):
    n = int(dur * SR); y = rng.standard_normal(n) * np.exp(-t(n) / 0.003)
    return signal.sosfilt(signal.butter(2, hp, "high", fs=SR, output="sos"), y)


def flip():
    y = np.concatenate([click(0.01), np.zeros(int(0.02 * SR))]); f = bandnoise(0.05, 1200, 2500) * np.hanning(int(0.05 * SR)) * 0.5
    out = np.zeros(int(0.08 * SR)); out[:len(y)] += y; out[int(0.02 * SR):int(0.02 * SR) + len(f)] += f
    return out


def thud(f0=120, f1=55, dur=0.25):
    n = int(dur * SR); x = t(n); f = f0 * (f1 / f0) ** (x / dur)
    y = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-x / 0.06)
    nz = signal.sosfilt(signal.butter(2, 900, "low", fs=SR, output="sos"), rng.standard_normal(n)) * np.exp(-x / 0.02) * 0.6
    return y + nz


def boom(dur=1.6):
    n = int(dur * SR); x = t(n); f = 75 * (32 / 75) ** (x / dur)
    y = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-x / 0.45)
    nz = signal.sosfilt(signal.butter(2, 400, "low", fs=SR, output="sos"), rng.standard_normal(n)) * np.exp(-x / 0.25)
    return y + 0.8 * nz / np.max(np.abs(nz))


def shimmer(dur=1.2, n_hits=40, lo=2500, hi=7500):
    out = np.zeros(int((dur + 0.4) * SR))
    for k in range(n_hits):
        s = int(rng.uniform(0, dur) * SR); b = bell(rng.uniform(lo, hi), 0.35, rng.uniform(0.2, 0.6))
        out[s:s + len(b)] += b[: len(out) - s]
    x = np.linspace(0, 1, len(out)); return out * np.minimum(1, x * 6) * (1 - x) ** 0.7


def jingle(dur=3.0, rate=18):
    out = np.zeros(int((dur + 0.3) * SR)); n = int(dur * rate)
    for k in range(n):
        tt = k / rate + rng.uniform(0, 0.02); shake = 0.55 + 0.45 * np.sin(2 * np.pi * 5.5 * tt) ** 2
        b = bell(rng.choice([3150, 3520, 3960, 4430, 5270]), 0.16, shake * rng.uniform(0.5, 1))
        s = int(tt * SR); out[s:s + len(b)] += b[: len(out) - s]
    x = np.linspace(0, 1, len(out)); return out * np.minimum(1, x * 10) * np.minimum(1, (1 - x) * 8)


def chord(notes=(1046.5, 1318.5, 1568.0, 2093.0), gap=0.045, dur=1.6):
    out = np.zeros(int((dur + gap * len(notes)) * SR))
    for k, f in enumerate(notes):
        b = bell(f, dur, 0.8); s = int(k * gap * SR); out[s:s + len(b)] += b
    return out


def riser(dur=0.7):
    n = int(dur * SR); x = t(n); f = 200 * (1400 / 200) ** (x / dur)
    y = 0.35 * np.sin(2 * np.pi * np.cumsum(f) / SR) + bandnoise(dur, 800, 6000) * 0.8
    return y * (x / dur) ** 2


def fire(dur):
    n = int(dur * SR); bed = signal.sosfilt(signal.butter(2, 700, "low", fs=SR, output="sos"), np.cumsum(rng.standard_normal(n)) * 0.02)
    bed = bed / (np.max(np.abs(bed)) + 1e-9) * 0.35; out = bed.copy()
    for k in range(int(dur * 14)):
        s = int(rng.uniform(0, dur - 0.05) * SR); c = click(0.008, 1500) * rng.uniform(0.2, 1.0); out[s:s + len(c)] += c
    return out


def wind(dur):
    n = int(dur * SR); w = signal.sosfilt(signal.butter(2, 380, "low", fs=SR, output="sos"), np.cumsum(rng.standard_normal(n)) * 0.02)
    w = w / (np.max(np.abs(w)) + 1e-9); return w * (0.55 + 0.45 * np.sin(2 * np.pi * 0.18 * t(n)))


def conveyor(dur):
    n = int(dur * SR); x = t(n); y = 0.25 * np.sin(2 * np.pi * 55 * x) + 0.12 * np.sin(2 * np.pi * 110 * x)
    for k in np.arange(0, dur, 0.42):
        b = bell(620, 0.12, 0.6); s = int(k * SR); y[s:s + len(b)] += b[: n - s]
    return y


def ticks(dur):
    out = np.zeros(int(dur * SR)); tt = 0.0
    while tt < dur:
        c = click(0.006, 3000) * 0.7; s = int(tt * SR); out[s:s + len(c)] += c[: len(out) - s]
        tt += 0.045 + 0.25 * (tt / dur) ** 2
    return out


# ---------- timeline ----------
sfx = np.zeros((N, 2))


def add(y, at, gain_db, pan=0.0):
    s = int(T(at) * SR); y = y * db(gain_db)
    if s >= N: return
    e = min(N, s + len(y)); y = y[: e - s]
    l, r = np.cos((pan + 1) * np.pi / 4), np.sin((pan + 1) * np.pi / 4)
    sfx[s:e, 0] += y * l * 1.41; sfx[s:e, 1] += y * r * 1.41


def add_sweep(y, at, gain_db, p0=-0.8, p1=0.8):
    s = int(T(at) * SR); y = y * db(gain_db); e = min(N, s + len(y)); y = y[: e - s]
    p = np.linspace(p0, p1, len(y)); sfx[s:e, 0] += y * np.cos((p + 1) * np.pi / 4) * 1.41; sfx[s:e, 1] += y * np.sin((p + 1) * np.pi / 4) * 1.41


add(wind(TOTAL), 0, -30)  # instants ci-dessous = temps d'origine (37 s), recalés par T()
add(chord(), 0.3, -16)
add_sweep(whoosh(0.6), 0.85, -18)
add_sweep(whoosh(1.5, True, 0.8), 3.55, -9)
add(thud(), 5.0, -14); add(bell(1568, 1.0), 5.05, -20)
add(conveyor(6.2), 5.0, -26)
add(ticks(5.4), 5.7, -24, 0.4)
add_sweep(whoosh(0.7), 11.15, -13, 0.8, -0.8)
add(pop(), 11.5, -14)
for k in range(4): add(flip(), 12.4 + k * 0.07, -9, -0.3 + k * 0.2)
add(bell(1568, 1.2), 12.95, -12)
add(jingle(3.2), 13.0, -12)
add_sweep(whoosh(2.3, True, 0.7), 13.0, -14, -0.7, 0.7)
for k in range(30): add(bell(rng.uniform(3500, 7000), 0.25, 0.6), 13.1 + k * 0.075, -26, -0.6 + k * 0.04)
add(riser(0.6), 15.35, -12)
add(boom(), 15.95, -6); add(shimmer(1.2), 15.95, -15)
add_sweep(whoosh(0.8, False), 16.35, -14)
notes = [1046.5, 1318.5, 1568.0, 2093.0]
for i, v in enumerate([18.4, 20.6, 21.8, 23.6]):
    add_sweep(whoosh(0.8, True, 0.8), v - 0.85, -21, 0.5, -0.5)
    add(pop(), v - 0.1, -10); add(bell(notes[i], 1.0), v, -13); add(shimmer(0.6, 14), v + 0.05, -19)
add_sweep(whoosh(0.9), 21.1, -17); add_sweep(whoosh(0.9, False), 22.55, -19)
add_sweep(whoosh(0.8), 25.35, -14)
add(jingle(1.3), 25.5, -14, -0.4); add(thud(), 26.7, -12)
add_sweep(whoosh(0.9, False, 0.85), 27.0, -9, 0, 0)
add(fire(3.8), 27.6, -21, -0.3)
for v in [27.9, 28.7, 29.5]: add(pop(700, 300, 0.1), v, -17)
for i in range(5):
    v = 29.6 + i * 0.22
    add(thud(140, 70), v + 0.27, -11, 0.3); add(thud(140, 70), v + 0.55, -20, 0.3); add(thud(140, 70), v + 0.68, -26, 0.3)
add_sweep(whoosh(0.7), 31.35, -14)
add(pop(600, 160, 0.2), 31.5, -10); add(thud(), 32.15, -17)
add(pop(1100, 300, 0.12), 32.3, -6); add(shimmer(1.6, 60), 32.3, -10); add(chord((1568, 2093, 2637, 3136)), 32.3, -14)
add(chord(), 33.35, -11); add(jingle(2.0), 33.3, -19)
add(bell(2093, 0.9), 34.8, -16)
add(chord((1046.5, 1568.0, 2093.0)), 35.9, -20)


# ---------- voix ----------
with wave.open(str(ICI / "audio" / "voix-calee-11labs.wav")) as w:
    voice = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float64) / 32768
voice = np.pad(voice, (0, max(0, N - len(voice))))[:N] * 1.15

# ducking : bruitages -7 dB quand la voix parle
fr = int(0.02 * SR); env = np.repeat([np.sqrt(np.mean(voice[k:k + fr] ** 2)) for k in range(0, N, fr)], fr)[:N]
duck = np.where(env > db(-40), db(-7), 1.0)
duck = signal.sosfiltfilt(signal.butter(1, 4, "low", fs=SR, output="sos"), duck)
mix = np.stack([voice, voice], 1) * 1.0 + sfx * duck[:, None]
mix = mix / (np.max(np.abs(mix)) + 1e-9) * 0.89
out = ICI / "audio"; out.mkdir(exist_ok=True)
brut = out / "mix-brut.wav"
with wave.open(str(brut), "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mix * 32767).astype(np.int16).tobytes())
subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(brut), "-af", "loudnorm=I=-14:TP=-1.0:LRA=9", "-ar", "48000", str(out / "mix3.wav")], check=True)
print("OK :", out / "mix3.wav")
