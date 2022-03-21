### Fichiers

#### Lire le contenu d'un fichier

Avoir ouvert un fichier, c'est bien, mais ce qui nous intéresse ici est son contenu.
Nous allons pour cela nous intéresser à l'objet renvoyé par `open`.

Il s'agit d'un objet de type `TextIOWrapper`, c'est ainsi que Python identifie un fichier textuel.
Cet objet possède différentes méthodes, et notamment la méthode `read`.
Utilisée sans argument, elle renvoie le contenu complet du fichier sous forme d'une chaîne de caractères.

```pycon
>>> f = open('hello.txt')
>>> f.read()
'Hello World!\n'
```

On remarque ici que mon fichier se termine par un saut de ligne, cela fait partie du contenu du fichier.

[[i]]
| Sous Windows, il est possible que votre fichier se termine par `\r\n`, qui est la représentation d'un passage à la ligne sur ce système.

Mais l'objet que nous avons en Python n'est pas à proprement parler un fichier, c'est une entité qui enrobe les opérations possibles sur le fichier, on parle de _wrapper_.
Et celui-ci ne représente qu'un curseur qui avance dans le fichier présent sur le système.
Ainsi, l'état d'un fichier évolue au fur et à mesure qu'on le parcourt.

À l'ouverture, le curseur se trouvait naturellement au début du fichier. Mais une fois le contenu lu, celui-ci s'est déplacé -- comme sur une bande d'enregistrement qui défilerait -- et se trouve maintenant à la fin.
Ne vous étonnez donc pas si vous tentez un nouveau `read` sur le même fichier et obtenez une chaîne vide.

```pycon
>>> f.read()
''
```

L'explication est que la fonction lit le contenu à partir de là où se trouve le curseur dans le fichier, et en l'occurrence il n'y a plus rien à lire.

Une seule lecture suffit généralement à traiter le contenu du fichier, mais il peut arriver dans certains cas que l'on veuille revenir en arrière.
Il existe pour cela la méthode `seek` prenant une position dans le fichier pour y déplacer le curseur.
`0` correspond au début du fichier.

```pycon
>>> f.seek(0)
0
>>> f.read()
'Hello World!\n'
```

Mais une autre position dans le fichier serait aussi valide.

```pycon
>>> f.seek(6)
6
>>> f.read()
'World!\n'
```

#### Fermer un fichier

Un tel curseur sur un fichier représente une ressource au niveau du système d'exploitation, et les ressources sont limitées.
Le nombre de fichiers qu'un programme peut ouvrir va dépendre de la machine et du système, il est par exemple de 1024 chez moi.
C'est-à-dire que chaque programme ne peut ouvrir plus de 1024 fichiers simultanément.

Vous me direz que nous en sommes encore loin mais toujours est-il qu'il n'est pas utile de gaspiller ces ressources.
Ainsi, nous prendrons l'habitude de libérer notre ressource dès que nous aurons terminé de travailler avec elle.

Cela se fait par exemple avec un appel à la méthode `close` sur le fichier.

```pycon
>>> f.close()
```

La méthode ne renvoie rien, tout s'est bien passé, la ressource est maintenant libérée sur le système.

Si nous essayons à nouveau de réaliser une opération sur notre fichier (`read`, `seek`), nous obtiendrons une erreur comme quoi le fichier est fermé.
Python n'a en effet plus de référence vers le fichier et il faudrait l'ouvrir à nouveau (avec un appel à `open`) pour retravailler dessus.

```pycon
>>> f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
```

#### Bloc `with`

Néanmoins, l'appel explicite à `close` n'est pas la manière à privilégier pour libérer la ressource.
Prenons par exemple la fonction suivante, pour récupérer le contenu d'un fichier sous forme d'un nombre entier (`int`).

```python
def get_file_number(filename):
    f = open(filename)
    content = f.read()
    value = int(content)
    f.close()
    return value
```

À l'usage, sur un fichier `number.txt` contenant le texte `42`, elle fonctionne très bien.

```pycon
>>> get_file_number('number.txt')
42
```

Mais si on tente de l'exécuter avec notre fichier `hello.txt` (qui ne contient pas un nombre) on obtient logiquement une erreur.

```pycon
>>> get_file_number('hello.txt')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in get_file_number
ValueError: invalid literal for int() with base 10: 'Hello World!\n'
```

L'erreur survient à la ligne 4 de notre fonction, `value = int(content)`.
À cet instant, l'exécution de la fonction s'arrête pour remonter l'erreur survenue.  
La ligne suivante, `f.close()` n'a donc pas pu être exécutée, et ne le sera pas.
C'est tout de même problématique.

Il y a des mécanismes pour traiter les erreurs et gérer des cas comme celui-ci (voir chapitres suivants), mais le plus simple est encore de ne pas avoir à faire l'appel à `close` nous-même.

Pour cela il existe en Python ce qu'on appelle des gestionnaires de contexte qui permettent de facilement traiter les ressources.
Ils prennent la forme d'un bloc `with`, suivi par l'expression récupérant la ressource (ici l'appel à `open`).
Le mot-clé `as` permet ensuite de récupérer cette ressource dans une variable.

```python
with open('hello.txt') as f:
    print(f.read())
```

Le code précédent est ainsi équivalent à :

```python
f = open('hello.txt')
print(f.read())
f.close()
```

À l'exception que le `close` sera réalisé dans tous les cas, même si le `read` échoue par exemple.

Le code de notre fonction `get_file_number` deviendrait donc :

```python
def get_file_number(filename):
    with open(filename) as f:
        content = f.read()
        return int(content)
```

Et on observe le même comportement que précédemment à l'utilisation.

```pycon
>>> get_file_number('number.txt')
42
>>> get_file_number('hello.txt')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in get_file_number
ValueError: invalid literal for int() with base 10: 'Hello World!\n'
```

L'erreurs survient toujours, mais cette fois-ci la ressource a correctement été libérée, le mécanisme est géré par Python.

[[i]]
| Quand vous manipulez des fichiers, utilisez donc toujours un bloc `with` pour éviter les soucis.
