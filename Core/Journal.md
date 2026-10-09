# Journal

## 2026-10-07
- Analyse créas Meta v2 reçue (compte Peryal Gambie, 31/08 → 07/10) : archivée dans Output/.
- Recoupement Cashel : 52 % des commandes sans statut final, taux de livraison non mesurés. Batana passe de « point mort » à « déficitaire ». Le bottleneck se déplace des créas vers le traitement des commandes.
- Décision proposée : rappel des commandes ouvertes avant production de nouvelles créas ; plan de flotte réduit de 23 à 8–10 créas.
- Retour entrepreneur : Batana reste actif ; non-livraisons COD acceptées comme réalité du marché (règle ajoutée dans CLAUDE.md). Focus : créas Miracle Balm et Kinoki.
- Angles créas d'origine conservés malgré le risque de conformité signalé. Prix Kinoki fixé à 1 650 GMD (Cashel mis à jour). Recherche faite par BOS : 4 documents fondateurs par produit. Découvertes : acheteurs majoritairement masculins (MB ~80 %), 30 % de commandes Kinoki multi-boîtes, achat calé sur le salaire et validé par un proche.
- Script MB-1 v0 écrit (témoignage Mama Fatou + fils au port). Vidéos gagnantes non récupérables via Meta : fichiers demandés à l'entrepreneur.
- 08/10 : swipe fait sur 4 vidéos. Découverte : 3 gagnantes MB sont des pubs américaines « Senzio » reprises (nom de marque, ingrédients et garantie 60 j différents du produit réel).
- 08/10 : organisation MB-1/2/3 validée ; « natural herbal formula » ; garantie 30 j. Script MB-1 v1 (nerfs) écrit.

### 2026-10-08 (suite) — Voix off MB-1
- ElevenLabs connecté. Voix off MB-1 (accroche A + corps) générée en 2 versions sur eleven_v4 : Christophe 108,9 s, Olaniyi Victor 121,0 s. Coût : 2 × 1 729 crédits (~1,26 $).
- Contrôle par transcription : texte complet sur les deux, aucun mot sauté. Choix de la voix en attente de l'entrepreneur.
- 3e version de la voix off MB-1 avec Christopher Smooth (voix américaine grave, choisie par l'entrepreneur) : 111,3 s, texte complet. Coût : 1 729 crédits (~0,63 $). Total voix MB-1 : 5 187 crédits (~1,89 $).
- Voix MB-1 retenue : Christopher Smooth. Accroche B générée (11,4 s, 166 crédits). Total voix MB-1 : 5 353 crédits (~1,95 $).
- Storyboard MB-1 v1 livré : 40 plans calés au mot près sur la voix (36 version A + 4 accroche B), 3 portraits de référence. Prochaine étape côté entrepreneur : générer les images sur Higgsfield.
- Portraits de référence MB-1 générés par l'entrepreneur et validés (Awa, Ebrima, Mariama). Mariama : dents normales, sans écart (choix de l'entrepreneur). Descriptions du storyboard alignées sur les portraits.
- 1re série d'images MB-1 reçue (A1, A2, A3, A4, 17). A1, A2, A4 validées. Plan 17 : « SENZIO » écrit sur la boîte et le pot, à corriger. A3 : petit texte illisible au-dessus du nom, à corriger aussi. Référence produit propre créée (references/produit.png) et règle ajoutée aux prompts : aucun autre nom de marque.
- Images A3 et 17 gardées avec « SENZIO » sur l'emballage (décision de l'entrepreneur). Script MB-2 v1 écrit (jambes lourdes, Binta et sa fille, anime 2D, ~2 min 10).
- 40 images finales MB-1 reçues (4 zips) et validées : 39 plans couverts, le plan 35-36 (livreur) en une seule image de 5 s, 1 image en réserve (Awa main sur le cœur). Plus aucun « SENZIO » : A3 et 17 refaites avec « ximonth ». Fichier kling-prompts.md prêt pour l'animation.
- Animation MB-1 : 39 clips Kling 3.0 standard (292,5 crédits Higgsfield). Correction de l'entrepreneur : jamais de qualité pro sans accord → règle ajoutée dans CLAUDE.md. 2 clips au pied déformé (09, B1) remplacés par un zoom lent sur l'image, sans coût.
- Montage MB-1 : versions A et B, voix -16 LUFS, fond musical ElevenLabs bouclé (Pixabay bloque l'accès automatique), bruitages ElevenLabs + HyperFrames, sous-titres karaoké majuscules jaunes copiés de Anc. Crea 2. Habillage : accroche en haut + carte de fin (Free delivery, Pay on delivery, 30-day money back).
- MB-2 : voix Christopher Smooth (1 943 crédits), storyboard anime 46 images.
- Originaux MB-1 A et B (124 et 119 Mo) : trop gros pour GitHub (fork public : >100 Mo et Git LFS refusés). Déposés sur Higgsfield (bibliothèque) et dans la bibliothèque vidéo Meta du compte **Peryal Gambie Secours** (vidéos 1606608711202069 et 4489490761290223) : l'outil d'envoi n'est pas encore activé sur le compte principal Peryal Gambie.
- MB-2 : style passé de l'anime 2D au 3D animé (décision de l'entrepreneur). Storyboard v2 régénéré, mêmes 46 plans et mêmes timecodes.
- MB-2 : 1er portrait de Binta refusé (rendu 3D trop réaliste). Style précisé : 3D cartoon façon Pixar, en tête de chaque prompt. Règle ajoutée dans CLAUDE.md.
- MB-2 : 2e essai de portraits (Binta trop réaliste, Isatou trop enfantine). L'entrepreneur veut le style de sa référence : personnages adultes caricaturés façon Les Indestructibles. Storyboard v4 : fiches personnages 3 vues en 16:9 avec la référence de style jointe.
- MB-2 : fiches Binta et Isatou validées (references/). Storyboard v5 : descriptions alignées sur les fiches, éclairage selon la scène.
- MB-2 : 46 images lancées sur Higgsfield (une génération par plan, 2K, 2 crédits l'image). 45 réussies, le 28 a échoué. Défauts repérés : 11 (homme en trop), 27 (personnage en trop sur le plan produit), 35 (Binta dupliquée) ; 20 en option (pieds dans la bassine avec les sandales). Régénération en attente de validation.
- MB-2 : 11, 20, 27, 28 et 35 refaites après validation (10 crédits). Cause des personnages en trop : le bloc de style décrivait des personnages, donc les plans vides en recevaient un. Correctif : bloc de style « décor » sans personnage pour les plans vides. 46/46 images prêtes.
- MB-1 : l'animation a été générée en 5 s par clip (292,5 crédits) alors que les durées utiles demandaient environ 199,5 crédits ; environ 93 crédits gaspillés. Règle ajoutée dans CLAUDE.md : durée de clip = durée utile au montage. MB-2 recalculé : 228 crédits au lieu de 345.
- MB-2 animé : 46 clips Kling 3.0 std aux durées utiles, 228 crédits au lieu de 345. Le 29 (manchon rose parasite) est remplacé par un zoom sur l'image. Montage A (126 s) et B (120 s) : voix Christopher Smooth, fond sonore de MB-1, 17 bruitages de la bibliothèque MB-1 (aucun nouveau), sous-titres karaoké découpés à la main, accroche écran + carte de fin. Exports 1080p dans `crea-2-lymphe/videos-finales/`.
- MB-2 : originaux HQ (96,5 Mo, réencodés sous la limite GitHub) sur GitHub et dans la bibliothèque Meta Peryal Gambie Secours (vidéos 1472046351452824 et 1789649565704172). K-1 : script v1 écrit (voix off, couple Lamin et Fatou, sans « toxins »), à valider.
- Correction de l'entrepreneur : les vidéos vont dans Peryal Gambie, pas dans Secours. Nouvel essai d'envoi sur Peryal Gambie : toujours refusé par l'outil Meta (déploiement progressif). Règle ajoutée dans CLAUDE.md ; import manuel par l'entrepreneur depuis les liens.
- K-1 validé : sans « toxins », voix off, Christopher Smooth, réaliste ; l'entrepreneur génère les images lui-même. Prompts des fiches Lamin et Fatou fournis.
- K-1 : voix Christopher Smooth en eleven_v4, une prise (corps + accroche A 68,0 s, 1 085 crédits ; accroche B 3,3 s, 61 crédits). Texte complet à la transcription.
- K-1 : storyboard v1 calé sur la voix (35 plans, prompts image et Kling, à joindre : fiches Lamin/Fatou ; pas de photo du vrai emballage). Animation estimée 159 crédits Higgsfield.
