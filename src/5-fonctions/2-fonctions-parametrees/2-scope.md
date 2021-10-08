### Espace de noms

Chaque fonction comporte son propre espace de noms (ou scope), c'est-à-dire une entité qui contient toutes les définitions de variables.
Ainsi, une variable définie à l'intérieur d'une fonction n'existe que dans celle-ci.

```python
>>> def f():
...     a = 5
...     print(a)
...
>>> a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
```

Que ce soit avant ou après l'appel de la fonction, la variable `a` n'existe pas dans l'espace de noms principal (ou global).

```python
>>> f()
5
>>> a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
```
Il en est de même pour les paramètres qui sont au final des variables comme les autres au sein de la fonction.

```python
>>> def f(x):
...     print(x)
... 
>>> f(5)
5
>>> x
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'x' is not defined
```

Il est en revanche possible pour une fonction d'accéder aux variables définies à l'extérieur de celle-ci.

```python
>>> value = 42
>>> 
>>> def f():
...     print(value)
... 
>>> f()
42
```

Ce qui implique que le comportement de la fonction change si la valeur de la variable est modifiée.

```python
>>> value = 13
>>> f()
13
```

Mais les espaces de noms extérieur et intérieur à la fonction sont bien deux scopes distincts.
Deux variables de même nom peuvent exister dans des scopes différents sans qu'elles n'interfèrent entre-elles.

```python
>>> x = 0
>>> 
>>> def f():
...     x = 1
...     print(x)
... 
>>> x
0
>>> f()
1
>>> x
0
```

Ce qui implique qu'il n'est pas possible de redéfinir une variable extérieure à la fonction (du moins pas de cette manière) car Python croira toujours que l'on cherche à définir une variable locale.

Cela peut poser problème si l'on essaie dans une fonction d'accéder à une variable avant de la redéfinir.
En effet, Python ne saura pas si l'on souhaite récupérer une variable extérieure portant ce nom (puisqu'elle n'aura pas encore été définie dans le scope local) ou en définir une nouvelle.
Il lèvera donc une erreur pour éviter toute ambigüité.

```python
>>> def f():
...     print(x)
...     x = 1
... 
>>> f()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in f
UnboundLocalError: local variable 'x' referenced before assignment
```
