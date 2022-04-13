### Écriture

Nous avons vu que la fonction `open` prenait un argument optionnel pour spécifier le mode d'ouverture du fichier, et n'avons pour le moment utilisé que le mode lecture (`'r'`).
Vous vous en doutez, il va ici être question d'un nouveau mode afin de pouvoir écrire dans nos fichiers.

Il n'y a pas un unique mode d'écriture, car plusieurs options sont possibles, mais nous allons commencer avec le mode `'w'` (pour *write*).

[[i]]
| Dans les exemples qui suivront je n'utiliserai pas de bloc `with` pour simplifier les opérations dans l'interpréteur interactif.  
| Il s'agit là d'une exception, gardez en tête de toujours utiliser un bloc `with` par défaut dans vos codes.

Commençons par ouvrir notre fichier `hello.txt`.

```pycon
>>> f = open('hello.txt', 'w')
>>> f
<_io.TextIOWrapper name='hello.txt' mode='w' encoding='UTF-8'>
```

Comme le mode l'indique, il ne nous est pas possible de lire le contenu du fichier, l'opération produirait une erreur.

```pycon
>>> f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
io.UnsupportedOperation: not readable
```

Mais il nous est alors possible d'écrire dans le fichier, à l'aide de la méthode `write`.

```pycon
>>> f.write('Salut')
5
```

La méthode prend naturellement une chaîne de caractères en argument et renvoie le nombre de caractères écrits, c'est-à-dire la longueur de la chaîne dans notre cas.

Si vous regardez alors le contenu de votre fichier depuis un éditeur de texte, il se peut que vous le voyiez vide.

En fait, les fichiers fonctionnent avec une mémoire tampon pour éviter les écritures trop nombreuses sur le disque dur.
Cette mémoire est généralement vidée (et donc le contenu du fichier écrit sur le disque) à la fermeture du fichier, lors d'un retour à la ligne ou par une demande explicite.

Ce dernier cas correspond à la méthode `flush` qui permet donc de valider toutes les opérations d'écriture en cours.

```pycon
>>> f.flush()
```

Si vous inspectez à nouveau le contenu du fichier, le contenu devrait cette fois-ci apparaître.  
Il n'est généralement pas utile de faire appel à `flush`, car celui-ci arrivera bien assez tôt (comme dans les cas expliqués plus haut).
Mais à titre d'exemple, vous saurez que la méthode existe et quel effet elle a.

```
salut
```
Code: hello.txt

Nous pouvons maintenant fermer notre fichier (en l'absence de `with`) : `f.close()`.

Pour rappel, notre fichier contenait précédemment le texte « Hello World! », celui-ci a été entièrement effacé lorsque nous avons ouvert le fichier en mode `'w'`.
C'est le comportement de Python avec ce mode.

Un autre comportement du mode d'écriture est de créer le fichier de destination si celui-ci n'existe pas.

```python
with open('newfile.txt', 'w') as f:
    f.write('I am a new file')
```

Ce code ne provoque pas d'erreur et crée un nouveau fichier `newfile.txt` contenant le texte « I am a new file ».

#### Écrire plusieurs lignes dans un fichier

Vous avez peut-être effectué plusieurs appels successifs à `write` en espérant écrire plusieurs lignes dans un fichier.
Mais ça ne fonctionne pas comme ça, vous avez juste obtenu des lettres à la suite.

```pycon
>>> with open('alphabet.txt', 'w') as f:
...     f.write('abc')
...     f.write('def')
...     f.write('ghi')
...
3
3
3
>>> with open('alphabet.txt', 'r') as f:
...     f.read()
...
'abcdefghi'
```

En fait, si vous vous souvenez de la lecture des fichiers, les lignes étaient chaque fois terminées d'un caractère pour marquer le saut de ligne, `'\n'`.
C'est aussi ce caractère que nous devons utiliser pour passer des lignes dans notre fichier.

```pycon
>>> with open('alphabet.txt', 'w') as f:
...     f.write('abc\n')
...     f.write('def\n')
...     f.write('ghi\n')
...
4
4
4
>>> with open('alphabet.txt', 'r') as f:
...     f.readlines()
...
['abc\n', 'def\n', 'ghi\n']
```

Bien sûr, cela fonctionnerait de la même manière avec un seul appel à `write`, celui-ci n'étant pas lié au nombre de lignes que l'on veut écrire.

```python
with open('alphabet.txt', 'w') as f:
    f.write('abc\ndef\nghi\n')
```

Mais on pourra trouver plusieurs appels à `write` si l'on dispose par exemple d'une liste d'éléments à écrire, auquel cas on procèdera avec une boucle `for`.

```python
lines = ['abc\n', 'def\n', 'ghi\n']

with open('alphabet.txt', 'w') as f:
    for line in lines:
        f.write(line)
```

Notez que les fichiers possèdent déjà une méthode `writelines` pour répondre à ce problème, qui est donc l'inverse de `readlines` (`writelines` prend en argument le même type de valeur que ce que renvoie `readlines`).

```pycon
>>> with open('alphabet.txt', 'w') as f:
...     f.writelines(['abc\n', 'def\n', 'ghi\n'])
...
>>> with open('alphabet.txt', 'r') as f:
...     f.readlines()
...
['abc\n', 'def\n', 'ghi\n']
```

#### La fonction `print`

Enfin, sachez qu'il est aussi possible d'utiliser la fonction `print` pour écrire dans des fichiers.
Par défaut cette fonction écrit son résultat sur le terminal (qui est vu comme un fichier par le système), mais il est possible de choisir une autre sortie (un autre fichier) avec l'argument nommé `file`.

```pycon
>>> with open('hello.txt', 'w') as f:
...     print('Hello', 'World!', file=f)
...
>>> with open('hello.txt', 'r') as f:
...     f.read()
...
'Hello World!\n'
```

La fonction procède de la même manière que sur le terminal et espace donc les arguments, puis ajoute un saut de ligne à la fin.

Cela permet aussi facilement d'écrire vers un fichier des objets autres que des chaînes de caractères, ce qui n'est pas possible avec des appels à `write` (à moins de convertir préalablement les valeurs).

```pycon
>>> with open('types', 'w') as f:
...     print(42, {'a': True}, [1.5], file=f)
...
>>> with open('types', 'r') as f:
...     f.read()
...
"42 {'a': True} [1.5]\n"
```

Ce saut de ligne ajouté à la fin est le comportement par défaut de `print` mais il est possible de le changer à l'aide de l'argument nommé `end`, qui prend une chaîne de caractères comme marqueur de fin de ligne.

```pycon
>>> print('hello', 'world', end='!\n')
hello world!
>>> print('hello', 'world', end='!')
hello world!>>>
```

[[i]]
| Le résultat sans `\n` peut paraître surprenant.
| Les `>>>` sont en fait l'invite de commande de Python : comme il n'y a pas eu de saut de ligne, il apparaît à la suite.

Dans un fichier cela donnerait les résultats que l'on pouvait avoir précédemment avec `write`.

```pycon
>>> with open('hello.txt', 'w') as f:
...     print('Hello', file=f, end=' ')
...     print('World!', file=f)
...
>>> with open('hello.txt', 'r') as f:
...     f.read()
...
'Hello World!\n'
```

Cela est bien sûr compatible avec l'argument `sep` pour préciser le séparateur de valeurs.

```pycon
>>> with open('hello.txt', 'w') as f:
...     print('Hello', 'World', file=f, sep=' - ', end='!\n')
...
>>> with open('hello.txt', 'r') as f:
...     f.read()
...
'Hello - World!\n'
```

Enfin la fonction `print` prend aussi un argument optionnel `flush` recevant un booléen, et qui permet donc un appel automatique à la méthode `flush` si `True` lui est passé.
Ce n'est encore une fois utile que dans de rares cas, et pour des écritures qui ne seraient pas déjà terminées d'un saut de ligne.
