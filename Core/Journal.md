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

## 2026-10-13 — Paiement branché
- Produit Chariow créé : https://peryal.mychariow.shop/prd_zqv7lcu4/checkout (boutique « peryal »). Branché sur tous les boutons de la page de vente (lien direct plutôt que widget, pour garder le design).
- Widget Chariow intégré à la demande de l'entrepreneur : bouton natif masqué, nos 6 boutons ouvrent la fenêtre de paiement Chariow (couleur #F4511E) ; repli automatique sur le lien de paiement si le widget ne charge pas. Testé : widget chargé + fenêtre ouverte au clic.
- Consigne de l'entrepreneur : livrer la page en HTML pour vérification ; c'est lui qui décide quand héberger.
- Lien communauté WhatsApp reçu et intégré au PDF (cliquable). Contact support provisoire : message privé à l'admin du groupe (en attente d'un numéro/e-mail dédié).
- Paiement 100 % dans la page : si le widget Chariow n'est pas chargé/bloqué, une fenêtre de secours affiche le même formulaire Chariow (iframe widget checkout) au lieu d'ouvrir la page Chariow. Testé : widget OK, secours OK, le visiteur reste sur la page.

## 2026-10-13 — Exemples motion : vidéo test HyperFrames
- HyperFrames 0.8.150 fonctionne dans l'environnement BOS (rendu local).
- Vidéo test « Menu du jour — Maquis Le Bon Goût » : 12 s, 1080×1920, 30 i/s, sans son → `Output/videos/menu-maquis/menu-maquis.mp4` (projet HyperFrames à côté). Contrôles HyperFrames OK (mise en page, contraste). En attente de validation du style avant les 5 autres.

## 2026-10-13 — Pub portfolio « Une nuit pour livrer le monde » (Noël, 3D isométrique)
- Demande : pub motion design isométrique sur le père Noël, pièce de portfolio, voix off Google TTS.
- Livré (sans voix) : `Output/videos/noel-isometrique/noel-isometrique.mp4` — 37 s, 1920×1080, 30 i/s, 6 scènes (île du pôle Nord, décollage 23:59→00:00, carte du monde isométrique Tokyo→Paris→Cotonou→New York, maison + zoom cheminée, salon, cadeau final + signature Vibe Motion). Script/storyboard : `script.md`.
- Bloqué : aucune clé Google dans l'environnement → voix off Google TTS impossible ici. Variable à ajouter : GEMINI_API_KEY (Gemini TTS) ou GOOGLE_API_KEY (Cloud TTS), visible dans une nouvelle session.
- Clé GEMINI_API_KEY ajoutée par l'entrepreneur dans les réglages de l'environnement (13/10). Invisible dans la session en cours : elle ne sera lue que par une nouvelle session.
- **À faire dès la prochaine session (« voix off Noël »)** : `python3 Output/videos/noel-isometrique/voix_off.py` → vérifier les durées (alerte si une phrase dépasse sa scène) → recaler les temps de l'animation si besoin → ajouter `<audio src="voix/voix-off.wav" data-start="0" data-duration="37">` dans `index.html` → `npx hyperframes@0.8.150 render --output noel-isometrique.mp4 --quality high` → envoyer la vidéo.
- Voix off générée avec Gemini TTS (voix « Sulafat », 6 phrases). Animations recalées sur la voix (mots « Tokyo », « Paris », « Une cheminée »… synchronisés) → durée 53,9 s.
- Livrés : `noel-isometrique-vertical.mp4` (1080×1920, avec voix) et `noel-isometrique-voix.mp4` (1920×1080, avec voix). Générateur : `gen.py`.
- Clé Gemini collée dans le chat par l'entrepreneur → enregistrée seulement dans `.env` (ignoré par git). Conseil donné : régénérer la clé. Quota gratuit : 3 requêtes/minute.
- Retour entrepreneur : version 54 s trop lente, voix trop lente → règle ajoutée dans CLAUDE.md (la voix s'adapte à la vidéo, rythme dynamique, bruitages par défaut).
- Version dynamique livrée : `noel-dynamique.mp4` (16:9) et `noel-dynamique-vertical.mp4` (9:16), 37 s, voix rapide calée segment par segment (villes une par une), ~45 bruitages synthétisés (souffles, clochettes, pops, clics d'horloge, boom, feu, chocs, scintillements), mixage -14 LUFS avec atténuation sous la voix. Scripts : `voix_dyn.py`, `voix3_gen.py`, `mix.py`, `gen2.py`.
- Quota Gemini gratuit : 10 voix/jour/modèle. 2.5-flash épuisé le 13/10 ; voix finale faite avec gemini-3.8-flash-tts (qui lit la consigne de style à voix haute → découpée, vérifiée par transcription).

### 2026-10-13 — Voix off Noël : prise unique
- Version 37 s (voix découpée) rejetée : le débit changeait d'une phrase à l'autre, tantôt trop rapide, tantôt lent.
- Nouvelle approche : tout le texte enregistré en une seule prise, avec deux moteurs à comparer.
  - ElevenLabs v4, voix « Paul K » (pub/bande-annonce) : 27,6 s, transcription propre.
  - Gemini 3.8 Flash TTS, voix Sulafat, sans consigne de style : 27,0 s.
- Fichiers dans Output/videos/noel-isometrique/voix-prise-unique/.
- Crédits ElevenLabs presque épuisés (102 restants, il en faut 376 par prise) : une seule prise générée sur les 4 prévues.
- En attente du choix de l'entrepreneur avant de recaler la vidéo.
- Choix : ElevenLabs (voix Paul K). Vidéo recalée sur cette prise : 33,3 s au lieu de 37, sans accélérer ni ralentir la voix, avec de courtes respirations aux changements de scène, couvertes par les bruitages. Rendu horizontal et vertical lancé (noel-11labs*.mp4).

### 2026-10-13 — Pub portfolio « STOPSCROLL »
- Brief motion design pro (storyboard d'abord, ressorts, son, boucle qualité) appliqué à un sujet choisi par BOS : STOPSCROLL, studio fictif de pubs motion pour e-commerçants.
- Objectif de la pub : « ta pub a 1 seconde pour arrêter le pouce ; une photo fixe se fait scroller, une pub qui bouge fait vendre ».
- Livré : Output/videos/stopscroll/out/final.mp4 (9:16, 60 i/s, 24 s, beat synthétisé + bruitages), plus affiche, planche, charte, storyboard et README. 4 passes de correction.
- Peut servir d'exemple n°1 sur la page de vente (l'exemple qui montre le « avant / après » vendable aux e-commerçants).
- Validé par l'entrepreneur. STOPSCROLL et la pub Noël (version ElevenLabs, verticale) ajoutées en tête de la section Exemples de la page de vente : 2 vraies vidéos, lecture muette quand elles sont visibles, bouton son. Versions web légères dans Output/site/media/ (1,1 Mo et 2,4 Mo). Paquet de mise en ligne mis à jour (pas encore hébergé : on attend le feu vert).
- Correction : l'entrepreneur veut visionner la page directement, pas de zip. Envoyé Output/site/apercu.html (un seul fichier, vidéos intégrées). Règle ajoutée dans CLAUDE.md.

### 2026-10-13 — Références « à reproduire » (11 vidéos Pinterest)
- Analyse : 7 sur 11 sont reproductibles en HTML. Les 3 photoréalistes et l'animation dessinée relèvent de la 3D ou de la vidéo IA. Recommandation acceptée : reprendre structure, rythme et effets, mais avec un contenu à nous (pas de copie à l'identique pour la vitrine).
- Vidéo n° 1 adaptée en « Tes revenus sont le reflet de tes habitudes » (version 2 du texte, choisie par l'entrepreneur). Voix ElevenLabs « Micha » (Nathan Roy demande le forfait Creator). ElevenLabs a été rechargé. Rendu : Output/videos/miroir-revenus/out/final.mp4, 24,6 s, 60 i/s.

### 2026-10-13 — Réf. n° 11 + kit « motion-kit »
- Vidéo n° 11 adaptée : pub du studio STOPSCROLL, avec Eden Food (restaurant) en client vedette. Texte version 2, voix ElevenLabs « Paul K » (prise 3). Output/videos/eden-studio/out/final.mp4, 32,5 s, 30 i/s.
- Demande de l'entrepreneur : aller plus vite sans perdre en qualité. Création du skill `.claude/skills/motion-kit` : briques d'animation, sous-titres automatiques, moteur de son générique, générateur de projet, méthode et garde-fous. Partageable avec les apprenants. Règle de vitesse ajoutée dans CLAUDE.md.
- ⚠ ElevenLabs a refusé 1 prise sur 4 : « activité inhabituelle, accès gratuit désactivé, passer à un abonnement payant ». Le compte est encore sur le palier gratuit, ou signalé. À régler avant les prochaines voix.
- Correction demandée : poubelle passée en blanc (elle était noire, peu visible) ; les étiquettes disparaissent dès qu'elles tombent dedans.

### 2026-10-13 — Vidéo SERVTHEM (restauration collective, à partir de leur affiche)
- Réalisée avec le kit : l'assiette sert de fenêtre, une cloche dorée révèle chacun des 4 engagements, les secteurs tournent en orbite, parallaxe en 3 bandes, slogan écrit à la main, contact. Voix « Micha » (prise 2). Photos Pexels (visages et plats africains). Logo recréé en vectoriel d'après l'affiche (à remplacer par le logo HD du client).
- Output/videos/servthem/out/final.mp4, 27 s, 30 i/s.
- Correction : uniquement des personnes afro dans les visuels (règle ajoutée). Bande parallaxe refaite avec 3 visages afro (chef, cheffe, cheffe qui dresse).
- Version « chic » SERVTHEM dans le style Eden Food (fond fluide vert et or, frappe au clavier, pastille dorée, assiette centrale avec 4 icônes, vague crème des secteurs, coupes sur visages afro, LE PAYS, LE GOÛT DU SERVICE). Output/videos/servthem-chic/out/final.mp4. Kit : MK.rise/exitUp masquent les textes avant et après (plus rien ne dépasse).

### 2026-10-13 · Portfolio : référence n°4 → « Eden Food, le récit » (`Output/videos/eden-recit`)
- Adaptation de la réf. 4 (récit de marque, gobelet produit, cartes photo en rotation 3D) pour Eden Food, Cotonou. 15,5 s, voix Micha (ElevenLabs, une prise), photos Pexels de personnes afro, nappe ambient + bruitages, -14 LUFS.
- Corrections avant rendu : titres qui débordaient (Eden Food, l'expérience, moments.), feuille qui masquait un titre. Rendu unique en 55 s.

### 2026-10-13 · Portfolio : référence n°9 → « Sikaflow » (`Output/videos/sikaflow`)
- Pub d'appli fintech fictive (gestion d'argent pour freelances et commerçants, Mobile Money, F CFA). 25,5 s, voix Paul K en une prise, musique pulse + bruitages, -14 LUFS.
- Corrections avant rendu : tableau de bord absent sur l'écran de fin, icônes et billets passant devant le texte, émojis sur « GRATUIT ».

### 2026-10-13 · Portfolio : référence n°6 → « Rempart Défense » (`Output/videos/rempart`)
- Pub d'un service de cybersécurité fictif pour PME (intro dorée → univers sarcelle néon, bouclier 3D, jauge, CTA démo). 25,8 s, voix Paul K, -14 LUFS.
- ElevenLabs : 3 prises sur 4 refusées (« Free Tier access disabled, unusual activity »). Une prise est passée. Risque de blocage total : passer sur un forfait payant (Starter) avant la prochaine vidéo.
