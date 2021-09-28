### Arguments variadiques

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
>>> def print_args(*args):
...     print(args)
... 
>>> print_args()
()
>>> print_args(1)
(1,)
>>> print_args(1, 2, 3)
(1, 2, 3)
```

`args` est ici un nom complètement arbitraire (mais très couramment utilisé) pour nommer cette liste, et n'importe quel autre nom fonctionnerait tout aussi bien.
C'est le `*` placé avant qui a pour effet de récupérer les arguments et non le nom donné au paramètre.

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
>>> print_args(foo='bar')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: print_args() got an unexpected keyword argument 'foo'
```

En effet, comment un tuple d'arguments pourrait représenter nos arguments nommés ?  
Mais il existe une autre syntaxe pour récupérer les arguments nommés, sous forme d'un dictionnaire cette fois : `**kwargs`.
`kwargs` pour *keyword arguments* (arguments nommés) car il ne pourra récupérer que les arguments qui sont explicitement nommés.
Là encore le nom du paramètre n'est qu'une convention.

```python
>>> def print_args(*args, **kwargs):
...     print(args, kwargs)
... 
>>> print_args()
() {}
>>> print_args(3, 5, foo='bar', toto='tata')
(3, 5) {'foo': 'bar', 'toto': 'tata'}
```

Le paramètre spécial `**kwargs` ne peut se placer que tout à la fin de la liste des paramètres puisqu'il récupère les arguments qui n'ont pas été attrapés par les paramètres précédents.
`*args` quant à lui peut se placer à peu près où vous le souhaitez (avant `**kwargs`) mais souvenez-vous qu'il attrape tous les arguments positionnels, donc les paramètres situés après ne pourront récupérer que des arguments nommés.

```python
>>> def print_args(foo, *args, bar, **kwargs):
...     print(foo, args, bar, kwargs)
...
>>> print_args(1, 2, 3, bar=4, baz=5)
1 (2, 3) 4 {'baz': 5}
```

Dans cet exemple, il n'est pas possible de fournir un argument positionnel au paramètre `bar`.
`bar` est ce qu'on appelle un paramètre _keyword-only_ (nommé uniquement).

#### Opérateur _splat_

L'opérateur `*` utilisé dans la liste des paramètres est appelé _splat_, et ce n'est pas sa seule utilisation.

Il permet en effet aussi de réaliser l'opération inverse, celle de transmettre à une fonction les éléments d'une liste (ou autre itérable) comme arguments positionnels différents.

```python
>>> def addition(a, b):
...     return a + b
... 
>>> addition(*[1, 2])
3
>>> args = [1, 2]
>>> addition(*args)
3
```

`addition(*[1, 2])` est ainsi strictement équivalent à `addition(1, 2)`.

Et on voit que le _splat_ du côté de l'appel n'est pas lié au _splat_ dans la définition des paramètres puisque notre fonction n'accepte pas d'arguments variadiques ici.
Mais les deux sont bien sûr compatibles.

```python
>>> print_args(*[1, 2, 3])
(1, 2, 3) {}
```

Contrairement aux paramètres, rien ne nous empêche ici d'utiliser plusieurs _splats_ pour envoyer des arguments de plusieurs listes, ni d'utiliser des arguments « normaux » en plus de nos listes.

```python
>>> print_args(1, 2, *[3, 4, 5], 6)
(1, 2, 3, 4, 5, 6) {}
>>> print_args(*[1, 2, 3], 4, *[5, 6])
(1, 2, 3, 4, 5, 6) {}
```

De manière équivalente, `**` est l'opérateur _double-splat_ et peut s'utiliser lors d'un appel pour transmettre le contenu d'un dictionnaire comme arguments nommés.
Il est alors nécessaire que les clés du dictionnaire soient des chaînes de caractères (un nom de paramètre ne peut pas être autre chose qu'une chaîne).

```python
>>> print_args(**{'foo': 0, 'bar': 'baz'})
() {'foo': 0, 'bar': 'baz'}
```
