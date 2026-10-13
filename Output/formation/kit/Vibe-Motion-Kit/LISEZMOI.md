# Kit Vibe Motion

Ton kit de création vidéo. Il contient :

| Élément | À quoi ça sert |
|---|---|
| `.claude/skills/motion-kit/` | Le **skill Vibe Motion** : la méthode complète et des briques d'animation déjà testées (textes qui montent, cartes, bouclier 3D, compteurs, coupes, fond fluide…), plus les outils pour la bande-son (musique + bruitages + voix) et les sous-titres. |
| `CLAUDE.md` | Les consignes que Claude lit automatiquement dans ton atelier : il parle français, suit la méthode et range tes vidéos. |
| `exemples/` | 3 vidéos complètes faites avec ce kit (Sikaflow, Rempart Défense, Eden Food), avec leur code : Claude s'en inspire. |

## Installer le kit

### Sur téléphone (application Claude + GitHub)
1. Dans ton dépôt GitHub `vibe-motion-atelier` : **Add file → Upload files** → choisis `Vibe-Motion-Kit.zip` → **Commit changes**.
2. Dans l'application Claude, ouvre **Code**, choisis ton dépôt, et envoie :

> Décompresse Vibe-Motion-Kit.zip à la racine du dépôt (le contenu du dossier Vibe-Motion-Kit doit se retrouver directement à la racine), puis supprime le fichier zip. Ensuite installe ce qu'il faut pour faire des vidéos : les skills HyperFrames (npx skills add heygen-com/hyperframes), le navigateur de rendu (npx hyperframes browser ensure), FFmpeg s'il manque, et les modules Python numpy et scipy. Fais un commit, pousse sur GitHub, et explique-moi chaque étape simplement.

### Sur ordinateur
1. Décompresse `Vibe-Motion-Kit.zip` et mets son **contenu** dans ton dossier `vibe-motion` (le dossier `.claude` est caché : c'est normal).
2. Ouvre ce dossier avec Claude (onglet Code de l'application) et envoie la même instruction qu'au-dessus, sans la première phrase sur le zip.

## Faire une vidéo
Demande simplement, en français :

> Fais une pub motion verticale de 20 secondes pour [nom de l'entreprise], [ce qu'elle vend], à [ville]. Style [élégant / énergique / tech]. Montre-moi les captures avant d'exporter.

Le guide Vibe Motion (PDF) contient 50 instructions prêtes à copier.

---
Kit réservé à l'acheteur de la formation Vibe Motion. Merci de ne pas le partager.
HyperFrames est un logiciel open source de HeyGen (licence Apache 2.0). Claude est une marque d'Anthropic. Vibe Motion est une formation indépendante.
