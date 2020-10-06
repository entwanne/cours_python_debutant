### Arguments variadiques

* `*args`, `**kwargs`

Vous pensiez avoir tout vu sur les arguments ? Que nenni !
Certaines fonctions que nous utilisons couramment exploitent encore des fonctionnalités inconnues.

Si je vous demandais par exemple de recoder la fonction `print`, comment procéderiez-vous ?
Pour rappel, la fonction permet de recevoir un nombre variable d'arguments.

```python
>>> print()

>>> print(1)
1
>>> print(1, 2, 3)
1 2 3
```

On pourrait essayer de placer plusieurs paramètres optionnels à la suite mais on ne couvrirait jamais tous les cas : si l'on créait une fonction avec 10 paramètres optionnels il ne serait pas possible de l'appeler avec 11 arguments.

Il doit donc y avoir autre chose, une manière de gérer un nombre variable d'arguments : les arguments variadiques !
L'idée derrière ce nom est simplement de récupérer les arguments positionnels sous forme d'une liste (ou plutôt d'un tuple).  
Et cela se fait avec une syntaxe plutôt simple en Python, il suffit de placer `*args` dans la liste des paramètres de la fonction.
On obtiendra ainsi un tuple `args` contenant ces arguments.

```python
>>> def get_args(*args):
...     print(args)
... 
>>> get_args()
()
>>> get_args(1)
(1,)
>>> get_args(1, 2, 3)
(1, 2, 3)
```

`args` est ici un nom complètement arbitraire (mais très couramment utilisé) pour nommer cette liste, et n'importe quel autre nom fonctionnerait tout aussi bien.
C'est le `*` placé avant qui a pour effet de récupérer les arguments et non le nom donné au paramètres.

Avec `*args`, tous les arguments sont ainsi optionnels.
Mais il est aussi possible de préciser d'autres paramètres avant `*args`, qui ne récupérera alors que le reste des arguments : cela permet alors de conserver des arguments obligatoires.

```python
>>> def my_sum(first, *args):
...     for n in args:
...         first += n
...     return first
... 
>>> my_sum(1)
1
>>> my_sum(1, 2, 3, 4, 5)
15
>>> my_sum()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: my_sum() missing 1 required positional argument: 'first'
```

Si vous testez un peu, vous remarquerez que cette syntaxe est valide pour les arguments positionnels mais pas les arguments nommés.

```python
>>> get_args(foo='bar')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: get_args() got an unexpected keyword argument 'foo'
```

En effet, comment un tuple d'arguments pourrait représenter nos arguments nommés ?  
Mais il existe une autre syntaxe pour récupérer les arguments nommés, sous forme d'un dictionnaire cette fois : `**kwargs`.
`kwargs` pour *keyword-only arguments* (arguments uniquement nommés) car il ne pourra récupérer que les arguments qui sont explicitement nommés.
Là encore le nom du paramètre n'est qu'une convention.

```python
>>> def get_args(*args, **kwargs):
...     print(args, kwargs)
... 
>>> get_args()
() {}
>>> get_args(3, 5, foo='bar', toto='tata')
(3, 5) {'foo': 'bar', 'toto': 'tata'}
```

Le paramètre spécial `**kwargs` ne peut se placer que tout à la fin de la liste des paramètres puisqu'il récupère les arguments qui n'ont pas été attrapés par les paramètres précédents.
`*args` quant à lui peut se placer à peu près où vous les souhaitez (avant `**kwargs`) mais souvenez-vous qu'il attrape tous les arguments positionnels, donc les paramètres situés après ne pourront récupérer que des arguments nommés (d'où le nom de paramètre uniquement nommé).

```python
>>> def get_args(foo, *args, bar, **kwargs):
...     print(foo, args, bar, kwargs)
...
>>> get_args(1, 2, 3, bar=4, baz=5)
1 (2, 3) 4 {'baz': 5}
```

* _unpacking_

Ce chapitre lui-même ne vous présente pas toutes les possibilités des arguments et paramètres en Python, aussi je vous invite à consulter les liens suivants :

*
