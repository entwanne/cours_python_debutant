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
>>> def get_default_color():
...     return 'noir'
... 
>>> colors = defaultdict(get_default_color)
>>> colors['mur'] = 'bleu'
>>> colors['mur']
'bleu'
>>> colors['sol']
'noir'
```

#### `OrderedDict`

Avant Python 3.6 les dictionnaires ne conservaient pas l'ordre d'insertion des clés.
La seule manière d'avoir un dictionnaire ordonné était d'utiliser le type `OrderedDict` du module `collections`.
Les choses ont évolué depuis et le type a un peu perdu de son intérêt.

Comme les dictionnaires, un `OrderedDict` se construit à partir d'un dictionnaire existant et/ou d'arguments nommés.
Sans argument, on construit simplement un dictionnaire vide.

```python
>>> from collections import OrderedDict
>>> OrderedDict()
OrderedDict()
>>> OrderedDict({'foo': 0, 'bar': 1})
OrderedDict([('foo', 0), ('bar', 1)])
>>> OrderedDict(foo=0, bar=1)
OrderedDict([('foo', 0), ('bar', 1)])
```

On le voit par sa représentation, le dictionnaire ordonné est en fait vu comme une liste de couples clé/valeur.

Il reste néanmoins une différence importante entre les dictionnaires ordonnés et les dictionnaires standards : l'ordre des éléments fait partie de la sémantique du premier.

Là où deux dictionnaires seront considérés comme égaux s'ils ont les mêmes couples clé/valeur, quel que soit leur ordre, ça ne sera pas le cas pour les `OrderedDict` qui ne seront égaux que si leurs clés sont dans le même ordre.

```python
>>> {'foo': 0, 'bar': 1} == {'bar': 1, 'foo': 0}
True
>>> OrderedDict(foo=0, bar=1) == OrderedDict(bar=1, foo=0)
False
>>> OrderedDict(foo=0, bar=1) == OrderedDict(foo=0, bar=1)
True
```

Ce n'est bien sûr valable que pour l'égalité entre deux dictionnaires ordonnés. L'égalité entre un dictionnaire ordonné et un standard ne tiendra pas compte de l'ordre.

```python
>>> OrderedDict(foo=0, bar=1) == {'bar': 1, 'foo': 0}
True
```

Faites donc appel à `OrderedDict` si vous avez besoin d'un tel comportement, sinon vous pouvez vous contenter d'un dictionnaire standard.

#### `ChainMap`

Parfois on a plusieurs dictionnaires que l'on aimerait pouvoir considérer comme un seul, sans pour autant nécessiter de copie vers un nouveau dictionnaire qui les intégrerait tous.
En effet, la copie peut être coûteuse et elle n'a surtout lieu qu'une fois, le dictionnaire copié ne sera pas affecté si les dictionnaires initiaux sont modifiés.

```python
>>> phonebook_sim = {'Alice': '0633432380', 'Bob': '0663621029'}
>>> phonebook_tel = {'Alex': '0714381809'}
>>> phonebook = dict(phonebook_sim) # Copie pour fusionner les deux dictionnaires
>>> phonebook.update(phonebook_tel)
>>> phonebook
{'Alice': '0633432380', 'Bob': '0663621029', 'Alex': '0714381809'}
>>> phonebook_tel['Mehdi'] = '0762253973'
>>> phonebook # phonebook n'a pas changé
{'Alice': '0633432380', 'Bob': '0663621029', 'Alex': '0714381809'}
```

Le type `ChainMap` répond à ce problème puisqu'il permet de chaîner des dictionnaires dans un seul tout.

```python
>>> from collections import ChainMap
>>> phonebook_sim = {'Alice': '0633432380', 'Bob': '0663621029'}
>>> phonebook_tel = {'Alex': '0714381809'}
>>> phonebook = ChainMap(phonebook_sim, phonebook_tel)
>>> phonebook
ChainMap({'Alice': '0633432380', 'Bob': '0663621029'}, {'Alex': '0714381809'})
```

Lors de la recherche d'une clé, les dictionnaires seront parcourus successivement pour trouver la valeur.

```python
>>> phonebook['Bob']
'0663621029'
>>> phonebook['Alex']
'0714381809'
```

Si la clé n'existe dans aucun dictionnaire, on obtient une erreur `KeyError` comme habituellement.

```python
>>> phonebook['Mehdi']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3.8/collections/__init__.py", line 891, in __getitem__
    return self.__missing__(key)            # support subclasses that define __missing__
  File "/usr/lib/python3.8/collections/__init__.py", line 883, in __missing__
    raise KeyError(key)
KeyError: 'Mehdi'
```

L'objet `ChainMap` ne contient que des références vers nos dictionnaires, et donc reflète bien les modifications sur ces derniers.

```python
>>> phonebook_tel['Mehdi'] = '0762253973'
>>> phonebook['Mehdi']
'0762253973'
```

Aussi, il est possible de directement affecter des valeurs au `ChainMap`, celles-ci seront affectées au premier dictionnaire de la chaîne.

```python
>>> phonebook['Julie'] = '0619096810'
>>> phonebook_sim
{'Alice': '0633432380', 'Bob': '0663621029', 'Julie': '0619096810'}
```

Il en est de même pour les clés qui existeraient dans les dictionnaires suivants, elles seraient tout de même assignées au premier (c'est le seul accessible en écriture).

```python
>>> phonebook['Alex'] = '0734593960'
>>> phonebook
ChainMap({'Alice': '0633432380', 'Bob': '0663621029', 'Julie': '0619096810', 'Alex': '0734593960'}, {'Alex': '0714381809', 'Mehdi': '0762253973'})
```

On voit ainsi comment se passe la priorité entre les dictionnaires en lecture : la chaîne est parcourue et s'arrête au premier dictionnaire contenant la clé.

```python
>>> phonebook['Alex']
'0734593960'
```

Cette fonctionnalité est très pratique pour mettre en place des espaces de noms, comme les scopes des fonctions en Python : des variables existent à l'intérieur de la fonction et sont prioritaires par rapport aux variables extérieures.

La méthode `new_child` et l'attribut `parents` sont utiles pour cela puisqu'ils permettent respectivement d'ajouter un nouveau dictionnaire en tête de la chaîne (qui comprendra donc toutes les futures modifications sur le `ChainMap`) et de récupérer la suite de la chaîne (la chaîne formée par tous les dictionnaires sauf le premier).

Tous deux renvoient un nouvel objet `ChainMap` sans altérer la chaîne courante.

```python
>>> new_phonebook = phonebook.new_child()
>>> new_phonebook['Max'] = '0704779572'
>>> new_phonebook
ChainMap({'Max': '0704779572'}, {'Alice': '0633432380', 'Bob': '0663621029', 'Julie': '0619096810', 'Alex': '0734593960'}, {'Alex': '0714381809', 'Mehdi': '0762253973'})
>>> new_phonebook.parents
ChainMap({'Alice': '0633432380', 'Bob': '0663621029', 'Julie': '0619096810', 'Alex': '0734593960'}, {'Alex': '0714381809', 'Mehdi': '0762253973'})
```

`new_child` peut s'utiliser sans argument, auquel cas un dictionnaire vide sera ajouté, ou en donnant directement le dictionnaire à ajouter en argument.

```python
>>> phonebook.new_child({'Max': '0704779572'})
ChainMap({'Max': '0704779572'}, {'Alice': '0633432380', 'Bob': '0663621029', 'Julie': '0619096810', 'Alex': '0734593960'}, {'Alex': '0714381809', 'Mehdi': '0762253973'})
```

On retrouve sinon les mêmes méthodes que sur les dictionnaires.

#### `deque`

En Python les tableaux sont trompeusement appelés des listes là où ce terme fait souvent référence à des listes chaînées.
Un tableau représente des données contigües en mémoire, qui ne peuvent pas être morcellées, et occupe donc une zone mémoire continue qui dépend de sa taille.

Ainsi, lorsque l'on ajoute ou retire des éléments à un tableau, il peut être nécessaire d'adapter la taille de la zone mémoire, voire d'en trouver une nouvelle plus grande et d'y copier tous les éléments.
Python fait cela pour nous, mais ce sont des opérations qui peuvent s'avérer coûteuses.

Les listes chaînées à l'inverse sont des chaînes constituées de maillons, chaque maillon étant un élément avec son propre espace mémoire, ceux-ci peuvent être n'importe où dans la mémoire.  
L'idée est que chaque maillon référence le précédent et le suivant dans la chaîne.

On pourrait par exemple voir un maillon comme un dictionnaire avec 2 clés : `next` pour référencer le maillon suivant et `value` pour la valeur contenue (car l'idée est quand même bien d'y stocker des valeurs).

Voici ainsi un équivalent en liste chaîne de la liste `[1, 2, 3, 4]`.

```python
>>> node4 = {'next': None, 'value': 4}
>>> node3 = {'next': node4, 'value': 3}
>>> node2 = {'next': node3, 'value': 2}
>>> node1 = {'next': node2, 'value': 1}
>>> values = node1
```

Les variables `node1`, `node2` etc. ne sont que temporaires pour la création de notre liste, elles n'existent plus après, seule `values` référence notre chaîne de maillons.

```python
>>> del node1
>>> del node2
>>> del node3
>>> del node4
```

Il nous serait alors possible d'itérer sur notre liste chaînée pour accéder à chacune des valeurs.

```python
>>> node = values # La liste représente le premier maillon
>>> while node is not None: # None représente la fin de liste
...     print(node['value'])
...     node = node['next'] # On passe au nœud suivant en réaffectant node
... 
1
2
3
4
```

Mais il n'est pas question ici de recoder une liste chaînée, Python en propose déjà une avec le type `deque` du module `collections`.  
*deque* pour *double-end queue*, c'est-à-dire une queue (liste chaînée) dont les deux extrêmités sont connues (le premier et le dernier maillon) et les liaisons sont doubles (chaque maillon référence le précédent et le suivant), contrairement à notre implémentation où seul le premier maillon était connu et les liaisons étaient simples (référence vers le maillon suivant uniquement).

Le principe est sinon le même.
Un *deque* se construit comme une liste, soit vide soit à partir d'un itérable existant.

```python
>>> deque()
deque([])
>>> deque([1, 2, 3, 4])
deque([1, 2, 3, 4])
```

Et le type propose les mêmes méthodes que les listes, ce sont juste les algorithmes derrière qui sont différents, et certaines opérations qui sont à privilégier plutôt que d'autres.

```python
>>> values = deque([1, 2, 3, 4])
>>> values[0]
1
>>> values.append(5)
>>> values
deque([1, 2, 3, 4, 5])
```

Par exemple, contrairement aux tableaux (`list`) il est très facile (peu coûteux) d'ajouter des éléments au début ou à la fin, puisqu'il suffit d'insérer un nouveau maillon à l'extrêmité et de changer la référence.
De même pour supprimer un élément au début ou à la fin.

Les *deque* proposent d'ailleurs des méthodes dédiées avec `appendleft` et `popleft`, équivalentes à `append` et `pop` mais pour opérer au début de la liste.

```python
>>> values.appendleft(0)
>>> values
deque([0, 1, 2, 3, 4, 5])
>>> values.popleft()
0
>>> values
deque([1, 2, 3, 4, 5])
```

En revanche, comme seules les extrêmités sont connues, il est coûteux d'aller chercher un élément en milieu de liste, puisqu'il est nécessaire pour cette opération de parcourir tous les maillons jusqu'au bon élément.

```python
>>> values[2]
3
```

Pour accéder à cette valeur, il a fallu parcourir 3 maillons. Il aurait fallu en parcourir 500 pour atteindre le milieu d'une liste chaînée de 1000 éléments.
Là où pour un tableau l'accès à chaque élément est direct puisque son emplacement mémoire est connu : il se calcule facilement à partir de la position du premier élément, les éléments étant contigüs en mémoire.

Ainsi, ne faites appel aux listes chaînées que pour des opérations qui nécessiteraient de souvent ajouter et/ou supprimer des données en début/fin de séquence, c'est là leur intérêt par rapport aux tableaux.  
Ne les utilisez pas si vous devez accéder régulièrement à des éléments situés loin des extrêmités, les performances pourraient être désastreuses.

#### `namedtuple`

Pour terminer avec le module `collections`, j'aimerais vous parler des *named tuples* (*tuples* nommés).

Vous le savez, un *tuple* représente un ensemble cohérent de données, par exemple deux coordonnées qui identifient un point dans le plan.
Il est sinon semblable à une liste (bien que non modifiable) et permet d'accéder aux éléments à partir de leur position.

```python
```python
>>> point = (3, 5)
>>> point[0]
3
```

Et par *unpacking* il est possible d'accéder à ses éléments indépendemment.

```python
>>> x, y = point
>>> y
5
```

Mais ne serait-il pas plus pratique de pouvoir directement taper `point.y` pour accéder à l'ordonnée du point ?
C'est plus facilement compréhensible que `point[0]` et moins contraignant que l'*unpacking* qui nécessite de définir une nouvelle variable.

Vous le voyez venir, c'est ce que proposent les *tuples* nommés, donner des noms aux éléments d'un *tuple*.
Mais tout d'abord, il faut créer un type associé à ces *tuples* nommés, pour définir justement les noms de champs.
Car un *tuple* nommé identifiant un point ne sera pas la même chose qu'un *tuple* nommé identifiant une couleur par exemple.

Nous allons donc devoir définir un nouveau type et c'est précisément ce que fait la fonction `namedtuple` du module `collections` : elle crée dynamiquement un type de *tuples* nommés en fonction des paramètres qu'elle reçoit.
Pour ça, elle prend en arguments le nom du type à créer (utilisé pour la représentation de l'objet) et la liste des noms des champs des *tuples*.

La fonction renvoie un type, mais il faudra assigner ce retour à une variable pour pouvoir l'utiliser, comme tout autre retour de fonction.
Les types en Python sont en fait des objets comme les autres, qui peuvent donc être assignés à des variables.
Par convention, on utilisera un nom commençant par une majuscule, pour identifier un type.

```python
>>> from collections import namedtuple
>>> Point = namedtuple('Point', ('x', 'y'))
>>> Point
<class '__main__.Point'>
```

Ensuite, pour instancier un objet `Point`, on appelle le type en lui donnant en arguments les deux coordonnées `x` et `y`.

```python
>>> point = Point(3, 5)
>>> point
Point(x=3, y=5)
>>> point.x
3
```

On le voit à sa représentation, il est aussi possible d'instancier l'objet en utilisant des arguments nommés.

```python
>>> Point(x=10, y=7)
Point(x=10, y=7)
```

Notre objet `point` est toujours un *tuple*, et il reste possible de l'utiliser comme tel.

```python
>>> point[0]
3
>>> x, y = point
>>> y
5
```
