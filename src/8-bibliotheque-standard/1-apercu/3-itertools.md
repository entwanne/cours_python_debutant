### Itertools

Nous l'avons vu plus tôt lors du [retour sur les boucles](https://zestedesavoir.com/tutoriels/2514/un-zeste-de-python/7-perfectionnement/3-boucles/#module-itertools) : [`itertools`](https://docs.python.org/fr/3/library/itertools.html) est un module de la bibliothèque standard qui fournit de nombreux outils pour manipuler des itérables.

Je présentais les fonctions `chain` (enchaîne plusieurs itérables), `zip_longest` (combine plusieurs itérables en s'alignant sur le plus long), `product` (réalise le produit cartésien de plusieurs itérables), `count` (itérateur infini pour compter) et `repeat` (itérateur répétant une même valeur).  
On voit par la diversité de ces fonctions que ce module couvre différents usages que j'aimerais explorer dans ce chapitre.

#### Combinaisons et permutations

Plusieurs fonctions du module permettent de réaliser des combinaisons différentes entre des itérables donnés en argument.

##### `chain`

Une première manière de combiner des itérables consiste à les enchaîner : la fonction `chain` permet cela et renvoie un itérateur qui parcourt successivement chacun des arguments, itérant sur leurs éléments un par un.

```pycon
>>> for item in itertools.chain([1, 2, 3], [4, 5], [6]):
...     print(item)
...
1
2
3
4
5
6
```

La fonction accepte bien sûr des itérables de tous types.

* `chain.from_iterable`

##### `zip_longest`

Une seconde manière est de les parcourir simultanément, c'est ce que fait `zip_longest` (ainsi que `zip` dans les _builtins_) qui produit des tuples contenant un élément de chaque argument.

```pycon
>>> for item in itertools.zip_longest([1, 2, 3], [4, 5], [6]):
...     print(item)
...
(1, 4, 6)
(2, 5, None)
(3, None, None)
```

On a vu que l'argument `fillvalue` permettait de spécifier la valeur à utiliser une fois qu'un itérable est entièrement consommé (`None` par défaut).

##### `product`

La fonction `product` réalise un produit cartésien entre ses arguments, renvoyant toutes les combinaisons possibles de tuples comprenant un élement de chaque argument (le premier élément du tuple étant un élément du premier argument, etc.).  
Ainsi, utilisée avec des listes de tailles respectives 3, 2 et 1 elle renverra 3×2×1 = 6 combinaisons.

```pycon
>>> for item in itertools.product([1, 2, 3], [4, 5], [6]):
...     print(item)
...
(1, 4, 6)
(1, 5, 6)
(2, 4, 6)
(2, 5, 6)
(3, 4, 6)
(3, 5, 6)
```

`product` accepte aussi un argument `repeat` qui lui permet de considérer plusieurs fois les itérables qui lui sont donnés.
`product([1, 2, 3], [4, 5], repeat=2)` est ainsi équivalent à `product([1, 2, 3], [4, 5], [1, 2, 3], [4, 5])`.

Cela permet notamment de calculer toutes les combinaisons possibles (non ordonnées et avec remise) de paires d'éléments dans un même ensemble.

```pycon
>>> for pair in itertools.product([1, 2, 3], repeat=2):
...     print(pair)
...
(1, 1)
(1, 2)
(1, 3)
(2, 1)
(2, 2)
(2, 3)
(3, 1)
(3, 2)
(3, 3)
```

##### `permutations`

Cette fonction permet de calculer les combinaisons possibles, non ordonnées et sans remise, de l'itérable donné en argument.  
C'est-à-dire que dans le cas de combinaisons entre deux éléments une paire apparaîtra deux fois, dans les deux ordres possibles (d'où le nom de permutations), et que cette fonction ne renverra pas de paires consistuées du même élement (à moins que l'élément soit présent plusieurs fois dans l'itérable).

```pycon
>>> for pair in itertools.permutations([1, 2, 3], 2):
...     print(pair)
...
(1, 2)
(1, 3)
(2, 1)
(2, 3)
(3, 1)
(3, 2)
```

Le second argument correspond au nombre d'éléments à tirer (2 pour former des paires), il est optionnel et égal à la taille de l'itérable s'il est omis (3 ici).

```pycon
>>> for item in itertools.permutations([1, 2, 3]):
...     print(item)
...
(1, 2, 3)
(1, 3, 2)
(2, 1, 3)
(2, 3, 1)
(3, 1, 2)
(3, 2, 1)
```

##### `combinations`

Cette fonction permet de calculer les combinaisons possibles, ordonnées et sans remise.  
Entre deux éléments, une paire n'apparaîtra donc qu'une fois (pas de permutations) et la fonction ne renverra pas de paires du même élément.

Le 2ème argument permet là encore de préciser le nombre d'éléments à tirer mais est cette fois-ci obligatoire.

```pycon
>>> for pair in itertools.combinations([1, 2, 3], 2):
...     print(pair)
...
(1, 2)
(1, 3)
(2, 3)
```

##### `combinations_with_replacement`

Enfin, il existe une variante de `combinations` avec remise.
Une paire de deux éléments n'apparaîtra qu'une fois mais la fonction renverra aussi les paires constituées du même élément.

```pycon
>>> for pair in itertools.combinations_with_replacement([1, 2, 3], 2):
...     print(pair)
...
(1, 1)
(1, 2)
(1, 3)
(2, 2)
(2, 3)
(3, 3)
```

#### Répétitions

##### `repeat`

`repeat` peut aussi prendre un argument qui indique le nombre de répétitions à effectuer, auquel cas il ne sera plus infini.

```pycon
>>> list(repeat('hello', 5))
['hello', 'hello', 'hello', 'hello', 'hello']
```

##### `cycle`

Dans le même genre on trouve aussi `cycle` pour boucler (indéfiniment) sur un même itérable.

```pycon
>>> from itertools import cycle
>>> values = cycle(['hello', 'world'])
>>> next(values)
'hello'
>>> next(values)
'world'
>>> next(values)
'hello'
```

C'est aussi un cas d'utilisation pour avoir un itérable que l'on voudrait au moins aussi grand qu'un autre.

```pycon
>>> additions(range(10), cycle([3, 5, 8]))
0 + 3 = 3
1 + 5 = 6
2 + 8 = 10
3 + 3 = 6
4 + 5 = 9
5 + 8 = 13
6 + 3 = 9
7 + 5 = 12
8 + 8 = 16
9 + 3 = 12
```

#### Agrégations

##### `groupby`

##### `batched`

##### `accumulate`

-----

Le module dispose encore de nombreuses autres fonctions (notamment pour filtrer les éléments d'un itérable) que je vous invite à découvrir dans [la documentation](https://docs.python.org/fr/3/library/itertools.html).

#### Recettes

En plus de donner des explications et exemples pour chacune de ses fonctions, la documentation du module `itertools` [fournit aussi quelques « recettes »](https://docs.python.org/fr/3/library/itertools.html#itertools-recipes).

Il s'agit de fonctions qui répondent à des besoins trop particuliers pour être vraiment intégrées au module.
Les recettes sont là pour que vous les repreniez dans votre code et que vous les adaptiez à votre convenance.
