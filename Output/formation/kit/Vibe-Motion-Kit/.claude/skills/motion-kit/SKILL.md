---
name: motion-kit
description: Crée des vidéos motion design verticales (pubs, posts, portfolio) avec Claude + HyperFrames, vite et sans baisser la qualité. Kit de briques déjà testées (ressorts, personnages-bulles, cartes, coupes diagonales, lentille, frappe au clavier, compteurs, fond fluide), sous-titres automatiques depuis la voix off, bande-son générée (musique + bruitages + voix, mixée à -14 LUFS) et méthode de contrôle avant rendu. Utilise ce skill dès qu'on demande une vidéo motion, une pub animée, une reproduction de référence (« refais cette vidéo en français »), une vidéo pour un client ou un exemple de portfolio.
---

# Skill : Motion Kit

## Objectif

Produire une vidéo motion verticale (1080×1920) de qualité « portfolio » en **15 à 25 minutes** au lieu de 45, à partir d'un brief ou d'une vidéo de référence. Le résultat :
- `out/final.mp4` (30 i/s, son à -14 LUFS) ;
- `out/contact.png` (planche d'images clés) ;
- `out/poster.png` (affiche) ;
- les sources, réutilisables.

Le travail est fini quand la planche a été relue, que `check` n'affiche aucune erreur réelle et que le rendu final a été fait **une seule fois**.

## Croyances

- **La voix d'abord, en une seule prise.** On écrit le texte, on génère la voix d'un seul tenant (ElevenLabs de préférence), puis l'animation se cale sur les mots. Une voix découpée phrase par phrase puis accélérée donne un débit irrégulier que l'oreille repère tout de suite.
- **C'est la vidéo qui suit la voix, et le rythme reste dynamique.** Chaque changement visuel tombe sur un mot ou un temps fort. On ne rallonge jamais une vidéo pour caser une voix lente : on réécrit le texte plus court.
- **Le son fait la moitié de la perception.** Les bruitages sont présents par défaut : souffle sur chaque transition, « pop » sur chaque apparition, impact sur les temps forts. Une vidéo muette paraît amateur même si l'image est parfaite.
- **On copie la grammaire d'une référence, pas son contenu.** Rythme, transitions et effets peuvent être repris à l'identique. Texte, marques, logos et chiffres sont toujours les nôtres. Copier la pièce d'un autre studio pour sa vitrine, c'est risquer sa crédibilité dès que quelqu'un reconnaît l'original.
- **Assembler plutôt qu'écrire.** Toute brique déjà validée (`MK.*`) bat du code neuf : elle a déjà survécu aux pièges. On n'écrit du code neuf que pour ce qui rend la vidéo unique.
- **Décider puis montrer.** On lance avec la meilleure recommandation (texte, voix, marque) et le client ou l'entrepreneur corrige après. Attendre une validation à chaque étape coûte plus cher qu'une correction.
- **On contrôle sur captures, on rend une seule fois.** Une planche d'images coûte 1 minute, un rendu en coûte 2 à 3. Les erreurs se trouvent sur les captures.

## Process

### Phase 0 : cadrage (2 min)
- Lire la référence s'il y en a une, ou le brief.
- Pour une référence : en extraire une planche dense (`ffmpeg … fps=2,tile=…`) et la transcription (`npx -y hyperframes@0.8.150 transcribe ref.mp4 -e whisper -m small --json`).
- Noter les scènes et leurs temps, la palette, les polices et les transitions.

### Phase 1 : texte (3 min)
- Écrire le texte de la voix off en **français oral**, avec des phrases courtes et le même nombre de temps que la référence.
- Proposer une version recommandée et 1 ou 2 variantes en une seule fois, puis lancer avec la recommandée sauf contre-ordre.

### Phase 2 : voix (3 min)
1. **ElevenLabs** (`creative_list_voices`, puis `creative_generate_speech` avec le modèle `eleven_v4`).
   - Voix testées en français : « Micha » (grave, posée), « Paul K » (pub, bande-annonce).
   - Certaines voix exigent un forfait payant.
2. Télécharger les prises dans `audio/`, les transcrire et choisir la plus nerveuse.
3. **Solution de secours gratuite :** Gemini TTS. Le modèle 3.8 lit à voix haute la consigne de style : ne pas en mettre.

### Phase 3 : projet et sous-titres (1 min)
```bash
python3 <skill>/tools/new_project.py videos/<nom> <durée_s>
python3 <skill>/tools/captions.py audio/prise-N.json --start 0.4 --fix "kotonu=Cotonou" > captions.json
```
`captions.json` donne les instants des mots. On s'en sert pour les sous-titres (`MK.captions`) **et** pour placer chaque animation.

### Phase 4 : composition (8 à 12 min)
- Dans `index.html`, une scène = un `div.sc`, avec la visibilité gérée par `MK.scenes`.
- On anime avec les briques `MK.*` (catalogue plus bas).
- Les états de départ se posent avec `gsap.set`, les animations avec `tl.to(…, t)`.
- On termine par `MK.done(tl, TOTAL)` puis l'enregistrement de la timeline :

```js
window.__timelines = window.__timelines || {};
window.__timelines["main"] = tl;
tl.seek(0);
```

### Phase 5 : son (2 min)
Remplir `sound.json` :
- la voix et son instant de départ ;
- la musique : `pulse` (beat) ou `ambient` (nappe), avec ses sections ;
- un bruitage par événement visuel.

Puis : `python3 <skill>/tools/sound.py sound.json` → `audio/mix.wav`.

### Phase 6 : contrôle (3 à 5 min)
```bash
npx -y hyperframes@0.8.150 snapshot --at 1.5,4,7,… --no-end --describe false -o /tmp/snap
npx -y hyperframes@0.8.150 check
```
1. Relire la planche et noter les 3 plus gros défauts : texte qui déborde ou qui est caché, accent coupé, moment mort, élément parasite, mauvais calque.
2. Corriger, puis refaire une capture **uniquement** sur les temps concernés.

### Phase 7 : rendu unique (2 à 3 min)
```bash
npx -y hyperframes@0.8.150 render --output out/final.mp4 --quality high --fps 30
```
Ensuite, générer la planche (`ffmpeg -ss t … tile=7x2`) et l'affiche, puis envoyer la vidéo.

## Catalogue des briques (`kit/motion-kit.js`, objet `MK`)

| Brique | Effet |
|---|---|
| `MK.ease.ui / card / type` | Ressorts : nerveux (pastilles), moyen (cartes), lourd (grande typo) |
| `MK.scenes(tl, [[sel, début, fin]], total)` | Visibilité des scènes |
| `MK.captions(tl, "#cap", chunks)` | Sous-titres (sortie de `captions.py`) |
| `MK.rise(tl, sel, t)` | Texte qui monte depuis un masque `.m` (le masque s'ajuste seul aux accents) |
| `MK.pop / slide / fadeIn / stamp` | Apparitions : ressort, glissé, fondu, tampon |
| `MK.exitUp(tl, sel, t)` | Sortie vers le haut |
| `MK.type(tl, sel, "texte", t)` | Frappe au clavier |
| `MK.count(tl, sel, de, à, t, durée)` | Compteur |
| `MK.marquee(tl, sel, t, durée, dx)` | Défilement horizontal |
| `MK.draw(tl, path, t)` · `MK.follow(tl, el, path, t)` | Tracé SVG qui se dessine, objet qui suit un tracé |
| `MK.diagonal(tl, panel, edge, t)` | Coupe diagonale avec bord lumineux (`.diag`, `.edge`) |
| `MK.circleIn / circleOut` | Révélation circulaire |
| `MK.wipeUp` | Volet plein écran qui monte |
| `MK.lens(tl, sel, tIn, tOut)` | Anneau de verre qui traverse la caméra (`.ring`) |
| `MK.shake / pulse` | Secousse, pulsation sur des temps |
| `MK.person(parent, x, y, échelle)` | Personnage-bulle en verre bleu |
| `MK.fluid(parent, couleurs)` + `MK.drift(tl, taches, total)` | Fond fluide flou qui dérive |
| `MK.split(sel)` | Découpe un texte en lettres `.ch` |

Styles (`kit/motion-kit.css`) :
- fonds : `.bg-light`, `.bg-night` ;
- cartes : `.card-light`, `.card-dark` ;
- textes et repères : `.pill`, `.hl` (surlignage), `.display` (titre condensé) ;
- verre : `.ring`, `.bubble`, `.sphere` ;
- disques d'icônes : `.icon-disc`.

## Output

- `out/final.mp4` : 1080×1920, 30 i/s (60 seulement si on le demande).
- `out/contact.png` et `out/poster.png`.
- Sources : `index.html`, `kit/`, `sound.json`, `audio/`, et `docs/shotlist.md` s'il y a une référence.

## Garde-fous

- **Jamais de `Math.random()`, de timer ni de transition CSS.** Le hasard passe par `MK.rng(graine)`, tout est fonction du temps.
- **Jamais de `fromTo` sans réfléchir.** Il applique son état de départ dès le montage, et un élément invisible peut apparaître à t = 0. Utiliser `gsap.set` + `tl.to`, ou `immediateRender: false`.
- **Jamais une scène avec `z-index` au-dessus des sous-titres.** `#cap` est à `z-index: 50`.
- **Jamais de texte de grande taille dans un `.m` sans `MK.rise`** (ou sans `font-size` sur le `.m`) : les accents des capitales (É, À) seraient coupés.
- **Ne pas animer `letterSpacing`, ni appeler `getBBox` sur une scène cachée.** Calculer les origines de transformation à la main.
- **Un flou CSS très large (`.fluid`, 90 px) ralentit le rendu.** Le limiter à un seul fond.
- **Whisper invente parfois « Sous-titres réalisés par… » sur le silence final.** `captions.py` l'ignore. Corriger les noms propres avec `--fix`.
- **`check` signale à tort :**
  - les textes masqués en attente : « text_occluded » ;
  - les superpositions voulues : « content_overlap » ; les marquer `data-layout-allow-overlap` ;
  - les éléments décoratifs : les marquer `data-layout-allow-occlusion` ou `data-layout-allow-overflow`.
- **Ne jamais reprendre logos, marques ou chiffres réels d'une référence**, et ne jamais présenter des chiffres fictifs comme des résultats réels.

## Checklist de qualité

- [ ] L'accroche se comprend sans le son dans les 2 premières secondes.
- [ ] Jamais plus de 2 s sans changement visible.
- [ ] Chaque temps fort visuel tombe sur un mot ou un temps de la musique.
- [ ] Aucun texte sous 30 px, aucun débord, aucun accent coupé.
- [ ] Une seule prise de voix, à débit constant ; bruitages sur les transitions et les apparitions.
- [ ] `check` : 0 erreur réelle. Planche relue. Un seul rendu final.
