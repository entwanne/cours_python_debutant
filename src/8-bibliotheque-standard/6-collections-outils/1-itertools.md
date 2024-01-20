### Module itertools

Nous l'avons vu plus tôt lors du [retour sur les boucles](https://zestedesavoir.com/tutoriels/2514/un-zeste-de-python/7-perfectionnement/3-boucles/#module-itertools) : [`itertools`](https://docs.python.org/fr/3/library/itertools.html) est un module de la bibliothèque standard qui fournit de nombreux outils pour manipuler des itérables.

Je présentais les fonctions `chain` (enchaîne plusieurs itérables), `zip_longest` (combine plusieurs itérables en s'alignant sur le plus long), `product` (réalise le produit cartésien de plusieurs itérables), `count` (itérateur infini pour compter) et `repeat` (itérateur répétant une même valeur).  
On voit par la diversité de ces fonctions que ce module couvre différents usages que j'aimerais explorer dans ce chapitre.

#### Enchaînements

Le module propose des fonctions pour enchaîner plusieurs itérables.

##### `chain`

La fonction `chain` que nous avons vu permet cela simplement et renvoie un itérateur qui parcourt successivement chacun des arguments, itérant sur leurs éléments un par un et se terminant une fois tous ses arguments parcourus.

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

Une autre utilisation de cette fonction consiste à appeler `chain.from_iterable` qui prend un unique argument : un itérable d'itérables afin de les chaîner ensemble.

```pycon
>>> for item in itertools.chain.from_iterable([[1, 2, 3], [4, 5], [6]]):
...     print(item)
... 
1
2
3
4
5
6
```

`chain.from_iterable(iterables)` est ainsi équivalent à `chain(*iterables)` à l'exception près que dans le premier cas `iterables` peut être infini.

##### `cycle`

Dans le même genre on trouve aussi `cycle` qui renvoie un itérateur bouclant (indéfiniment) sur un même itérable.

```pycon
>>> values = itertools.cycle(['hello', 'world'])
>>> next(values)
'hello'
>>> next(values)
'world'
>>> next(values)
'hello'
```

C'est aussi un cas d'utilisation pour avoir un itérable que l'on voudrait au moins aussi grand qu'un autre.

```pycon
>>> for x, y in zip(range(10), itertools.cycle([3, 5, 6])):
...     print(x, y)
... 
0 3
1 5
2 6
3 3
4 5
5 6
6 3
7 5
8 6
9 3
```

##### `repeat`

La fonction `repeat` est un cas d'usage plus simple puisqu'elle permet juste de répéter (indéfiniment) une même valeur.

```pycon
>>> values = itertools.repeat('hello')
>>> next(values)
'hello'
>>> next(values)
'hello'
>>> next(values)
'hello'
```

On peut peut aussi lui donner un argument qui indique le nombre de répétitions à effectuer (l'itérateur produit n'est alors plus infini).

```pycon
>>> list(itertools.repeat('hello', 5))
['hello', 'hello', 'hello', 'hello', 'hello']
```

#### Combinaisons et permutations

Plusieurs fonctions du module permettent de réaliser différentes combinaisons entre un ou plusieurs itérables donnés en argument.

##### `zip_longest`

Une première manière de combiner des itérables consiste à les parcourir simultanément, c'est ce que fait `zip_longest` (ainsi que `zip` dans les _built-ins_) qui produit des tuples contenant un élément de chaque argument.

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

#### Agrégations

Les fonctions qui suivent permettent de regrouper et agréger les éléments d'un itérable selon certains critères.

##### `groupby`

`groupby` prend en argument un itérable et une fonction `key` pour identifier le groupe de chaque élément, et produit des paires composées d'une clé de groupe et d'un itérateur sur les éléments correspondants.

```pycon
>>> for group_key, items in itertools.groupby(['foo', 'bar', 'toto', 'tata'], key=len):
...     print(group_key, list(items))
... 
3 ['foo', 'bar']
4 ['toto', 'tata']
```

Attention cependant, cette fonction n'opère que sur les éléments consécutifs qui partagent la même clé : un nouveau groupe sera créé chaque fois que la clé d'un élément diffère par rapport au précédent.
Cela peut être surprenant sur une liste non triée puisque l'on peut alors obtenir plusieurs groupes avec la même clé.

```pycon
>>> for group_key, items in itertools.groupby(['foo', 'toto', 'tata', 'bar'], key=len):
...     print(group_key, list(items))
... 
3 ['foo']
4 ['toto', 'tata']
3 ['bar']
```

Un premier tri avec la même clé est alors utile si l'on veut s'assurer de l'unicité des groupes.

```pycon
>>> for group_key, items in itertools.groupby(sorted(['foo', 'toto', 'tata', 'bar'], key=len), key=len):
...     print(group_key, list(items))
... 
3 ['foo', 'bar']
4 ['toto', 'tata']
```

On notera que l'argument `key` est optionnel : s'il n'est pas fourni, chaque élément devient sa propre clé.
La fonction permet alors de grouper les éléments égaux consécutifs.

```pycon
>>> for c, items in itertools.groupby(['A', 'A', 'B', 'C', 'C', 'C']):
...     print(c, list(items))
... 
A ['A', 'A']
B ['B']
C ['C', 'C', 'C']
```

##### `batched`

`batched` est une fonction introduite dans Python 3.12 qui s'occupe de découper un itérable en groupes de taille donnée, dans l'ordre des éléments.
Il se peut que le dernier groupe soit plus petit s'il n'y a plus assez d'éléments pour le remplir.

```pycon
>>> for batch in itertools.batched(range(10), 3):
...     print(batch)
... 
(0, 1, 2)
(3, 4, 5)
(6, 7, 8)
(9,)
```

##### `pairwise`

La fonction `pairwise` permet d'itérer sur des paires successives formées par les éléments de l'itérable.
La première paire contiendra les deux premiers éléments de l'itérable, la seconde paire contiendra le deuxième et le troisième élément et ainsi de suite.

```pycon
>>> for pair in itertools.pairwise(range(10)):
...     print(pair)
... 
(0, 1)
(1, 2)
(2, 3)
(3, 4)
(4, 5)
(5, 6)
(6, 7)
(7, 8)
(8, 9)
```

##### `accumulate`

Cette fonction permet d'appliquer une opération au fur et à mesure que l'on parcourt l'itérable.
Elle prend ainsi en argument un itérable et une opération, et produit les résultats de l'opération après application sur le précédent résultat et l'élément en cours.

```pycon
>>> for current_max in itertools.accumulate([1, 8, 2, 4, 9, 7], max):
...     print(current_max)
... 
1
8
8
8
9
9
```

Le second argument est optionnel et l'opération par défaut est l'addition / concaténation.

```pycon
>>> for current_sum in itertools.accumulate([1, 8, 2, 4, 9, 7]):
...     print(current_sum)
... 
1
9
11
15
24
31
```

```pycon
>>> for word in itertools.accumulate('ABCD'):
...     print(word)
... 
A
AB
ABC
ABCD
```

-----

Le module dispose encore de nombreuses autres fonctions (notamment pour filtrer les éléments d'un itérable) que je vous invite à découvrir dans [la documentation](https://docs.python.org/fr/3/library/itertools.html).

#### Recettes

En plus de donner des explications et exemples pour chacune de ses fonctions, la documentation du module `itertools` [fournit aussi quelques « recettes »](https://docs.python.org/fr/3/library/itertools.html#itertools-recipes).

Il s'agit de fonctions qui répondent à des besoins trop particuliers pour être vraiment intégrées au module.
Les recettes sont là pour que vous les repreniez dans votre code et que vous les adaptiez à votre convenance.  
Vous y trouverez d'autres manières d'enchaîner, combiner ou agréger vos itérables.
