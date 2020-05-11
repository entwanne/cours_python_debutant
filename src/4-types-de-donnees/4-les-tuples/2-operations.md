### Opérations sur les tuples

Les opérations sont semblables à celles des listes.

Il est possible de convertir un itérable en tuple en appelant le type `tuple` comme une fonction.

```python
>>> tuple([1, 2, 3])
(1, 2, 3)
>>> tuple('abcd')
('a', 'b', 'c', 'd')
```

On peut accéder aux éléments d'un tuple (en lecture uniquement) avec l'opérateur d'indexation `[]`, qui gère les index négatifs et les slices.

```python
>>> values = (4, 5, 6)
>>> values[1]
5
>>> values[-1]
6
>>> values[::2]
(4, 6)
```

`in` permet de vérifier si une valeur est présente dans le tuple.

```python
>>> 3 in values
False
>>> 4 in values
True
```

On peut concaténer deux tuples avec `+`, et multiplier un tuple par un nombre avec `*`.

```python
>>> (4, 5, 6) + (7, 8, 9)
(4, 5, 6, 7, 8, 9)
>>> (4, 5, 6) * 2
(4, 5, 6, 4, 5, 6)
```

Les tuples sont ordonnables les uns par rapport aux autres, de la même manière que les listes.

```python
>>> (1, 2, 3) < (1, 2, 4)
True
>>> (1, 2, 3) <= (1, 2, 2)
False
```

Les fonctions `len`, `min`, `max`, `all`, `any` etc. sont aussi applicables aux tuples.

```python
>>> len(values)
3
>>> min(values)
4
>>> max(values)
6
>>> all((True, True, False))
False
>>> any((True, True, False))
True
```

Enfin, les tuples sont pourvus de deux méthodes, `index` et `count`, pour respectivement trouver la position d'un élément et compter les occurrences d'un élément.

```python
>>> values.index(6)
2
>>> values.count(6)
1
```
