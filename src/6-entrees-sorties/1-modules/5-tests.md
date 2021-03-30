### Modules de tests

Revenons-en à notre TP.
Il serait intéressant dans un premier temps de séparer les tests du reste du code.
Ils n'ont en effet pas de raison particulière d'être placés là.

Dans un fichiers `tests.py`, on va donc placer toutes les fonctions `test_*`.
Mais ce module `tests` n'aura par défaut pas accès aux fonctions à tester, il va donc nous falloir les importer.
Au début du module `tests`, on placera donc les lignes d'import suivantes.

```python
from game import ...
from game import ...
```

Aussi, vous vous souvenez de notre fonction pour réunir tous les tests ?
Elle n'a maintenant plus lieu d'être, étant donné que nous sommes dans un module à part nous savons que son code ne sera pas exécuté par erreur.

On peut donc placer les appels des fonctions de tests à la toute fin de notre module.
Enfin pas tout à fait, on va inclure nos appels dans un bloc conditionnel `if __name__ == '__main__':`.

```python
if __name__ == '__main__':
    test_...()
    test_...()
```

Cette ligne obscure permet de savoir si on exécute directement le module ou si on l'importe.
En effet, la variable spéciale `__name__` contient le nom du module.
Dans le cas où le module est exécuté directement par Python (`python tests.py`), ce nom vaudra `'__main__'` (il s'agira sinon de `'tests'` lors d'un import).

Par cette ligne, nous nous assurons donc que les fonctions de tests ne seront pas exécutées lors d'un import.
Ce n'est pas très important pour un module de tests qui n'a pas vocation à être importé, mais ça reste un outil pratique pour qu'un script soit importable.
C'est donc toujours une bonne habitude à prendre.

```python
print('A')

if __name__ == '__main__':
    print('B')
```
Code: foo.by

```bash
$ python foo.by
A
B
```

```python
>>> import foo
A
```
