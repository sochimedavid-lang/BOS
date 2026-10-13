"""Voix off en UNE seule prise (Gemini 3.8 flash TTS), débit constant. Sortie : voix-prise-unique/gemini38.wav"""
import pathlib, sys, time, urllib.error
import voix_off as vo

ICI = pathlib.Path(__file__).resolve().parent
TEXTE = ("Vingt-quatre décembre. Une seule nuit pour livrer le monde entier ! "
         "Au pôle Nord, l'atelier tourne à fond : des millions de cadeaux, emballés, triés, chargés ! "
         "Minuit pile… décollage ! Son secret ? Il suit la nuit. "
         "Tokyo ! Paris ! Cotonou ! New York ! "
         "Une cheminée, un sapin, un cadeau… et on recommence ! "
         "Joyeux Noël ! Et si votre marque avait, elle aussi, sa vidéo magique ?")

if __name__ == "__main__":
    vo.STYLE = ""  # 3.8 lit la consigne à voix haute : aucune consigne
    voix = sys.argv[1] if len(sys.argv) > 1 else "Sulafat"
    cle = vo.lire_cle()
    for essai in range(8):
        try:
            pcm = vo.synthese(cle, "gemini-3.8-flash-tts", voix, TEXTE); break
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 503) and essai < 7:
                print(f"erreur {e.code}, nouvelle tentative dans 30 s", flush=True); time.sleep(30); continue
            sys.exit(f"Erreur {e.code} : {e.read().decode()[:300]}")
    d = vo.ecrire_wav(ICI / "voix-prise-unique" / f"gemini38-{voix}.wav", pcm)
    print(f"OK {d:.2f} s")
