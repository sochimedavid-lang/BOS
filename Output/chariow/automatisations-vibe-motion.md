# Automatisations Chariow — Vibe Motion (14/10/2026)

Boutique PERYAL. Produit : Vibe Motion 2026 (prd_zqv7lcu4).
Balises confirmées dans tes anciens workflows : {{customerName}} et {{checkoutUrl}}.

## Réglages communs
- Produit concerné : **Vibe Motion 2026 uniquement** (pas tout le catalogue).
- « Répondre à » : ton adresse email (pour que les réponses des clients t'arrivent).
- Les 3 anciens workflows (Abandon, Echoué, Réussie) parlent du PACK KING SEDUCTION et s'appliquent à tout le catalogue : les supprimer, ou au minimum ne jamais les réactiver.

---

## Workflow 1 — « VM · Paiement non finalisé »
- Déclencheurs : **Vente abandonnée** + **Vente échouée**
- Arrêter si le client possède le produit : **OUI**
- Limite : 1 exécution par client sur 30 jours
- Arrêt en cas d'échec : non

### Email 1 — 30 min après
**Objet :** {{customerName}}, ta place à 2 900 F t'attend

Salut {{customerName}} 👋

Tu as commencé ton inscription à Vibe Motion, mais le paiement ne s'est pas terminé.

Ça arrive souvent avec le Mobile Money : la confirmation n'a pas été validée à temps, le réseau a coupé, ou le solde était un peu juste. Rien de grave.

👉 Reprendre mon inscription : {{checkoutUrl}}

Si ça a bloqué, 3 astuces :
• Garde ton téléphone déverrouillé et valide la demande de ton opérateur dès qu'elle arrive (elle expire vite).
• Vérifie que ton solde couvre 2 900 F.
• Si la page s'ouvre dans Facebook ou Instagram, ouvre le lien dans Chrome.

Ta place à 2 900 F est encore disponible. Ensuite, le prix passe à 10 000 F.

Un souci ? Réponds simplement à cet email, on t'aide.

— L'équipe Vibe Motion

### Email 2 — 1 jour après
**Objet :** « Je n'ai qu'un téléphone, ça marche pour moi ? »

Salut {{customerName}},

C'est la question qu'on nous pose le plus. La réponse est oui.

Tout Vibe Motion se fait depuis ton téléphone : tu décris la vidéo à l'IA, elle crée l'animation, tu la récupères prête à publier. Pas d'ordinateur, pas de logiciel de montage, pas besoin d'être doué en design.

Ce que tu apprends, étape par étape :
1. Créer ta première pub animée pour un commerce (restaurant, boutique, salon…)
2. Monter un portfolio qui donne confiance
3. Trouver tes premiers clients autour de toi

Ce qu'il te faut : ton téléphone, une connexion internet et un abonnement Claude (on te montre comment le payer par Mobile Money).

Et si tu n'as pas fait ta première vidéo en 7 jours, on te rembourse.

👉 Je finalise mon inscription (2 900 F) : {{checkoutUrl}}

— L'équipe Vibe Motion

### Email 3 — 3 jours après
**Objet :** Dernier rappel pour ta place à 2 900 F

Salut {{customerName}},

C'est mon dernier message à ce sujet, promis.

Les places à 2 900 F sont réservées aux 50 premiers élèves. Après, l'accès passe à 10 000 F.

Si tu veux apprendre un métier que tu peux exercer depuis ton téléphone, c'est le moment le moins cher pour commencer, et tu restes couvert par la garantie 7 jours.

👉 Je prends ma place : {{checkoutUrl}}

Si ce n'est pas le bon moment, aucun souci. Et si quelque chose te freine, réponds-moi en une phrase : je lis tout.

— L'équipe Vibe Motion

---

## Workflow 2 — « VM · Bienvenue élève »
- Déclencheur : **Vente réussie**
- Limite : 1 exécution par client
- Arrêt en cas d'échec : non

### Email 1 — immédiat (1 min)
**Objet :** Bienvenue dans Vibe Motion 🎬 Voici ta première étape

Salut {{customerName}},

Bienvenue ! Ton paiement est validé et ton accès est prêt.

📥 Ton guide : tu le retrouves à tout moment dans ton espace client Chariow → https://portal.chariow.com (connecte-toi avec l'email de ta commande).
💬 La communauté des élèves : [LIEN DU GROUPE WHATSAPP]

Ta mission pour aujourd'hui (20 minutes) :
1. Ouvre le guide et lis le module 1.
2. Crée ton compte Claude (le guide te montre comment le payer par Mobile Money).

Ne cherche pas à tout lire d'un coup. Une étape par jour suffit pour sortir ta première vidéo cette semaine.

Ta garantie court sur 7 jours. Si tu bloques, réponds à cet email : on t'aide à avancer.

— L'équipe Vibe Motion

### Email 2 — 2 jours après
**Objet :** Tu en es où, {{customerName}} ?

Salut {{customerName}},

Petit point rapide : ton compte Claude est prêt ?

Si oui, lance ta première vidéo aujourd'hui. Choisis un commerce que tu connais (le maquis du coin, une boutique, un salon de coiffure) et fais-lui une pub. Pas besoin qu'il te l'ait demandé : ce sera le premier exemple de ton portfolio.

Si tu bloques quelque part, réponds à cet email avec une capture d'écran. On te débloque.

— L'équipe Vibe Motion

### Email 3 — 6 jours après
**Objet :** Montre-nous ta première vidéo 🎥

Salut {{customerName}},

Ça fait bientôt une semaine. Si ta première vidéo est prête, envoie-la en réponse à cet email (ou dans le groupe) : on la regarde et on te dit comment la rendre encore plus pro.

Pas encore terminée ? Dis-nous où tu bloques. C'est exactement pour ça qu'on est là, et ta garantie est toujours valable.

Et si Vibe Motion te plaît, transfère cet email à un ami qui veut apprendre un métier sur son téléphone.

— L'équipe Vibe Motion
