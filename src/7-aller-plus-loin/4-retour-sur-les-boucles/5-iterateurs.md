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
Ils sont itérables bien sûr, nous l'avons montré plus tôt, mais on peut justement voir qu'il ne le sont qu'une fois.

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

Une fois parcourus, il n'est plus possible d'itérer sur leurs valeurs.
Contrairement aux listes par exemple que l'on parcourt autant de fois que l'on veut.

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

#### Fonction `iter`

`iter` est une fonction qui renvoie un simple itérateur sur l'itérable donné en argument.
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

* `iter(callable, sentinel)`

* `map` & `filter`
* Itérateurs infinis (`itertools.count`)
