### Itération

#### Parcourir des listes

Avec ce bloc, il nous est ainsi possible d'itérer sur une liste et d'appliquer un même traitement à toutes les valeurs.
Mais est-ce que c'est toujours ça que l'on veut ? Pas nécessairement, non, il peut être utile de différencier les cas.  
Heureusement, nous avons pour cela les conditions avec lesquelles nous allons séparer nos cas.

Par exemple, on pourrait imaginer un mécanisme de recherche dans une liste.
Le code parcourerait tous les éléments jusqu'à trouver celui ou ceux qui répondent à notre critère.

Disons par exemple que nous voulions trouver un nombre impair dans une liste de nombres.
Dans le bloc de notre boucle, nous testerons si la valeur actuelle est impaire, et la conserverons dans une variable si tel est le cas.  
Ainsi, à la fin de la boucle, cette variable définie uniquement sous condition sera toujours assignée à notre valeur.

```pycon
>>> numbers = [8, 2, 6, 3, 4, 0]
>>> for number in numbers:
...     if number % 2 == 1:
...         found = number
... 
>>> print('Trouvé :', found)
Trouvé : 3
```

Vous pouvez changer l'ordre des éléments de la liste, le résultat est toujours le même.

On a par contre un petit soucis si notre liste contient plusieurs éléments impairs.

```pycon
>>> numbers = [8, 2, 6, 3, 4, 0, 5]
>>> for number in numbers:
...     if number % 2 == 1:
...         found = number
... 
>>> print('Trouvé :', found)
Trouvé : 5
```

Et oui, la condition est certes vraie pour 3 mais elle l'est aussi pour 5.
Ainsi, on définit une première fois `found = 3` mais on l'écrase ensuite pour lui assigner 5, et on perd toute trace du 3.

Il serait bien de pouvoir conserver toutes les valeurs qui correspondent à notre recherche.
On n'aurait pas un type de donnée pour contenir un nombre indéterminé de valeurs ? La liste bien entendu !

```pycon
>>> found = []
>>> for number in numbers:
...     if number % 2 == 1:
...         found.append(number)
... 
>>> found
[3, 5]
```

Passons maintenant à un exemple plus complexe et tentons d'identifier le plus grand nombre dans une liste.
On va ainsi itérer sur les nombres, et s'il est le plus grand, on le conserve dans une variable.

Sur le principe c'est très bien, mais comment saura-t-on sur le moment qu'il est le plus grand de tous les nombres ?
C'est difficile à déterminer, il nous faudrait à chaque fois reparcourir toute la liste pour voir si l'on trouve un autre nombre encore plus grand… ça fait beaucoup d'opérations.

Mais ce qu'on peut facilement déterminer, c'est s'il est le plus grand nombre jusqu'ici.
En effet, on peut conserver dans une variable le plus grand nombre trouvé, et le mettre à jour chaque fois qu'on tombe sur un nombre qui lui est supérieur.
À la fin du parcours, on est sûr que notre variable contient le plus grand nombre de la liste.

```pycon
>>> numbers = [3, 2, 5, 8, 4, 7, 9, 1, 6]
>>> max_number = 0
>>> for number in numbers:
...     if number > max_number:
...         max_number = number
...         print("Le plus grand nombre trouvé jusqu'ici est", max_number)
... 
Le plus grand nombre trouvé jusqu'ici est 3
Le plus grand nombre trouvé jusqu'ici est 5
Le plus grand nombre trouvé jusqu'ici est 8
Le plus grand nombre trouvé jusqu'ici est 9
>>> max_number
9
```

On notera que cette opération existe déjà en Python et est réalisée par la fonction `max`.

```pycon
>>> max(numbers)
9
```

#### Itérables

Les listes ne sont pas le seul type de données que l'on peut utiliser dans une boucle `for`, cela fonctionne aussi avec des chaînes de caractères par exemple, pour les parcourir caractère par caractère.

```pycon
>>> for char in 'Hello':
...     print(char)
... 
H
e
l
l
o
```

Plus généralement on parle d'itérables pour désigner les types que l'on peut parcourir avec un bloc `for`, c'est-à-dire sur lesquels on peut itérer.

Un nouveau type de données va nous être bien utile ici, c'est le `range`.
Un `range` représente un intervalle entre deux nombres entiers, on peut le voir comme la liste des nombres entre ces deux bornes.

L'intervalle formé entre 1 et 10 se note par exemple `range(1, 10)`.
Il faut savoir que c'est un intervalle fermé à gauche mais ouvert à droite, il contient ainsi 1 mais pas 10 (il s'arrête à 9).

```pycon
>>> for n in range(1, 10):
...     print(n)
... 
1
2
3
4
5
6
7
8
9
```

Avec ça, nous pouvons donc avoir une boucle itérant sur des nombres.
Et encore une fois `n` est ici une variable redéfinie à chaque tour de boucle.
On peut utiliser sa valeur dans nos calculs, comme ici pour la table de multiplication par 3.

```pycon
>>> for n in range(1, 11):
...     print('3 ×', n, '=', 3 * n)
... 
3 × 1 = 3
3 × 2 = 6
3 × 3 = 9
3 × 4 = 12
3 × 5 = 15
3 × 6 = 18
3 × 7 = 21
3 × 8 = 24
3 × 9 = 27
3 × 10 = 30
```

[[i]]
| Il faut savoir qu'il est courant, dans des petites boucles (quelques lignes), d'utiliser un nom de variable court pour itérer sur nos valeurs.
| Ne soyez donc pas surpris de rencontrer des `i` (indice) ou `n` (_number_) utilisés à cet effet pour itérer sur des nombres, ou des `s` (_string_) pour itérer sur des chaînes de caractères.

Le premier argument donné à `range` est optionnel, et vaut 0 s'il est omis. Ainsi, `range(5)` est équivalent à `range(0, 5)`.

```pycon
>>> for n in range(5):
...     print(n)
... 
0
1
2
3
4
```

Et comme pour le _slicing_, les intervalles possèdent un pas optionnel, qui représente le nombre de valeurs à passer entre chaque élément. Un intervalle de 0 à 10 avec un pas de 2 représentera donc tous les nombres pairs de cet intervalle.

```pycon
>>> for n in range(0, 10, 2):
...     print(n)
... 
0
2
4
6
8
```

#### Construire une liste

À l'aide de `range` et de la méthode `append` des listes, on peut alors facilement construire une liste itérativement, en ajoutant un nouvel élément à chaque tour de boucle.
Par exemple ici une liste de cinq zéros (équivalente à `[0] * 5`).

```pycon
>>> zeros = []
>>> for _ in range(5):
...     zeros.append(0)
... 
>>> zeros
[0, 0, 0, 0, 0]
```

[[i]]
| Pour rappel, `_` est le nom de variable usuel pour une valeur que l'on n'utilise pas.
| On n'a en effet pas besoin ici de savoir quelle est la valeur de l'itération en cours, tout ce qui nous importe est de faire deux itérations.

Ou la liste des carrés des 10 premiers entiers naturels.

```pycon
>>> squares = []
>>> for i in range(10):
...     squares.append(i**2)
... 
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

C'est aussi la solution à notre problème de multiplication des listes multi-dimensionnelles, puisque nous avons maintenant un moyen d'instancier séparément chacune des sous-listes !

```pycon
>>> grid = []
>>> for _ in range(2):
...     grid.append([1, 2, 3])
... 
>>> grid
[[1, 2, 3], [1, 2, 3]]
>>> grid[0].append(4)
>>> grid
[[1, 2, 3, 4], [1, 2, 3]]
```

#### Boucles imbriquées

De la même manière que pour les conditions, les boucles peuvent être imbriquées les unes aux autres.
Ce qui va permettre d'avoir un traitement répétitif dans une autre répétition.

Pour revenir à l'exemple des tables de mutliplication, on peut ainsi représenter toutes les tables de 1 à 3.

```pycon
>>> for a in range(1, 4):
...     for b in range(1, 11):
...         print(a, '×', b, '=', a * b)
...     print'---')
... 
1 × 1 = 1
1 × 2 = 2
1 × 3 = 3
1 × 4 = 4
1 × 5 = 5
1 × 6 = 6
1 × 7 = 7
1 × 8 = 8
1 × 9 = 9
1 × 10 = 10
---
2 × 1 = 2
2 × 2 = 4
2 × 3 = 6
2 × 4 = 8
2 × 5 = 10
2 × 6 = 12
2 × 7 = 14
2 × 8 = 16
2 × 9 = 18
2 × 10 = 20
---
3 × 1 = 3
3 × 2 = 6
3 × 3 = 9
3 × 4 = 12
3 × 5 = 15
3 × 6 = 18
3 × 7 = 21
3 × 8 = 24
3 × 9 = 27
3 × 10 = 30
---
```

On remarque que le second `print` est en dehors de la deuxième boucle, il est ainsi exécuté à chaque itération de la première et permet de marquer une séparation entre chaque table.

Les boucles imbriquées nous permettent aussi de réaliser toutes sortes de combinaisons entre plusieurs ensembles de données.

```pycon
>>> names = ['Jeanne', 'Paul', 'Max']
>>> fruits = ['pommes', 'poires', 'cerises', 'fraises']
>>> 
>>> for name in names:
...     for fruit in fruits:
...         print(name, 'aime les', fruit)
... 
Jeanne aime les pommes
Jeanne aime les poires
Jeanne aime les cerises
Jeanne aime les fraises
Paul aime les pommes
Paul aime les poires
Paul aime les cerises
Paul aime les fraises
Max aime les pommes
Max aime les poires
Max aime les cerises
Max aime les fraises
```

Et bien sûr, on peut ajouter toutes sortes de conditions au sein de nos boucles.

```pycon
>>> for name in names:
...     for fruit in fruits:
...         if name == 'Paul' and (fruit == 'pommes' or fruit == 'cerises'):
...             print(name, "n'aime pas les", fruit)
...         else:
...             print(name, "aime les", fruit)
... 
Jeanne aime les pommes
Jeanne aime les poires
Jeanne aime les cerises
Jeanne aime les fraises
Paul n'aime pas les pommes
Paul aime les poires
Paul n'aime pas les cerises
Paul aime les fraises
Max aime les pommes
Max aime les poires
Max aime les cerises
Max aime les fraises
```
