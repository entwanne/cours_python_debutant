### Unittest

_Unittest_ est le module de la bibliothèque standard dédié à l'écriture de tests.
Je ne vous en ai pas parlé jusqu'ici parce que celui-ci nécessite l'écriture de classes, qui ne sont abordées que dans le cours sur [la programmation orientée objet en Python](https://zestedesavoir.com/tutoriels/1253/la-programmation-orientee-objet-en-python/).

On peut en apprendre plus [sur la page de documentation du module](https://docs.python.org/fr/3.8/library/unittest.html) et on découvre notamment quelle structure respecter pour écrire une suite de tests.

```python
import unittest

from operations import addition, soustraction


class TestOperations(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(3, 5), 8)
        self.assertEqual(addition(1, 0), 1)
        self.assertEqual(addition(5, -8), -3)

    def test_soustraction(self):
        self.assertEqual(soustraction(8, 5), 3)
        self.assertEqual(soustraction(5, 8), -3)
        self.assertEqual(soustraction(1, 0), 1)
        self.assertEqual(soustraction(3, -5), 8)
```
Code: `test_operations.py`

Il faut ainsi écrire une classe `TestFooBar`[^nommage] que l'on indique comme étant un cas de test (via `unittest.TestCase` entre parenthèses, qui signifie que notre classe dérive de `TestCase`) à l'interieur de laquelle on place nos fonctions de tests.

[^nommage]: Il est coutume d'utiliser un style _CamelCase_, où les différents mots qui forment le nom sont écrits avec une majuscule et ne sont pas séparés d'_underscores_.

Ces fonctions possèdent un paramètre spécial `self` qui sera fourni automatiquement.
Cet objet `self` possède différentes méthodes, notamment `assertEqual` pour vérifier que les deux arguments sont égaux, `assertTrue` qui revient à faire une assertion et `assertFalse` pour l'inverse (vérifier qu'une expression est fausse).

On peut exécuter un fichier de tests à l'aide de la commande `python -m unittest`.

```sh
% python -m unittest test_operations.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

En cas d'erreur(s), celles-ci sont aussi signalées par le programme.

```sh
% python -m unittest test_operations.py
F.
======================================================================
FAIL: test_addition (test_operations.TestOperations)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/antoine/test_operations.py", line 10, in test_addition
    self.assertEqual(addition(5, -8), 3)
AssertionError: -3 != 3

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)
```
