"""Voix off de la pub Noël avec Google Gemini TTS.

Clé lue dans la variable d'environnement GEMINI_API_KEY, sinon dans le fichier .env à la racine du dépôt.
Produit : voix/ligne-N.wav (une par phrase) et voix/voix-off.wav (37 s, phrases calées sur la vidéo).
Usage : python3 voix_off.py [--voix Sulafat] [--modele gemini-2.5-flash-preview-tts]
"""
import argparse, base64, json, os, pathlib, subprocess, sys, urllib.request, urllib.error, wave

ICI = pathlib.Path(__file__).resolve().parent
RACINE = ICI.parents[2]

# (début en secondes, texte) — voir script.md
LIGNES = [
    (0.3, "24 décembre. Il reste une seule nuit… pour livrer le monde entier."),
    (5.3, "Au pôle Nord, l'atelier tourne à plein régime. Des millions de cadeaux : emballés, triés, chargés."),
    (11.6, "À minuit pile… le traîneau décolle."),
    (16.6, "Son secret ? Il suit la nuit, fuseau après fuseau. Tokyo. Paris. Cotonou. New York."),
    (25.6, "Une cheminée. Un sapin. Un cadeau. Et on recommence… des millions de fois."),
    (31.8, "Joyeux Noël. Et si votre marque avait, elle aussi, sa vidéo magique ?"),
]
STYLE = ("Lis ce texte en français, d'une voix chaleureuse et posée de conteur de Noël, "
         "avec un sourire dans la voix et une légère emphase sur les mots importants : ")
DUREE_TOTALE = 37.0


def lire_cle():
    cle = os.environ.get("GEMINI_API_KEY", "").strip()
    if cle:
        return cle
    env = RACINE / ".env"
    if env.exists():
        for ligne in env.read_text(encoding="utf-8").splitlines():
            if ligne.strip().startswith("GEMINI_API_KEY="):
                cle = ligne.split("=", 1)[1].strip().strip('"').strip("'")
                if cle:
                    return cle
    sys.exit("Clé introuvable : renseigne GEMINI_API_KEY (variable d'environnement ou fichier .env à la racine).")


def synthese(cle, modele, voix, texte):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{modele}:generateContent"
    corps = {
        "contents": [{"parts": [{"text": STYLE + texte}]}],
        "generationConfig": {
            "responseModalities": ["AUDIO"],
            "speechConfig": {"voiceConfig": {"prebuiltVoiceConfig": {"voiceName": voix}}},
        },
    }
    req = urllib.request.Request(url, data=json.dumps(corps).encode(), method="POST",
                                 headers={"Content-Type": "application/json", "x-goog-api-key": cle})
    with urllib.request.urlopen(req, timeout=120) as r:
        rep = json.load(r)
    part = rep["candidates"][0]["content"]["parts"][0]["inlineData"]
    return base64.b64decode(part["data"])  # PCM 16 bits, mono, 24 kHz


def ecrire_wav(chemin, pcm, taux=24000):
    with wave.open(str(chemin), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(taux); w.writeframes(pcm)
    return len(pcm) / 2 / taux


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--voix", default="Sulafat")
    ap.add_argument("--refaire", action="store_true", help="régénérer même les phrases déjà présentes")
    ap.add_argument("--modele", default=os.environ.get("GEMINI_TTS_MODEL", "gemini-2.5-flash-preview-tts"))
    a = ap.parse_args()
    cle = lire_cle()
    sortie = ICI / "voix"; sortie.mkdir(exist_ok=True)
    fichiers = []
    for i, (debut, texte) in enumerate(LIGNES, 1):
        f = sortie / f"ligne-{i}.wav"
        if f.exists() and not a.refaire:
            with wave.open(str(f)) as w:
                duree = w.getnframes() / w.getframerate()
        else:
            for essai in range(4):
                try:
                    pcm = synthese(cle, a.modele, a.voix, texte)
                    break
                except urllib.error.HTTPError as e:
                    if e.code == 429 and essai < 3:
                        print(f"quota atteint, nouvelle tentative dans 65 s (ligne {i})"); import time; time.sleep(65); continue
                    sys.exit(f"Erreur Google TTS ({e.code}) sur la ligne {i} : {e.read().decode()[:400]}")
            duree = ecrire_wav(f, pcm)
        fin_dispo = LIGNES[i][0] if i < len(LIGNES) else DUREE_TOTALE
        alerte = "  ⚠ dépasse la scène" if debut + duree > fin_dispo else ""
        print(f"ligne {i} : {duree:.2f} s (de {debut:.1f} à {debut + duree:.1f} s){alerte}")
        fichiers.append((debut, f))
    # Assemblage calé sur la vidéo
    cmd = ["ffmpeg", "-y", "-v", "error"]
    for _, f in fichiers:
        cmd += ["-i", str(f)]
    filtres = [f"[{k}:a]adelay={int(d * 1000)}|{int(d * 1000)}[a{k}]" for k, (d, _) in enumerate(fichiers)]
    filtres.append("".join(f"[a{k}]" for k in range(len(fichiers))) +
                   f"amix=inputs={len(fichiers)}:normalize=0,apad,atrim=0:{DUREE_TOTALE}[out]")
    cmd += ["-filter_complex", ";".join(filtres), "-map", "[out]", "-ar", "48000", str(sortie / "voix-off.wav")]
    subprocess.run(cmd, check=True)
    print(f"OK : {sortie / 'voix-off.wav'}")


if __name__ == "__main__":
    main()
