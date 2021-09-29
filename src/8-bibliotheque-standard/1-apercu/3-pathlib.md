### Chemins et fichiers

On a déjà croisé la `pathlib` plus tôt pour tester l'existence d'un fichier.
Mais ce module de la bibliothèque standard va bien au-delà et propose une ribambelle d'outils pour travailler avec les chemins et les fichiers.

Le module `pathlib` définit principalement le type `Path` ainsi que d'autres types qui en dépendent suivant l'implémentation.
Ainsi, quand vous instanciez un objet `Path` vous obtiendrez une instance d'un autre type suivant votre système d'exploitation (`WindowsPath` pour Windows et `PosixPath` pour les autres systèmes).

```python
>>> from pathlib import Path
>>> Path()
PosixPath('.')
```

#### Usage des chemins

On le voit, on peut instancier un `Path` sans argument, le chemin correspond alors au répertoire courant (c'est ce que signifie le point).
Mais on peut aussi passer un chemin (relatif comme absolu) en argument pour obtenir un objet `Path` correspondant.

```python
>>> Path('/')
PosixPath('/')
>>> Path('../subdir/file.py')
PosixPath('../subdir/file.py')
```

L'intérêt des objets `Path` est qu'ils sont composables entre-eux, à l'aide de l'opérateur `/` (qui représente la séparation entre répertoires).

```python
>>> Path('a') / Path('b') / Path('c')
PosixPath('a/b/c')
```

Un raccourci permet d'ailleurs de composer des chemins directement avec des chaînes de caractères.

```python
>>> Path('a') / 'b'
PosixPath('a/b')
```

Et les chemins de type `Path` sont bien sûr convertibles en chaînes de caractères via un appel explicite à `str`, ou en chaîne d'octets avec `bytes`

```python
>>> path = Path('a')
>>> str(path)
'a'
>>> str(path / 'b')
'a/b'
>>> bytes(path)
b'a'
```

Ces objets peuvent aussi directement être utilisés pour certaines opérations qui attendent des chemins.

```python
>>> with open(path, 'w') as f:
...     f.write('hello')
... 
5
```

#### Propriétés des chemins

Les objets `Path` sont pourvus de nombreux attributs et méthodes et j'aimerais vous en présenter les plus importants.

##### `parts`

Premièrement il est possible d'accéder à la décomposition d'un chemin à l'aide de son attribut `parts`.
On obtient ainsi un tuple des répertoires / fichiers qui composent notre chemin.

```python
>>> path.parts
('a',)
>>> Path('../subdir/file.py').parts
('..', 'subdir', 'file.py')
```

##### `name`

L'attribut `name` renvoie la dernière partie du chemin, soit le nom du fichier cible.

```python
>>> path.name
'a'
>>> Path('../subdir/file.py').name
'file.py'
```

##### `suffix`, `stem` et `suffixes`

`suffix` renvoie le suffixe d'un chemin, plus communément appelé l'extension du fichier.
Si aucune extension n'est présente, `suffix` renvoie une chaîne vide.

```python
>>> path.suffix
''
>>> Path('../subdir/file.py').suffix
'.py'
```

À l'inverse, l'attribut `stem` renvoie le nom du fichier dépourvu du suffixe.

```python
>>> path.stem
'a'
>>> Path('../subdir/file.py').stem
'file'
```

Si un chemin contient plusieurs extensions (`.tar.gz` par exemple), seule la dernière extension sera renvoyée par `suffix` (et retirée de `stem`).
L'attribut `suffixes` permet alors de récupérer la liste de toutes les extensions.

```python
>>> Path('photos.tar.gz').suffix
'.gz'
>>> Path('photos.tar.gz').stem
'photos.tar'
>>> Path('photos.tar.gz').suffixes
['.tar', '.gz']
```

##### `parent` et `parents`

On peut accéder au parent d'un chemin (son répertoire parent) via l'attribut `parent`.
`parent` est en quelque sort l'inverse de `name`.

```python
>>> path.parent
PosixPath('.')
>>> Path('../subdir/file.py').parent
PosixPath('../subdir')
```

L'attribut `parents` permet aussi d'accéder à l'ensemble des parents d'un chemin.
`path.parents[0]` correspondra ainsi à `path.parent`, `path.parents[1]` à `path.parent.parent`, etc.

```python
>>> Path('../subdir/file.py').parents[0]
PosixPath('../subdir')
>>> Path('../subdir/file.py').parents[1]
PosixPath('..')
>>> Path('../subdir/file.py').parents[2]
PosixPath('.')
```

[[a]]
| Attention, l'attribut `parents` ne renvoie pas une liste mais un type particulier de séquence.
| On peut bien sûr le convertir en liste avec un appel à `list`.
|
| ```python
| >>> Path('../subdir/file.py').parents
| <PosixPath.parents>
| >>> list(Path('../subdir/file.py').parents)
| [PosixPath('../subdir'), PosixPath('..'), PosixPath('.')]
| ```

##### `is_absolute`

La méthode `is_absolute` est un prédicat pour savoir si un chemin est absolu (débute par la racine du système de fichiers) ou non.

```python
>>> Path('dir/hello.txt').is_absolute()
False
>>> Path('/home/antoine/dir/hello.txt').is_absolute()
True
```

##### `relative_to`

La méthode `relative_to` permet de convertir un chemin pour l'obtenir relativement à un autre.
Elle offre ainsi un moyen de convertir un chemin absolu vers un chemin relatif.

Par exemple le chemin `/home/antoine/dir/hello.txt` donne `dir/hello.txt` relativement à `/home/antoine`.

```python
>>> Path('/home/antoine/dir/hello.txt').relative_to('/home/antoine')
PosixPath('dir/hello.txt')
```

Mais on peut aussi le calculer à partir de chemins relatifs.

```python
>>> Path('dir/hello.txt').relative_to('dir')
PosixPath('hello.txt')
```

Dans le cas où aucune correspondance n'est trouvée et qu'il n'est donc pas possible de construire un chemin relatif entre les deux, la méthode lève une exception `ValueError`.  
De même si on mélange chemins absolus et relatifs.

```python
>>> Path('dir/hello.txt').relative_to('dir2')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3.9/pathlib.py", line 939, in relative_to
    raise ValueError("{!r} is not in the subpath of {!r}"
ValueError: 'dir/hello.txt' is not in the subpath of 'dir2' OR one path is relative and the other is absolute.
```

#### Méthodes concrètes

Toutes les méthodes précédentes permettent de manipuler les chemins de façon abstraite, déconnectée du système de fichiers.
Mais d'autres méthodes servent à réaliser des opérations concrètes en s'appuyant sur le système.

##### `exists`

Nous l'avons déjà rencontrée, la méthode `exists` est un prédicat pour tester si le chemin pointe vers un fichier/répertoire qui existe ou non.

```python
>>> Path('notfound').exists()
False
>>> Path('hello.txt').exists()
True
>>> Path('/').exists()
True
```

##### `is_dir` et `is_file`

Les méthodes `is_dir` et `is_file` permettent respectivement de tester si un chemin pointe vers un répertoire ou vers un fichier.

```python
>>> Path('hello.txt').is_dir()
False
>>> Path('hello.txt').is_file()
True
>>> Path('/').is_dir()
True
>>> Path('/').is_file()
False
```

Ces méthodes renvoient `False` quand le chemin n'existe pas.

```python
>>> Path('notfound').is_dir()
False
>>> Path('notfound').is_file()
False
```

##### `resolve`

La méthode `resolve` permet de résoudre un chemin, soit de trouver le chemin absolu correspondant.

```python
>>> path.resolve()
PosixPath('/home/antoine/a')
>>> Path('hello.txt').resolve()
PosixPath('/home/antoine/hello.txt')
>>> Path('../subdir/file.py').resolve()
PosixPath('/home/subdir/file.py')
>>> Path('/').resolve()
PosixPath('/')
```

Elle peut s'utiliser avec un argument `strict` pour lever une erreur si le chemin en question n'existe pas.

```python
>>> Path('notfound').resolve()
PosixPath('/home/antoine/notfound')
>>> Path('hello.txt').resolve(strict=True)
PosixPath('/home/antoine/hello.txt')
>>> Path('notfound').resolve(strict=True)
Traceback (most recent call last):
[...]
FileNotFoundError: [Errno 2] No such file or directory: '/home/antoine/notfound'
```

##### `cwd`

`cwd` est une méthode du type `Path`, qui renvoie le chemin vers le répertoire courant.
C'est ce chemin qui est utilisé pour les résolutions de `resolve`.

```python
>>> Path.cwd()
PosixPath('/home/antoine')
```

#### Méthodes pour les répertoires

Certaines méthodes sont spécifiques aux chemins représentant des répertoires.

##### `mkdir` et `rmdir`

La méthode `mkdir` permet de créer un répertoire là où pointe le chemin.

```python
>>> Path('subdir').exists()
False
>>> Path('subdir').mkdir()
>>> Path('subdir').exists()
True
>>> Path('subdir').is_dir()
True
```

La méthode lève une erreur `FileExistsError` si le répertoire (ou un fichier) existe déjà à ce chemin.

À l'inverse, la méthode `rmdir` permet de supprimer le répertoire pointé, et lève une erreur `FileNotFoundError` s'il n'existe pas.

```python
>>> Path('subdir').rmdir()
>>> Path('subdir').rmdir()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3.9/pathlib.py", line 1363, in rmdir
    self._accessor.rmdir(self)
FileNotFoundError: [Errno 2] No such file or directory: 'subdir'
```

Un répertoire doit être vide pour pouvoir être supprimé par `rmdir`.

##### `iterdir`

Le principe des répertoires, c'est de contenir des fichiers.
Ainsi les chemins possèdent une méthode `iterdir` qui renvoie un itérable pour parcourir les fichiers contenus dans le dossier.

```python
>>> for p in Path('.').iterdir():
...     print(p)
... 
hello.txt
subdir
game.py
```

[[i]]
| Comme on le voit, les fichiers que l'on obtient ne sont pas particulièrement triés.
| On peut toujours faire appel à `sorted` si cela est nécessaire.

[[a]]
| Le parcours n'est pas récursif, les fichiers contenus dans les sous-dossiers (`subdir` par exemple) ne sont donc pas explorés.

##### `glob`

`glob` est une autre méthode pour explorer les fichiers présents dans un dossier, qui permet de les rechercher selon un critère.
En effet, `glob` prend une chaîne de caractères en argument qui décrit quels fichiers rechercher dans le répertoire.

Cette chaîne doit correspondre à un nom de fichier mais peut comprendre des `*` qui agissent comme des jokers et correspondent à n'importe quels caractères. Ainsi, `*.py` permet de trouver tous les fichiers `.py` d'un répertoire, et `glob('*')` est équivalent à `iterdir()`.

```python
>>> for p in Path('.').glob('*.py'):
...     print(p)
... 
game.py
```

#### Méthodes pour les fichiers

Certaines autres méthodes sont spécifiques aux fichiers.

##### `touch` et `unlink`

`touch` est la méthode qui permet de créer le fichier pointé par le chemin.

```python
>>> Path('newfile.txt').exists()
False
>>> Path('newfile.txt').touch()
>>> Path('newfile.txt').exists()
True
```

La méthode ne produit pas d'erreur si le fichier existe déjà (met elle modifiera sa date de dernière modification).

```python
>>> Path('newfile.txt').touch()
```

Et dans l'autre sens, on trouve la méthod `unlink` pour supprimer un fichier.

```python
>>> Path('newfile.txt').unlink()
>>> Path('newfile.txt').exists()
False
```

La méthode lève une exception `FileNotFoundError` si le fichier n'existe pas, mais depuis Python 3.8 il est possible de lui préciser un argument booléen `missing_ok` pour ne pas produire d'erreur.

```python
>>> Path('newfile.txt').unlink()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3.9/pathlib.py", line 1354, in unlink
    self._accessor.unlink(self)
FileNotFoundError: [Errno 2] No such file or directory: 'newfile.txt'
>>> Path('newfile.txt').unlink(missing_ok=True)
```

##### `open`

Nous l'avons déjà vu, la méthode `open` est semblable à la fonction _built-in_ `open`, sauf qu'elle s'applique à un chemin.
La méthode prend alors un mode en argument, `'r'` par défaut, et renvoie un gestionnaire de contexte sur le fichier.

```python
>>> with path.open('w') as f_out:
...     f_out.write('coucou')
... 
6
>>> with path.open() as f_in:
...     print(f_in.read())
... 
coucou
```

##### `read_text` et `read_bytes`

Pour simplifier certaines opérations, il existe aussi des méthodes `read_text` et `read_bytes` pour lire dans une chaîne le contenu d'un fichier.  
`read_text` renvoie une chaîne de caractères et `read_bytes` une chaîne d'octets.

```python
>>> path.read_text()
'coucou'
>>> path.read_bytes()
b'coucou'
```

##### `write_text` et `write_bytes`

Et réciproquement, les méthodes `write_text` et `write_bytes` permettent de remplacer le contenu d'un fichier par la chaîne donnée en argument.

```python
>>> path.write_text('bonne soirée')
12
>>> path.read_text()
'bonne soirée'
>>> path.write_bytes(b'\x01\x02\x03')
3
>>> path.read_bytes()
b'\x01\x02\x03'
```

Le fichier est automatiquement créé s'il n'existe pas.

```python
>>> Path('notfound').write_text('abc')
3
>>> Path('notfound').read_text()
'abc'
```

--------------------

Toutes les autres méthodes des objets `Path` sont à découvrir sur [la page de documentation du module `pathlib`](https://docs.python.org/fr/3.8/library/pathlib.html).
