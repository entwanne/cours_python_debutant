### None

`None` est une valeur particulière en Python, qui représente l'absence de valeur.
On l'a déjà rencontrée sans vraiment y faire attention.

C'est par exemple la valeur renvoyée par les fonctions ou méthodes qui ne renvoient rien.

```python
>>> [].clear()
>>> print([].clear())
None
```

La fonction `print` en elle-même renvoie `None`.

```python
>>> print(print())

None
```

Dans certains traitements, il est parfois utile de savoir si l'on a affaire à `None` ou à une autre valeur.
Pour vérifier ça, on serait tenter si notre valeur est égale à `None` avec un `==`.

Mais `None` est une valeur unique en Python, il n'en existe qu'un (on parle de _singleton_) et on préférera donc utiliser l'opérateur d'idendité : `is`.

```python
>>> None is None
True
>>> [].clear() is None
True
>>> abs(-5) is None
False
```

Il est aussi possible de tester la non-identité avec l'opérateur `is not`.

```python
>>> abs(-5) is not None
True
>>> [].clear() is not None
False
```
