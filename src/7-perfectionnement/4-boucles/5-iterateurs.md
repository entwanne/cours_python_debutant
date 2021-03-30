### Itérateurs

#### Itérables et itérateurs

Depuis plusieurs chapitres j'utilise le terme d'itérables pour qualifier les objets qui peuvent être parcourus à l'aide d'une boucle `for`, mais qu'en est-il ?
On a vu qu'il eistait un grand nombre d'itérables, tels que les chaînes de caractères, les listes, les _range_, les dictionnaires, les fichiers, etc.

Il y en a d'autres encore et l'on en a vus plus récemment dans ce chapitre : les retours des fonctions `enumerate` ou `zip` sont aussi des itérables.
Mais si on les regarde de plus près, on voit qu'ils sont un peu particuliers.

```python
>>> enumerate('abcde')
<enumerate object at 0x7f30749e0240>
>>> zip('abc', 'def')
<zip object at 0x7f30749e02c0>
```

Ou plutôt on ne voit pas grand chose justement, ces objets sont assez intrigants.
On sait qu'ils sont itérables, on l'a vu plus tôt, et on peut donc se servir de cette propriété pour les transformer en liste si c'est ce qui nous intéresse.

```python
>>> list(enumerate('abcde'))
[(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')]
>>> list(zip('abc', 'def'))
[('a', 'd'), ('b', 'e'), ('c', 'f')]
```

Mais ce qui est plus étonnant c'est qu'on ne peut itérer dessus qu'une seule fois.

```python
>>> values = enumerate('abcde')
>>> for v in values:
...     print(v)
... 
(0, 'a')
(1, 'b')
(2, 'c')
(3, 'd')
(4, 'e')
>>> for v in values:
...     print(v)
...
```

On constate le même comportement avec la conversion en liste.

```
>>> values = zip('abc', 'def')
>>> list(values)
[('a', 'd'), ('b', 'e'), ('c', 'f')]
>>> list(values)
[]
```

Une fois parcourus une première fois, il n'est plus possible d'itérer à nouveau sur leurs valeurs.
Contrairement à d'autres itérables comme les listes ou les _ranges_ que l'on parcourt autant de fois que l'on veut.

En fait, ces objets _enumerate_ et _zip_ ne sont pas seulement des itérables, ils sont des itérateurs.
Un itérateur peut se voir comme un curseur qui se déplace le long d'un itérable, et qui logiquement se consume à chaque étape.
Ici l'objet _enumerate_ est donc un itérateur le long de notre chaîne `'abcde'`.

La fonction `next` en Python permet de récupérer la prochaine valeur d'un itérateur.
Elle prend l'itérateur en argument et renvoie la valeur pointée par le curseur tout en le faisant avancer.
Puisque l'itérateur avance, le retour de la fonction sera différent à chaque appel.

```python
>>> values = enumerate('abcde')
>>> next(values)
(0, 'a')
>>> next(values)
(1, 'b')
>>> next(values)
(2, 'c')
```

En fin de parcours, l'itérateur lève une exception `StopIteration` pour signaler que l'itération est terminée.

```python
>>> next(values)
(3, 'd')
>>> next(values)
(4, 'e')
>>> next(values)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

On ne peut alors pas revenir en arrière : une fois notre itérateur parcouru il est entièrement consumé.
C'est pourquoi il n'est pas possible de faire deux `for` à la suite sur un même objet `enumerate` ou `zip`, ils sont à usage unique.

Mais ils se basent sur des itérables réutilisables que sont les chaînes de caractères, listes ou autres : on peut donc à nouveau appeler `enumerate` pour obtenir un itérateur tout neuf et recommencer à boucler.

```python
>>> values = 'abcde'
>>> for v in enumerate(values):
...     print(v)
... 
(0, 'a')
(1, 'b')
(2, 'c')
(3, 'd')
(4, 'e')
>>> for v in enumerate(values):
...     print(v)
... 
(0, 'a')
(1, 'b')
(2, 'c')
(3, 'd')
(4, 'e')
```

#### Fonctions `map` et `filter`

En évoquant les outils d'itération plus tôt, j'ai volontairement omis les fonctions `map` et `filter`.
Parce que leurs fonctionnalités sont couvertes par les listes en intension et parce qu'elles renvoient des itérateurs.

`map` et `filter` sont issues de la programmation fonctionnelle et servent respectivement à convertir et à filtrer les données d'un itérable.

`map` prend en arguments une fonction et un itérable, et applique la fonction à chaque élément de l'itérable , renvoyant un itérateur sur les résultats.

```python
>>> values = [1.3, 2.5, 3.8, 4.2]
>>> map(round, values)
<map object at 0x7f4ae2db16a0>
>>> list(map(round, values))
[1, 2, 4, 4]
```

Cela revient donc à utiliser la liste en intension suivante.

```python
>>> [round(v) for v in values]
[1, 2, 4, 4]
```

`filter` est le pendant pour le filtrage des éléments.
Ici le premier argument est une fonction utilisée comme prédicat : l'élément est conservé si le prédicat et vrai et ignoré sinon.

```python
>>> def greater_than_two(n):
...     return n >= 2
... 
>>> list(filter(greater_than_two, values))
[2.5, 3.8, 4.2]
```

Ici, la liste en intension équivalente serait la suivante.

```python
>>> [v for v in values if v >= 2]
[2.5, 3.8, 4.2]
```

`map` et `filter` existaient avant les listes en intension et sont moins utilisées aujourd'hui, surtout lorsqu'il s'agit de les transformer en listes.
Elles restent parfois utilisées quand on n'attend rien de plus qu'un itérateur, par exemple pour fournir en argument à une autre fonction.

C'est le cas de `str.join` qui attend un itérable de chaînes de caractères et nécessite donc que les données soient converties en chaînes, ce que permet `map`.

```python
>>> ', '.join(map(str, values))
'1.3, 2.5, 3.8, 4.2'
```

#### Itérateurs infinis

Comme je disais, un itérateur ne représente qu'un curseur, il a donc une empreinte très faible en mémoire.
Mieux encore, il n'a même pas besoin de s'appuyer sur des données qui existent déjà, celles-ci peuvent être générées à la volée lors du parcours.

C'est déjà le principe des objets _range_ qui occupent très peu d'espace : tous les nombres de l'intervalle ne sont pas stockés en mémoire à la création du _range_, ils sont simplement calculés pendant l'itération et disparaissent après.

On peut pousser le concept plus loin et itérer sur des données qui ne pourraient jamais tenir dans la mémoire de l'ordinateur, des données infinies.
C'est le cas des itérateurs que nous allons voir ici, ils ne se terminent jamais.  
Ces itérateurs infinis sont tirés du module `itertools`.

Le plus simple d'entre tous c'est `count`, qui permet de compter de 1 en 1.

```python
>>> from itertools import count
>>> numbers = count()
>>> next(numbers)
0
>>> next(numbers)
1
>>> next(numbers)
2
```

À quoi cela peut-il servir ? C'est très pratique pour générer des identifiants uniques puisque chaque appel à `next` renverra un nombre différent.

```python
>>> id_seq = count()
>>> def new_event():
...     return {'id': next(id_seq), 'type': 'monstre', 'message': 'Un pythachu sauvage apparaît'}
... 
>>> new_event()
{'id': 0, 'type': 'monstre', 'message': 'Un pythachu sauvage apparaît'}
>>> new_event()
{'id': 1, 'type': 'monstre', 'message': 'Un pythachu sauvage apparaît'}
>>> new_event()
```

Cela peut être aussi utile mathématiquement, pour simplement calculer un seuil à partir duquel une propriété est vraie.

```python
>>> for i in count():
...     if 2**i > 1000:
...         break
... 
>>> i
10
```

On sait ainsi que $2^{10}$ est la première puissance de 2 à être supérieur à 1000.

On notera que `count` peut prendre deux arguments : le premier est le nombre de départ (0 par défaut) et le second est le pas (1 par défaut).

```python
>>> numbers = count(1, 2)
>>> next(numbers)
1
>>> next(numbers)
3
>>> next(numbers)
5
```

Un autre itérateur infini est `repeat`, qui répète simplement en boucle le même élément.

```python
>>> from itertools import repeat
>>> values = repeat('hello')
>>> next(values)
'hello'
>>> next(values)
'hello'
```

On pourra le voir utiliser dans des `zip` pour simuler une séquence de même longueur qu'une autre.

```python
>>> def additions(seq1, seq2):
...     for i, j in zip(seq1, seq2):
...         print(f'{i} + {j} = {i+j}')
... 
>>> additions(range(10), repeat(5))
0 + 5 = 5
1 + 5 = 6
2 + 5 = 7
3 + 5 = 8
4 + 5 = 9
5 + 5 = 10
6 + 5 = 11
7 + 5 = 12
8 + 5 = 13
9 + 5 = 14
```

`repeat` peut aussi prendre un argument qui indique le nombre de répétitions à effectuer, auquel cas il ne sera plus infini.

```python
>>> list(repeat('hello', 5))
['hello', 'hello', 'hello', 'hello', 'hello']
```

Dans le même genre on trouve enfin `cycle` pour boucler (indéfiniment) sur un même itérable.

```python
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

```python
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

#### Fonction `iter`

Pour terminer ce chapitre je voudrais vous parler d'`iter`, une fonction qui renvoie un simple itérateur sur l'itérable donné en argument.
Un nouvel itérateur est construit et renvoyé à chaque appel sur l'itérable.

```python
>>> values = [0, 1, 2, 3, 4]
>>> iter(values)
<list_iterator object at 0x7f3074a28850>
>>> iter(values)
<list_iterator object at 0x7f3074a28bb0>
```

Ces itérateurs sont semblables à nos objets `enumerate`, on peut appeler `next` dessus et récupérer la valeur suivante.
Ils sont donc utiles si l'on souhaite parcourir manuellement un itérable à coups de `next`.

```python
>>> it = iter(values)
>>> next(it)
0
>>> next(it)
1
>>> next(it)
2
```

Et bien sûr on peut aussi les parcourir avec un `for`.
Attention encore, l'itérateur avance pendant le parcours, et le `for` continuera donc l'itération à partir d'où il se trouve.

```python
>>> for v in it:
...     print(v)
... 
3
4
>>> for v in it:
...     print(v)
... 
```

Les itérateurs étant des itérables, il est possible de les donner à leur tour à `iter`.
La fonction renverra alors simplement le même itérateur.

```python
>>> it
<list_iterator object at 0x7f3074a21070>
>>> iter(it)
<list_iterator object at 0x7f3074a21070>
```
