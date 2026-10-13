"""Sous-titres automatiques à partir d'une transcription HyperFrames (whisper --json).

Usage : python3 captions.py audio/voix.json --start 0.4 [--max 4] > captions.json
Sortie : [[temps, "texte"], …] à donner à MK.captions(tl, "#cap", chunks).
Coupe à chaque ponctuation forte (. ? ! …) et toutes les --max mots ; un texte vide efface la ligne
après la dernière phrase. --fix "cotonoux=Cotonou" corrige les mots mal transcrits.
"""
import argparse, json

ap = argparse.ArgumentParser()
ap.add_argument("transcript"); ap.add_argument("--start", type=float, default=0.3)
ap.add_argument("--max", type=int, default=4); ap.add_argument("--fix", action="append", default=[])
a = ap.parse_args()
d = json.load(open(a.transcript, encoding="utf-8"))
words = d["words"] if isinstance(d, dict) else d
fixes = dict(f.split("=", 1) for f in a.fix)
out, cur, t0, last_end = [], [], None, 0.0
for w in words:
    txt = w["text"].strip()
    if not txt or txt.lower().startswith("sous-titres"): break  # hallucination fréquente de whisper sur le silence final
    key = txt.strip(".,?!…;:").lower()
    for k, v in fixes.items():
        if key == k.lower(): txt = txt.lower().replace(k.lower(), v)
    if t0 is None: t0 = w["start"]
    cur.append(txt); last_end = w["end"]
    if txt[-1] in ".?!…" or len(cur) >= a.max or txt.endswith(","):
        out.append([round(t0 + a.start, 2), " ".join(cur)]); cur, t0 = [], None
if cur: out.append([round(t0 + a.start, 2), " ".join(cur)])
out.append([round(last_end + a.start + 0.4, 2), ""])
print("[\n " + ",\n ".join(json.dumps(c, ensure_ascii=False) for c in out) + "\n]")
