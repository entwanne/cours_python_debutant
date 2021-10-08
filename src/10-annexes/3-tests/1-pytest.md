### Pytest

_Pytest_ est une bibliothèque tierce fréquemment utilisée pour l'écriture de tests en Python, par la simplicité avec laquelle elle permet de décrire les cas de tests.

Premièrement vous pouvez installer _Pytest_ avec la commande `pip install pytest`.  
Celle-ci installe l'utilitaire `pytest` dans l'environnement courant.

Ensuite, il suffit d'utiliser la commande `pytest`, seule ou accompagnée de fichiers ou répertoires en arguments (par défaut il explorera le répertoire courant).
_Pytest_ se charge d'identifier les fichiers de tests, qui sont les fichiers Python préfixés de `test_`.  
À l'intérieur de ces fichiers, les fonctions avec ce même préfixe sont identifiées comme des fonctions de tests.

Ainsi, les modules de tests que vous nous avons écrits précédemment, contenant des fonctions de tests formées d'assertions, sont déjà compatibles avec _Pytest_.

```python
from operations import addition, soustraction


def test_addition():
    assert addition(3, 5) == 8
    assert addition(1, 0) == 1
    assert addition(5, -8) == -3


def test_soustraction():
    assert soustraction(8, 5) == 3
    assert soustraction(5, 8) == -3
    assert soustraction(1, 0) == 1
    assert soustraction(3, -5) == 8
```
Code: `test_operations.py`

```sh
% pytest test_operations.py
======================== test session starts ========================
platform linux -- Python 3.9.7, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: /home/antoine
collected 2 items


test_operations.py ..                                          [100%]

========================= 2 passed in 0.01s =========================
```

Tout se passe bien, nos fonctions valident les tests !
En cas d'erreur, _Pytest_ s'arrête à la première assertion fausse de la fonction et affiche un rapport explicite du problème.

```sh
======================== test session starts ========================
platform linux -- Python 3.9.7, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: /home/antoine
collected 2 items
  

test_operations.py F.                                          [100%]

============================== FAILURES =============================
___________________________ test_addition ___________________________

    def test_addition():
        assert addition(3, 5) == 8
        assert addition(1, 0) == 1
>       assert addition(5, -8) == 3
E       assert -3 == 3
E        +  where -3 = addition(5, -8)

test_operations.py:7: AssertionError
====================== short test summary info ======================
FAILED test_operations.py::test_addition - assert -3 == 3
==================== 1 failed, 1 passed in 0.02s ====================
```

_Pytest_ permet d'aller plus loin que ça, et fournit des outils pour paramétrer facilement nos tests (générer différentes valeurs en entrée), abstraire les entrées et sorties standards (pour tester des fonctions qui utiliseraient `print` ou `input`) et bien d'autres encore que vous découvrirez [dans sa documentation](https://docs.pytest.org/).
