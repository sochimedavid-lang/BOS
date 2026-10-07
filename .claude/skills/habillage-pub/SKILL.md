---
name: habillage-pub
description: Habille une pub vidéo finie avec HyperFrames — une phrase d'accroche animée en haut de l'écran pendant les premières secondes, et une carte de fin animée (produit détouré, nom, bénéfice, livraison gratuite, paiement à la livraison, bouton « Order now » qui pointe vers le bouton de la pub) collée à la fin. Utilise ce skill après le montage d'une créa (phase 6 de creative-ia-center / montage-pub-ia), ou dès que l'utilisateur veut ajouter une « phrase d'accroche en haut », un « hook en haut », une « carte de fin », un « CTA de fin », une « end card » ou « habiller » une pub, même finie et même faite ailleurs.
---

# Habillage pub (accroche + carte de fin)

Deux ajouts validés par l'utilisateur sur sa pub Kinoki : la carte de fin « donne plus envie de commander », et la
phrase d'accroche animée sert à **intégrer l'accroche en haut au début des vidéos**. Le reste de la pub (scènes,
voix, sous-titres karaoké) vient de `creative-ia-center` + `montage-pub-ia` et n'est pas touché.

Un seul script fait tout : `scripts/habiller.py` (ci-dessous `$H`). Il rend l'accroche en vidéo transparente et la
carte de fin avec HyperFrames, puis pose l'accroche sur le début et colle la carte à la fin en **un seul encodage**
ffmpeg (son d'origine conservé, silence sous la carte).

## 0. Prérequis (une fois par machine)

- Node.js 22+, ffmpeg/ffprobe, Python 3. Sous Windows : `python` au lieu de `python3`.
- `npx hyperframes browser ensure` (télécharge Chrome Headless pour le rendu, ~150 Mo, une seule fois).

## 1. Rassembler les entrées

Dans le dossier de la créa (`crea-N-<nom>/`), crée `habillage.json` à partir de `config.example.json` :

| Champ | D'où il vient |
|---|---|
| `video` | le rendu validé de `montage-pub-ia` (`renders/<nom>-vN.mp4`) |
| `hook.lines` | une des 2-3 accroches alternatives de `script.md`, ou une nouvelle ; 1 à 3 lignes courtes, 1 à 2 mots surlignés (`highlight`) |
| `hook.end` | la fin de la 1re phrase de la voix (temps des mots dans `captions/whisper-words.json`), en général 2,5 à 4,5 s |
| `endcard.product_image` | un **packshot PNG détouré** (fond transparent) : la planche emballage de la phase 5a ou la photo de la page produit. Sans PNG détouré, détoure une image nette (voir § Détourer) |
| `endcard.title`, `subtitle` | nom du produit + bénéfice en une phrase, tiré de la fiche produit |
| `endcard.perks` | uniquement des faits vrais : « Free delivery », « Pay on delivery »… |
| `endcard.kicker` | bandeau du haut (« Free delivery today » est autorisé par l'utilisateur) |
| `endcard.accent` | couleur de la marque / de l'emballage (vert `#1f9d55` par défaut) |

La langue est celle de la pub. Le texte de l'accroche et de la carte suit `creative-ia-center` →
`references/conformite.md` : pas de santé du spectateur à la 2e personne (« Tired every morning? » est à éviter ;
« Her bedtime habit changed her mornings » passe), pas de promesse chiffrée ou datée, pas de fausse urgence, et
**pas de prix** (`endcard.price` reste absent sauf décision explicite de l'utilisateur pour cette pub).

## 2. Aperçu avant rendu

```bash
python3 $H habillage.json --preview
```

Produit une image de l'accroche (fond transparent) et une de la carte de fin dans `habillage-build/*/snapshots/`.
Regarde-les, puis superpose l'accroche sur une image de la vidéo au même instant pour vérifier :

- l'accroche reste dans la zone haute sans couvrir le visage ni le produit (`hook.top`, 280 px par défaut = sous la
  zone d'interface des Reels ; descendre ou monter par pas de 40 px) ;
- elle ne double pas un titre déjà incrusté dans la vidéo ;
- la carte est lisible, le produit est net (packshot d'au moins 600 px de haut, sinon il paraît flou).

Montre les deux aperçus à l'utilisateur avant le rendu final.

## 3. Rendu

```bash
python3 $H habillage.json      # -> "out" du fichier de config
```

Ordre de grandeur : 1 min 30 pour une pub de 20 s sur une machine à 4 cœurs (accroche 25 s, carte 20 s, encodage
final ~40 s). Sur le PC de l'utilisateur (2 cœurs, souvent chargé), compter plusieurs fois plus : lancer en arrière-plan
avec un délai long, ne pas promettre de durée.

Vérifie avant d'envoyer : durée = vidéo + carte, une planche d'images (début, milieu de l'accroche, sortie de
l'accroche, carte), et le volume (`volumedetect`). Envoie avec `SendUserFile` et nomme les moments à regarder :
l'apparition de l'accroche, sa sortie, l'arrivée du bouton.

## 4. Corrections

| L'utilisateur dit | Faire |
|---|---|
| « l'accroche cache son visage » | changer `hook.top` (ou passer à 1-2 lignes) → `--preview` → rendu |
| « l'accroche reste trop / pas assez » | changer `hook.end` |
| « change le texte » | `hook.lines` / `endcard.*` → rendu (pas besoin de refaire le montage) |
| « la carte est trop courte » | `endcard.duration` (3,2 s par défaut ; 3 à 4 s) |
| « mets le prix » | `endcard.price` (et `old_price` barré si une vraie promo existe) — seulement sur sa demande |
| « autre style d'accroche » | `hook.style` : `boites` (fond noir, défaut, assorti aux sous-titres), `blanc`, `contour` |

## Détourer un produit

Si seule une photo avec fond existe : découpe le produit (`ffmpeg -vf crop=...` sur une image nette de la vidéo ou la
photo) puis détoure avec `rembg` (modèle `isnet-general-use`, ~180 Mo téléchargés une fois) :

```bash
pip install "rembg[cpu]"
python3 -c "from rembg import remove,new_session;from PIL import Image;o=remove(Image.open('in.png'),session=new_session('isnet-general-use'));o.crop(o.getbbox()).save('produit.png')"
```

Le `remove-background` de HyperFrames est entraîné sur les personnes : il ne convient pas aux emballages.

## Fichiers

| Fichier | Rôle |
|---|---|
| `scripts/habiller.py` | aperçu (`--preview`) ou rendu complet |
| `templates/hook.html` | composition HyperFrames de l'accroche (scène 1080×1920 mise à l'échelle de la vidéo, fond transparent) |
| `templates/endcard.html` | composition de la carte de fin (dernière image floutée, rayons, produit, bénéfices, bouton, flèche) |
| `config.example.json` | modèle de `habillage.json` (exemple Kinoki) |
| `assets/fonts/` | Montserrat ExtraBold (même police que les sous-titres karaoké) + Inter, licences OFL |
