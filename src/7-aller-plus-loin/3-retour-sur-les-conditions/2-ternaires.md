### Expressions conditionnelles

Et c'est heureusement possible grâce aux expressions conditionnelles.
Comme leur nom l'indique, ce sont des conditions sous forme d'expressions.

Elles reprennent les mêmes mots-clés `if` et `else` mais sans construire de bloc, leur syntaxe est la suivante :

```python
valeur if condition else autre_valeur
```

Cette expression vaut `valeur` si `condition` est vraie et `autre_valeur` sinon.

```python
>>> 'good' if 5 + 3 == 8 else 'bad'
'good'
>>> 'good' if 5 + 3 == 7 else 'bad'
'bad'
```

Étant une expression, elle doit toujours avoir une valeur, c'est pourquoi le `else` est obligatoire dans tous les cas.

Les expressions conditionnelles permettent d'avoir un code plus concis lorsque les conditions à traiter sont simples.

```python
>>> x = 3
>>> y = 5
>>> z = (2 * x if x < 10 else x) / (y if y else 1)
```

Sans elles, il nous aurait fallu écrire le code suivant :

```python
>>> if x < 10:
...     tmp1 = 2 * x
... else:
...     tmp1 = x
... 
>>> if y:
...     tmp2 = y
... else:
...     tmp2 = 1
... 
>>> z = tmp1 / tmp2
```

Elles sont souvent utilisées aussi lors d'appels de fonctions ou méthodes.

```python
>>> sep = None
>>> 'a,b,c'.split(sep if sep is not None else ',')
['a', 'b', 'c']
```

On parle aussi de « conditions ternaires » pour qualifier les expressions conditionnelles, car c'est un opérateur à 3 opérandes (`op1 if op2 else op3`).
