### Ligne de commande

Pour l'instant nous appelons nos programmes depuis la ligne de commande en tapant `python program.py` (mais nous savons aussi [comment utiliser `./program.py` sous Linux](https://zestedesavoir.com/tutoriels/2514/un-zeste-de-python/10-annexes/2-notes-diverses/#shebang)).

Dans les deux cas, cela fait appel à l'interpréteur Python en lui donnant le chemin de notre programme en argument.
Mais il est possible de renseigner d'autres arguments lors du lancement et ceux-ci seront transmis à notre programme.

Ils seront accessibles sous la forme d'une liste de chaînes de caractères, la liste `argv` qu'il faudra importer depuis le module `sys` (un module qui gère les informations sur le système).

```python
import sys

print(sys.argv)
```
Code: program.py

À l'utilisation, nous recevons bien les différents arguments passés au programme.

```shell
% python program.py
['program.py']
% python program.py foo bar
['program.py', 'foo', 'bar']
% python program.py 1 2 3
['program.py', '1', '2', '3']
```

On voit que le premier argument est toujours le nom du programme.

Comme indiqué, il ne s'agit que de chaînes de caractères et il va donc falloir convertir les types lorsque cela est nécessaire.
Par exemple avec cette mini-calculatrice.

```python
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
print(a + b)
```
Code: addition.py

```shell
% python addition.py 3 5
8
% python addition.py 10 -3
7
```

Mais attention, notre code plantera méchamment si nous ne fournissons pas suffisamment d'arguments.

```shell
% python addition.py 1
Traceback (most recent call last):
  File "addition.py", line 4, in <module>
    b = int(sys.argv[2])
IndexError: list index out of range
```

En effet, `sys.argv` est une liste ordinaire, et si sa taille n'est que de 2, alors elle ne possède pas d'élément à l'index 2.

Pour nous prémunir de ce genre d'erreurs, il faut donc vérifier la taille de la liste avant d'accéder à ses éléments.
Et généralement dans ces cas là, on quittera le programme en affichant un message expliquant comment l'appeler.

Pour quitter un programme à tout moment, on peut faire appel à la fonction `sys.exit`.

```python
import sys

if len(sys.argv) < 3:
    print('Usage: addition.py nb1 nb2')
    sys.exit()

a = int(sys.argv[1])
b = int(sys.argv[2])
print(a + b)
```

À l'utilisation c'est tout de suite plus propre.

```shell
% python addition.py 1 2
3
% python addition.py 1
Usage: addition.py nb1 nb2
```

Pour plus de généricité, on pourrait écrire `print(f'Usage: {sys.argv[0]} nb1 nb2')` évitant d'inscrire en dur le nom du programme.
Le premier élément de `sys.argv` sera toujours présent, notre programme n'aurait pas pu être appelé sinon.

#### Sortie standard et sortie d'erreur

Il y a un seul soucis avec notre message d'erreur : celui-ci est imprimé sur la sortie standard.

[[q]]
| Qu'est-ce que la sortie standard ?
|
| Sur Linux, les programmes qui tournent sont automatiquement reliés à 3 périphériques :
|
| * L'entrée standard, celle qui récupère le texte entré sur le terminal, accessible via `input()`.
| * La sortie standard, où est affiché par défaut tout ce qui sort du programme sur le terminal (avec `print` par exemple).
| * La sortie d'erreur, spécifiquement dédiée aux erreurs.

Les sorties standard et d'erreur sont toutes deux affichées par défaut sur le terminal, mais elles sont pourtant différentes.
Dans un shell Bash, il est possible d'utiliser l'opérateur `>` pour rediriger le flux de sortie standard vers un fichier, et l'opérateur `2>` pour la sortie d'erreur.

```bash
% python addition.py > out 2> err
```

Si l'on inspecte nos fichiers, on constate bien que `out` contient le message d'erreur et que `err` est vide.
On aimerait que ce soit l'inverse en cas d'erreur.

En fait, chaque sortie correspond à un fichier ouvert par défaut par le programme.
Pour la sortie standard, il s'agit de `sys.stdout`. (_standard output_).
On peut l'utiliser comme tout autre fichier ouvert en écriture.

```pycon
>>> import sys
>>> sys.stdout.write('hello\n')
hello
6
>>> print('world', file=sys.stdout)
world
```

Le 6 qui apparaît n'est que le retour de l'appel à `write` (6 caractères ont été écrits).

Et de façon similaire, on a `sys.stderr` qui correspond à la sortie d'erreur.

```pycon
>>> print('error', file=sys.stderr)
error
```

Bien sûr la différence n'est pas flagrante dans cet exemple, elle le sera si l'on redirige les sorties standard et d'erreur vers des fichiers différents.
Ce qui est généralement fait pour la journalisation d'un programme.

```python
import sys

print('standard output', file=sys.stdout)
print('error output', file=sys.stderr)
```
Code: outputs.py

```shell
% python outputs.py > out 2> err
% cat out
standard output
% cat err
error output
```

Ainsi, nous pouvons remplacer notre code de traitement d'erreur par le suivant.

```python
if len(sys.argv) < 3:
    print(f'Usage: {sys.argv[0]} nb1 nb2', file=sys.stderr)
    sys.exit()
```
