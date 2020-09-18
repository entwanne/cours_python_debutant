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

On notera que

* Arguments nommés des builtins (key/reverse sur sorted, etc.)
* `zip`
* Module `itertools`
* Recettes d'`itertools`
