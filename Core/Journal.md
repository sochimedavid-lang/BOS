# Journal

## 2026-10-12 — Onboarding
- Onboarding complété. Niveau : pré-lancement (0 vente, 0 audience, budget pub dispo).
- Projet : 2 formations (A motion design IA middle ticket, B pubs IA Higgsfield low ticket). Marché Bénin, puis CI. Acquisition Meta + TikTok Ads.
- Objectif : 3 M FCFA/mois. Palier 1 : 10 ventes en 14 jours.
- Décision BOS : lancer A seul, en prévente + cohorte live (démarrage 19/10), via Meta click-to-WhatsApp. B en attente. « Pôle entrepreneurs » sorti de A.
- Bottleneck : offre non validée par le marché.
- Points ouverts : origine/montant des preuves, compétence motion de l'entrepreneur, budget pub/jour.

## 2026-10-12 — Décisions de lancement
- Validé : formation motion d'abord, garantie 7 jours, « pôle entrepreneurs » retiré.
- Changements de l'entrepreneur : site + paiement Chariow (pas de vente par WhatsApp) ; prix 9 900 FCFA (lancement) puis 15 000 ; pas de lives ; communauté WhatsApp après achat ; objectif 10 ventes avant dimanche ; lancement mardi soir / mercredi.
- BOS : page de vente V1 construite. Points ouverts : vidéo existante qu'il veut utiliser comme contenu (droits ?), méthode exacte MTN MoMo pour payer Claude, preuves.

## 2026-10-12 — Refonte de la page
- L'entrepreneur rejette la page V1 (pas assez pro/belle). Concurrent fourni : Ibrahim Oué (analysé → Business.md › Concurrence).
- BOS : 3 directions visuelles maquettées (A Studio, B Cinéma, C Afro-moderne) → `Output/site/directions/`. En attente du choix.
- Question critique posée : la « personne aux contrats de 500 000 F » est-elle Ibrahim Oué ? Si oui, ses preuves ne sont pas utilisables.
- Retour : aucune des 3 directions ne plaît. La personne aux preuves n'est pas Ibrahim Oué. Selon l'entrepreneur, les « 15 000 apprenants » d'Ibrahim sont faux.
- BOS : on change de méthode → références de goût de l'entrepreneur avant toute nouvelle maquette.

## 2026-10-12 — Page de vente finale (V2)
- L'entrepreneur adore le style D2 (tech chaleureux) ; références de goût : ofmstarter.com (captures fournies).
- BOS : page finale `Output/site/index.html` sur la structure d'OFM Starter, adaptée sans faux témoignages : hero + lecteur vidéo + « ce qui est inclus » (valeur estimée 80 000 F → 9 900 F), chiffres produit, bandeau, démo « phrase → vidéo », « pourquoi 9 900 F », exemples, programme, grille de prix, 3 étapes, manifeste, garantie, FAQ, carte finale, avertissement revenus.
- Emplacements prêts (cachés tant que vides) : vidéo de présentation, témoignages, preuves. Tout se règle dans le bloc CONFIG.
- V1 archivée : `Output/site/v1-rejetee.html`.

## 2026-10-12 — Nom du produit
- BOS a proposé Motion Starter (reco), Motion 7, Studio IA, Prompt Motion. L'entrepreneur choisit « Vibe Motion ».
- BOS a déconseillé (nom du challenge d'Ibrahim Oué). Vérif. bibliothèque pub Meta : aucune pub « Vibe Motion » active, mais Ibrahim a déjà fait des pubs (sept. 2025, juin 2026) et des affiliés diffusent des pubs à son nom (dont une créée le 11/10/2026). Décision de l'entrepreneur respectée.
- Page renommée « Vibe Motion ». Description Chariow rédigée : `Output/2026-10-13_Description_Chariow_Vibe_Motion.md`.

## 2026-10-13 — Visuels Chariow
- Vignette 1200×1200 (1:1, sans texte superposé) et bannière 1620×600 (ratio 2,7) aux formats recommandés par Chariow → `Output/visuels/`.

## 2026-10-13 — Guide PDF (produit livré par Chariow)
- `Output/formation/Vibe-Motion-Guide.pdf` (~31 p.) : bienvenue, lexique, modules 0 à 5 complets avec instructions à copier, 50 instructions bonus, plan 7 jours, garantie.
- Vérifié : install Claude Code (docs officielles), Claude Pro requis pour Claude Code, Bénin et CI dans les pays supportés, carte virtuelle MoMo Card MTN Bénin (CG déc. 2025), commande skills Remotion `npx skills add remotion-dev/skills`.
- À compléter : lien communauté WhatsApp + contact support (repères rouges dans le PDF).
- Guide basculé de Remotion vers HyperFrames (demande de l'entrepreneur : c'est l'outil qu'il a testé). Prérequis ajoutés : Node 22+, FFmpeg, `npx skills add heygen-com/hyperframes`, `npx hyperframes browser ensure`, preview/render. Sources : quickstart + GitHub HyperFrames.
