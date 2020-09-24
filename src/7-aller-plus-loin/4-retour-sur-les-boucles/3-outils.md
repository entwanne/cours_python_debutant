### Outils

Le monde de l'itération est très vaste en Python, les itérables se retrouvent au cœur de nombreux mécanismes.
C'est pourquoi Python propose de base de nombreux outils relatifs à l'itération tels que les fonctions `all` et `any` que l'on a déjà vues.

Vous êtes-vous déjà demandé comment itérer simultanément sur plusieurs listes ou comment répéter une liste ? Ce chapitre est fait pour vous !

#### Fonctions *builtins*

On a déjà vu un certain nombre de *builtins* dans les chapitres précédents, mais il en reste quelques unes très intéressantes que j'ai omises jusqu'ici.

##### `enumerate`

Notamment la fonction `enumerate`, qui prend une liste (ou n'importe quel itérable) et permet d'itérer sur ses valeurs tout en leur associant leur index.
C'est-à-dire que pour chaque valeur on connaîtra la position qu'elle occupe dans la liste.

```python
>>> values = ['abc', 'def', 'ghi']
>>> for i, value in enumerate(values):
...     print(i, ':', value)
... 
0 : abc
1 : def
2 : ghi
```

Cela remplace aisément les constructions à base de `range(len(values))` que l'on voit trop souvent et qui sont à éviter.

```python
>>> for i in range(len(values)):
...     print(i, ':', values[i])
... 
0 : abc
1 : def
2 : ghi
```

On les évite justement parce qu'`enumerate` répond mieux au problème tout en étant plus polyvalent (on peut par exemple itérer sur un fichier), et qu'on a directement accès à la valeur (`value`) sans besoin d'une indirection supplémentaire par le conteneur (`values[i]`).

On notera au passage que la fonction `enumerate` accepte un deuxième argument pour préciser l'index de départ, qui est par défaut de zéro.

```python
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

```python
>>> values = ['abc', 'def', 'ghi']
>>> for value in reversed(values):
...     print(value)
... 
ghi
def
abc
```

La fonction ne modifie pas la séquence initiale (contrairement à la méthode `reverse` des listes).

```python
>>> values
['abc', 'def', 'ghi']
```

#### `sorted`

Dans la même veine on a la fonction `sorted`, semblable à la méthode `sort` des listes mais renvoyant ici une copie.

```python
>>> values = [5, 3, 2, 4, 6, 1, 9, 7, 8]
>>> sorted(values)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> values
[5, 3, 2, 4, 6, 1, 9, 7, 8]
```

On notera que le tri se fait en ordre croissant (les plus éléments d'abord) par défaut, mais la fonction accepte un argument `reverse` pour trier en ordre décroissant (les plus grands d'abord).

```python
>>> sorted(values, reverse=True)
[9, 8, 7, 6, 5, 4, 3, 2, 1]
```

Mieux encore, la fonction propose un paramètre `key` pour pour personnaliser comment seront triés nos éléments.
C'est une fonction qui recevra un élément en paramètre et renverra une valeur (par exemple un nombre), le tri se fera donc suivant l'ordre entre ces valeurs.

Par exemple, le tri par défaut pour les chaînes de caractères est l'ordre lexicographique (plus ou moins équivalent à l'ordre alphabétique).

```python
>>> words = ['zèbre', 'autruche', 'cheval', 'oie']
>>> sorted(words)
['autruche', 'cheval', 'oie', 'zèbre']
```

On pourrait alors préciser une fonction de tri `key=len` pour les trier par taille.

```python
>>> sorted(words, key=len)
['oie', 'zèbre', 'cheval', 'autruche']
```

En effet, la fonction `len` sera appelée pour chaque mot et les mots seront triés suivant le retour de la fonction (en l'occurrence 3, 5, 6 et 8).
Mais il est possible d'utiliser n'importe quelle fonction en tant que clé de tri, tant que cette fonction renvoie quelque chose d'ordonnable.

Voici un autre exemple avec une fonction pour trier les mots dans l'ordre alphabétique mais en commençant par la dernière lettre du mot.

```python
>>> def key_func(word):
...     return word[::-1] # On renvoie le mot à l'envers
... 
>>> sorted(words, key=key_func)
['autruche', 'oie', 'zèbre', 'cheval']
```

Ces deux arguments sont aussi disponibles sur la méthode `sort` des listes.

```python
>>> words.sort(key=len, reverse=True)
>>> words
['autruche', 'cheval', 'zèbre', 'oie']
```

#### `zip`

`zip` est une fonction très pratique de Python, puisqu'elle permet de parcourir simultanément sur plusieurs itérables.
On appelle la fonction en lui fournissant nos itérables en arguments, et l'on itère ensuite sur l'objet qu'elle nous renvoie.  
Les éléments que l'on obtient alors sont des tuples formés des éléments de nos itérables de départ.

```python
>>> for elem in zip(words, 'abcd', range(4)):
...     print(elem)
... 
('autruche', 'a', 0)
('cheval', 'b', 1)
('zèbre', 'c', 2)
('oie', 'd', 3)
```

Il est ainsi possible d'utiliser l'_unpacking_ de Python pour avoir quelque chose de plus explicite.

```python
>>> for word, letter, number in zip(words, 'abcd', range(4)):
...     print(word, letter, number)
... 
autruche a 0
cheval b 1
zèbre c 2
oie d 3
```

`zip` accepte autant d'arguments que l'on souhaite, on peut l'appeler avec deux itérables comme avec dix.

Aussi, il s'arrête dès que l'un des itérables se termine, [...]

```python
```

* Module `itertools`
* Recettes d'`itertools`
