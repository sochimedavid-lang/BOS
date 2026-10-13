# Charte visuelle STOPSCROLL

Références : `refs/gout-site-D2.png` (la page de vente validée par l'entrepreneur) et ofmstarter.com. On reprend leur grammaire visuelle, jamais leur contenu.

## Ce qu'on reprend des références
- **Un sombre chaud**, plutôt que du noir pur ou du bleu nuit : fond brun-noir, surfaces un cran plus claires, coins arrondis généreux.
- **Une seule couleur qui crie** (orange), une couleur « preuve / succès » (lime), le reste est crème et gris chaud.
- **Une typographie en contraste** : grotesque très gras et serré pour l'impact, serif italique pour le mot qui porte l'émotion (« avec l'IA », « premier client »).
- **Des étiquettes en petites capitales espacées**, en orange, au-dessus des titres.
- **Des pastilles (pills)** pour les infos de confiance : paiement, garantie, livraison.

## Couleurs
| Rôle | Valeur |
|---|---|
| Fond | `#100E0C` |
| Surface 1 / 2 | `#1A1714` / `#24201B` |
| Texte | `#F6F1EA` |
| Texte secondaire | `#A39A8F` |
| Accent (action, impact) | `#F4511E` |
| Accent clair | `#FF7A45` |
| Preuve / succès | `#DDF247` |
| Alerte (échec) | `#FF5A4E` |

Règle : une seule grande zone orange à l'écran à la fois. Le lime n'apparaît que pour un résultat positif.

## Typographie
- **Impact** : Bricolage Grotesque 800, interlettrage -0,05 em, interligne 0,88. Tailles de 150 à 420 px.
- **Émotion** : Instrument Serif italique, en général 1,1× la taille du grotesque voisin.
- **Information** : Inter 600/700, 34 à 44 px minimum (lisible sur téléphone).
- **Étiquettes** : Inter 700, 30 px, capitales, interlettrage 0,28 em, orange.
- Aucun texte sous 30 px. Marges latérales de 80 px minimum.

## Mouvement
- Des ressorts (spring) plutôt que des fondus : chaque élément arrive avec une masse.
  - **Petits éléments d'interface** (pastilles, prix) : ressort rapide et nerveux, léger dépassement.
  - **Cartes** : ressort moyen, dépassement discret.
  - **Grande typo** : ressort lourd, presque sans rebond (elle pèse).
  - **Caméra** : `expo.inOut` ou `power3.inOut`, jamais de ressort.
- Les transitions naissent d'un objet déjà à l'écran (le compteur devient le titre, la carte devient le flux, le bouton devient la marque) plutôt que d'un fondu au noir.
- Pas de lueurs, pas de particules aléatoires, pas de verre dépoli.

## Son
- 120 BPM (un temps = 0,5 s, une mesure = 2 s). Chaque changement important tombe sur un temps.
- Bruitages secs : clics du compteur, impact au gel, souffle sur les balayages, « pops » sur les pastilles, montée avant la marque.
