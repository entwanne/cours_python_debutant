### Itérer sur les attaques

Nous allons donc modifier le code de notre TP pour mettre les attaques disponibles sous la forme d'une liste.
Ou même plutôt deux listes, une pour les noms d'attaques et une pour les dégats associés.

Ainsi, il suffira d'itérer sur cette liste pour proposer chaque attaque au joueur, plutôt que de devoir les écrire une par une.

```
1. charge
2. tonnerre
```

En plus de ça, on pourra identifier l'attaque par son index (sa position dans la liste) et donc directement savoir quelle est l'attaque sélectionnée.
En effet, si l'utilisateur entre `2`, on peut savoir que ça correspond au nombre 2 (conversion en nombre avec `int`) soit à l'index 1 (puisqu'on commence à 0), et donc on peut exécuter l'attaque « tonnerre » sans avoir un bloc conditionnel par attaque.

On peut aussi ajouter une boucle `while` pour vérifier la validité de la saisie : si l'utilisateur entre un numéro d'attaque incorrect, il serait bon de lui demander à nouveau de choisir une attaque.  
On utilisera pour ça la méthode `isdigit` des chaînes de caractères qui renvoie un booléen indiquant si la chaîne représente un nombre ou non (ce qui permet d'effectuer la conversion sans erreur), on testera aussi si ce nombre est dans le bon intervalle.

En bonus, plutôt que de demander à l'utilisateur d'entrer un nombre, on pourrait directement récupérer un nom d'attaque, et retrouver cette attaque dans notre liste de noms.