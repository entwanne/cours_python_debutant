### Format INI

Le format INI (*Initialization*) est un format dédié à l'écriture de fichiers de configuration simples.

Il permet de décrire différents paramètres de configuration (sous forme de couples clé-valeur) et de les regrouper en sections.

```ini
[game]
save=game.dat

[window]
title=Mon super jeu
width=800
height=600
```
Code: config.ini

Ainsi une section est définie par un `[nom_de_la_section]` et réunit en son sein toutes les définitions suivantes (de la forme `cle=valeur`).

Toutes les valeurs sont considérées comme des chaînes de caractères et peuvent donc nécessiter une conversion manuelle au cas par cas (on voudra par exemple convertir les valeurs `width` et `height` vers des nombres).

#### Module `configparser`

Python propose une implémentation du format INI via [son module `configparser`](https://docs.python.org/fr/3/library/configparser.html).

##### Lecture

Afin de lire un document INI, il faut au préalable instancier un objet `ConfigParser`.

```pycon
>>> from configparser import ConfigParser
>>> config = ConfigParser()
```

Cet objet possède une méthode `read` qui prend un chemin de fichier en argument et complète la configuration à partir du contenu de ce fichier.

```pycon
>>> config.read('config.ini')
['config.ini']
```

On peut ensuite accéder aux différentes sections de la configuration à l'aide de la méthode `sections` et utiliser l'objet `config` comme un dictionnaire.

```pycon
>>> config.sections()
['game', 'window']
>>> config['game']
<Section: game>
>>> config['window']
<Section: window>
```

Les sections elles aussi sont des objets semblables à des dictionnaires que l'on peut donc manipuler pour accéder aux différentes valeurs.

```pycon
>>> config['game']['save']
'game.dat'
>>> config['window']['height']
'600'
>>> int(config['window']['height'])
600
>>> dict(config['window'])
{'title': 'Mon super jeu', 'width': '800', 'height': '600'}
```

En cas de fichier invalide, la méthode `read` lèvera une exception `configparser.ParsongError`.

```pycon
>>> config.read('invalid.ini')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3.10/configparser.py", line 698, in read
    self._read(fp, filename)
  File "/usr/lib/python3.10/configparser.py", line 1117, in _read
    raise e
configparser.ParsingError: Source contains parsing errors: 'invalid.ini'
	[line  6]: 'width\n'
```

##### Écriture

En écriture, un objet `ConfigParser` se comporte là aussi comme un dictionnaire.

```pycon
>>> config = ConfigParser()
>>> config['game'] = {'save': 'new.dat'}
>>> config['window'] = {}
>>> config['window']['width'] = '200'
```

[[a]]
| Attention, toutes les valeurs renseignées dans la configuration doivent être des chaînes de caractères, sans quoi vous obtiendrez une erreur `TypeError`.

Et l'objet possède une méthode `write` pour écriture le contenu de la configuration dans un fichier précédemment ouvert en écriture.

```python
>>> with open('new.ini', 'w') as configfile:
...     config.write(configfile)
... 
```

```ini
[game]
save = new.dat

[window]
width = 200

```
Code: new.ini

#### Avantages et inconvénients

Le format INI est un format plat (il n'y a pas de structures arborescentes), ce qui est à la fois un avantage et un inconvénient : cela permet de garder des fichiers de configuration simples puisque les constructions complexes n'y sont pas permises.

Ce format a aussi l'avantage d'être clair pour comprendre en un coup d'œil la configuration d'un programme, il est aussi assez répandu.

Son principal inconvénient est de n'autoriser que les chaînes de caractères et donc de forcer les conversions manuelles pour chacune des valeurs.
