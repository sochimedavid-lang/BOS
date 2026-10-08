# MB-1 — Storyboard (v1, 08/10/2026)

Voix : **Christopher Smooth** (ElevenLabs `SSfU0eLfP3qeuR4j2bwD`, eleven_v4). Corps + accroche A : `voix-off-christopher-smooth.mp3` (111,3 s). Accroche B : `accroche-B-christopher-smooth.mp3` (11,4 s).
Timecodes = position exacte des mots dans la voix (transcription mot à mot).

## Comment produire
1. **Images (toi, Higgsfield Nano Banana Pro) :** copie le « Text-to-image prompt » de chaque plan. Pour tout plan où apparaît Miracle Balm, joins la photo produit (`01-recherche/fournisseur-visuels.jpg`, vignette en haut à gauche) en image de référence : sans elle, le texte de la boîte sera faux.
2. **Personnages :** portraits de référence validés le 08/10, dans `references/` (awa.webp, ebrima.webp, mariama.webp). Joins le bon portrait à chaque plan où le personnage apparaît : c'est ce qui garde les mêmes visages d'un plan à l'autre.
3. **Vidéos (Kling, image → vidéo) :** colle le « Image-to-video prompt ». Clips de 5 s, je les recoupe au montage à la bonne durée.
4. **Rythme :** la pub d'origine coupe toutes les ~1 s. Au montage, je découpe les plans de plus de 3 s en deux (zoom avant sur la 2e moitié) pour retrouver ce rythme sans générer plus d'images.
5. **Accroche B :** même vidéo, on remplace les plans A1–A4 par B1–B4 et la voix 0–12,40 s par le fichier accroche B.

## Blueprint de la référence (Anc. Crea 2 / Nouv. Crea 4)
- Format vertical 9:16, mélange de rushes « UGC » réalistes et de schémas anatomiques 3D (nerfs rouges sur le pied).
- Accroche « on vous a dit que c'était sans espoir » + question qui intrigue, en moins de 13 s.
- Plans très courts (médiane ≈ 1 s), zooms et flous de transition, aucune coupe lente.
- Caméra proche des visages et des pieds, mouvement à la main ; les schémas tournent ou avancent lentement.
- Fil visuel récurrent : nerfs qui brûlent en rouge → produit → nerfs apaisés.
- Personnages = utilisateurs ordinaires qui montrent la boîte ; le produit apparaît au nom puis à chaque bénéfice.
- Sous-titres karaoké mot par mot, mot actif en jaune, au centre de l'écran.
- Phases : accroche → preuve sociale → fausses solutions → percée + nom → mécanisme → mode d'emploi → garantie → appel (livraison, paiement à la livraison).

## Verrou personnages, voix, son et style

**Personnages (à recopier tels quels, c'est déjà fait dans chaque prompt)**
- **Awa** : Awa, a Gambian woman about 55 years old, medium build, deep dark-brown skin, round face with high cheekbones, warm brown eyes, small gold stud earrings, hair wrapped in an orange-and-indigo patterned head tie, wearing a loose orange-and-indigo wax-print kaftan.
- **Ebrima** : Ebrima, a Gambian man about 65 years old, slim and tall, very dark-brown skin, oval lined face with a short white-grey beard and close-cropped grey hair, thin gold-rimmed rectangular glasses, wearing a light-blue cotton kaftan with a tone-on-tone embroidered neckline and a white openwork crocheted kufi cap.
- **Mariama** : Mariama, a Gambian woman about 42 years old, slender, dark-brown skin, oval face with a warm smile and even teeth, long thin black braids parted in the middle and gathered behind her shoulders, small gold hoop earrings, wearing a bright yellow-and-green wax-print fitted top with puffed sleeves and matching wrap skirt.
- **Livreur (plans 35–36)** : a young Gambian delivery rider about 25 years old, athletic, dark-brown skin, short black hair, wearing a red polo shirt and a black open-face motorbike helmet.
- **Produit** : the Miracle Balm product: a small lime-green cardboard box with a dark-green leafy wreath illustration around bold white text 'MIRACLE BALM' and small white daisy flowers, next to a round silver metal tin (30 g) whose lid shows the same dark-green leaf wreath and 'MIRACLE BALM', the open tin revealing a smooth light-pink balm.
- **Schéma du pied** : a semi-transparent human foot and lower leg seen from the side, showing the fine network of nerves running from the ankle to the toes and thin blood vessels beside them.

**Styles**
- Réaliste : Photorealistic vertical 9:16 smartphone photo in authentic UGC style, natural warm West African light, true-to-life dark skin texture, shallow depth of field, no captions or added text overlays, no watermark.
- Schémas : Clean 3D medical-style illustration, vertical 9:16, semi-transparent warm-brown skin over visible anatomy, deep dark-navy background, soft cinematic rim light, no text, no labels.

**Images de référence personnages (à générer en premier, une fois)**
- Awa : `Awa, a Gambian woman about 55 years old, medium build, deep dark-brown skin, round face with high cheekbones, warm brown eyes, small gold stud earrings, hair wrapped in an orange-and-indigo patterned head tie, wearing a loose orange-and-indigo wax-print kaftan. Front-facing head-and-shoulders portrait, neutral light-grey background, soft even light, calm neutral expression. Photorealistic vertical 9:16 smartphone photo in authentic UGC style, natural warm West African light, true-to-life dark skin texture, shallow depth of field, no captions or added text overlays, no watermark.`
- Ebrima : `Ebrima, a Gambian man about 65 years old, slim and tall, very dark-brown skin, oval lined face with a short white-grey beard and close-cropped grey hair, thin gold-rimmed rectangular glasses, wearing a light-blue cotton kaftan with a tone-on-tone embroidered neckline and a white openwork crocheted kufi cap. Front-facing head-and-shoulders portrait, neutral light-grey background, soft even light, calm neutral expression. Photorealistic vertical 9:16 smartphone photo in authentic UGC style, natural warm West African light, true-to-life dark skin texture, shallow depth of field, no captions or added text overlays, no watermark.`
- Mariama : `Mariama, a Gambian woman about 42 years old, slender, dark-brown skin, oval face with a warm smile and even teeth, long thin black braids parted in the middle and gathered behind her shoulders, small gold hoop earrings, wearing a bright yellow-and-green wax-print fitted top with puffed sleeves and matching wrap skirt. Front-facing head-and-shoulders portrait, neutral light-grey background, soft even light, calm neutral expression. Photorealistic vertical 9:16 smartphone photo in authentic UGC style, natural warm West African light, true-to-life dark skin texture, shallow depth of field, no captions or added text overlays, no watermark.`

**Variations autorisées** : Awa et Ebrima retirent foulard, lunettes ou bonnet seulement au lit la nuit (plans B3, 08, 29) — c'est écrit dans le prompt concerné.

**Voix** : Narrator (off-screen): middle-aged American man, deep smooth baritone, warm polished promotional timbre, General American accent, steady measured pace with short dramatic pauses, confident and reassuring, persuasive without shouting.

**Son**
- **Voix :** une seule, le narrateur hors champ. Aucun personnage ne parle à l'écran, donc aucune synchronisation labiale.
- **Musique :** fond cinématique doux et émotionnel (piano feutré + nappes), environ 20 dB sous la voix ; petit pic sur le nom du produit (plan 17) ; énergie finale sur l'appel (32 à 36).
- **Ambiances :** propres à chaque lieu (nuit avec grillons, cour, marché), toujours basses.
- **Effets :** whoosh discret sur les changements de lieu ; pulsation grave sur les schémas de nerfs ; un effet maximum par plan.
- **Mixage :** la voix domine toujours. Sous-titres karaoké mot par mot ajoutés au montage, pas dans les images.

**Carte des voix** : 100 % narrateur hors champ, du premier au dernier plan.

---

## Accroche A (0 – 12,40 s)

### Plan A1 — 0.00 → 3.20 s

**Script section / voiceover text**
“For years, people with burning feet were told:”

**Text-to-image prompt**
Ebrima, a Gambian man about 65 years old, slim and tall, very dark-brown skin, oval lined face with a short white-grey beard and close-cropped grey hair, thin gold-rimmed rectangular glasses, wearing a light-blue cotton kaftan with a tone-on-tone embroidered neckline and a white openwork crocheted kufi cap. Sitting on the edge of a simple bed at night, bare feet on a concrete floor, holding one foot in both hands with a pained grimace, lit by a single warm bedside lamp, medium shot. Photorealistic vertical 9:16 smartphone photo in authentic UGC style, natural warm West African light, true-to-life dark skin texture, shallow depth of field, no captions or added text overlays, no watermark.

**Image-to-video prompt**
Ebrima (Gambian man ~65, short white-grey beard, gold-rimmed glasses, light-blue kaftan, white kufi) slowly rubs the sole of his foot and winces, eyes lowered to his foot. Slow push-in. Mood: weary, heavy. Visible characters do not lip-sync and keep their mouths closed or relaxed while the locked narrator says off-screen: “For years, people with burning feet were told:” Preserve faces, bodies, clothing, product design and rendering style exactly.

**Sound / voiceover direction**
Voix off narrateur hors champ — Narrator (off-screen): middle-aged American man, deep smooth baritone, warm polished promotional timbre, General American accent, steady measured pace with short dramatic pauses, confident and reassuring, persuasive without shouting. Segment `voix-off-christopher-smooth.mp3` de 0.00 à 3.20 s. Aucun personnage ne parle. Calme intérieur de nuit, grillons au loin. Effet : souffle grave à l'ouverture. Voix toujours dominante.

**Estimated length**
3.2 seconds

### Plan A2 — 3.20 → 5.88 s

**Script section / voiceover text**
“it's just old age. Nothing to do.”

**Text-to-image prompt**
Ebrima, a Gambian man about 65 years old, slim and tall, very dark-brown skin, oval lined face with a short white-grey beard and close-cropped grey hair, thin gold-rimmed rectangular glasses, wearing a light-blue cotton kaftan with a tone-on-tone embroidered neckline and a white openwork crocheted kufi cap. Sitting on a plastic chair in a sandy family compound in late afternoon, hands resting on his knees, looking down at his bare feet with a resigned expression, medium-wide shot. Photorealistic vertical 9:16 smartphone photo in authentic UGC style, natural warm West African light, true-to-life dark skin texture, shallow depth of field, no captions or added text overlays, no watermark.

**Image-to-video prompt**
Ebrima (Gambian man ~65, short white-grey beard, gold-rimmed glasses, light-blue kaftan, white kufi) lets out a slow sigh, his shoulders drop and he shakes his head slightly, eyes down. Static camera. Mood: resignation. Visible characters do not lip-sync and keep their mouths closed or relaxed while the locked narrator says off-screen: “it's just old age. Nothing to do.” Preserve faces, bodies, clothing, product design and rendering style exactly.

**Sound / voiceover direction**
Voix off narrateur hors champ — Narrator (off-screen): middle-aged American man, deep smooth baritone, warm polished promotional timbre, General American accent, steady measured pace with short dramatic pauses, confident and reassuring, persuasive without shouting. Segment `voix-off-christopher-smooth.mp3` de 3.20 à 5.88 s. Aucun personnage ne parle. Ambiance de cour : poules, voix lointaines. Pas d'effet. Voix toujours dominante.

**Estimated length**
2.7 seconds

### Plan A3 — 5.88 → 9.60 s

**Script section / voiceover text**
“Then a simple evening habit started spreading in The Gambia…”

**Text-to-image prompt**
Awa, a Gambian woman about 55 years old, medium build, deep dark-brown skin, round face with high cheekbones, warm brown eyes, small gold stud earrings, hair wrapped in an orange-and-indigo patterned head tie, wearing a loose orange-and-indigo wax-print kaftan. Holding the Miracle Balm product: a small lime-green cardboard box with a dark-green leafy wreath illustration around bold white text 'MIRACLE BALM' and small white daisy flowers, next to a round silver metal tin (30 g) whose lid shows the same dark-green leaf wreath and 'MIRACLE BALM', the open tin revealing a smooth light-pink balm. Sitting on her bed at dusk, about to twist open the silver tin, a window behind her showing an orange sky and palm trees, medium shot. Photorealistic vertical 9:16 smartphone photo in authentic UGC style, natural warm West African light, true-to-life dark skin texture, shallow depth of field, no captions or added text overlays, no watermark.

**Image-to-video prompt**
Awa (Gambian woman ~55, orange-and-indigo head tie and kaftan, gold stud earrings) twists open the lime-green Miracle Balm box and round silver tin with pink balm, glances down at the pink balm and a small smile appears. Slow dolly-in. Mood: curiosity, hope. Visible characters do not lip-sync and keep their mouths closed or relaxed while the locked narrator says off-screen: “Then a simple evening habit started spreading in The Gambia…” Preserve faces, bodies, clothing, product design and rendering style exactly.

**Sound / voiceover direction**
Voix off narrateur hors champ — Narrator (off-screen): middle-aged American man, deep smooth baritone, warm polished promotional timbre, General American accent, steady measured pace with short dramatic pauses, confident and reassuring, persuasive without shouting. Segment `voix-off-christopher-smooth.mp3` de 5.88 à 9.60 s. Aucun personnage ne parle. Fin de journée : oiseaux du soir. Effet : léger « tic » métallique à l'ouverture de la boîte. Voix toujours dominante.

**Estimated length**
3.7 seconds

### Plan A4 — 9.60 → 12.40 s

**Script section / voiceover text**
“and people noticed something surprising.”

**Text-to-image prompt**
Mariama, a Gambian woman about 42 years old, slender, dark-brown skin, oval face with a warm smile and even teeth, long thin black braids parted in the middle and gathered behind her shoulders, small gold hoop earrings, wearing a bright yellow-and-green wax-print fitted top with puffed sleeves and matching wrap skirt. Standing at her colourful market stall in Serekunda, looking down at her own feet in sandals with eyebrows raised in pleasant surprise, medium shot. Photorealistic vertical 9:16 smartphone photo in authentic UGC style, natural warm West African light, true-to-life dark skin texture, shallow depth of field, no captions or added text overlays, no watermark.

**Image-to-video prompt**
Mariama (Gambian woman ~42, middle-parted braids, gold hoops, yellow-and-green wax-print outfit) looks down at her feet, raises her eyebrows, then a broad smile spreads across her face. Static camera with slight handheld sway. Mood: pleasant surprise. Visible characters do not lip-sync and keep their mouths closed or relaxed while the locked narrator says off-screen: “and people noticed something surprising.” Preserve faces, bodies, clothing, product design and rendering style exactly.

**Sound / voiceover direction**
Voix off narrateur hors champ — Narrator (off-screen): middle-aged American man, deep smooth baritone, warm polished promotional timbre, General American accent, steady measured pace with short dramatic pauses, confident and reassuring, persuasive without shouting. Segment `voix-off-christopher-smooth.mp3` de 9.60 à 12.40 s. Aucun personnage ne parle. Marché : brouhaha doux. Effet : petit « pop » montant sur le sourire. Voix toujours dominante.

**Estimated length**
2.8 seconds

## Accroche B (remplace A1–A4, fichier séparé)

### Plan B1 — 0.00 → 4.24 s

**Script section / voiceover text**
“For years, people with burning, tingling feet were told:”

**Text-to-image prompt**
Ebrima, a Gambian man about 65 years old, slim and tall, very dark-brown skin, oval lined face with a short white-grey beard and close-cropped grey hair, thin gold-rimmed rectangular glasses, wearing a light-blue cotton kaftan with a tone-on-tone embroidered neckline and a white openwork crocheted kufi cap. Close-up of his bare feet on a woven straw mat, both his hands squeezing his toes, his face partly visible above, grimacing, warm lamp light at night. Photorealistic vertical 9:16 smartphone photo in authentic UGC style, natural warm West African light, true-to-life dark skin texture, shallow depth of field, no captions or added text overlays, no watermark.

**Image-to-video prompt**
Ebrima (Gambian man ~65, short white-grey beard, gold-rimmed glasses, light-blue kaftan, white kufi) curls his toes and presses them hard with both hands, jaw tight, eyes on his feet. Slow tilt up from feet to face. Mood: pain. Visible characters do not lip-sync and keep their mouths closed or relaxed while the locked narrator says off-screen: “For years, people with burning, tingling feet were told:” Preserve faces, bodies, clothing, product design and rendering style exactly.

**Sound / voiceover direction**
Voix off narrateur hors champ — Narrator (off-screen): middle-aged American man, deep smooth baritone, warm polished promotional timbre, General American accent, steady measured pace with short dramatic pauses, confident and reassuring, persuasive without shouting. Segment `accroche-B-christopher-smooth.mp3` de 0.00 à 4.24 s. Aucun personnage ne parle. Nuit : grillons. Effet : souffle grave à l'ouverture. Voix toujours dominante.

**Estimated length**
4.2 seconds

### Plan B2 — 4.24 → 6.02 s

**Script section / voiceover text**
“you have to live with it.”

**Text-to-image prompt**
Ebrima, a Gambian man about 65 years old, slim and tall, very dark-brown skin, oval lined face with a short white-grey beard and close-cropped grey hair, thin gold-rimmed rectangular glasses, wearing a light-blue cotton kaftan with a tone-on-tone embroidered neckline and a white openwork crocheted kufi cap. Sitting alone on a wooden bench on a veranda at dusk, looking away into the distance with a resigned face, medium-wide shot. Photorealistic vertical 9:16 smartphone photo in authentic UGC style, natural warm West African light, true-to-life dark skin texture, shallow depth of field, no captions or added text overlays, no watermark.

**Image-to-video prompt**
Ebrima (Gambian man ~65, short white-grey beard, gold-rimmed glasses, light-blue kaftan, white kufi) exhales slowly and drops his gaze, shoulders sinking. Static camera. Mood: resignation. Visible characters do not lip-sync and keep their mouths closed or relaxed while the locked narrator says off-screen: “you have to live with it.” Preserve faces, bodies, clothing, product design and rendering style exactly.

**Sound / voiceover direction**
Voix off narrateur hors champ — Narrator (off-screen): middle-aged American man, deep smooth baritone, warm polished promotional timbre, General American accent, steady measured pace with short dramatic pauses, confident and reassuring, persuasive without shouting. Segment `accroche-B-christopher-smooth.mp3` de 4.24 à 6.02 s. Aucun personnage ne parle. Soir : vent léger, insectes. Pas d'effet. Voix toujours dominante.

**Estimated length**
1.8 seconds

### Plan B3 — 6.02 → 8.44 s

**Script section / voiceover text**
“But one question kept coming back.”

**Text-to-image prompt**
Awa, a Gambian woman about 55 years old, medium build, deep dark-brown skin, round face with high cheekbones, warm brown eyes, small gold stud earrings, hair wrapped in an orange-and-indigo patterned head tie, wearing a loose orange-and-indigo wax-print kaftan, without head tie, short natural grey-black hair, wearing a plain cotton nightdress. Lying awake in bed under a white mosquito net at night, eyes open staring at the ceiling, cool blue moonlight. Photorealistic vertical 9:16 smartphone photo in authentic UGC style, natural warm West African light, true-to-life dark skin texture, shallow depth of field, no captions or added text overlays, no watermark.

**Image-to-video prompt**
Awa (Gambian woman ~55, orange-and-indigo head tie and kaftan, gold stud earrings) blinks slowly, then turns her head toward the camera with a troubled look. Very slow push-in. Mood: sleepless worry. Visible characters do not lip-sync and keep their mouths closed or relaxed while the locked narrator says off-screen: “But one question kept coming back.” Preserve faces, bodies, clothing, product design and rendering style exactly.

**Sound / voiceover direction**
Voix off narrateur hors champ — Narrator (off-screen): middle-aged American man, deep smooth baritone, warm polished promotional timbre, General American accent, steady measured pace with short dramatic pauses, confident and reassuring, persuasive without shouting. Segment `accroche-B-christopher-smooth.mp3` de 6.02 à 8.44 s. Aucun personnage ne parle. Silence nocturne, horloge lointaine. Effet : un « tic » d'horloge. Voix toujours dominante.

**Estimated length**
2.4 seconds

### Plan B4 — 8.44 → 11.44 s

**Script section / voiceover text**
“Why does the burning always get worse at night?”

**Text-to-image prompt**
a semi-transparent human foot and lower leg seen from the side, showing the fine network of nerves running from the ankle to the toes and thin blood vessels beside them, the nerves glowing angry bright red around the sole and toes. Clean 3D medical-style illustration, vertical 9:16, semi-transparent warm-brown skin over visible anatomy, deep dark-navy background, soft cinematic rim light, no text, no labels.

**Image-to-video prompt**
the semi-transparent foot with its nerve network: the red nerves pulse brighter and brighter in waves from heel to toes. Slow orbit around the foot. Mood: tension. Visible characters do not lip-sync and keep their mouths closed or relaxed while the locked narrator says off-screen: “Why does the burning always get worse at night?” Preserve faces, bodies, clothing, product design and rendering style exactly.

**Sound / voiceover direction**
Voix off narrateur hors champ — Narrator (off-screen): middle-aged American man, deep smooth baritone, warm polished promotional timbre, General American accent, steady measured pace with short dramatic pauses, confident and reassuring, persuasive without shouting. Segment `accroche-B-christopher-smooth.mp3` de 8.44 à 11.44 s. Aucun personnage ne parle. Effet : pulsation grave synchronisée sur l'éclat rouge. Voix toujours dominante.

**Estimated length**
3.0 seconds

## Corps (commun aux deux versions, à partir de 12,40 s)

### Plan 05 — 12.40 → 14.48 s

**Script section / voiceover text**
“From Serekunda to Brikama,”

**Text-to-image prompt**
A busy street market in Serekunda, The Gambia, with yellow-and-green taxis, colourful stalls and people walking in bright wax-print clothes, wide shot at eye level, midday sun. Photorealistic vertical 9:16 smartphone photo in authentic UGC style, natural warm West African light, true-to-life dark skin texture, shallow depth of field, no captions or added text overlays, no watermark.

**Image-to-video prompt**
Pedestrians walk across the frame and a yellow-and-green taxi passes slowly. Slow lateral pan right. Mood: lively, everyday. Visible characters do not lip-sync and keep their mouths closed or relaxed while the locked narrator says off-screen: “From Serekunda to Brikama,” Preserve faces, bodies, clothing, product design and rendering style exactly.

**Sound / voiceover direction**
Voix off narrateur hors champ — Narrator (off-screen): middle-aged American man, deep smooth baritone, warm polished promotional timbre, General American accent, steady measured pace with short dramatic pauses, confident and reassuring, persuasive without shouting. Segment `voix-off-christopher-smooth.mp3` de 12.40 à 14.48 s. Aucun personnage ne parle. Rue animée : klaxons, voix. Effet : whoosh de transition. Voix toujours dominante.

**Estimated length**
2.1 seconds

### Plan 06 — 14.48 → 17.48 s

**Script section / voiceover text**
“more and more people are switching to this.”

**Text-to-image prompt**
Mariama, a Gambian woman about 42 years old, slender, dark-brown skin, oval face with a warm smile and even teeth, long thin black braids parted in the middle and gathered behind her shoulders, small gold hoop earrings, wearing a bright yellow-and-green wax-print fitted top with puffed sleeves and matching wrap skirt. Holding the Miracle Balm product: a small lime-green cardboard box with a dark-green leafy wreath illustration around bold white text 'MIRACLE BALM' and small white daisy flowers, next to a round silver metal tin (30 g) whose lid shows the same dark-green leaf wreath and 'MIRACLE BALM', the open tin revealing a smooth light-pink balm toward the camera at her colourful market stall, smiling confidently, medium close-up. Photorealistic vertical 9:16 smartphone photo in authentic UGC style, natural warm West African light, true-to-life dark skin texture, shallow depth of field, no captions or added text overlays, no watermark.

**Image-to-video prompt**
Mariama (Gambian woman ~42, middle-parted braids, gold hoops, yellow-and-green wax-print outfit) lifts the lime-green Miracle Balm box and round silver tin with pink balm toward the camera and nods with a confident smile, mouth closed. Slight push-in. Mood: enthusiastic recommendation. Visible characters do not lip-sync and keep their mouths closed or relaxed while the locked narrator says off-screen: “more and more people are switching to this.” Preserve faces, bodies, clothing, product design and rendering style exactly.

**Sound / voiceover direction**
Voix off narrateur hors champ — Narrator (off-screen): middle-aged American man, deep smooth baritone, warm polished promotional timbre, General American accent, steady measured pace with short dramatic pauses, confident and reassuring, persuasive without shouting. Segment `voix-off-christopher-smooth.mp3` de 14.48 à 17.48 s. Aucun personnage ne parle. Marché doux en fond. Effet : petit « ding » quand le produit arrive face caméra. Voix toujours dominante.

**Estimated length**
3.0 seconds

### Plan 07 — 17.48 → 19.98 s

**Script section / voiceover text**
“And what they tell us is always the same.”

**Text-to-image prompt**
Awa, a Gambian woman about 55 years old, medium build, deep dark-brown skin, round face with high cheekbones, warm brown eyes, small gold stud earrings, hair wrapped in an orange-and-indigo patterned head tie, wearing a loose orange-and-indigo wax-print kaftan. Mariama, a Gambian woman about 42 years old, slender, dark-brown skin, oval face with a warm smile and even teeth, long thin black braids parted in the middle and gathered behind her shoulders, small gold hoop earrings, wearing a bright yellow-and-green wax-print fitted top with puffed sleeves and matching wrap skirt. Sitting side by side on a veranda bench in afternoon light, turned toward each other and laughing, medium shot. Photorealistic vertical 9:16 smartphone photo in authentic UGC style, natural warm West African light, true-to-life dark skin texture, shallow depth of field, no captions or added text overlays, no watermark.

**Image-to-video prompt**
Awa (Gambian woman ~55, orange-and-indigo head tie and kaftan, gold stud earrings) touches the arm of Mariama (Gambian woman ~42, middle-parted braids, gold hoops, yellow-and-green wax-print outfit); both laugh warmly with closed lips and nod, no speaking. Static camera. Mood: friendly complicity. Visible characters do not lip-sync and keep their mouths closed or relaxed while the locked narrator says off-screen: “And what they tell us is always the same.” Preserve faces, bodies, clothing, product design and rendering style exactly.

**Sound / voiceover direction**
Voix off narrateur hors champ — Narrator (off-screen): middle-aged American man, deep smooth baritone, warm polished promotional timbre, General American accent, steady measured pace with short dramatic pauses, confident and reassuring, persuasive without shouting. Segment `voix-off-christopher-smooth.mp3` de 17.48 à 19.98 s. Aucun personnage ne parle. Cour paisible : oiseaux. Pas d'effet. Voix toujours dominante.

**Estimated length**
2.5 seconds

### Plan 08 — 19.98 → 22.40 s

**Script section / voiceover text**
“They finally sleep through the night.”

**Text-to-image prompt**
Awa, a Gambian woman about 55 years old, medium build, deep dark-brown skin, round face with high cheekbones, warm brown eyes, small gold stud earrings, hair wrapped in an orange-and-indigo patterned head tie, wearing a loose orange-and-indigo wax-print kaftan, without head tie, short natural grey-black hair, wearing a plain cotton nightdress. Sleeping peacefully on her side in bed under a white mosquito net, soft blue moonlight from the window, medium shot. Photorealistic vertical 9:16 smartphone photo in authentic UGC style, natural warm West African light, true-to-life dark skin texture, shallow depth of field, no captions or added text overlays, no watermark.

**Image-to-video prompt**
Awa (Gambian woman ~55, orange-and-indigo head tie and kaftan, gold stud earrings) sleeps deeply, chest rising slowly, a faint relaxed smile. Very slow push-in. Mood: calm relief. Visible characters do not lip-sync and keep their mouths closed or relaxed while the locked narrator says off-screen: “They finally sleep through the night.” Preserve faces, bodies, clothing, product design and rendering style exactly.

**Sound / voiceover direction**
Voix off narrateur hors champ — Narrator (off-screen): middle-aged American man, deep smooth baritone, warm polished promotional timbre, General American accent, steady measured pace with short dramatic pauses, confident and reassuring, persuasive without shouting. Segment `voix-off-christopher-smooth.mp3` de 19.98 à 22.40 s. Aucun personnage ne parle. Nuit calme, grillons très bas. Musique : s'adoucit. Voix toujours dominante.

**Estimated length**
2.4 seconds

### Plan 09 — 22.40 → 24.80 s

**Script section / voiceover text**
“Less burning. Less tingling.”

**Text-to-image prompt**
Close-up of the relaxed bare feet of Awa, a Gambian woman about 55 years old, medium build, deep dark-brown skin, round face with high cheekbones, warm brown eyes, small gold stud earrings, hair wrapped in an orange-and-indigo patterned head tie, wearing a loose orange-and-indigo wax-print kaftan, resting on a white bed sheet in soft morning light. Photorealistic vertical 9:16 smartphone photo in authentic UGC style, natural warm West African light, true-to-life dark skin texture, shallow depth of field, no captions or added text overlays, no watermark.

**Image-to-video prompt**
The bare feet of Awa (Gambian woman ~55, orange-and-indigo head tie and kaftan, gold stud earrings) relax and the toes stretch gently once. Static macro shot. Mood: comfort. Visible characters do not lip-sync and keep their mouths closed or relaxed while the locked narrator says off-screen: “Less burning. Less tingling.” Preserve faces, bodies, clothing, product design and rendering style exactly.

**Sound / voiceover direction**
Voix off narrateur hors champ — Narrator (off-screen): middle-aged American man, deep smooth baritone, warm polished promotional timbre, General American accent, steady measured pace with short dramatic pauses, confident and reassuring, persuasive without shouting. Segment `voix-off-christopher-smooth.mp3` de 22.40 à 24.80 s. Aucun personnage ne parle. Matin : oiseaux. Pas d'effet. Voix toujours dominante.

**Estimated length**
2.4 seconds

### Plan 10 — 24.80 → 26.80 s

**Script section / voiceover text**
“They are back on their feet.”

**Text-to-image prompt**
Ebrima, a Gambian man about 65 years old, slim and tall, very dark-brown skin, oval lined face with a short white-grey beard and close-cropped grey hair, thin gold-rimmed rectangular glasses, wearing a light-blue cotton kaftan with a tone-on-tone embroidered neckline and a white openwork crocheted kufi cap. Walking confidently along a sandy street in Brikama under bright morning sun, smiling, full-body shot from the front. Photorealistic vertical 9:16 smartphone photo in authentic UGC style, natural warm West African light, true-to-life dark skin texture, shallow depth of field, no captions or added text overlays, no watermark.

**Image-to-video prompt**
Ebrima (Gambian man ~65, short white-grey beard, gold-rimmed glasses, light-blue kaftan, white kufi) walks steadily toward the camera with a proud smile, arms swinging naturally. Camera tracks backward. Mood: regained energy. Visible characters do not lip-sync and keep their mouths closed or relaxed while the locked narrator says off-screen: “They are back on their feet.” Preserve faces, bodies, clothing, product design and rendering style exactly.

**Sound / voiceover direction**
Voix off narrateur hors champ — Narrator (off-screen): middle-aged American man, deep smooth baritone, warm polished promotional timbre, General American accent, steady measured pace with short dramatic pauses, confident and reassuring, persuasive without shouting. Segment `voix-off-christopher-smooth.mp3` de 24.80 à 26.80 s. Aucun personnage ne parle. Rue : pas sur le sable, coq lointain. Effet : léger whoosh à l'entrée. Voix toujours dominante.

**Estimated length**
2.0 seconds

### Plan 11 — 26.80 → 29.46 s

**Script section / voiceover text**
“This is not another tablet you swallow every day.”

**Text-to-image prompt**
Close-up of an older dark-skinned man's hand pouring many white tablets from a plastic pill bottle into his palm above a worn wooden table. Photorealistic vertical 9:16 smartphone photo in authentic UGC style, natural warm West African light, true-to-life dark skin texture, shallow depth of field, no captions or added text overlays, no watermark.

**Image-to-video prompt**
The tablets spill into the palm; the hand closes, then pushes the bottle away across the table. Static camera. Mood: fed up. Visible characters do not lip-sync and keep their mouths closed or relaxed while the locked narrator says off-screen: “This is not another tablet you swallow every day.” Preserve faces, bodies, clothing, product design and rendering style exactly.

**Sound / voiceover direction**
Voix off narrateur hors champ — Narrator (off-screen): middle-aged American man, deep smooth baritone, warm polished promotional timbre, General American accent, steady measured pace with short dramatic pauses, confident and reassuring, persuasive without shouting. Segment `voix-off-christopher-smooth.mp3` de 26.80 à 29.46 s. Aucun personnage ne parle. Effet : bruit de comprimés qui s'entrechoquent. Voix toujours dominante.

**Estimated length**
2.7 seconds

### Plan 12 — 29.46 → 34.30 s

**Script section / voiceover text**
“Not a cream that only makes the skin soft — and does nothing for the burning.”

**Text-to-image prompt**
Awa, a Gambian woman about 55 years old, medium build, deep dark-brown skin, round face with high cheekbones, warm brown eyes, small gold stud earrings, hair wrapped in an orange-and-indigo patterned head tie, wearing a loose orange-and-indigo wax-print kaftan. Sitting on her bed rubbing a plain white unbranded lotion on her shin and foot, frowning in frustration, medium shot, warm indoor light. Photorealistic vertical 9:16 smartphone photo in authentic UGC style, natural warm West African light, true-to-life dark skin texture, shallow depth of field, no captions or added text overlays, no watermark.

**Image-to-video prompt**
Awa (Gambian woman ~55, orange-and-indigo head tie and kaftan, gold stud earrings) rubs the white lotion on her shin, stops, then frowns and shakes her head, looking at her foot. Static camera. Mood: frustration. Visible characters do not lip-sync and keep their mouths closed or relaxed while the locked narrator says off-screen: “Not a cream that only makes the skin soft — and does nothing for the burning.” Preserve faces, bodies, clothing, product design and rendering style exactly.

**Sound / voiceover direction**
Voix off narrateur hors champ — Narrator (off-screen): middle-aged American man, deep smooth baritone, warm polished promotional timbre, General American accent, steady measured pace with short dramatic pauses, confident and reassuring, persuasive without shouting. Segment `voix-off-christopher-smooth.mp3` de 29.46 à 34.30 s. Aucun personnage ne parle. Intérieur calme. Effet : petit « buzz » négatif discret sur le froncement. Voix toujours dominante.

**Estimated length**
4.8 seconds

### Plan 13 — 34.30 → 37.78 s

**Script section / voiceover text**
“Not hot water with salt, that calms you for one hour.”

**Text-to-image prompt**
Ebrima, a Gambian man about 65 years old, slim and tall, very dark-brown skin, oval lined face with a short white-grey beard and close-cropped grey hair, thin gold-rimmed rectangular glasses, wearing a light-blue cotton kaftan with a tone-on-tone embroidered neckline and a white openwork crocheted kufi cap. Sitting on a low wooden stool, both feet soaking in a plastic basin of steaming salty water on a concrete floor, tired expression, medium shot. Photorealistic vertical 9:16 smartphone photo in authentic UGC style, natural warm West African light, true-to-life dark skin texture, shallow depth of field, no captions or added text overlays, no watermark.

**Image-to-video prompt**
Ebrima (Gambian man ~65, short white-grey beard, gold-rimmed glasses, light-blue kaftan, white kufi) shifts his feet in the steaming water and lets out a tired breath, looking down. Steam rises. Static camera. Mood: temporary, weary relief. Visible characters do not lip-sync and keep their mouths closed or relaxed while the locked narrator says off-screen: “Not hot water with salt, that calms you for one hour.” Preserve faces, bodies, clothing, product design and rendering style exactly.

**Sound / voiceover direction**
Voix off narrateur hors champ — Narrator (off-screen): middle-aged American man, deep smooth baritone, warm polished promotional timbre, General American accent, steady measured pace with short dramatic pauses, confident and reassuring, persuasive without shouting. Segment `voix-off-christopher-smooth.mp3` de 34.30 à 37.78 s. Aucun personnage ne parle. Effet : clapotis d'eau. Voix toujours dominante.

**Estimated length**
3.5 seconds

### Plan 14 — 37.78 → 40.90 s

**Script section / voiceover text**
“Because the burning does not start in the skin.”

**Text-to-image prompt**
a semi-transparent human foot and lower leg seen from the side, showing the fine network of nerves running from the ankle to the toes and thin blood vessels beside them, the outer skin surface highlighted with a thin pale glow, the nerves below still faint. Clean 3D medical-style illustration, vertical 9:16, semi-transparent warm-brown skin over visible anatomy, deep dark-navy background, soft cinematic rim light, no text, no labels.

**Image-to-video prompt**
Camera pushes slowly through the glowing skin surface of the semi-transparent foot with its nerve network, moving inward. Mood: discovery. Visible characters do not lip-sync and keep their mouths closed or relaxed while the locked narrator says off-screen: “Because the burning does not start in the skin.” Preserve faces, bodies, clothing, product design and rendering style exactly.

**Sound / voiceover direction**
Voix off narrateur hors champ — Narrator (off-screen): middle-aged American man, deep smooth baritone, warm polished promotional timbre, General American accent, steady measured pace with short dramatic pauses, confident and reassuring, persuasive without shouting. Segment `voix-off-christopher-smooth.mp3` de 37.78 à 40.90 s. Aucun personnage ne parle. Effet : whoosh grave d'immersion. Voix toujours dominante.

**Estimated length**
3.1 seconds

### Plan 15 — 40.90 → 44.22 s

**Script section / voiceover text**
“It starts deeper… in the nerves of the feet.”

**Text-to-image prompt**
a semi-transparent human foot and lower leg seen from the side, showing the fine network of nerves running from the ankle to the toes and thin blood vessels beside them, close view inside the foot, the nerves glowing angry bright red and flickering. Clean 3D medical-style illustration, vertical 9:16, semi-transparent warm-brown skin over visible anatomy, deep dark-navy background, soft cinematic rim light, no text, no labels.

**Image-to-video prompt**
Red pulses travel along the nerves of the semi-transparent foot with its nerve network toward the toes, flickering like irritated wires. Slow push-in. Mood: revelation. Visible characters do not lip-sync and keep their mouths closed or relaxed while the locked narrator says off-screen: “It starts deeper… in the nerves of the feet.” Preserve faces, bodies, clothing, product design and rendering style exactly.

**Sound / voiceover direction**
Voix off narrateur hors champ — Narrator (off-screen): middle-aged American man, deep smooth baritone, warm polished promotional timbre, General American accent, steady measured pace with short dramatic pauses, confident and reassuring, persuasive without shouting. Segment `voix-off-christopher-smooth.mp3` de 40.90 à 44.22 s. Aucun personnage ne parle. Effet : grésillement électrique léger + pulsation. Voix toujours dominante.

**Estimated length**
3.3 seconds

### Plan 16 — 44.22 → 48.02 s

**Script section / voiceover text**
“And the funny thing is, the answer is very simple to use.”

**Text-to-image prompt**
Awa, a Gambian woman about 55 years old, medium build, deep dark-brown skin, round face with high cheekbones, warm brown eyes, small gold stud earrings, hair wrapped in an orange-and-indigo patterned head tie, wearing a loose orange-and-indigo wax-print kaftan. Sitting on her bed holding the closed round silver tin of the Miracle Balm product: a small lime-green cardboard box with a dark-green leafy wreath illustration around bold white text 'MIRACLE BALM' and small white daisy flowers, next to a round silver metal tin (30 g) whose lid shows the same dark-green leaf wreath and 'MIRACLE BALM', the open tin revealing a smooth light-pink balm in her open palm, smiling at the camera, warm morning light, medium close-up. Photorealistic vertical 9:16 smartphone photo in authentic UGC style, natural warm West African light, true-to-life dark skin texture, shallow depth of field, no captions or added text overlays, no watermark.

**Image-to-video prompt**
Awa (Gambian woman ~55, orange-and-indigo head tie and kaftan, gold stud earrings) raises the lime-green Miracle Balm box and round silver tin with pink balm in her palm toward the camera with a knowing smile and a slight head tilt, no speaking. Slow push-in. Mood: reassuring simplicity. Visible characters do not lip-sync and keep their mouths closed or relaxed while the locked narrator says off-screen: “And the funny thing is, the answer is very simple to use.” Preserve faces, bodies, clothing, product design and rendering style exactly.

**Sound / voiceover direction**
Voix off narrateur hors champ — Narrator (off-screen): middle-aged American man, deep smooth baritone, warm polished promotional timbre, General American accent, steady measured pace with short dramatic pauses, confident and reassuring, persuasive without shouting. Segment `voix-off-christopher-smooth.mp3` de 44.22 à 48.02 s. Aucun personnage ne parle. Matin : oiseaux. Musique : remonte légèrement. Voix toujours dominante.

**Estimated length**
3.8 seconds

### Plan 17 — 48.02 → 50.10 s

**Script section / voiceover text**
“It's called Miracle Balm.”

**Text-to-image prompt**
the Miracle Balm product: a small lime-green cardboard box with a dark-green leafy wreath illustration around bold white text 'MIRACLE BALM' and small white daisy flowers, next to a round silver metal tin (30 g) whose lid shows the same dark-green leaf wreath and 'MIRACLE BALM', the open tin revealing a smooth light-pink balm, placed on a woven raffia mat in soft morning sunlight with shadows of tropical leaves, close-up product hero shot. Photorealistic vertical 9:16 smartphone photo in authentic UGC style, natural warm West African light, true-to-life dark skin texture, shallow depth of field, no captions or added text overlays, no watermark.

**Image-to-video prompt**
Sunlight sweeps across the lime-green Miracle Balm box and round silver tin with pink balm. Slow push-in with a soft light flare. Mood: reveal. Visible characters do not lip-sync and keep their mouths closed or relaxed while the locked narrator says off-screen: “It's called Miracle Balm.” Preserve faces, bodies, clothing, product design and rendering style exactly.

**Sound / voiceover direction**
Voix off narrateur hors champ — Narrator (off-screen): middle-aged American man, deep smooth baritone, warm polished promotional timbre, General American accent, steady measured pace with short dramatic pauses, confident and reassuring, persuasive without shouting. Segment `voix-off-christopher-smooth.mp3` de 48.02 à 50.10 s. Aucun personnage ne parle. Effet : carillon clair sur « Miracle Balm ». Musique : petit pic. Voix toujours dominante.

**Estimated length**
2.1 seconds

### Plan 18 — 50.10 → 52.34 s

**Script section / voiceover text**
“Here is why it works differently.”

**Text-to-image prompt**
a semi-transparent human foot and lower leg seen from the side, showing the fine network of nerves running from the ankle to the toes and thin blood vessels beside them, full view, calm, nerves and blood vessels both softly visible. Clean 3D medical-style illustration, vertical 9:16, semi-transparent warm-brown skin over visible anatomy, deep dark-navy background, soft cinematic rim light, no text, no labels.

**Image-to-video prompt**
the semi-transparent foot with its nerve network rotates slowly in 3D. Slow orbit. Mood: explanation begins. Visible characters do not lip-sync and keep their mouths closed or relaxed while the locked narrator says off-screen: “Here is why it works differently.” Preserve faces, bodies, clothing, product design and rendering style exactly.

**Sound / voiceover direction**
Voix off narrateur hors champ — Narrator (off-screen): middle-aged American man, deep smooth baritone, warm polished promotional timbre, General American accent, steady measured pace with short dramatic pauses, confident and reassuring, persuasive without shouting. Segment `voix-off-christopher-smooth.mp3` de 50.10 à 52.34 s. Aucun personnage ne parle. Effet : whoosh doux. Voix toujours dominante.

**Estimated length**
2.2 seconds

### Plan 19 — 52.34 → 54.56 s

**Script section / voiceover text**
“Tired nerves need blood.”

**Text-to-image prompt**
a semi-transparent human foot and lower leg seen from the side, showing the fine network of nerves running from the ankle to the toes and thin blood vessels beside them, macro view of one nerve fibre lying beside a thin blood vessel, the nerve dim greyish red. Clean 3D medical-style illustration, vertical 9:16, semi-transparent warm-brown skin over visible anatomy, deep dark-navy background, soft cinematic rim light, no text, no labels.

**Image-to-video prompt**
The nerve of the semi-transparent foot with its nerve network flickers weakly, dimming. Very slow push-in. Mood: fragility. Visible characters do not lip-sync and keep their mouths closed or relaxed while the locked narrator says off-screen: “Tired nerves need blood.” Preserve faces, bodies, clothing, product design and rendering style exactly.

**Sound / voiceover direction**
Voix off narrateur hors champ — Narrator (off-screen): middle-aged American man, deep smooth baritone, warm polished promotional timbre, General American accent, steady measured pace with short dramatic pauses, confident and reassuring, persuasive without shouting. Segment `voix-off-christopher-smooth.mp3` de 52.34 à 54.56 s. Aucun personnage ne parle. Effet : battement de cœur très bas. Voix toujours dominante.

**Estimated length**
2.2 seconds

### Plan 20 — 54.56 → 59.02 s

**Script section / voiceover text**
“When the blood moves slowly in the feet, the nerves don't get what they need.”

**Text-to-image prompt**
a semi-transparent human foot and lower leg seen from the side, showing the fine network of nerves running from the ankle to the toes and thin blood vessels beside them, the blood vessels carrying sluggish dark-red flow, the nerves beside them dim and greyish. Clean 3D medical-style illustration, vertical 9:16, semi-transparent warm-brown skin over visible anatomy, deep dark-navy background, soft cinematic rim light, no text, no labels.

**Image-to-video prompt**
Dark-red particles crawl slowly through the vessels of the semi-transparent foot with its nerve network while the nerves stay dim. Slow lateral move along the foot. Mood: deficit. Visible characters do not lip-sync and keep their mouths closed or relaxed while the locked narrator says off-screen: “When the blood moves slowly in the feet, the nerves don't get what they need.” Preserve faces, bodies, clothing, product design and rendering style exactly.

**Sound / voiceover direction**
Voix off narrateur hors champ — Narrator (off-screen): middle-aged American man, deep smooth baritone, warm polished promotional timbre, General American accent, steady measured pace with short dramatic pauses, confident and reassuring, persuasive without shouting. Segment `voix-off-christopher-smooth.mp3` de 54.56 à 59.02 s. Aucun personnage ne parle. Effet : battement de cœur lent. Voix toujours dominante.

**Estimated length**
4.5 seconds

### Plan 21 — 59.02 → 62.20 s

**Script section / voiceover text**
“So they send burning. Tingling. Needles.”

**Text-to-image prompt**
a semi-transparent human foot and lower leg seen from the side, showing the fine network of nerves running from the ankle to the toes and thin blood vessels beside them, the nerves flashing bright red with small sharp sparks at the toes. Clean 3D medical-style illustration, vertical 9:16, semi-transparent warm-brown skin over visible anatomy, deep dark-navy background, soft cinematic rim light, no text, no labels.

**Image-to-video prompt**
Three successive sharp red flashes burst along the nerves of the semi-transparent foot with its nerve network, timed like jolts. Static camera with a tiny shake on each flash. Mood: pain. Visible characters do not lip-sync and keep their mouths closed or relaxed while the locked narrator says off-screen: “So they send burning. Tingling. Needles.” Preserve faces, bodies, clothing, product design and rendering style exactly.

**Sound / voiceover direction**
Voix off narrateur hors champ — Narrator (off-screen): middle-aged American man, deep smooth baritone, warm polished promotional timbre, General American accent, steady measured pace with short dramatic pauses, confident and reassuring, persuasive without shouting. Segment `voix-off-christopher-smooth.mp3` de 59.02 à 62.20 s. Aucun personnage ne parle. Effets : trois impacts secs calés sur « burning », « tingling », « needles ». Voix toujours dominante.

**Estimated length**
3.2 seconds

### Plan 22 — 62.20 → 64.80 s

**Script section / voiceover text**
“Miracle Balm is a natural herbal formula,”

**Text-to-image prompt**
the Miracle Balm product: a small lime-green cardboard box with a dark-green leafy wreath illustration around bold white text 'MIRACLE BALM' and small white daisy flowers, next to a round silver metal tin (30 g) whose lid shows the same dark-green leaf wreath and 'MIRACLE BALM', the open tin revealing a smooth light-pink balm, the open tin on a light wooden table surrounded by fresh green leaves and small white daisy flowers, close-up. Photorealistic vertical 9:16 smartphone photo in authentic UGC style, natural warm West African light, true-to-life dark skin texture, shallow depth of field, no captions or added text overlays, no watermark.

**Image-to-video prompt**
A few green leaves drift down around the lime-green Miracle Balm box and round silver tin with pink balm. Slow push-in. Mood: natural, fresh. Visible characters do not lip-sync and keep their mouths closed or relaxed while the locked narrator says off-screen: “Miracle Balm is a natural herbal formula,” Preserve faces, bodies, clothing, product design and rendering style exactly.

**Sound / voiceover direction**
Voix off narrateur hors champ — Narrator (off-screen): middle-aged American man, deep smooth baritone, warm polished promotional timbre, General American accent, steady measured pace with short dramatic pauses, confident and reassuring, persuasive without shouting. Segment `voix-off-christopher-smooth.mp3` de 62.20 à 64.80 s. Aucun personnage ne parle. Effet : bruissement de feuilles. Musique : lumineuse. Voix toujours dominante.

**Estimated length**
2.6 seconds

### Plan 23 — 64.80 → 67.76 s

**Script section / voiceover text**
“made to be massaged deep into the feet.”

**Text-to-image prompt**
Close-up of the hands of Awa, a Gambian woman about 55 years old, medium build, deep dark-brown skin, round face with high cheekbones, warm brown eyes, small gold stud earrings, hair wrapped in an orange-and-indigo patterned head tie, wearing a loose orange-and-indigo wax-print kaftan massaging light-pink balm into the sole of her bare foot while sitting on her bed, the open round silver tin beside her. Photorealistic vertical 9:16 smartphone photo in authentic UGC style, natural warm West African light, true-to-life dark skin texture, shallow depth of field, no captions or added text overlays, no watermark.

**Image-to-video prompt**
The thumbs of Awa (Gambian woman ~55, orange-and-indigo head tie and kaftan, gold stud earrings) press into the sole in slow firm circles. Static close-up. Mood: care. Visible characters do not lip-sync and keep their mouths closed or relaxed while the locked narrator says off-screen: “made to be massaged deep into the feet.” Preserve faces, bodies, clothing, product design and rendering style exactly.

**Sound / voiceover direction**
Voix off narrateur hors champ — Narrator (off-screen): middle-aged American man, deep smooth baritone, warm polished promotional timbre, General American accent, steady measured pace with short dramatic pauses, confident and reassuring, persuasive without shouting. Segment `voix-off-christopher-smooth.mp3` de 64.80 à 67.76 s. Aucun personnage ne parle. Effet : frottement doux de la peau. Voix toujours dominante.

**Estimated length**
3.0 seconds

### Plan 24 — 67.76 → 71.98 s

**Script section / voiceover text**
“The balm and the massage work together to wake up the circulation —”

**Text-to-image prompt**
a semi-transparent human foot and lower leg seen from the side, showing the fine network of nerves running from the ankle to the toes and thin blood vessels beside them, a warm golden glow on the sole where two hands press, the blood vessels starting to brighten. Clean 3D medical-style illustration, vertical 9:16, semi-transparent warm-brown skin over visible anatomy, deep dark-navy background, soft cinematic rim light, no text, no labels.

**Image-to-video prompt**
The blood flow in the semi-transparent foot with its nerve network speeds up from the heel to the toes, vessels brightening to vivid red. Slow push-in. Mood: awakening. Visible characters do not lip-sync and keep their mouths closed or relaxed while the locked narrator says off-screen: “The balm and the massage work together to wake up the circulation —” Preserve faces, bodies, clothing, product design and rendering style exactly.

**Sound / voiceover direction**
Voix off narrateur hors champ — Narrator (off-screen): middle-aged American man, deep smooth baritone, warm polished promotional timbre, General American accent, steady measured pace with short dramatic pauses, confident and reassuring, persuasive without shouting. Segment `voix-off-christopher-smooth.mp3` de 67.76 à 71.98 s. Aucun personnage ne parle. Effet : montée sonore douce (riser). Voix toujours dominante.

**Estimated length**
4.2 seconds

### Plan 25 — 71.98 → 74.94 s

**Script section / voiceover text**
“so fresh blood can reach the tired nerves again.”

**Text-to-image prompt**
a semi-transparent human foot and lower leg seen from the side, showing the fine network of nerves running from the ankle to the toes and thin blood vessels beside them, bright red blood flowing into the toes, the nerves turning from angry red to calm soft gold. Clean 3D medical-style illustration, vertical 9:16, semi-transparent warm-brown skin over visible anatomy, deep dark-navy background, soft cinematic rim light, no text, no labels.

**Image-to-video prompt**
Fresh red flow reaches the nerves of the semi-transparent foot with its nerve network and they shift gradually from angry red to calm gold. Static camera. Mood: relief. Visible characters do not lip-sync and keep their mouths closed or relaxed while the locked narrator says off-screen: “so fresh blood can reach the tired nerves again.” Preserve faces, bodies, clothing, product design and rendering style exactly.

**Sound / voiceover direction**
Voix off narrateur hors champ — Narrator (off-screen): middle-aged American man, deep smooth baritone, warm polished promotional timbre, General American accent, steady measured pace with short dramatic pauses, confident and reassuring, persuasive without shouting. Segment `voix-off-christopher-smooth.mp3` de 71.98 à 74.94 s. Aucun personnage ne parle. Effet : son apaisant (nappe qui s'ouvre). Voix toujours dominante.

**Estimated length**
3.0 seconds

### Plan 26 — 74.94 → 78.36 s

**Script section / voiceover text**
“That's why you are not just covering the pain on top of the skin.”

**Text-to-image prompt**
Ebrima, a Gambian man about 65 years old, slim and tall, very dark-brown skin, oval lined face with a short white-grey beard and close-cropped grey hair, thin gold-rimmed rectangular glasses, wearing a light-blue cotton kaftan with a tone-on-tone embroidered neckline and a white openwork crocheted kufi cap. Sitting on a low stool on his veranda massaging light-pink balm into the top of his bare foot, the open round silver tin of the Miracle Balm product: a small lime-green cardboard box with a dark-green leafy wreath illustration around bold white text 'MIRACLE BALM' and small white daisy flowers, next to a round silver metal tin (30 g) whose lid shows the same dark-green leaf wreath and 'MIRACLE BALM', the open tin revealing a smooth light-pink balm on the floor beside him, medium shot. Photorealistic vertical 9:16 smartphone photo in authentic UGC style, natural warm West African light, true-to-life dark skin texture, shallow depth of field, no captions or added text overlays, no watermark.

**Image-to-video prompt**
Ebrima (Gambian man ~65, short white-grey beard, gold-rimmed glasses, light-blue kaftan, white kufi) massages the balm firmly into his foot with circular motions, focused, eyes on his foot. Static camera. Mood: diligence. Visible characters do not lip-sync and keep their mouths closed or relaxed while the locked narrator says off-screen: “That's why you are not just covering the pain on top of the skin.” Preserve faces, bodies, clothing, product design and rendering style exactly.

**Sound / voiceover direction**
Voix off narrateur hors champ — Narrator (off-screen): middle-aged American man, deep smooth baritone, warm polished promotional timbre, General American accent, steady measured pace with short dramatic pauses, confident and reassuring, persuasive without shouting. Segment `voix-off-christopher-smooth.mp3` de 74.94 à 78.36 s. Aucun personnage ne parle. Veranda : oiseaux. Pas d'effet. Voix toujours dominante.

**Estimated length**
3.4 seconds

### Plan 27 — 78.36 → 81.38 s

**Script section / voiceover text**
“You are helping your feet from the inside.”

**Text-to-image prompt**
a semi-transparent human foot and lower leg seen from the side, showing the fine network of nerves running from the ankle to the toes and thin blood vessels beside them, calm golden nerves and steady bright blood flow, a gentle overall glow. Clean 3D medical-style illustration, vertical 9:16, semi-transparent warm-brown skin over visible anatomy, deep dark-navy background, soft cinematic rim light, no text, no labels.

**Image-to-video prompt**
the semi-transparent foot with its nerve network glows softly, the golden nerves breathing gently in light. Slow orbit. Mood: balance. Visible characters do not lip-sync and keep their mouths closed or relaxed while the locked narrator says off-screen: “You are helping your feet from the inside.” Preserve faces, bodies, clothing, product design and rendering style exactly.

**Sound / voiceover direction**
Voix off narrateur hors champ — Narrator (off-screen): middle-aged American man, deep smooth baritone, warm polished promotional timbre, General American accent, steady measured pace with short dramatic pauses, confident and reassuring, persuasive without shouting. Segment `voix-off-christopher-smooth.mp3` de 78.36 à 81.38 s. Aucun personnage ne parle. Effet : nappe douce. Voix toujours dominante.

**Estimated length**
3.0 seconds

### Plan 28 — 81.38 → 85.34 s

**Script section / voiceover text**
“Morning and night, massage it into each foot for one minute.”

**Text-to-image prompt**
Awa, a Gambian woman about 55 years old, medium build, deep dark-brown skin, round face with high cheekbones, warm brown eyes, small gold stud earrings, hair wrapped in an orange-and-indigo patterned head tie, wearing a loose orange-and-indigo wax-print kaftan. Sitting on the edge of her bed in bright morning light, massaging her bare foot, the open round silver tin of the Miracle Balm product: a small lime-green cardboard box with a dark-green leafy wreath illustration around bold white text 'MIRACLE BALM' and small white daisy flowers, next to a round silver metal tin (30 g) whose lid shows the same dark-green leaf wreath and 'MIRACLE BALM', the open tin revealing a smooth light-pink balm on the bed beside her, medium shot. Photorealistic vertical 9:16 smartphone photo in authentic UGC style, natural warm West African light, true-to-life dark skin texture, shallow depth of field, no captions or added text overlays, no watermark.

**Image-to-video prompt**
Awa (Gambian woman ~55, orange-and-indigo head tie and kaftan, gold stud earrings) massages her foot in circles, then looks up at the camera with a calm smile, no speaking. Static camera. Mood: easy routine. Visible characters do not lip-sync and keep their mouths closed or relaxed while the locked narrator says off-screen: “Morning and night, massage it into each foot for one minute.” Preserve faces, bodies, clothing, product design and rendering style exactly.

**Sound / voiceover direction**
Voix off narrateur hors champ — Narrator (off-screen): middle-aged American man, deep smooth baritone, warm polished promotional timbre, General American accent, steady measured pace with short dramatic pauses, confident and reassuring, persuasive without shouting. Segment `voix-off-christopher-smooth.mp3` de 81.38 à 85.34 s. Aucun personnage ne parle. Matin : oiseaux, radio très lointaine. Voix toujours dominante.

**Estimated length**
4.0 seconds

### Plan 29 — 85.34 → 88.80 s

**Script section / voiceover text**
“Many people feel the burning calm down in the first nights…”

**Text-to-image prompt**
Ebrima, a Gambian man about 65 years old, slim and tall, very dark-brown skin, oval lined face with a short white-grey beard and close-cropped grey hair, thin gold-rimmed rectangular glasses, wearing a light-blue cotton kaftan with a tone-on-tone embroidered neckline and a white openwork crocheted kufi cap, without glasses or cap, wearing a plain white cotton sleeping shirt. Lying on his back in bed at night under a white mosquito net, eyes closing with a relieved expression, cool blue moonlight. Photorealistic vertical 9:16 smartphone photo in authentic UGC style, natural warm West African light, true-to-life dark skin texture, shallow depth of field, no captions or added text overlays, no watermark.

**Image-to-video prompt**
Ebrima (Gambian man ~65, short white-grey beard, gold-rimmed glasses, light-blue kaftan, white kufi) lets out a long relieved breath, closes his eyes and smiles faintly. Very slow push-in. Mood: relief. Visible characters do not lip-sync and keep their mouths closed or relaxed while the locked narrator says off-screen: “Many people feel the burning calm down in the first nights…” Preserve faces, bodies, clothing, product design and rendering style exactly.

**Sound / voiceover direction**
Voix off narrateur hors champ — Narrator (off-screen): middle-aged American man, deep smooth baritone, warm polished promotional timbre, General American accent, steady measured pace with short dramatic pauses, confident and reassuring, persuasive without shouting. Segment `voix-off-christopher-smooth.mp3` de 85.34 à 88.80 s. Aucun personnage ne parle. Nuit : grillons doux. Voix toujours dominante.

**Estimated length**
3.5 seconds

### Plan 30 — 88.80 → 91.58 s

**Script section / voiceover text**
“and it keeps getting better as they keep the habit.”

**Text-to-image prompt**
Awa, a Gambian woman about 55 years old, medium build, deep dark-brown skin, round face with high cheekbones, warm brown eyes, small gold stud earrings, hair wrapped in an orange-and-indigo patterned head tie, wearing a loose orange-and-indigo wax-print kaftan. Walking across a sunny sandy compound carrying a woven basket on her hip, energetic and smiling, full-body shot. Photorealistic vertical 9:16 smartphone photo in authentic UGC style, natural warm West African light, true-to-life dark skin texture, shallow depth of field, no captions or added text overlays, no watermark.

**Image-to-video prompt**
Awa (Gambian woman ~55, orange-and-indigo head tie and kaftan, gold stud earrings) walks briskly across the frame with a light step and a broad smile. Camera pans to follow. Mood: vitality. Visible characters do not lip-sync and keep their mouths closed or relaxed while the locked narrator says off-screen: “and it keeps getting better as they keep the habit.” Preserve faces, bodies, clothing, product design and rendering style exactly.

**Sound / voiceover direction**
Voix off narrateur hors champ — Narrator (off-screen): middle-aged American man, deep smooth baritone, warm polished promotional timbre, General American accent, steady measured pace with short dramatic pauses, confident and reassuring, persuasive without shouting. Segment `voix-off-christopher-smooth.mp3` de 88.80 à 91.58 s. Aucun personnage ne parle. Cour : pas, enfants au loin. Musique : remonte. Voix toujours dominante.

**Estimated length**
2.8 seconds

### Plan 31 — 91.58 → 96.94 s

**Script section / voiceover text**
“If there is a wound that does not heal, or very strong pain, see a doctor first.”

**Text-to-image prompt**
Ebrima, a Gambian man about 65 years old, slim and tall, very dark-brown skin, oval lined face with a short white-grey beard and close-cropped grey hair, thin gold-rimmed rectangular glasses, wearing a light-blue cotton kaftan with a tone-on-tone embroidered neckline and a white openwork crocheted kufi cap. Sitting in a simple bright health-centre consultation room, listening attentively to a Gambian female nurse in a white uniform who sits facing him, medium shot. Photorealistic vertical 9:16 smartphone photo in authentic UGC style, natural warm West African light, true-to-life dark skin texture, shallow depth of field, no captions or added text overlays, no watermark.

**Image-to-video prompt**
Ebrima (Gambian man ~65, short white-grey beard, gold-rimmed glasses, light-blue kaftan, white kufi) listens and nods slowly while the nurse speaks to him calmly with a reassuring hand gesture; Ebrima does not speak. Static camera. Mood: responsible, serious. Visible characters do not lip-sync and keep their mouths closed or relaxed while the locked narrator says off-screen: “If there is a wound that does not heal, or very strong pain, see a doctor first.” Preserve faces, bodies, clothing, product design and rendering style exactly.

**Sound / voiceover direction**
Voix off narrateur hors champ — Narrator (off-screen): middle-aged American man, deep smooth baritone, warm polished promotional timbre, General American accent, steady measured pace with short dramatic pauses, confident and reassuring, persuasive without shouting. Segment `voix-off-christopher-smooth.mp3` de 91.58 à 96.94 s. Aucun personnage ne parle. Ambiance feutrée. Musique : baisse. Pas d'effet. Voix toujours dominante.

**Estimated length**
5.4 seconds

### Plan 32 — 96.94 → 100.04 s

**Script section / voiceover text**
“Try Miracle Balm today, without any risk.”

**Text-to-image prompt**
Mariama, a Gambian woman about 42 years old, slender, dark-brown skin, oval face with a warm smile and even teeth, long thin black braids parted in the middle and gathered behind her shoulders, small gold hoop earrings, wearing a bright yellow-and-green wax-print fitted top with puffed sleeves and matching wrap skirt. Holding the Miracle Balm product: a small lime-green cardboard box with a dark-green leafy wreath illustration around bold white text 'MIRACLE BALM' and small white daisy flowers, next to a round silver metal tin (30 g) whose lid shows the same dark-green leaf wreath and 'MIRACLE BALM', the open tin revealing a smooth light-pink balm up beside her face at her market stall, confident smile, medium close-up. Photorealistic vertical 9:16 smartphone photo in authentic UGC style, natural warm West African light, true-to-life dark skin texture, shallow depth of field, no captions or added text overlays, no watermark.

**Image-to-video prompt**
Mariama (Gambian woman ~42, middle-parted braids, gold hoops, yellow-and-green wax-print outfit) raises the lime-green Miracle Balm box and round silver tin with pink balm beside her face and gives a confident nod, mouth closed. Slight push-in. Mood: trust. Visible characters do not lip-sync and keep their mouths closed or relaxed while the locked narrator says off-screen: “Try Miracle Balm today, without any risk.” Preserve faces, bodies, clothing, product design and rendering style exactly.

**Sound / voiceover direction**
Voix off narrateur hors champ — Narrator (off-screen): middle-aged American man, deep smooth baritone, warm polished promotional timbre, General American accent, steady measured pace with short dramatic pauses, confident and reassuring, persuasive without shouting. Segment `voix-off-christopher-smooth.mp3` de 96.94 à 100.04 s. Aucun personnage ne parle. Marché doux. Musique : énergie finale. Voix toujours dominante.

**Estimated length**
3.1 seconds

### Plan 33 — 100.04 → 104.76 s

**Script section / voiceover text**
“You have thirty days. If the burning doesn't calm down, you get your money back.”

**Text-to-image prompt**
Awa, a Gambian woman about 55 years old, medium build, deep dark-brown skin, round face with high cheekbones, warm brown eyes, small gold stud earrings, hair wrapped in an orange-and-indigo patterned head tie, wearing a loose orange-and-indigo wax-print kaftan. Standing in her compound in afternoon light, one hand on her heart and the other holding the round silver tin of the Miracle Balm product: a small lime-green cardboard box with a dark-green leafy wreath illustration around bold white text 'MIRACLE BALM' and small white daisy flowers, next to a round silver metal tin (30 g) whose lid shows the same dark-green leaf wreath and 'MIRACLE BALM', the open tin revealing a smooth light-pink balm, warm reassuring smile at the camera, medium shot. Photorealistic vertical 9:16 smartphone photo in authentic UGC style, natural warm West African light, true-to-life dark skin texture, shallow depth of field, no captions or added text overlays, no watermark.

**Image-to-video prompt**
Awa (Gambian woman ~55, orange-and-indigo head tie and kaftan, gold stud earrings) keeps her hand on her heart and nods reassuringly toward the camera, no speaking. Static camera. Mood: reassurance. Visible characters do not lip-sync and keep their mouths closed or relaxed while the locked narrator says off-screen: “You have thirty days. If the burning doesn't calm down, you get your money back.” Preserve faces, bodies, clothing, product design and rendering style exactly.

**Sound / voiceover direction**
Voix off narrateur hors champ — Narrator (off-screen): middle-aged American man, deep smooth baritone, warm polished promotional timbre, General American accent, steady measured pace with short dramatic pauses, confident and reassuring, persuasive without shouting. Segment `voix-off-christopher-smooth.mp3` de 100.04 à 104.76 s. Aucun personnage ne parle. Effet : petit son « validation » au moment de « money back ». Voix toujours dominante.

**Estimated length**
4.7 seconds

### Plan 34 — 104.76 → 106.32 s

**Script section / voiceover text**
“Click below to order.”

**Text-to-image prompt**
Mariama, a Gambian woman about 42 years old, slender, dark-brown skin, oval face with a warm smile and even teeth, long thin black braids parted in the middle and gathered behind her shoulders, small gold hoop earrings, wearing a bright yellow-and-green wax-print fitted top with puffed sleeves and matching wrap skirt. At her market stall, pointing down toward the bottom of the frame with her index finger, smiling, medium close-up. Photorealistic vertical 9:16 smartphone photo in authentic UGC style, natural warm West African light, true-to-life dark skin texture, shallow depth of field, no captions or added text overlays, no watermark.

**Image-to-video prompt**
Mariama (Gambian woman ~42, middle-parted braids, gold hoops, yellow-and-green wax-print outfit) points down twice toward the bottom of the frame with an encouraging smile, no speaking. Static camera. Mood: call to action. Visible characters do not lip-sync and keep their mouths closed or relaxed while the locked narrator says off-screen: “Click below to order.” Preserve faces, bodies, clothing, product design and rendering style exactly.

**Sound / voiceover direction**
Voix off narrateur hors champ — Narrator (off-screen): middle-aged American man, deep smooth baritone, warm polished promotional timbre, General American accent, steady measured pace with short dramatic pauses, confident and reassuring, persuasive without shouting. Segment `voix-off-christopher-smooth.mp3` de 104.76 à 106.32 s. Aucun personnage ne parle. Effet : « clic » discret. Voix toujours dominante.

**Estimated length**
1.6 seconds

### Plan 35 — 106.32 → 109.14 s

**Script section / voiceover text**
“Free delivery today, and cash on delivery —”

**Text-to-image prompt**
a young Gambian delivery rider about 25 years old, athletic, dark-brown skin, short black hair, wearing a red polo shirt and a black open-face motorbike helmet. Stopped on his motorbike at the metal gate of a family compound, handing a small parcel to Awa, a Gambian woman about 55 years old, medium build, deep dark-brown skin, round face with high cheekbones, warm brown eyes, small gold stud earrings, hair wrapped in an orange-and-indigo patterned head tie, wearing a loose orange-and-indigo wax-print kaftan, who reaches out smiling, medium-wide shot, afternoon sun. Photorealistic vertical 9:16 smartphone photo in authentic UGC style, natural warm West African light, true-to-life dark skin texture, shallow depth of field, no captions or added text overlays, no watermark.

**Image-to-video prompt**
the rider (young Gambian man, red polo, black open-face helmet) hands the parcel to Awa (Gambian woman ~55, orange-and-indigo head tie and kaftan, gold stud earrings), who takes it with a smile; neither speaks. Static camera. Mood: easy, friendly. Visible characters do not lip-sync and keep their mouths closed or relaxed while the locked narrator says off-screen: “Free delivery today, and cash on delivery —” Preserve faces, bodies, clothing, product design and rendering style exactly.

**Sound / voiceover direction**
Voix off narrateur hors champ — Narrator (off-screen): middle-aged American man, deep smooth baritone, warm polished promotional timbre, General American accent, steady measured pace with short dramatic pauses, confident and reassuring, persuasive without shouting. Segment `voix-off-christopher-smooth.mp3` de 106.32 à 109.14 s. Aucun personnage ne parle. Effet : moteur de moto au ralenti. Voix toujours dominante.

**Estimated length**
2.8 seconds

### Plan 36 — 109.14 → 111.31 s

**Script section / voiceover text**
“you pay only when it's in your hand.”

**Text-to-image prompt**
Close-up of the hands of Awa, a Gambian woman about 55 years old, medium build, deep dark-brown skin, round face with high cheekbones, warm brown eyes, small gold stud earrings, hair wrapped in an orange-and-indigo patterned head tie, wearing a loose orange-and-indigo wax-print kaftan holding the lime-green Miracle Balm box while handing Gambian dalasi banknotes to a young Gambian delivery rider about 25 years old, athletic, dark-brown skin, short black hair, wearing a red polo shirt and a black open-face motorbike helmet. Photorealistic vertical 9:16 smartphone photo in authentic UGC style, natural warm West African light, true-to-life dark skin texture, shallow depth of field, no captions or added text overlays, no watermark.

**Image-to-video prompt**
The hands of Awa (Gambian woman ~55, orange-and-indigo head tie and kaftan, gold stud earrings) pass the dalasi notes to the rider (young Gambian man, red polo, black open-face helmet) while keeping the Miracle Balm box. Static close-up. Mood: trust, done deal. Visible characters do not lip-sync and keep their mouths closed or relaxed while the locked narrator says off-screen: “you pay only when it's in your hand.” Preserve faces, bodies, clothing, product design and rendering style exactly.

**Sound / voiceover direction**
Voix off narrateur hors champ — Narrator (off-screen): middle-aged American man, deep smooth baritone, warm polished promotional timbre, General American accent, steady measured pace with short dramatic pauses, confident and reassuring, persuasive without shouting. Segment `voix-off-christopher-smooth.mp3` de 109.14 à 111.31 s. Aucun personnage ne parle. Effet : froissement de billets. Musique : résolution finale. Voix toujours dominante.

**Estimated length**
2.2 seconds

---

**Durée totale : 111.3 s** (accroche A + corps). Version accroche B : 110.3 s.

**À générer :** 40 images (36 pour la version A, + 4 pour l'accroche B), 3 images de référence personnages, puis autant de clips Kling.
