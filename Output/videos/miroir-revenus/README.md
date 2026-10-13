# « Tes revenus sont le reflet de tes habitudes » : motion vertical

Adaptation en français de la référence n° 1 du dossier « à reproduire ». On garde la même structure, le même rythme et la même grammaire visuelle (personnages-bulles en verre, dégradés bleus, cartes d'interface, coupes diagonales, lentille, titre condensé). Le contenu est réécrit : texte, interfaces, chiffres.

- **Format :** 1080×1920, 60 i/s, 24,6 s.
- **Voix :** ElevenLabs « Micha », une seule prise (`audio/prise-N.mp3`, 4 prises disponibles).
- **Sorties :**
  - `out/final.mp4` : la vidéo ;
  - `out/poster.png` : l'affiche ;
  - `out/contact.png` : la planche d'images clés.
- **Sources :**
  - `index.html` : composition HyperFrames + GSAP ;
  - `sound.py` : musique et bruitages synthétisés, plus la voix ;
  - `docs/shotlist.md` : le storyboard.
- **Référence :** `refs/reference.mp4`, pour étude uniquement. Non versionnée.

## Changer de prise de voix et refaire le rendu
```bash
python3 sound.py 3        # 1, 2, 3 ou 4 → audio/mix.wav
npx -y hyperframes@0.8.150 render --output out/final.mp4 --quality high --fps 60
```
