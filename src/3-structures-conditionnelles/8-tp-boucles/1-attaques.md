### Itérer sur les attaques

Nous allons donc modifier le code de notre TP pour mettre les attaques disponibles sous la forme d'une liste.
Ou même plutôt deux listes : une pour les noms d'attaques et une pour les dégats associés.

```python
attack_names = ['charge', 'tonnerre']
attack_damages = [20, 50]
```

Ainsi, il suffira d'itérer sur cette liste pour proposer chaque attaque au joueur, plutôt que de devoir les écrire manuellement une par une.

```
1. charge
2. tonnerre
```

En plus de ça, on pourra identifier l'attaque par son index (sa position dans la liste) et donc directement savoir quelle est l'attaque sélectionnée.
En effet, si l'utilisateur entre `2`, on peut savoir que ça correspond au nombre 2 (conversion en nombre avec `int`) soit à l'index 1 (puisqu'on commence toujours à l'index 0), et donc on peut exécuter l'attaque « tonnerre » sans avoir un bloc conditionnel par attaque.

```pycon
>>> attack_idx = int(input('Quelle attaque ? ')) - 1
Quelle attaque ? 2
>>> attack_names[attack_idx]
'tonnerre'
```

On peut aussi ajouter une boucle `while` pour vérifier la validité de la saisie : si l'utilisateur entre un numéro d'attaque incorrect, il serait bon de lui demander à nouveau de choisir une attaque plutôt que de couper le programme.  
On utilisera pour ça la méthode `isdigit` des chaînes de caractères qui renvoie un booléen indiquant si la chaîne représente un nombre ou non (ce qui permet d'effectuer la conversion sans erreur), on testera aussi si ce nombre est dans le bon intervalle.

```pycon
>>> 'abc'.isdigit()
False
>>> '123'.isdigit()
True
>>> n = 2
>>> 1 <= n <= len(attack_names)
True
>>> n = 3
>>> 1 <= n <= len(attack_names)
False
```

L'utilisation d'expressions booléennes (à base d'opérations `not` et `or`) nous sera alors utile pour écrire la condition sous laquelle une saisie sera invalide.

Je vous laisse compléter cette partie avant de passer à la section suivante pour continuer à améliorer notre programme.

#### Solution

Voici la solution pour cette étape de l'exercice, le reste du code étant inchangé.

[[s]]
| ```python
| ...
| 
| attack_names = ['charge', 'tonnerre']
| attack_damages = [20, 50]
| 
| menu = 'quelle attaque voulez-vous utiliser ?'
| 
| # Joueur 1
| 
| print(name1, menu)
| i = 1
| for name in attack_names:
|     print(i, name.capitalize(), -attack_damages[i - 1], 'PV')
|     i += 1
| 
| att1 = input('> ')
| while not att1.isdigit() or not 1 <= int(att1) <= len(attack_names):
|     print('Attaque invalide, veuillez resaisir le numéro')
|     att1 = input('> ')
| 
| att1_idx = int(att1) - 1
| damages = attack_damages[att1_idx]
| 
| pv2 -= damages
| print(name1, 'attaque', name2, 'qui perd', damages, 'PV')
| 
| # Même chose pour le joueur 2
| 
| ...
| ```
