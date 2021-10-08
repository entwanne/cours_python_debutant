### Parseur d'arguments

Manipuler `sys.argv` ça va quand on a des arguments simples comme deux nombres ici, mais ça devient vite compliqué pour gérer les options passées à un programme.

En effet, il serait difficile de gérer manuellement les arguments d'un appel tel que `python cmd.py -v -f pdf --foo=bar --foo2 42 photo.jpg`.
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
* S'il ne débute pas par un tiret, alors il s'agira d'un argument positionnel du programme.

Un paramètre `action` sert à préciser quoi faire de l'argument rencontré.

* `store_const` permet de simplement stocker la valeur associée à l'argument.
* `store_true` permet de stocker `True` si l'argument est présent et `False` sinon.

Une valeur par défaut pour l'argument peut être renseignée avec le paramètre `default`.

Par défaut, la valeur de l'argument sera stockée dans l'objet résultant sous le nom de l'argument.
Il est cependant possible de choisir un autre nom pour le stockage à l'aide du paramètre `dest`.

Enfin, il est possible d'utiliser le paramètre `type` pour convertir automatiquement la valeur d'un argument vers le type voulu.

Voilà par exemple comment nous pourrions traiter les arguments présentés pour la commande plus haut.

```python
parser.add_argument('-v', dest='verbose', action='store_true')
parser.add_argument('-f', dest='format', default='text')
parser.add_argument('--foo')
parser.add_argument('--foo2', type=int)
parser.add_argument('file')

args = parser.parse_args()
print(args)
print('Verbose:', args.verbose)
print('Format:', args.format)
```
Code: cmd.py

```shell
% python cmd.py -v -f pdf --foo=bar --foo2 42 photo.jpg
Namespace(verbose=True, format='pdf', foo='bar', foo2=42, file='photo.jpg')
Verbose: True
Format: pdf
% python cmd.py doc.odt
Namespace(verbose=False, format='text', foo=None, foo2=None, file='doc.odt')
Verbose: False
Format: text
```

Pour plus d'informations au sujet du module `argparse`, vous pouvez consulter sa page de documentation : <https://docs.python.org/fr/3/library/argparse.html>.
