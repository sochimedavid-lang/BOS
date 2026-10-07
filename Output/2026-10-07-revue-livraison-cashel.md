# Revue de l'analyse créas Meta à la lumière de Cashel — 7 octobre 2026

Complément à `2026-10-07-analyse-creas-meta.md`. Source : Cashel, Gambie, commandes du 31 août au 7 octobre 2026.

## Constat principal

Les seuils de l'analyse créas reposent sur les taux de livraison saisis dans la config Cashel (10 % à 40 %). Ces taux ne sont pas mesurés : la moitié des commandes n'a pas de statut final.

| Période | Commandes | Livrées | Statut ouvert (nouvelle, confirmée, veut rappeler, programmée) |
|---|---:|---:|---:|
| 31/08 → 07/10 | 565 | 108 | 296 (52 %) |
| 31/08 → 20/09 (17 jours et plus) | 339 | 78 | 168 (50 %) |

Sur la cohorte de 17 jours et plus, en excluant les « nouvelle » (Turmeric sans stock, lot Batana du 31/08), il reste **137 commandes confirmées, à rappeler ou programmées** sans issue. En paiement à la livraison, une commande non livrée après 7 à 10 jours est quasi perdue. Soit le traitement des commandes a décroché, soit Cashel n'est pas mis à jour.

Commandes « nouvelle » jamais appelées (83) : 41 Turmeric (stock en transit, normal), 15 Batana datées du 31/08, 12 sans produit rattaché (erreur de mapping), 15 du jour.

## Taux de livraison par produit : fourchette réelle

Borne basse = taux actuel (toute commande ouverte est perdue). Borne haute = livrées / commandes clôturées (livrée, annulée, injoignable).

| Produit | Commandes | Livrées | Annulées | Injoignables | Ouvertes | Taux actuel | Taux sur clôturées | Taux config |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Miracle Balm | 65 | 28 | 5 | 5 | 27 | 43 % | 74 % | 40 % |
| Kinoki | 168 | 50 | 13 | 25 | 80 | 30 % | 57 % | 30 % |
| North Moon | 175 | 27 | 31 | 44 | 73 | 15 % | 26 % | 15 % |
| Batana | 103 | 3 | 13 | 25 | 62 | **3 %** | **7 %** | 10 % |

## Ce que ça change aux verdicts

Point mort = marge par livraison × taux. Marge = prix − coût de revient − 420 GMD ; 76,66 GMD = 1 $.

| Produit | CPA observé | Point mort au taux actuel | Point mort au taux sur clôturées | Verdict |
|---|---:|---:|---:|---|
| Miracle Balm | 1,72 $ | 7,3 $ | 12,5 $ | Très rentable dans les deux cas. Priorité 1 confirmée |
| Kinoki | 2,42 $ | 4,8 $ | 9,1 $ | Rentable dans les deux cas |
| North Moon | 2,10 $ | 2,6 $ | 4,6 $ | Rentable ; dans l'objectif (1,66 $) seulement si les commandes ouvertes se livrent |
| Batana | 1,56 $ | 0,44 $ | 1,10 $ | **Perd de l'argent dans les deux cas**, toutes créas confondues sauf New Créa 8 (0,77 $) dans le meilleur scénario |

Conclusions robustes (vraies quel que soit le devenir des commandes ouvertes) :
- Miracle Balm > Kinoki > North Moon > Batana.
- Batana est déficitaire. L'analyse le donnait au point mort sur la base d'un taux de 10 % que Cashel ne montre pas.

Conclusion fragile : le niveau de priorité de North Moon. Il dépend entièrement du traitement des 73 commandes ouvertes et des 44 injoignables (25 % des commandes).

## Corrections au plan de flotte

1. **Retirer Batana du plan** (BO-1 à BO-5) et mettre ses pubs en pause tant que la cause des injoignables (25 sur 41 commandes clôturées) n'est pas trouvée. Faux numéros, mauvais ciblage ou délai d'appel : à vérifier sur un échantillon de 10 fiches.
2. **Réduire le plan de 23 créas à 8–10** concentrées sur Miracle Balm et Kinoki. Cinq produits en parallèle dispersent la production pour des produits dont la livraison n'est pas mesurée.
3. **North Moon : aucune nouvelle créa** tant que les injoignables et les rappels ne sont pas traités. Les créas actuelles (1,0–1,5 $) suffisent si la livraison remonte vers 25 %.
4. **Turmeric : pas de pub avant l'arrivée du stock.** 41 clients attendent depuis le 20–23 septembre ; les rappeler dès réception, avant de relancer la pub.

## Levier n° 1 : le stock de commandes ouvertes

213 commandes confirmées, à rappeler ou programmées. Marge moyenne par livraison ≈ 1 250 GMD (16 $). Récupérer 20 % de ces commandes = ~43 livraisons ≈ **690 $ de marge sans un dollar de pub**, soit 80 % de la dépense Meta de la période. Hypothèse de récupération de 20 % : confiance faible à moyenne. Elle tombe si ces commandes sont en réalité déjà livrées mais non saisies, auquel cas c'est un problème de saisie et tous les taux de livraison sont sous-estimés.

## Données à corriger dans Cashel

- 12 commandes « nouvelle » sans produit rattaché (23–26 sept.).
- Taux de livraison config Batana : 10 % saisi, 3–7 % observé.
- Statuts des commandes programmées depuis plus de 10 jours.
