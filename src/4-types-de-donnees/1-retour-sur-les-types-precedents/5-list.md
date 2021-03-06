### Listes

Les listes représentent des tableaux de valeurs de tous types.
Contrairement aux types précédents, les listes sont des objets modifiables (leur valeur peut varier avec le temps).

#### Conversions

Une chaîne de caractères étant un tableau, elle peut être convertie en liste de caractères en faisant appel à `list`.

```python
>>> list('hello')
['h', 'e', 'l', 'l', 'o']
```

Cela peut justement permettre de récupérer l'équivalent modifiable d'une chaîne de caractère.

#### Opérations

On retrouve pour les listes les opérations d'indexation (`[]`), de concaténation (`+`, `*`) et d'appartenance (`in`).

L'indexation permet cependant de modifier une liste en assignant une valeur à une position et d'en supprimer avec `del`.

```python
>>> values = [3, 4, 5]
>>> values[0]
3
>>> values[1:]
[4, 5]
>>> values[-1] = 6
>>> del values[0]
>>> values
[4, 6]
>>> [1, 2] + values
[1, 2, 4, 6]
>>> values * 2
[4, 6, 4, 6]
>>> 4 in [1, 2, 3]
False
>>> 4 in [1, 2, 4]
True
```

Contraîrement aux chaînes de caractères, l'opérateur `in` n'ira pas chercher de sous-liste dans une liste.

```python
>>> [1, 2] in [1, 2, 3]
False
>>> [1, 2] in [[1, 2], [3, 4]]
True
```

Au niveau de la multiplication d'une liste par un nombre, il faut bien faire attention aux cas de références multiples.
Quand on multiplie ainsi une liste, on ne copie pas les éléments qu'elle contient mais on ne fait que les dupliquer. On a donc plusieurs fois un même objet dans la liste.

Ce n'est pas gênant pour des valeurs non modifiables (nombres, chaînes), mais si une liste contient d'autres listes ça peut vite devenir problématique.

```python
>>> table = [[0, 0, 0]] * 2
>>> table
[[0, 0, 0], [0, 0, 0]]
>>> table[0][1] = 5
>>> table
[[0, 5, 0], [0, 5, 0]]
```

Les opérateurs d'ordre (`<`, `>`) sont aussi utilisables entre deux listes, leur résultat dépend de la comparaison entre les éléments des listes.

C'est-à-dire qu'on commence par comparer les premièrs éléments des deux listes, puis les deuxièmes et ainsi de suite jusqu'à ce qu'une des listes soit épuisée.

La comparaison s'arrête dès que deux éléments sont différents, où l'on sait alors lequel est supérieur à l'autre.
Ou alors si une seule des listes est épuisée, elle est considérée comme inférieure.

```python
>>> [1, 2, 3] < [1, 2, 4]
True
>>> [1, 2, 3] < [1, 2, 2]
False
>>> [1, 2, 3, 9] < [1, 2, 4]
True
>>> [1, 2, 3] < [2]
True
>>> [1, 2, 3] < [1]
False
```

Si ces éléments sont de types non compatibles, alors l'opération produira une erreur.

```python
>>> [1, 2] < [1, 'a']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'int' and 'str'
```

D'autres opérateurs prennent la forme de fonctions.
C'est le cas de `len` pour récupérer la taille d'une liste.

```python
>>> len(['a', 'b', 'c'])
3
```

On a aussi les fonctions `min` et `max` pour récupérer le plus petit ou le plus grand élément d'une liste.

```python
>>> min([3, 1, 2])
1
>>> max(['z', 'c', 'a', 'y'])
'z'
```

`sum` est une fonction qui opère sur une liste de nombres et en calcule la somme.

```python
>>> sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
55
```

Enfin je voulais aussi présenter les fonctions `all` et `any`, qui agissent comme des `and`/`or` sur l'ensemble des éléments d'une liste, mais renvoyant un booléen dans tous les cas.
`all` vérifie que tous les éléments sont vrais, et `æny` qu'au moins un élément est vrai.

Ainsi, `all([a, b, c, d])` est équivalent à `a and b and c and d` et `any([a, b, c, d])` à `a or b or c or d`.

```python
>>> all([1, 2, 3, 4])
True
>>> all([1, 2, 3, 4])
True
>>> all([0, 1, 2, 3, 4])
False
>>> any([0, 1, 2, 3, 4])
True
>>> any([0])
False
```

Attention cependant au comportement sur les listes vides : `all` s'attend à ce que tous les éléments sont vrais ; mais si la liste ne contient aucun élément, alors techniquement ils sont bien tous vrais.
De même pour `any` qui veut au moins un élément vrai, ce qui ne peut pas être le cas s'il n'y a aucun élément.

```python
>>> all([])
True
>>> any([])
False
```

#### Principales méthodes

Venons-en maintenant à quelques méthodes sur les listes.

Comme sur les chaînes, on a une méthode `index` pour rechercher le premier index d'un élément.

```python
>>> values = ['a', 'b', 'c', 'd']
>>> values.index('c')
2
```

Les méthodes `append`, `insert`, `pop` et `clear` permettent de modifier la liste en ajoutant / insérant / supprimant un élément, ou en la vidant.

```python
>>> values.append('e') 
>>> values.insert(3, 'ç')
>>> values.pop(1)
'b'
>>> values
['a', 'c', 'ç', 'd', 'e']
>>> values.clear()
>>> values
[]
```

Les listes ont aussi une méthode `remove` pour supprimer un élément en fonction de sa valeur plutôt que son index.

```python
>>> values = ['a', 'b', 'c', 'd']
>>> values.remove('c')
>>> values
['a', 'b', 'd']
```

La méthode `extend` permet d'ajouter une liste d'éléments à la fin, ce qui revient à concaténer la liste donnée en argument dans la liste actuelle.

```python
>>> values.extend(['c', 'e', 'f'])
>>> values
['a', 'b', 'd', 'c', 'e', 'f']
```

Quelques méthodes permettent de faire varier l'ordre des éléments dans la liste.
C'est le cas de `reverse` qui inverse l'ordre des éléments.

```python
>>> values.reverse()
>>> values
['f', 'e', 'c', 'd', 'b', 'a']
```

`sort` permet quant à elle de trier les éléments du plus petit au plus grand.

```python
>>> values.sort()
>>> values
['a', 'b', 'c', 'd', 'e', 'f']
```

Il est possible de passer un booléen comme argument nommé `reverse` pour trier dans l'autre sens.

```python
>>> values.sort(reverse=True)
>>> values
['f', 'e', 'd', 'c', 'b', 'a']
```

Enfin, on a vu plus haut les problèmes que pouvaient causer les multiples références sur une même liste.
Parfois, on veut simplement deux listes contenant les mêmes valeurs mais indépendantes l'une de l'autre, et l'on doit pour cela en réaliser une copie.
Les listes possèdent pour cela une méthode `copy`.

```python
>>> other_values = values.copy()
>>> values.append('g')
>>> values
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> other_values
['a', 'b', 'c', 'd', 'e', 'f']
```

Ce même comportement est aussi possible en appelant `list` sur une liste existante, ou en utilisant un _slicing_ vide.

```python
>>> list(values)
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> values[:]
['a', 'b', 'c', 'd', 'e', 'f', 'g']
```

Pour savoir si deux valeurs sont la même liste, on peut utiliser l'opérateur d'identité `is`.
Cette opérateur vérifie que deux valeurs sont un seul et même objet.

```python
>>> values = [1, 2, 3]
>>> other_values = values
>>> other_values is values
True
>>> other_values = values.copy()
>>> other_values is values
False
>>> other_values == values
True
```

À l'inverse, on trouve l'opérateur `is not` pour tester la non-identité.

```python
>>> other_values is not values
True
```

[[a]]
| Attention cependant avec les listes multi-dimensionnelles : `copy` ne réalise une copie que du premier niveau de la liste.

Ainsi, avec le code qui suit, nous aurons encore des références communes entre les deux listes.

```python
>>> values = [['a', 'b', 'c'], ['d', 'e', 'f']]
>>> other_values = values.copy()
>>> values[1].append('g')
>>> other_values
[['a', 'b', 'c'], ['d', 'e', 'f', 'g']]
```

Nous verrons par la suite comment réaliser une copie en profondeur et éviter ce problème.

Mais cela ne concerne bien sûr que les dimensions imbriquées : `values` et `other_values` restent deux listes distinctes.

```python
>>> values.append(['h', 'i', 'j'])
>>> values
[['a', 'b', 'c'], ['d', 'e', 'f', 'g'], ['h', 'i', 'j']]
>>> other_values
[['a', 'b', 'c'], ['d', 'e', 'f', 'g']]
```
