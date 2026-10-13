"""Voix off DYNAMIQUE (version 37 s) : texte court, débit rapide, chaque segment calé sur un moment de l'animation.
Sortie : voix2/seg-NN.wav. Usage : python3 voix_dyn.py [--voix Sulafat] [--refaire]
"""
import argparse, pathlib, sys, time, urllib.error, wave
import voix_off as vo

ICI = pathlib.Path(__file__).resolve().parent
# (instant d'attaque dans la vidéo d'origine en s, fin max, texte)
SEGMENTS = [
    (0.35, 4.9, "Vingt-quatre décembre. Une seule nuit pour livrer le monde entier !"),
    (5.15, 11.2, "Au pôle Nord, l'atelier tourne à fond ! Des millions de cadeaux : emballés, triés, chargés !"),
    (11.75, 13.2, "Minuit pile…"),
    (13.0, 15.4, "Décollage !"),
    (16.45, 18.25, "Son secret ? Il suit la nuit !"),
    (18.3, 19.6, "Tokyo !"),
    (20.5, 21.6, "Paris !"),
    (21.7, 23.4, "Cotonou !"),
    (23.5, 25.2, "New York !"),
    (27.8, 31.3, "Une cheminée, un sapin, un cadeau… et on recommence !"),
    (33.0, 36.9, "Joyeux Noël ! Et si votre marque avait, elle aussi, sa vidéo magique ?"),
]
# Attention : gemini-3.8-flash-tts lit cette consigne à voix haute (la couper ensuite) ; gemini-2.5-flash-preview-tts l'applique sans la lire.
STYLE = ("Lis ce texte en français avec beaucoup d'énergie, un débit rapide et rythmé comme une bande-annonce de pub, "
         "voix enjouée et souriante, sans traîner sur les pauses : ")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--voix", default="Sulafat")
    ap.add_argument("--modele", default="gemini-2.5-flash-preview-tts")
    ap.add_argument("--refaire", action="store_true")
    a = ap.parse_args()
    vo.STYLE = STYLE
    cle = vo.lire_cle()
    out = ICI / "voix2"; out.mkdir(exist_ok=True)
    for i, (t0, fin, texte) in enumerate(SEGMENTS, 1):
        f = out / f"seg-{i:02d}.wav"
        if f.exists() and not a.refaire:
            continue
        for essai in range(6):
            try:
                pcm = vo.synthese(cle, a.modele, a.voix, texte); break
            except urllib.error.HTTPError as e:
                if e.code == 429 and essai < 5:
                    print(f"quota, attente 62 s (segment {i})", flush=True); time.sleep(62); continue
                sys.exit(f"Erreur {e.code} segment {i} : {e.read().decode()[:300]}")
        d = vo.ecrire_wav(f, pcm)
        print(f"segment {i:02d} : {d:.2f} s  (créneau {fin - t0:.2f} s)  {texte}", flush=True)


if __name__ == "__main__":
    main()
