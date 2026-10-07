# Journal

## 2026-10-07
- Installé les skills HyperFrames (heygen-com/hyperframes). Règle de répartition ajoutée dans CLAUDE.md : pubs avec scènes réalistes → `creative-ia-center` (méthode actuelle, inchangée) ; graphisme animé (texte, prix, sous-titres, incrustations, packshot 3D simple) → HyperFrames.
- Test capacité HyperFrames sur une pub fictive de 10 s (huile capillaire « KORA », 15 000 FCFA, paiement à la livraison), en 2 versions : 3D (modèle 3D animé + flacon) et humain natif (illustration plate). Rendus dans `Output/2026-10-07_test-hyperframes/`.
- Constat : HyperFrames ne génère pas de personnes réalistes. Humain réaliste possible seulement via un avatar HeyGen face caméra (compte HeyGen requis, non testé). En 3D, il anime des modèles existants mais n'en crée pas.
- Test combinaison sur une vraie vidéo (Kinoki, face caméra, sous-titres déjà incrustés) : ajout avec HyperFrames d'une accroche animée, d'un badge produit, d'une pastille « tonight → fresh morning » et d'une carte de fin CTA (+3 s). Rendu : `Output/2026-10-07_test-hyperframes/kinoki-avec-couche-hyperframes.mp4` (2 min de rendu). Faute repérée dans l'original : « CLICK BELLOW » → « BELOW ».
