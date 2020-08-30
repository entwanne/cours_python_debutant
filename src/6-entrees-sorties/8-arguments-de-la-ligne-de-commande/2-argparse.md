### Parseur d'arguments

Manipuler `sys.argv` ça va quand on a des arguments simples comme deux nombres ici, mais ça devient vite compliqué pour gérer les options passées à un programme.

En effet, il serait difficile de gérer manuellement les arguments d'un appel tel que `python cmd.py -v -f pdf --foo=bar --foo2 bar2 photo.jpg`.
C'est pourquoi des outils existent pour analyser à votre place les arguments, les valider en fonction de ce qui est attendu, et les classer convenablement.  
Le module `argparse` de la bibliothèque standard propose l'un de ces outils.

`argparse` fournit un type `ArgumentParser` que l'on peut instancier pour obtenir un parseur d'arguments.

```python
import argparse

parser = argparse.ArgumentParser()
```
Code: cmd.py

Des méthodes sont ensuite disponibles sur ce parseur pour le personnaliser et préciser les arguments que l'on attend.  
Notamment la méthode `add_argument` qui permet de demander à gérer un nouvel argument.

Celle-ci accepte de nombreuses options que je ne détaillerai pas ici.
Sachez simplement qu'elle attend en premier le nom voulu pour l'agument.

* Si ce nom est de type `-x` alors elle gèrera l'argument comme `-x VALEUR` lors de l'appel au programme.
* S'il est de type `--abc`, elle gèrera `--abc=VALEUR` et `--abc VALEUR`.

Un paramètre `action` sert à préciser quoi faire de l'argument rencontré.

* `store_const`
* `store_true`

Une valeur par défaut pour l'argument peut être renseignée avec le paramètre `default`.

* `dest`
* `type`

Voilà par exemple comment nous pourrions traiter les arguments présentés pour la commande plus haut.

```python
parser.add_argument('-v', dest='verbose', action='store_true')
parser.add_argument('-f', dest='format', default='text')
parser.add_argument('--foo')
parser.add_argument('--foo2')
parser.add_argument('file')

args = parser.parse_args()
print(args)
```
Code: cmd.py

* Lien vers la documentation
