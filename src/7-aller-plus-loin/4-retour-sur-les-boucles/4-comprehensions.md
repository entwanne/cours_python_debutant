### Listes en intension

On a vu qu'il était possible d'écrire des conditions sous forme d'expressions, qu'en est-il des boucles ?

Une expression est une instruction qui possède une valeur.
Pour une condition c'est facile : on a une valeur si la condition est vraie et une autre valeur sinon.
Mais quelle pourrait être la valeur d'une boucle ?

Il n'y a pas de réponse évident à cette question, et c'est pourquoi il n'y a pas d'expression générale pour exécuter une boucle.
Il existe en revanche les listes en intension, qui permettent de construire une liste à partir d'une boucle `for`.

L'intension est un concept mathématique qui s'oppose à l'extension pour définir un ensemble[^intension_extension].
La définition par extension, c'est celle que nous avons utilisée jusqu'ici, qui consiste à définir l'ensemble par les éléments qu'il possède.

```python
powers = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
```

La définition par intension consiste à décrire l'ensemble selon une règle, par exemple « les dix premières puissances de 2 ».
On la traduirait en Python par le code suivant :

```python
>>> powers = [2**i for i in range(10)]
>>> powers
[1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
```

[^intension_extension]: <https://fr.wikipedia.org/wiki/Intension_et_extension>

On voit alors que l'on utilise le `for` dans une expression pour construire une liste.
Le code précédent est équivalent à la boucle suivante.

```python
powers = []
for i in range(10):
    powers.append(2**i)
```

On peut ainsi transposer vers une liste en intension toute boucle `for` ne consistant qu'à évaluer une expression à chaque itération.

```python
>>> [letter + '!' for letter in 'ABCD']
['A!', 'B!', 'C!', 'D!']
>>> [len(word) for word in ['zeste', 'de', 'savoir']]
[5, 2, 6]
>>> [letter * i for letter, i in zip('ABCD', range(1, 5))]
['A', 'BB', 'CCC', 'DDDD']
```

[[i]]
| Le terme anglais pour les listes en intension est _list comprehensions_, aussi il est courant de rencontrer en français les expressions « liste en compréhension » ou « compréhension de liste », il s'agit évidemment de la même chose.

#### Conditions de filtrage

Mais les listes en intension ne s'arrêtent pas là et permettent des constructions plus complexes : il est possible de filtrer les éléments à intégrer ou non à la liste.
Pour cela on utilise une expression de la forme suivante.

```python
[expression for item in iterable if condition]
```

La condition interviendra à chaque itération et déterminera s'il faut ajouter `expression` aux éléments de la liste en construction ou non.
Voici par exemple la liste des entiers naturels pairs strictement inférieurs à 10.

```python
>>> [i for i in range(10) if i % 2 == 0]
[0, 2, 4, 6, 8]
```

Ce code est équivalent à la boucle suivante :

```python
values = []
for i in range(10):
    if i % 2 == 0:
        values.append(i)
```

[[a]]
| Attention à ne pas confondre le `if` utilisé ici avec le `if` de l'expression conditionnelle.
| Ce premier n'autorise pas le `else` puisque cela n'aurait pas de sens sur une condition de filtrage.

Par ailleurs, les expressions conditionnelles étant des expressions à part entière, il est parfaitement possible de les utiliser dans des listes en intension.

```python
>>> [i // 2 if i % 2 == 0 else i * 3 + 1 for i in range(10)]
[0, 4, 1, 10, 2, 16, 3, 22, 4, 28]
```

On peut même les combiner aux conditions de filtrage sans que cela ne pose problème, veillez tout de même à ce que le code reste toujours lisible.

```python
>>> [i // 2 if i % 2 == 0 else i * 3 + 1 for i in range(10) if i % 3 == 0]
[0, 10, 3, 28]
```

Pour plus de clarté, il est ainsi parfois conseillé de placer des parenthèses autour de l'expression conditionnelle.
Mais de manière générale, une liste en intension trop longue peut signifier que ce n'est pas la meilleure solution au problème et qu'une boucle « standard » irait tout aussi bien.

```python
>>> [(i // 2 if i % 2 == 0 else i * 3 + 1) for i in range(10) if i % 3 == 0]
[0, 10, 3, 28]
```

Il est aussi possible d'utiliser plusieurs `if` dans l'intension pour définir plusieurs conditions sur lesquelles filtrer, celles-ci s'additionnant les unes aux autres.

```python
>>> [i for i in range(10) if i % 2 == 0 if i % 3 == 0] # Multiples de 2 et 3
[0, 6]
```

#### Boucles imbriquées

D'ailleurs, les `for` aussi peuvent être chaînés au sein d'une même intension.
Cela permet alors de faire la même chose qu'avec des boucles imbriquées pour remplir notre liste.

```python
>>> [(i, c) for i in range(3) for c in 'AB']
[(0, 'A'), (0, 'B'), (1, 'A'), (1, 'B'), (2, 'A'), (2, 'B')]
```

Les boucles sont à lire de gauche à droite comme si elles étaient écrites de haut en bas, le code précédent est équivalent à :

```python
values = []
for i in range(3):
    for c in 'AB':
        values.append((i, c))
```

Et il est possible d'enchaîner autant de `for` que l'on veut dans l'intension, comme l'on pourrait en imbriquer autant qu'on veut.
Mais attention, nous obtenons bien une seule liste en sortie, comportant toutes les combinaisons parcourues lors de l'itération.

Les listes en intension étant des expressions comme les autres, il est aussi possible d'imbriquer les intensions.
C'est ainsi que l'on peut construire des listes à plusieurs dimensions.

```python
>>> table = [[0 for x in range(3)] for y in range(2)]
>>> table
[[0, 0, 0], [0, 0, 0]]
```

C'est un modèle de construction assez courant en Python puisqu'il ne souffre pas du problème de références multiples dont je parlais lors de la présentation des listes.
Ici, chaque sous-liste est une instance différente et peut donc être modifiée indépendamment des autres.

```python
>>> table[0][1] = 5
>>> table
[[0, 5, 0], [0, 0, 0]]
```

Souvenez-vous, ce n'est pas le résultat qu'on obtenait avec `[[0] * 3] * 2` où chaque ligne était une référence vers la même liste.

```python
>>> table = [[0] * 3] * 2
>>> table
[[0, 0, 0], [0, 0, 0]]
>>> table[0][1] = 5
>>> table
[[0, 5, 0], [0, 5, 0]]
```

#### Autres constructions en intension

On parle souvent de listes en intension mais ce n'est pas le seul type qui peut être construit ainsi.
Au programme, on trouve aussi les ensembles et les dictionnaires.

Pour les ensembles, la syntaxe est identique aux listes à l'exception qu'on utilise des accolades plutôt que des crochets.

```python
>>> {i**2 for i in range(10)}
{0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
```

Et on retrouve les mêmes fonctionnalités sur les intensions : il est possible d'avoir plusieurs boucles et d'utiliser des conditions de filtrage.

```python
>>> {i+j for i in range(10) for j in range(10) if (i+j) % 2 == 0}
{0, 2, 4, 6, 8, 10, 12, 14, 16, 18}
```

Vous constaterez pour ce dernier exemple que le résultat ne serait pas du tout le même avec une liste, l'ensemble ne permettant pas les duplications.

Pour les dictionnaires on retrouve quelque chose de similaire mais utilisant la syntaxe `cle: valeur` plutôt qu'une simple expression (où `cle` et `valeur` sont aussi des expressions).

```python
>>> {i: i**2 for i in range(10)}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
```
