### Types

Nous avons maintenant vu de nombreux types Python, mais savons-nous reconnaître les valeurs d'un certain type ?
Oui, à l'usage on sait différencier une chaîne de caractères d'un nombre, parce qu'ils se représentent différemment, et qu'on y applique des opérations différentes.  
Mais il est possible d'aller plus loin dans la reconnaissance des types et nous allons voir quels outils sont mis à disposition par Python pour cela.

Premièrement, la *fonction* `type`[^type] permet de connaître le type d'un objet.
On lui donne une valeur en argument et la fonction nous renvoie simplement son type.

[^type]: C'est en fait plus compliqué que cela et je ne rentrerai pas dans les détails ici, mais `type` est lui-même un type, le type de tous les types. Nous ne l'utiliserons dans ce tutoriel que comme une fonction.

```pycon
>>> type(5)
<class 'int'>
>>> type('foo')
<class 'str'>
>>> type([0])
<class 'list'>
```

Cela peut être utile dans des phases de débogage, pour s'assurer qu'une valeur est bien du type auquel on pense.  
On peut aussi l'utiliser dans le code pour vérifier le type d'un objet mais ce n'est généralement pas recommandé (car trop strict, voir plus bas).

```pycon
>>> def check_type(value):
...     if type(value) is str:
...         print("C'est une chaîne de caractères")
...     else:
...         print("Ce n'est pas une chaîne de caractères")
... 
>>> check_type('foo')
C'est une chaîne de caractères
>>> check_type(5)
Ce n'est pas une chaîne de caractères
```

L'autre outil mis à disposition de Python pour reconnaître le type d'une valeur est la fonction `isinstance`.
Cette fonction reçoit une valeur et un type, et renvoie un booléen selon que la valeur soit de ce type ou non.

```pycon
>>> isinstance('foo', str)
True
>>> isinstance(5, str)
False
```

Mais une valeur n'est pas d'un seul type, il existe en fait une hiérarchie entre les types.
Par exemple, tous les objets Python sont des instances du type `object`, car `object` est le parent de tous les types.

```pycon
>>> isinstance('foo', object)
True
>>> isinstance(5, object)
True
```

Ou encore, avec notre objet `point` construit précédemment, qui est à la fois une instance de `Point` et de `tuple`.

```pycon
>>> type(point)
<class '__main__.Point'>
>>> isinstance(point, Point)
True
>>> isinstance(point, tuple)
True
```

Cela nous montre une première limitation de l'appel à `type` pour vérifier le type, qui ne verrait pas que nos valeurs sont aussi des `object`, ou notre point un `tuple`.

```pycon
>>> type('foo') is object
False
>>> type(5) is object
False
>>> type(point) is tuple
False
```

Vérifier avec `type` est donc à limiter aux cas où l'on veut s'assurer strictement du type d'un objet, sans considérer la hiérarchie des types, et ce sont des cas assez rares.

Il faut cependant faire attention aussi aux appels à `isinstance` et les utiliser avec parcimonie, au risque de contrevenir à une caractéristique importante du Python, le *duck-typing*.

[[i]]
| Le *duck-typing* (*typage canard*) est une philosophie dans la reconnaissance des types des valeurs.
| Elle repose sur la phrase « Si cela a un bec, marche comme un canard et cancanne comme un canard, alors je peux considérer que c'est un canard ».
|
| Appliqué au Python, cela veut dire par exemple qu'on préfère savoir qu'un objet se comporte comme une liste (que les mêmes opérations y sont applicables) plutôt que de vérifier que ce soit réellement une liste. On dit aussi que les valeurs doivent avoir la même interface qu'une liste.  
| Cela laisse la possibilité aux développeurs d'utiliser les types de leur choix tout en gardant une compatibilité avec les fonctions existantes.
|
| C'est tout le principe des itérables : les fonctions de Python n'attendent jamais précisément une liste mais juste un objet sur lequel on puisse itérer. Que ce soit une liste, un *tuple*, une chaîne de caractères ou encore un fichier, peu importe.

Ainsi, on évitera les `if isinstance(value, list): ...` si ce n'est pas strictement nécessaire (un traitement particulier à réserver aux objets de ce type), pour ne pas laisser de côté les autres types qui auraient pu convenir tels que les *tuples*.

Mais `isinstance` ne se limite pas à des types clairement définis et permet aussi de vérifier des interfaces.
C'est ce que propose le module `collections.abc` qui fournit une collection de types abstraits (*abc* pour *abstract base classes*, classes mères abstraites), des interfaces correspondant à des comportements en particulier.

On trouve ainsi un type `Iterable`.
Il n'est pas utilisable en tant que tel, on ne peut pas instancier d'objets du type `Iterable`, mais on peut l'utiliser pour vérifier qu'un objet est bien itérable en appelant `isinstance`.

```pycon
>>> from collections.abc import Iterable
>>> isinstance([1, 2, 3], Iterable)
True
>>> isinstance((4, 5, 6), Iterable)
True
>>> isinstance('hello', Iterable)
True
>>> isinstance(42, Iterable)
False
```

Il y a aussi `Hashable` par exemple pour vérifier qu'une valeur est hashable, que l'on peut l'utiliser en tant que clé dans un dictionnaire ou la stocker dans un ensemble.

```pycon
>>> from collections.abc import Hashable
>>> isinstance(42, Hashable)
True
>>> isinstance('hello', Hashable)
True
>>> isinstance([1, 2, 3], Hashable)
False
>>> isinstance((4, 5, 6), Hashable)
True
```

On trouve encore d'autres types abstraits définis dans `collections.abc` mais il est un peu tôt pour les aborder.
