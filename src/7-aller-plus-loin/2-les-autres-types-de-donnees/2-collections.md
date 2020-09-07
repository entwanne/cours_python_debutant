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

Quand une valeur est redéfinie, elle est donc présente « pour de vrai » dans le dictionnaire.

* opérateurs (+, -, &, |), méthodes (elements, most_common, update/substract)

* utiliser Counter pour compter des données existantes (lettres d'une chaîne)

#### `defaultdict`

* Dictionnaires avec valeur par défaut (`setdefault` partout)
* `defaultdict(list)`, `d[key].append(...)`

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
