# STOPSCROLL : pub motion (portfolio)

Pub verticale de 24 s pour **STOPSCROLL**, un studio fictif de pubs motion pour e-commerçants. C'est une pièce de portfolio, qui sert aussi d'exemple pour la page de vente Vibe Motion.

- **Objectif :** l'e-commerçant comprend que sa pub n'a qu'une seconde pour arrêter le pouce, qu'une photo fixe se fait scroller et qu'une pub qui bouge fait vendre. Ensuite, il écrit au studio sur WhatsApp.
- **Format :** 1080×1920 (9:16), 60 i/s, 24 s, son stéréo à -14 LUFS.

## Fichiers
| Chemin | Contenu |
|---|---|
| `out/final.mp4` | Rendu final |
| `out/poster.png` | Affiche (image à 11,9 s) |
| `out/contact.png` | Planche de 12 images clés |
| `index.html` | Composition HyperFrames (HTML + GSAP), fonction déterministe du temps |
| `sound.py` | Bande-son synthétisée (beat 120 BPM + bruitages calés sur l'image) → `audio/soundtrack.wav` |
| `docs/style_guide.md` | Charte (couleurs, typo, mouvement, son) |
| `docs/shotlist.md` | Storyboard plan par plan |
| `refs/` | Référence de goût (page de vente validée) |

## Refaire le rendu
```bash
python3 sound.py                                   # régénère la bande-son (numpy, scipy, ffmpeg)
npx -y hyperframes@0.8.150 check                   # contrôle (les textes masqués sont signalés à tort)
npx -y hyperframes@0.8.150 render --output out/final.mp4 --quality high --fps 60
npx -y hyperframes@0.8.150 snapshot --at 0.5,7.65,13.4 --describe false   # images de contrôle
```

## Notes techniques
- **Ressorts :** oscillateur amorti écrit à la main (`spring(z, w)`), utilisé comme ease GSAP, avec trois poids (interface, cartes, grande typo).
- **Aucun hasard non déterministe :** générateur pseudo-aléatoire à graine fixe, ni timer ni transition CSS.
- **Grille rythmique :** 120 BPM (un temps = 0,5 s). Les changements importants tombent sur les temps, et les bruitages de `sound.py` reprennent les mêmes instants que la timeline.
- **Continuité :**
  - le compteur devient le titre ;
  - la carte balayée revient vivante, puis retourne dans le flux ;
  - le point du « ? » devient le fond orange ;
  - un panneau orange monte et devient la marque.
- **Boucle qualité :** 4 passes de relecture.
  1. Parasite visuel (onde du tap visible dès le début), flux illisible dans l'accroche, logo ambigu.
  2. Trou dans la révélation de la marque, étiquette trop proche du compteur.
  3. Naissance de la bulle orange, entrée du flacon, temps de lecture de « Le pouce s'arrête. ».
  4. Équilibre de la carte de fin, sous-titre de la marque sous 30 px.
