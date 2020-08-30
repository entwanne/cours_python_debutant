### Fonction open

* Fonction `open` pour ouvrir un fichier
* Répertoire courant
* Modes d'ouverture, `'r'` pour lecture

Nous allons commencer simplement avec un fichier texte.
Commencez par créer un fichier `hello.txt` dans votre répertoire courant, contenant simplement la phrase `Hello World!`.

[[attention]]
| Sous Windows, l'extension des fichiers n'est pas affichée par défaut.
| Assurez-vous donc que votre fichier se nomme bien `hello.txt` (extension comprise) pour que la suite puisse fonctionner correctement.

Depuis Python, nous utiliserons ensuite la fonction `open` pour ouvrir le fichier, avec comme argument le chemin vers notre fichier.
Ici, comme notre fichier se trouve dans le répertoire courant, il nous suffira de faire `open('hello.txt')`.

Pour un fichier dans le répertoire parent, nous aurions par exemple écrit `open('../hello.txt')`, ou `open('subdirectory/hello.txt')` pour un répertoire enfant.

```python
>>> open('hello.txt')
<_io.TextIOWrapper name='hello.txt' mode='r' encoding='UTF-8'>
```

On voit que l'appel nous renvoie un objet un peu étrange mais l'essentiel est là : nous avons ouvert un fichier `hello.txt` encodé en *UTF-8* et en mode `r`.

Qu'est-ce que ce mode ?  
Il faut savoir que plusieurs opérations sont possibles pour les fichiers, de lecture et d'écriture.
Les différentes opérations impliques des besoins différents et le système d'exploitation requiert donc un mode lors de l'ouverture du fichier.  
Ici, `r` signifie que nous ouvrons le fichier en lecture seule (*read*), nous verrons par la suite quels autres modes d'ouverture existent.

La fonction open prend un deuxième argument optionnel pour spécifier ce mode. Il vaut `'r'` par défaut, d'où le comportement que nous observons.

```python
>>> open('hello.txt', 'r')
<_io.TextIOWrapper name='hello.txt' mode='r' encoding='UTF-8'>
```

Ça c'est pour les cas où ça se passe bien.
Il se peut aussi que l'ouverture échoue : si le fichier est introuvable ou que les droits sont insuffisants par exemple.
Dans ce cas, une erreur sera levée par la fonction `open` et le fichier ne sera pas ouvert.

```python
>>> open('notfound.txt')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'notfound.txt'
>>> open('cantread.txt')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
PermissionError: [Errno 13] Permission denied: 'cantread.txt'
```

Dans le cas où vous rencontriez ces erreurs pour un fichier qui devrait être bon, assurez-vous donc toujours que vous êtes dans le bon répertoire et que l'utilisateur a les droits suffisants pour lire le fichier.
