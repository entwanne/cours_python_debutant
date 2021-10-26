### Outils

Le monde de l'itération est très vaste en Python, les itérables se retrouvent au cœur de nombreux mécanismes.
C'est pourquoi Python propose de base de nombreux outils relatifs à l'itération tels que les fonctions `all` et `any` que l'on a déjà vues.

Vous êtes-vous déjà demandé comment itérer simultanément sur plusieurs listes ou comment répéter une liste ? Ce chapitre est fait pour vous !

#### Fonctions natives (_builtins_)

On a déjà vu un certain nombre de *builtins* dans les chapitres précédents, mais il en reste quelques unes très intéressantes que j'ai omises jusqu'ici.

##### `enumerate`

Notamment la fonction `enumerate`, qui prend une liste (ou n'importe quel itérable) et permet d'itérer sur ses valeurs tout en leur associant leur index.
C'est-à-dire que pour chaque valeur on connaîtra la position qu'elle occupe dans la liste.

```pycon
>>> values = ['abc', 'def', 'ghi']
>>> for i, value in enumerate(values):
...     print(i, ':', value)
... 
0 : abc
1 : def
2 : ghi
```

Cela remplace aisément les constructions à base de `range(len(values))` que l'on voit trop souvent et qui sont à éviter.

```pycon
>>> for i in range(len(values)):
...     print(i, ':', values[i])
... 
0 : abc
1 : def
2 : ghi
```

On les évite justement parce qu'`enumerate` répond mieux au problème tout en étant plus polyvalent (on peut par exemple itérer sur un fichier), et qu'on a directement accès à la valeur (`value`) sans besoin d'une indirection supplémentaire par le conteneur (`values[i]`).

On notera au passage que la fonction `enumerate` accepte un deuxième argument pour préciser l'index de départ, qui est par défaut de zéro.

```pycon
>>> with open('corbeau.txt') as f:
...     for i, line in enumerate(f, 1):
...         print(i, ':', line.rstrip())
... 
1 : Maître Corbeau, sur un arbre perché,
2 : Tenait en son bec un fromage.
3 : Maître Renard, par l'odeur alléché,
4 : Lui tint à peu près ce langage :
5 : Et bonjour, Monsieur du Corbeau.
6 : Que vous êtes joli ! que vous me semblez beau !
7 : Sans mentir, si votre ramage
8 : Se rapporte à votre plumage,
9 : Vous êtes le Phénix des hôtes de ces bois.
10 : À ces mots, le Corbeau ne se sent pas de joie ;
11 : Et pour montrer sa belle voix,
12 : Il ouvre un large bec, laisse tomber sa proie.
13 : Le Renard s'en saisit, et dit : Mon bon Monsieur,
14 : Apprenez que tout flatteur
15 : Vit aux dépens de celui qui l'écoute.
16 : Cette leçon vaut bien un fromage, sans doute.
17 : Le Corbeau honteux et confus
18 : Jura, mais un peu tard, qu'on ne l'y prendrait plus.
```

#### `reversed`

`reversed` est une fonction très simple, elle permet d'inverser une séquence d'éléments, pour les parcourir dans l'ordre inverse.

```pycon
>>> values = ['abc', 'def', 'ghi']
>>> for value in reversed(values):
...     print(value)
... 
ghi
def
abc
```

La fonction ne modifie pas la séquence initiale (contrairement à la méthode `reverse` des listes).

```pycon
>>> values
['abc', 'def', 'ghi']
```

#### `sorted`

Dans la même veine on a la fonction `sorted`, semblable à la méthode `sort` des listes mais renvoyant ici une copie.

```pycon
>>> values = [5, 3, 2, 4, 6, 1, 9, 7, 8]
>>> sorted(values)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> values
[5, 3, 2, 4, 6, 1, 9, 7, 8]
```

On notera que le tri se fait en ordre croissant (les plus petits éléments d'abord) par défaut, mais la fonction accepte un argument `reverse` pour trier en ordre décroissant (les plus grands d'abord).

```pycon
>>> sorted(values, reverse=True)
[9, 8, 7, 6, 5, 4, 3, 2, 1]
```

Mieux encore, la fonction propose un paramètre `key` pour personnaliser la manière dont seront triés nos éléments.
C'est une fonction qui recevra un élément en paramètre et renverra une valeur (par exemple un nombre), le tri se fera alors suivant l'ordre entre ces valeurs renvoyées.

[[i]]
| Les fonctions en Python sont des valeurs comme les autres que l'on peut donc parfaitement passer en argument.
| Ces arguments-fonctions sont généralement appelés des _callbacks_ (ou « fonctions de rappel »).

Par exemple, le tri par défaut pour les chaînes de caractères est l'ordre lexicographique (plus ou moins équivalent à l'ordre alphabétique).

```pycon
>>> words = ['zèbre', 'autruche', 'cheval', 'oie']
>>> sorted(words)
['autruche', 'cheval', 'oie', 'zèbre']
```

On pourrait alors préciser une fonction de tri `key=len` pour les trier par taille.

```pycon
>>> sorted(words, key=len)
['oie', 'zèbre', 'cheval', 'autruche']
```

En effet, la fonction `len` sera appelée pour chaque mot et les mots seront triés suivant le retour de la fonction (en l'occurrence 3, 5, 6 et 8).
Mais il est possible d'utiliser n'importe quelle fonction en tant que clé de tri, tant que cette fonction renvoie quelque chose d'ordonnable.

Voici un autre exemple avec une fonction pour trier les mots dans l'ordre alphabétique mais en commençant par la dernière lettre du mot.

```pycon
>>> def key_func(word):
...     return word[::-1] # On renvoie le mot à l'envers
...
>>> key_func('autruche')
'ehcurtua'
>>> sorted(words, key=key_func)
['autruche', 'oie', 'zèbre', 'cheval']
```

Ces deux arguments sont aussi disponibles sur la méthode `sort` des listes.

```pycon
>>> words.sort(key=len, reverse=True)
>>> words
['autruche', 'cheval', 'zèbre', 'oie']
```

#### `min` et `max`

On a déjà vu les fonctions `min` et `max` qui permettent respectivement de récupérer le minimum/maximum parmi leurs arguments.

```pycon
>>> min(3, 1, 2)
1
>>> max(3, 1, 2)
3
```

On sait aussi qu'on peut les appeler avec un seul argument (un itérable) et récupérer le minimum/maximum dans cet itérable.

```pycon
>>> min({3, 1, 2})
1
>>> max([3, 1, 2])
3
```

Mais sachez maintenant que ces fonctions acceptent aussi un argument `key` qui fonctionne de la même manière que pour `sorted`.  
Ainsi il est possible d'expliquer comment doivent être comparées les valeurs.
On peut alors simplement demander la valeur minimale/minimale d'une liste en comparant les nombres selon leur valeur absolue.

```pycon
>>> min([-5, -2, 1, 3], key=abs)
1
>>> max([-5, -2, 1, 3], key=abs)
-5
```

Ces fonctions acceptent aussi un argument `default` dont la valeur est renvoyée (plutôt qu'une erreur) si l'itérable est vide.

```pycon
>>> min([])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: min() arg is an empty sequence
>>> min([], default=42)
42
```

#### `zip`

`zip` est une fonction très pratique de Python, puisqu'elle permet de parcourir simultanément plusieurs itérables.
On appelle la fonction en lui fournissant nos itérables en arguments, et l'on itère ensuite sur l'objet qu'elle nous renvoie.  
Les éléments que l'on obtient alors sont des tuples formés des éléments de nos itérables de départ.

```pycon
>>> for elem in zip(words, 'abcd', range(4)):
...     print(elem)
... 
('autruche', 'a', 0)
('cheval', 'b', 1)
('zèbre', 'c', 2)
('oie', 'd', 3)
```

Il est ainsi possible d'utiliser l'_unpacking_ de Python pour avoir quelque chose de plus explicite.

```pycon
>>> for word, letter, number in zip(words, 'abcd', range(4)):
...     print(word, letter, number)
... 
autruche a 0
cheval b 1
zèbre c 2
oie d 3
```

`zip` accepte autant d'arguments que l'on souhaite, on peut l'appeler avec deux itérables comme avec dix.

Aussi, il s'arrête dès que l'un des itérables se termine, puisqu'il ne peut alors plus produire de tuple contenant un élément de chaque.

```pycon
>>> for i, j in zip(range(2, 6), range(10)):
...     print(i, j)
... 
2 0
3 1
4 2
5 3
```

#### Module `itertools`

En plus des outils *built-in* pour manipuler les itérables, la bibliothèque standard fournit aussi une mine d'or : le module [`itertools`](https://docs.python.org/fr/3/library/itertools.html).

Je ne détaillerai pas tout ce que contient le module, la documentation fera cela beaucoup mieux que moi.
Je veux juste vous présenter quelques fonctions qui pourraient vous être bien utiles.

##### `chain`

Comme son nom l'indique, `chain` permet de chaîner plusieurs itérables, de façon transparente et quels que soient leurs types.

```pycon
>>> from itertools import chain
>>> for letter in chain('ABC', ['D', 'E'], ('F', 'G')):
...     print(letter)
... 
A
B
C
D
E
F
G
```

##### `zip_longest`

`zip_longest` est un équivalent à `zip` qui ne s'arrête pas au premier itérable terminé mais qui continue jusqu'au dernier.
Les valeurs manquantes seront alors complétées par `None`, ou par la valeur précisée au paramètre `fillvalue`.

```pycon
>>> from itertools import zip_longest
>>> for i, j in zip_longest(range(2, 6), range(10)):
...     print(i, j)
... 
2 0
3 1
4 2
5 3
None 4
None 5
None 6
None 7
None 8
None 9
>>> for letter1, letter2 in zip_longest('ABCD', 'EF', fillvalue='.'):
...     print(letter1, letter2)
... 
A E
B F
C .
D .
```

##### `product`

`product` calcule le produit cartésien entre plusieurs itérables, c'est-à-dire qu'il produit toutes les combinaisons d'éléments possibles.

```pycon
>>> from itertools import product
>>> for i, c in product(range(5), 'ABC'):
...     print(i, c)
... 
0 A
0 B
0 C
1 A
1 B
1 C
2 A
2 B
2 C
3 A
3 B
3 C
4 A
4 B
4 C
```

Cela revient à écrire des boucles `for` imbriquées tout en économisant des niveaux d'indentation.
L'exemple précédent est ainsi équivalent au code suivant.

```python
for i in range(5):
    for c in 'ABC':
        print(i, c)
```

Le module propose d'autres fonctions combinatoires que je vous invite à regarder.

##### Recettes

En plus de donner des explications et exemples pour chacune de ses fonctions, la documentation du module `itertools` [fournit aussi quelques « recettes »](https://docs.python.org/fr/3/library/itertools.html#itertools-recipes).

Il s'agit de fonctions qui répondent à des besoins trop particuliers pour être vraiment intégrées au module.
Les recettes sont là pour que vous les repreniez dans votre code et que vous les adaptiez à votre convenance.
