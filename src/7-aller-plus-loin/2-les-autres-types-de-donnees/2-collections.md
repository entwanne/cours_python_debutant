### Module collections

Python dispose encore de nombreux autres types définis dans différents modules de sa bibliothèque standard.
Par exemple le module `collections` propose plusieurs types pour gérer des collections de données avec diverses spécificités.

#### `Counter`

Dans le chapitre précédent on utilisait des dictionnaires pour compter les occurrences de nombres tirés aléatoirement et vérifier leur distribution.

On les initialisait avec les occurrences de chaque nombre à 0, pour ensuite pouvoir faire des `+= 1` sans se soucier de savoir si la clé existait ou non.

```python
>>> occurrences = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6:0}
```

Il y a en fait beaucoup plus simple et c'est le type `Counter` du module `collections`, spécialement dédié à compter des objets.  
Il se comporte comme un dictionnaire où chaque clé non existante serait considérée comme associée à la valeur 0.

```python
>>> from collections import Counter
>>> occurrences = Counter()
>>> occurrences[4]
0
>>> occurrences
Counter()
```

On peut donc facilement modifier les valeurs sans avoir à se demander si la clé existe déjà.

```python
>>> occurrences[3] += 1
>>> occurrences[5] += 2
>>> occurrences
Counter({5: 2, 3: 1})
```

Quand une valeur est redéfinie, elle est donc présente « pour de vrai » dans le dictionnaire, même si elle nulle.

```python
>>> occurrences[4] = 0
>>> occurrences
Counter({5: 2, 3: 1, 4: 0})
```

Un objet `Counter` peut être initialisé comme un dictionnaire : à partir d'un dictionnaire existant ou à l'aide d'arguments nommés.

```python
>>> Counter({'foo': 3, 'bar': 5})
Counter({'bar': 5, 'foo': 3})
>>> Counter(foo=3, bar=5)
Counter({'bar': 5, 'foo': 3})
```

Mais il peut aussi être instancié avec un itérable quelconque, auquel cas il s'initialisera en comptant les différentes valeurs de cet itérable.

```python
>>> Counter([1, 2, 3, 4, 3, 1, 3])
Counter({3: 3, 1: 2, 2: 1, 4: 1})
>>> Counter('tortue')
Counter({'t': 2, 'o': 1, 'r': 1, 'u': 1, 'e': 1})
```

Très pratique donc pour compter directement ce qui nous intéresse.

En plus des opérations communes aux dictionnaires, on trouve aussi des opérations arithmétiques.  
Il est ainsi possible d'additionner deux compteurs, ce qui renvoie un nouveau compteur contenant les sommes des valeurs.

```python
>>> Counter(a=5, b=1) + Counter(a=3, c=2)
Counter({'a': 8, 'c': 2, 'b': 1})
```

À l'inverse, la soustraction entre compteurs renvoie les différences.
Les valeurs négatives sont ensuite retirées du résultat.

```python
>>> Counter(a=5, b=1) - Counter(a=3, c=2)
Counter({'a': 2, 'b': 1})
```

Il est possible de calculer l'union et l'intersection entre deux objets `Counter`, l'union étant composée des maximums de chaque valeur et l'intersection des minimums.

```python
>>> Counter(a=5, b=1) | Counter(a=3, c=2)
Counter({'a': 5, 'c': 2, 'b': 1})
>>> Counter(a=5, b=1) & Counter(a=3, c=2)
Counter({'a': 3})
```

Enfin, les compteurs ajoutent quelques méthodes par rapport aux dictionnaires.  
`most_common` par exemple permet d'avoir la liste ordonnée des valeurs les plus communes, associées à leur nombre d'occurrences.
La méthode prend un paramètre `n` pour spécifier le nombre de valeurs que l'on veut obtenir (par défaut toutes les valeurs seront présentes).

```python
>>> count = Counter('abcdabcaba')
>>> count.most_common()
[('a', 4), ('b', 3), ('c', 2), ('d', 1)]
>>> count.most_common(2)
[('a', 4), ('b', 3)]
```

La méthode `elements` permet d'itérer sur les valeurs comme si elles étaient représentées plusieurs fois selon leur nombre d'occurrences.

```python
>>> for item in count.elements():
...     print(item)
... 
a
a
a
a
b
b
b
c
c
d
```

`update` est une méthode déjà présente sur les dictionnaires, qui a pour effet d'affecter de nouvelles valeurs aux clés existantes.
Sur les compteurs, la méthode se chargera de faire la somme des valeurs.  
Elle peut prendre n'importe quel itérable en argument, qu'elle considérera comme un compteur.

```python
>>> count.update('bcde')
>>> count
Counter({'a': 4, 'b': 4, 'c': 3, 'd': 2, 'e': 1})
```

Il est aussi possible de faire la même chose en soustrayant les compteurs avec la méthode `substract`.

```python
>>> count.subtract('abcd')
>>> count
Counter({'a': 3, 'b': 3, 'c': 2, 'd': 1, 'e': 1})
```

#### `defaultdict`

* Dictionnaires avec valeur par défaut (`setdefault` partout)
* `defaultdict(list)`, `d[key].append(...)`

On a vu il y a quelques chapitres que les dictionnaires possédaient une méthode `setdefault`.
Cette méthode permettait d'assurer qu'une valeur soit toujours présente pour une clé.

Cela simplifie des problèmes où l'on veut associer des listes de valeurs à des clés, comme un annuaire où chaque personne pourrait avoir plusieurs numéros.

```python
>>> phonebook = {}
>>> phonebook.setdefault('Bob', []).append('0663621029')
>>> phonebook.setdefault('Bob', []).append('0714381809')
>>> phonebook.setdefault('Alice', []).append('0633432380')
>>> phonebook
{'Bob': ['0663621029', '0714381809'], 'Alice': ['0633432380']}
```

Mais les `defaultdict` permettent cela encore plus facilement : les valeurs manquantes seront automatiquement instanciées, sans besoin d'appel explicite à `setdefault`.
Pour cela, un `defaultdict` s'instancie avec une fonction (ou un type) qui sera appelée à chaque clé manquante pour obtenir la valeur.

Ainsi, l'exemple précédent pourrait se réécrire comme suit.

```python
>>> from collections import defaultdict
>>> phonebook = defaultdict(list)
>>> phonebook['Bob'].append('0663621029')
>>> phonebook['Bob'].append('0714381809')
>>> phonebook['Alice'].append('0633432380')
>>> phonebook
defaultdict(<class 'list'>, {'Bob': ['0663621029', '0714381809'], 'Alice': ['0633432380']})
```

Chaque fois qu'une clé n'existe pas dans le dictionnaire, `defaultdict` fait appel à `list` qui renvoie une nouvelle liste vide.

Il suffit d'ailleurs d'essayer d'accéder à la valeur associée à une telle clé pour provoquer sa création.

```python
>>> phonebook['Alex']
[]
>>> phonebook
defaultdict(<class 'list'>, {'Bob': ['0663621029', '0714381809'], 'Alice': ['0633432380'], 'Alex': []})
```

Et bien sûr, toute fonction pourrait être utilisée comme argument à `defaultdict`.

```python
>>> def get_default():
...     return 'default'
... 
>>> titles = defaultdict(get_default)
>>> titles['Alice'] = 'foo'
>>> titles['Alice']
'foo'
>>> titles['Bob']
'default'
```

#### `OrderedDict`

* Antérieur à Python 3.6
* Mais toujours utile : égalité entre dictionnaires ordonnés

#### `ChainMap`

* Chaînage de dictionnaires sans copie
* Représentation d'espaces de noms
* Ajouter/retirer des maillons

#### `deque`

* Liste chaînée
* Données non contigues en mémoire contrairement aux tableaux (listes)
* Accès lent aux éléments situés en milieu de liste, mais ajout d'éléments en tête/queue très rapide (pas besoin de réallouer un tableau)

#### `namedtuple`

* Un tuple représente un ensemble cohérent de données
* Donner un nom aux éléments d'un tuple

```python
>>> point = (3, 5)
>>> point[0]
3
>>> x, y = point
>>> y
5
```

```python
>>> from collections import namedtuple
>>> Point = namedtuple('Point', ('x', 'y'))
>>> point = Point(3, 5)
>>> point
Point(x=3, y=5)
>>> point.x
3
>>> point[0]
3
>>> x, y = point
>>> y
5
```
