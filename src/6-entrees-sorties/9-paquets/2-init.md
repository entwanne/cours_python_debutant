### Fichier __init__.py

Comme je le disais précédemment, le code des modules n'est pas directement chargé quand on importe le paquet.
Qu'est-ce qui se passe alors quand on fait un `import operations` ?

À notre niveau pas grand chose en fait. Python identifie où se trouvent les fichiers du paquet `operations` et instancie un module vide qu'il nous renvoie.

Mais dans les faits, il cherche un fichier `__init__.py` à l'intérieur du paquet pour l'exécuter.
C'est en fait ce fichier qui contient le code du paquet à proprement parler : tout ce qui sera présent dedans sera exécuté lors d'un `import operations`.

```python
print('Hello')
```
Code: `operations/__init__.py`

```python
>>> import operations
Hello
```

[[w]]
| Attention au nommage du fichier, il faut bien deux *underscores* de part et d'autre de `init`.

Bien sûr cet exemple n'est pas très utile, mais ce fichier `__init__.py` peut aussi nous servir à charger directement le code des modules du paquet.  
Par exemple on peut y importer nos fonctions `addition` et `soustraction` pour les rendre accessibles plus facilement.

```python
from .addition import addition
from .soustraction import soustraction
```
Code: `operations/__init__.py`

```python
>>> import operations
>>> operations.addition(3, 5)
8
>>> from operations import soustraction
>>> soustraction(8, 5)
3
```

[[i]]
| Avant Python 3.3, le fichier `__init__.py` était nécessaire pour que Python considère le répertoire comme un paquet.
| Ce n'est plus le cas aujourd'hui mais ce fichier reste toutefois utile pour indiquer à Python que tout le code du paquet se trouve dans ce même répertoire.
|
| Prenez ainsi l'habitude de toujours avoir un fichier `__init__.py` (même vide) dans vos paquets, cela pourrait vous éviter certaines déconvenues.
