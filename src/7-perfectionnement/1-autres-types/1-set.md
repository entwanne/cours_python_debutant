### Les ensembles

Les ensembles sont des collections de données pour représenter des valeurs uniques.
Dans un ensemble, il ne peut pas y avoir de doublons, un peu comme pour les clés de dictionnaires.

D'ailleurs, la syntaxe pour définir un ensemble ressemble à celle des dictionnaires : un ensemble se définit à l'aide d'accolades à l'intérieur desquelles on sépare les valeurs par des virgules.

```pycon
>>> {0, 1, 2, 3, 4, 5}
{0, 1, 2, 3, 4, 5}
```

Si l'on essaie d'insérer des doublons, on voit que ceux-ci ne sont pas pris en compte.

```pycon
>>> {0, 1, 2, 3, 4, 5, 2, 3}
{0, 1, 2, 3, 4, 5}
```

Une autre particularité commune aux ensembles et aux dictionnaires est que les valeurs d'un ensemble doivent être *hashables*, impossible donc d'y stocker des listes.

```pycon
>>> {[]}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

Il est aussi possible de convertir en ensemble un autre objet en appelant explicitement `set` (le type des ensembles).

```pycon
>>> set([0, 1, 2, 3, 4, 5, 2, 3])
{0, 1, 2, 3, 4, 5}
```

Par ailleurs, `{}` étant la syntaxe pour définir un dictionnaire vide, un ensemble vide se définit avec `set()`.

```pycon
>>> set()
set()
```

#### Opérations

Les ensembles peuvent être considérés au sens mathématique du terme, une collection contenant juste des valeurs.
Et il est ainsi possible d'appliquer des opérations ensemblistes à ces collections.

Ainsi, on peut calculer l'union entre deux ensembles à l'aide de l'opérateur `|`.
L'union de deux ensembles consiste en l'ensemble des valeurs contenues dans l'un ou dans l'autre (ou les deux).

```pycon
>>> {0, 1, 3, 4} | {2, 3, 4, 5}
{0, 1, 2, 3, 4, 5}
```

À l'inverse, l'intersection est obtenue avec l'opérateur `&`.
L'intersection ne contient que les valeurs présentes dans les deux ensembles.

```pycon
>>> {0, 1, 3, 4} & {2, 3, 4, 5}
{3, 4}
```

La différence est l'opération qui consiste à soustraire au premier ensemble les éléments du second.
Elle se calcule avec l'opérateur `-`.

```pycon
>>> {0, 1, 3, 4} - {2, 3, 4, 5}
{0, 1}
```

Enfin, `^` est l'opérateur de différence symétrique.
La différence symétrique calcule l'ensemble des valeurs qui ne sont pas communes aux deux ensembles, c'est l'inverse de l'intersection.
Ou autrement dit la différence entre l'union et l'intersection.

```pycon
>>> {0, 1, 3, 4} ^ {2, 3, 4, 5}
{0, 1, 2, 5}
>>> ({0, 1, 3, 4} | {2, 3, 4, 5}) - ({0, 1, 3, 4} & {2, 3, 4, 5})
{0, 1, 2, 5}
```

J'ai représenté ici les ensembles comme des collections d'éléments ordonnés, mais il n'en est rien, aucune relation d'ordre n'existe dans un ensemble.

Ainsi, deux ensembles sont égaux s'ils contiennent exactement les mêmes valeurs, et différents dans le cas contraire.

```pycon
>>> {1, 2, 3} == {3, 2, 1}
True
>>> {1, 2, 3} != {2, 3, 4}
True
```

Il n'y a d'ailleurs pas d'accès direct aux éléments comme il peut y avoir sur une liste, car les éléments ne sont associés à aucun index.  
Pour autant, il reste possible de parcourir un ensemble avec une boucle `for` pour itérer sur ses valeurs.

```pycon
>>> for i in {1, 2, 3}:
...     print(i)
... 
1
2
3
```

On peut tester si une valeur est présente dans un ensemble à l'aide de l'opérateur `in`.
Et c'est là tout l'intérêt des ensembles : cette opération est optimisée pour s'exécuter en temps constant (là où il peut être nécessaire de parcourir tous les éléments sur une liste).

```pycon
>>> 3 in {1, 2, 3}
True
>>> 4 in {1, 2, 3}
False
```

L'opérateur `not in` est l'inverse de `in`, il permet de tester l'absence de valeur.

```pycon
>>> 3 not in {1, 2, 3}
False
>>> 4 not in {1, 2, 3}
True
```

Enfin, on trouve d'autres opérations ensemblistes liées aux opérateurs d'égalité.

`<`, `<=`, `>` et `>=` permettent de tester les sur-ensembles et sous-ensembles.  
Avec `a` et `b` deux ensembles, `a <= b` est vraie si tous les éléments de `a` sont présents dans `b` (`a` est un sous-ensemble de `b`).

```pycon
>>> {2, 3} <= {1, 2, 3, 4}
True
>>> {2, 3, 5} <= {1, 2, 3, 4}
False
```

Et l'opération est équivalente à `b >= a`, vue dans l'autre sens (`b` est un sur-ensemble de `a`).

```pycon
>>> {1, 2, 3, 4} >= {2, 3}
True
>>> {1, 2, 3, 4} >= {2, 3, 5}
False
```

`<` et `>` sont les pendants stricts de ces opérateurs : `a < b` ne sera pas vraie si `a` et `b` contiennent exactement les mêmes valeurs.

```pycon
>>> {1, 2, 3} < {1, 2, 3, 4}
True
>>> {1, 2, 3} < {1, 2, 3}
False
>>> {1, 2, 3} <= {1, 2, 3}
True
```

#### Méthodes

Les ensembles étant des collections, il est naturellement possible d'utiliser la fonction `len` pour calculer leur taille.

```pycon
>>> len({1, 2, 3})
3
>>> len({1, 2, 3, 5})
4
```

Étant modifiables, il est possible d'ajouter et de retirer des éléments dans des ensembles.
Cela se fait avec les fonctions `add` et `remove`.

```pycon
>>> values = set()
>>> values.add(2)
>>> values.add(4)
>>> values.add(6)
>>> values
{2, 4, 6}
>>> values.remove(4)
>>> values
{2, 6}
```

La méthode `discard` est semblable à `remove` mais ne lève pas d'erreur si l'élément à supprimer est absent.

```pycon
>>> values.remove(8)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 8
>>> values.discard(8)
>>> values.discard(2)
>>> values
{6}
```

Et la méthode `pop` permet aussi de retirer (et renvoyer) un élément de l'ensemble, sans sélectionner lequel.
Elle lève une exception si l'ensemble est vide.

```pycon
>>> values.pop()
6
>>> values.pop()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'pop from an empty set'
```

On retrouve sinon différentes méthodes sur les ensembles équivalentes aux opérateurs décrits au-dessus : `union`, `intersection`, `difference` et `symmetric_difference`.
L'avantage par rapport aux opérateurs est que ces méthodes peuvent prendre plusieurs ensembles en paramètres, ou même des objets de tous types (itérables) et opérer dessus.

```pycon
>>> {1, 2}.union({2, 3}, [4], (5, 6))
{1, 2, 3, 4, 5, 6}
```

Chacune de ces méthodes est doublée d'une version qui modifie en place l'ensemble courant, respectivement `update`, `intersection_update`, `difference_update` et `symmetric_difference_update`.
Ces méthodes ne renvoient rien.

```pycon
>>> values = {1, 2, 3}
>>> values.intersection_update([3, 4, 5])
>>> values
{3}
```

Les ensembles disposent aussi de méthodes booléennes, notamment `issubset` et `issuperset` équivalentes aux opérateurs `<=` et `>=`, ainsi que `isdisjoint` pour tester si deux ensembles sont disjoints (dont l'intersection est vide).

```pycon
>>> {1, 2, 3}.isdisjoint({4, 5, 6})
True
>>> {1, 2, 3}.isdisjoint({3, 4, 5})
False
```

Enfin, on retrouve les méthodes `clear` et `copy`, comme sur les listes et les dictionnaires, respectivement pour vider l'ensensemble et pour en faire une copie.

#### `frozenset`

Un ensemble étant une collection de données mutable, il n'est pas *hashable* et ne peut donc pas être utilisé comme clé de dictionnaire.
Ainsi, un autre type existe pour représenter un ensemble immutable de données : le `frozenset`.

Un `frozenset` se définit en appelant explicitement le type avec n'importe quel itérable en argument.

```pycon
>>> frozenset({1, 2, 3})
frozenset({1, 2, 3})
```

Il peut aussi s'appeler seul pour définir un ensemble vide.

```pycon
>>> frozenset()
frozenset()
```

Le `frozenset` dispose des mêmes méthodes et opérateurs que les ensembles classiques, à l'exception de celles qui modifient l'objet.

```pycon
>>> frozenset({1, 2, 3}) | frozenset({3, 4, 5})
frozenset({1, 2, 3, 4, 5})
>>> frozenset({1, 2, 3}).isdisjoint(frozenset({3, 4, 5}))
False
```

Les ensembles et les `frozenset` sont compatibles entre eux, mais attention au type de retour qui dépendra de l'objet sur lequel la méthode ou l'opérateur est appliqué.

```pycon
>>> frozenset({1, 2, 3}) & {3, 4, 5}
frozenset({3})
>>> {3, 4, 5} & frozenset({1, 2, 3})
{3}
```
