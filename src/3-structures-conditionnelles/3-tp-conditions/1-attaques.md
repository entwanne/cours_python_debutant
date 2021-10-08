### Proposer plusieurs attaques

L'idée maintenant va donc être d'avoir un nombre de dégâts pour chaque attaque, et de proposer à l'utilisateur l'une ou l'autre des attaques.

Ce qu'on voudrait c'est afficher une sorte de menu proposant les différentes attaques.
Par exemple on pourrait utiliser le message suivant lors de l'`input` :

```
Quelle attaque voulez-vous utiliser ?
1. Charge (-20 PV)
2. Tonnerre (-50 PV)
```

Une condition permettrait ensuite de savoir quelle attaque a été choisie (`'1'` ou `'2'`) et d'agir en conséquence en infligeant les dégâts à l'adversaire.

En bonus on pourrait même autoriser d'entrer le nom de l'attaque plutôt que son numéro, je vous laisse y réfléchir.

Notre jeu ne comporte encore qu'un seul tour, mais on pourrait aussi conclure la fin du tour en annonçant le vainqueur, à l'aide d'une condition sur le nombre de PV..
