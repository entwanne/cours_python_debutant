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

* Multiples `for` dans une intension

* Intensions imbriquées

#### Autres constructions en intension

* Dictionnaires et ensembles en intension
