### Bloc with

Nous avons vu les gestionnaires de contexte (blocs `with`) plus tôt, quand nous apprenions à utiliser les fichiers.
Permettant de gérer l'acquisition/libération de ressources, ils sont en fait une autre manière de traiter les exceptions en Python.

```python
with open('hello.txt') as f:
    print(int(f.read()))
```

Dans le code précédent, même si la ligne 2 échoue (si le fichier ne contient pas un nombre), le fichier sera correctement fermé (Python appellera `f.close()` pour nous).  
Car c'est ce que garantit le bloc `with` : assurer que le code de libération de la ressource sera toujours appelé.

En cela, il s'apperente à un `try` / `finally`, puisqu'il s'agit d'exécuter une action pour acquérir la ressource (avant le `try`) puis pour la libérer (dans le `finally`).  
Mais on n'a pas à faire d'appel explicite à `f.close()` pour fermer notre fichier, tout cela est fait de façon transparente.

Le bloc précédent est alors équivalent à :

```python
f = open('hello.txt')
try:
    print(int(f.read())
finally:
    f.close()
```

#### Supprimer une exception

En plus de ça, le bloc `with` peut aussi influer sur la remontée d'exceptions, et donc stopper une exception qui serait levée à l'intérieur du bloc.

C'est ce que permet facilement le gestionnaire de contexte `suppress` du module `contextlib` de la bibliothèque standard.  
Il s'utilise en précisant les types d'erreurs que l'on veut voir supprimés.

```python
>>> from contextlib import suppress
>>> with suppress(ValueError):
...     print(int('abc'))
...
```

Plusieurs types peuvent être donnés en arguments pour tous les supprimer.

```python
>>> with suppress(ValueError, TypeError):
...     print(1 + 'b')
...
```

Il ne permet pas de traitement plus avancé que ça, et se limite bien sûr à n'attraper que les erreurs des types spécifiés.

```python
>>> with suppress(ValueError):
...     print(1 + 'b')
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```
