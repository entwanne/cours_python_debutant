### Proposer plusieurs attaques

```python
if attaque == 'charge':
    pv2 -= 20
elif attaque == 'tonnerre':
    pv2 -= 50
```

L'idée va donc être maintenant d'avoir un nombre de dégâts pour chaque attaque, et de proposer à l'utilisateur l'une ou l'autre des attaques.

Ce qu'on voudrait c'est afficher une sorte de menu proposant les différentes attaques.

```
Quelle attaque voulez-vous utiliser ?
1. Charge (-20 PV)
2. Tonnerre (-50 PV)
```

Une condition permettrait ensuite de savoir quelle attaque a été choisie (`'1'` ou `'2'`) et d'agir en conséquence en infligeant les dégâts à l'adversaire.

Malgré le fait que notre jeu ne comporte qu'un seul tour, on pourrait aussi conclure la fin du tour en annonçant le vainqueur (celui à qui il reste le plus de PV).
