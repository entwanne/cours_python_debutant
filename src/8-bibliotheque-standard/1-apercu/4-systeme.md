### Modules systèmes

Python dispose aussi de modules pour interagir avec le système, notamment les modules `sys`, `shutil` et `os`.

#### Module `sys`

`sys` est un module qui fournit différentes informations sur le système d'exploitation et l'interpréteur Python.

On trouve notamment des attributs `platform`, `version` et `version_info` pour connaître l'OS utilisé et la version de Python.

```pycon
>>> import sys
>>> sys.platform
'linux'
>>> sys.version
'3.9.7 (default, Aug 31 2021, 13:28:12) \n[GCC 11.1.0]'
>>> sys.version_info
sys.version_info(major=3, minor=9, micro=7, releaselevel='final', serial=0)
>>> sys.version_info.major, sys.version_info.minor
(3, 9)
```

On peut aussi accéder au chemin de l'exécutable Python (`executable`), ainsi qu'à la liste des arguments du programme (`argv`).

```pycon
>>> sys.executable
'/usr/bin/python'
>>> sys.argv
['']
```

Le module met à disposition les fichiers `stdin`, `stdout` et `stderr` qui sont liés respectivement à l'entrée standard, la sortie standard et la sortie d'erreur.

```pycon
>>> sys.stdin.readline()
hello
'hello\n'
>>> sys.stdout.write('coucou\n')
coucou
7
>>> sys.stderr.write('error\n')
error
6
```

Le dictionnaire `modules` référence tous les modules importés au sein de l'interpréteur.
C'est un mécanisme de cache au sein de Python pour éviter de charger plusieurs fois un même module.

```pycon
>>> sys.modules
{'sys': <module 'sys' (built-in)>, 'builtins': <module 'builtins' (built-in)>, ...}
>>> sys.modules['sys']
<module 'sys' (built-in)>
>>> sys.modules['sys'].platform
'linux'
```

Quand je vous parlais de récursivité, j'évoquais une limite au nombre de récursions autorisées par l'interpréteur Python.
Cette limite peut être connue via un appel à la fonction `getrecursionlimit` du module `sys`.

```pycon
>>> sys.getrecursionlimit()
1000
```

Enfin, nous l'avons déjà rencontrée, la fonction `exit` permet de couper le programme en cours d'exécution.
Utilisée sans argument, la fonction coupe le programme normalement avec un code de retour de 0 (signifiant que tout s'est bien passé).

```pycon
>>> sys.exit()
% echo $?
0
```

Avec un nombre en argument, c'est ce nombre qui sera utilisé comme code de retour (un code de retour différent de 0 signifie que le programme s'est terminé sur une erreur).

```pycon
>>> sys.exit(12)
% echo $?
12
```

Avec une chaîne de caractères en argument, la chaîne sera écrite sur la sortie d'erreur et le code de retour sera 1.

```pycon
>>> sys.exit('error')
error
% echo $?
1
```

L'ensemble de ces fonctions, et bien d'autres encore, peut être retrouvé sur [la page de documentation du module `sys`](https://docs.python.org/fr/3/library/sys.html).

#### Module `shutil`

`shutil` peut venir en complément de `pathlib`, il propose des opérations de haut-niveau sur les fichiers et répertoires, notamment pour les copies, les déplacements et la suppression.

On trouve ainsi une fonction `copy` qui permet de copier un fichier à un autre endroit sur le système.
La fonction prend en arguments le chemin source et sa destination, les chaînes de caractères et les objets `Path` sont acceptés.  
Elle renvoie le chemin du fichier copié.

```pycon
>>> from pathlib import Path
>>> import shutil
>>> shutil.copy(Path('hello.txt'), 'new.txt')
'new.txt'
>>> Path('new.txt').read_text()
'salut\n'
```

Il est aussi possible de préciser un répertoire en second argument pour copier le fichier (en conservant son nom) vers ce répertoire.

```pycon
>>> shutil.copy('hello.txt', 'subdir')
'subdir/hello.txt'
>>> Path('subdir/hello.txt').read_text()
'salut\n'
```

Pour copier des arborescences de fichiers (fichiers et répertoires), `shutil` propose une fonction `copytree` sur le même principe que `copy`.
La fonction copie récursivement le répertoire source et les fichiers qu'il contient vers la destination.

```pycon
>>> shutil.copytree('subdir', 'newdir')
'newdir'
>>> list(Path('newdir').iterdir())
[PosixPath('newdir/hello.txt'), PosixPath('newdir/file.py')]
```

De la même manière, on trouve une fonction `move` pour déplacer un fichier ou un répertoire vers une destination.

```pycon
>>> shutil.move('new.txt', 'moved.txt')
'moved.txt'
>>> Path('moved.txt').read_text()
'salut\n'
>>> Path('new.txt').exists()
False
>>> shutil.move('newdir', 'moveddir')
'moveddir'
>>> list(Path('moveddir').iterdir())
[PosixPath('moveddir/hello.txt'), PosixPath('moveddir/file.py')]
>>> Path('newdir').exists()
False
```

Et le module offre aussi une fonction `rmtree` pour supprimer récursivement un répertoire.

```pycon
>>> shutil.rmtree('moveddir')
>>> Path('moveddir').exists()
False
```

Enfin, dans un tout autre genre, la fonction `get_terminal_size` permet de connaître la taille (en lignes de caractères et en colonnes) du terminal.
La fonction renvoie un tuple nommé avec deux champs `columns` et `lines`.

```pycon
>>> shutil.get_terminal_size()
os.terminal_size(columns=136, lines=66)
```

La [page de documentation de `shutil`](https://docs.python.org/fr/3/library/shutil.html) complètera les informations au sujet de ce module.

#### Module `os`

`os` est l'interface bas-niveau du système d'exploitation (_os_ pour _operating system_), le module offre une multitude de fonctions pour communiquer avec lui.

On trouve notamment des fonctions pour manipuler les fichiers et répertoires telles que `mkdir`, `rmdir`, `unlink`, `open`, etc.
Ces fonctions sont celles qui sont utilisées par la `pathlib` qui leur ajoute une interface plus haut-niveau pour manipuler ces données.

La plupart des fonctions exposées dans `os` sont d'ailleurs abstraites dans d'autres modules (`subprocess`, `shutil`) pour les rendre plus faciles à utiliser.

[[i]]
| De la même manière, on trouve le module `os.path`, antérieur à la `pathlib`, pour gérer les chemins de fichiers avec des fonctions comme `exists`, `dirname`, `basename` ou encore `splitext`.

Le module propose aussi une fonction `chdir` (pour _change directory_) qui prend un chemin (relatif ou absolu) en argument et permet de changer le répertoire courant.

```pycon
>>> Path.cwd()
PosixPath('/home/antoine')
>>> os.chdir('..')
>>> Path.cwd()
PosixPath('/home')
```

[[a]]
| Attention, changer de répertoire courant affecte ensuite toutes les opérations utilisant des chemins relatifs, c'est une opération à réaliser avec précaution.

Parmi les autres outils présents dans le module, on trouve par exemple la fonction `cpu_count` qui permet de savoir combien de cœurs sont disponibles sur la machine.

```pycon
>>> os.cpu_count()
8
```

##### Gestion de l'environnement

Un programme est toujours exécuté dans un certain environnement.
Cet environnement consiste en un ensemble de variables définies par le système, sur lesquelles les programmes peuvent se baser pour certaines de leurs actions.  
Il est ainsi courant de trouver des variables d'environnement telles que `SHELL` (le shell utilisé), `USER` (l'utilisateur courant), `LANG` (la langue de l'utilisateur), `HOME` (le dossier de l'utilisateur) ou `PWD` (le répertoire courant).

Depuis le shell, on peut spécifier des variables d'environnement supplémentaires pour un programme en plaçant `VAR=value` avant l'invocation du programme.

```shell
% OUTPUT=/tmp/out MAX_VALUE=256 python script.py
```

[[i]]
| Il est coutume d'utiliser exclusivement des lettres capitales (ainsi que des chiffres et des _underscores_) dans les noms de variables d'environnement.

En Python, l'environnement est accessible via le dictionnaire `environ` du module `os`.
Ce dictionnaire associe les valeurs des variables d'environnement à leurs noms.

```pycon
>>> import os
>>> os.environ
environ({..., 'OUTPUT': '/tmp/out', 'MAX_VALUE': '256'})
```

On le voit, les valeurs des variables d'environnement sont toujours des chaînes de caractères, il peut alors être nécessaire de les convertir.

```pycon
>>> os.environ['MAX_VALUE']
'256'
>>> int(os.environ['MAX_VALUE'])
256
```

Le module dispose aussi d'une fonction `getenv` pour récupérer une variable d'environnement.

```pycon
>>> os.getenv('OUTPUT')
'/tmp/out'
```

La fonction renvoie `None` si la variable d'environnement n'est pas définie, mais il est possible de lui spécifier un argument `default` pour choisir cette valeur par défaut.

```pycon
>>> os.getenv('NOTFOUND')
>>> os.getenv('NOTFOUND', 'no')
'no'
```

Le dictionnaire `environ` est bien sûr éditable, ce qui permet de faire évoluer l'environnement du programme.

```pycon
>>> os.environ['MAX_VALUE'] = str(int(os.environ['MAX_VALUE']) * 2)
>>> os.getenv('MAX_VALUE')
'512'
```

Afin de traiter l'environnement comme des chaînes d'octets, on trouve aussi le dictionnaire `environb` et la fonction `getenvb` qui remplissent le même rôle que `environ` et `getenv`.

```pycon
>>> os.environb
environ({..., b'OUTPUT': b'/tmp/out', b'MAX_VALUE': b'512'})
>>> os.getenvb(b'MAX_VALUE')
b'512'
```

Pour plus d'informations, vous pouvez consulter [la documentation du module `os`](https://docs.python.org/fr/3/library/os.html).
