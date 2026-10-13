# Motion Kit : le skill pour créer tes vidéos motion avec Claude

Ce dossier est un **skill** pour Claude Code. Une fois installé, tu demandes à Claude « fais-moi une pub motion de 20 secondes pour le restaurant X » ou « refais cette vidéo en français ». Claude suit alors la méthode du kit : texte, voix off, animation, bruitages, contrôle, rendu.

## Ce qu'il te faut (une seule fois)
- **Claude Code**, l'outil où tu travailles avec Claude sur ton ordinateur.
- **Node.js** : HyperFrames se lance avec `npx`, rien d'autre à installer.
- **Python 3** avec `numpy` et `scipy` (`pip install numpy scipy`), ainsi que **ffmpeg**.
- **En option :** un compte ElevenLabs pour les voix off (sinon Gemini TTS, gratuit).

## Installer le skill
Copie le dossier `motion-kit` complet dans l'un de ces deux endroits :
- `~/.claude/skills/motion-kit/` : disponible dans tous tes projets ;
- ou `ton-projet/.claude/skills/motion-kit/` : disponible dans ce projet seulement.

Relance Claude Code. Le skill s'active tout seul dès que tu parles de vidéo motion.

## Exemples de demandes
- « Fais une pub motion verticale de 20 s pour Eden Food, un restaurant à Cotonou. Voix off énergique. »
- « Voici une vidéo de référence : refais la même structure en français pour mon client. »
- « Fais un post motion sur le thème "tes revenus sont le reflet de tes habitudes". »

## Ce que tu obtiens
- `out/final.mp4` : la vidéo verticale, prête pour TikTok, Reels ou un statut WhatsApp.
- `out/contact.png` : une planche pour vérifier d'un coup d'œil.
- Les sources : tu peux redemander une modification (texte, couleur, rythme) sans tout refaire.

## Contenu du dossier
| Fichier | Rôle |
|---|---|
| `SKILL.md` | La méthode que Claude suit |
| `kit/motion-kit.js` · `kit/motion-kit.css` | Les briques d'animation et les styles |
| `tools/new_project.py` | Crée un nouveau projet vidéo prêt à remplir |
| `tools/captions.py` | Sous-titres automatiques à partir de la voix off |
| `tools/sound.py` | Musique, bruitages et voix, mixés au bon volume |
| `templates/index.html` | Le gabarit de départ |
