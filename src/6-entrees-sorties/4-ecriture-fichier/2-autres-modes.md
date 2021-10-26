### Autres modes des fichiers

On l'a vu, le mode `'w'` a pour effet de supprimer le contenu du fichier pour partir sur un contenu vierge.

```python
with open('hello.txt', 'w') as f:
    f.write('salut')
```

Ce n'est pas toujours le comportement voulu, et c'est pourquoi il existe différents modes d'ouverture.

#### Insérer à la fin du fichier

On a ainsi un mode `'a'` (pour *append*, ajouter) qui permet d'insérer du texte à la fin du fichier.
C'est-à-dire que tout le contenu déjà présent sera conservé, les modifications apportées seront simplement ajoutées au fichier.

Voyez par exemple avec notre fichier `hello.txt` contenant pour le moment `salut`.

```pycon
>>> with open('hello.txt', 'a') as f:
...     f.write(' tout le monde')
...
14
>>> with open('hello.txt', 'r') as f:
...     f.read()
...
'salut tout le monde'
```

C'est un mode qui peut être particulièrement utile pour des outils de journalisation, car cela évite les conflits entre de multiples écritures.

#### Créer un fichier

On l'a vu, le mode `'w'` crée le fichier s'il n'existe pas.
Il existe un mode plus strict, `'x'` (pour *eXclusif*), spécialement dédié à la création de fichier : ce mode échouera si le fichier existe déjà.

```pycon
>>> with open('hello.txt', 'x') as f:
...     pass
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileExistsError: [Errno 17] File exists: 'hello.txt'
```

Mais dans le cas d'un fichier inexistant, il aura le même effet que le mode `'w'`.
C'est un mode qui permet par exemple d'éviter que deux programmes concurrents n'écrasent un fichier en croyant le créer.

[[q]]
| Quelle est donc cette instruction `pass` ?  
| C'est une instruction Python qui permet juste de ne rien faire, elle permet de conclure un bloc indenté (quand Python attend quelque chose) sans rien faire de particulier, juste _passer_.
|
| Elle n'est pas équivalente à `...`, qui est une expression et possède donc une valeur (`Ellipsis`).

```pycon
>>> with open('newfile.txt', 'x') as f:
...     f.write('New file')
... 
8
```

#### Lire et écrire à la fois

Nous avons vu que nous pouvions ouvrir un fichier pour le lire ou pour y écrire, mais il est aussi possible d'y faire les deux à la fois.
Cela se fait avec le mode `'r+'`, dédié à la mise à jour (_update_).

```pycon
>>> with open('hello.txt', 'r+') as f:
...     f.read()
...     f.write('!!!')
... 
'salut tout le monde'
3
>>> with open('hello.txt', 'r') as f:
...     f.read()
... 
'salut tout le monde!!!'
```

Mais attention à ne pas vous emmêler avec les lectures/écritures et la mémoire tampon, sachant qu'il n'y a qu'un unique curseur dans le fichier.
Il est ainsi possible d'écraser des portions du fichier qui n'ont pas encore été lues, c'est pourquoi il faut être vigilent lors de l'utilisation de ce mode.

```pycon
>>> with open('hello.txt', 'r+') as f:
...     f.write('>>>')
...     f.read()
... 
3
'ut tout le monde!!!'
>>> with open('hello.txt', 'r') as f:
...     f.read()
... 
'>>>ut tout le monde!!!'
```

Pensez donc aux méthodes `seek` et `flush` qui pourraient vous être utiles pour vous déplacer dans le fichier et vider le tampon.

De façon similaire on trouve aussi des modes de mise à jour en ajout (`'a+'`), en troncature (`'w+'`) et en création (`'x+'`).
Le premier aura pour effet de placer le curseur à la fin du fichier, et le second d'effacer le contenu actuel du fichier.

Il ne s'agit ici que de modes pour opérer sur les fichiers en mode texte, nous verrons par la suite comment traiter les fichiers binaires.
