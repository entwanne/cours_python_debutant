### Première étape

Nous allons y aller par étapes et la première consistera en un seul tour de jeu.

D'abord, nous utiliserons `input` pour initialiser le jeu en demandant aux joueurs les noms et points de vie de leurs monstres.
Nous les conserverons dans des variables pour les afficher au cours du jeu.

Nous ne sommes pour l'instant pas en mesure de traiter une liste d'attaques, nous demanderons alors simplement aux joueurs d'entrer le nombre de PV qu'ils souhaitent infliger à l'adversaire.
Chaque monstre aura un tour de jeu puis un récapitulatif des PV sera affiché.

Nous utiliserons toutes les informations recueillies pour fournir le plus d'informations possibles aux joueurs.

Voici à quoi pourrait ressembler le déroulé d'une partie :

```
Entrez le nom du 1er joueur : pythachu
Et son nombre de PV : 50
Entrez le nom du 2ème joueur : pythard
Et son nombre de PV : 40

+++++++++++++++++++++++++++++++++++++++++++++
+ Pythachu (50 PV) affronte Pythard (40 PV) +
+++++++++++++++++++++++++++++++++++++++++++++

Pythachu, combien de PV infligez-vous à Pythard ? 30

+++++++++++++++++++++++++++++++++++++++++++
+ Pythachu attaque Pythard qui perd 30 PV +
+ Pythard a maintenant 10 PV              +
+++++++++++++++++++++++++++++++++++++++++++

Pythard, combien de PV infligez-vous à Pythachu ? 15

+++++++++++++++++++++++++++++++++++++++++++
+ Pythard attaque Pythachu qui perd 15 PV +
+ Pythachu a maintenant 35 PV             +
+++++++++++++++++++++++++++++++++++++++++++

+++++++++++++++++++++++
+ Résulat du combat : +
+ Pythachu a 35 PV    +
+ Pythard a 10 PV     +
+++++++++++++++++++++++
```

* Ajouter quelques notes sur le formattage
