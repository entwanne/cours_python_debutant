### Arguments positionnels et nommés

Nous n'avons vu pour le moment que les arguments positionnels.
C'est-à-dire dont l'association avec les paramètres se fait par la position de l'argument (n-ième argument pour le n-ième paramètre).

Mais il est aussi possible de spécifier des arguments nommés, où la correspondance avec le paramètre se fait par le nom.

```pycon
>>> def f(a, b):
...     print(a, b)
... 
>>> f(a=1, b=2)
1 2
```

Dans ce contexte, il est possible d'inverser l'ordre des paramètres (puisqu'il n'importe pas pour les identifier).

```pycon
>>> f(b=2, a=1)
1 2
```

Il est possible de passer à la fois des arguments positionnels et nommés, mais les positionnels devront toujours se trouver avant (puisque c'est leur position qui détermine le paramètre).

```pycon
>>> f(1, b=2)
1 2
>>> f(b=2, 1)
  File "<stdin>", line 1
SyntaxError: positional argument follows keyword argument
```

Un paramètre ne peut toujours correspondre qu'à un seul argument, Python lèvera donc une erreur s'il reçoit deux arguments (un positionnel et un nommé) pour un même paramètre.

```pycon
>>> f(1, 2, b=3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: f() got multiple values for argument 'b'
```

Ou si un argument nommé est répété.

```pycon
>>> f(1, b=2, b=3)
  File "<stdin>", line 1
SyntaxError: keyword argument repeated
```

De la même manière, il n'est pas possible de préciser un argument positionnel pour le second paramètre sans en préciser pour le premier (puisque le premier argument positionnel est forcément destiné au premier paramètre).  
Ainsi, dans l'appel suivant Python considèrera qu'il reçoit l'argument positionnel `2` pour le paramètre `a` (le premier) et donc lèvera aussi une erreur.

```pycon
>>> f(2, a=1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: f() got multiple values for argument 'a'
```
