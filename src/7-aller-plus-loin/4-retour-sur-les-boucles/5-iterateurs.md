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

* `map` & `filter`

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

* Itérateurs infinis (`itertools.count`)

#### Fonction `iter`

Enfin, `iter` est une fonction qui renvoie un simple itérateur sur l'itérable donné en argument.
Un nouvel itérateur est construit et renvoyé à chaque appel sur l'itérable.

```python
>>> values = [0, 1, 2, 3, 4]
>>> iter(values)
<list_iterator object at 0x7f3074a28850>
>>> iter(values)
<list_iterator object at 0x7f3074a28bb0>
```

Ces itérateurs sont semblables à nos objets `enumerate`, on peut appeler `next` dessus et récupérer la valeur suivante, on peut les parcourir et les consommer avec un `for`.

```python
>>> it = iter(values)
>>> next(it)
0
>>> for v in it:
...     print(v)
... 
1
2
3
4
>>> for v in it:
...     print(v)
... 
```

Les itérateurs étant des itérables, il est possible de les donner à `iter`.
La fonction renverra alors simplement le même itérateur.

```python
>>> it
<list_iterator object at 0x7f3074a21070>
>>> iter(it)
<list_iterator object at 0x7f3074a21070>
```
