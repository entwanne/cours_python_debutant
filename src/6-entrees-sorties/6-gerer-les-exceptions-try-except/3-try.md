### Traiter l'exception

Pour gérer les exceptions on va utiliser un nouveau type de bloc, ou plutôt un couple de blocs, introduits par les mots-clés `try` et `except` (littéralement « essaie » et « à l'exception de »).

Ces deux mots-clés vont de paire pour intercepter les erreurs.  
Dans le bloc `try` on place le code qui peut échouer, et le bloc `except` sera exécuté si et seulement si une exception survient.
Il aura pour effet d'attraper cette exception et donc éviter que le programme ne plante, en proposant un traitement adapté.

```python
>>> try:
...     result = 1 / 0
... except:
...     print('Division par zéro')
...
Division par zéro
```

Ici notre traitement est simplement d'afficher un message, mais il est possible de faire ce que l'on veut dans le bloc `except`, comme renvoyer une valeur particulière.

```python
def division(a, b):
    try:
        return a / b
    except:
        return float('nan')
```

[[q]]
| Quel est ce `float('nan')` ?
|
| _NaN_, pour _Not a Number_ (_Pas un Nombre_), est une valeur particulière de la norme des nombres flottants évoquant un résultat qui ne serait pas un nombre.  
| On y accède en Python via la variable `nan` du module `math`, ou avec un simple `float('nan')`.

```python
>>> division(3, 5)
0.6
>>> division(4, 2)
2.0
>>> division(10, 0)
nan
```

L'exécution du programme reprend normalement à l'issue du `except`.
On ne le voit pas dans l'exemple car on y utilise un `return`, mais la suite de la fonction est bien exécutée.

```python
def division(a, b):
    try:
        result = a / b
    except:
        result = float('nan')
    print('Résultat :', result)
    return result
```

Si l'exécution s'arrêtait juste après le `except`, nous ne passerions pas dans le `print` et le `return`.

```python
>>> division(1, 2)
Résultat : 0.5
0.5
>>> division(1, 0)
Résultat : nan
nan
```

Aussi, nous utilisons `except` sans lui préciser aucun argument, il attrapera donc toute exception qui surviendrait, quel qu'en soit son type.

```python
>>> division('x', 'y')
Résultat : nan
nan
```

Pourtant ce n'est pas toujours souhaitable.
Par exemple dans le cas présent il s'agit d'une erreur de type et donc d'un mauvais usage de la fonction, on pourrait préférer ne pas traiter cette exception et la laisser survenir.  
Ainsi, on pourra préciser derrière `except` le type de l'exception que l'on veut attraper, dans notre cas `ZeroDivisionError`.

```python
def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return float('nan')
```

Notre fonction interceptera maintenant les erreurs de division par zéro, et uniquement celles-ci.

```python
>>> division(1, 2)
0.5
>>> division(1, 0)
nan
>>> division(1, 'x')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in division
TypeError: unsupported operand type(s) for /: 'int' and 'str'
```

#### Attraper plusieurs exceptions

On peut placer plusieurs blocs `except` à la suite d'un `try` pour traiter des exceptions différentes.
Sur le même principe que les `if` / `elif` / `else`, un seul de ces blocs sera exécuté, le premier qui correspond à l'exception survenue.

Changeons d'exemple et passons à un cas plus réel de lecture de fichier.
Imaginons que l'on souhaite simplement lire un score dans un fichier.
Il nous faut alors une fonction prenant un chemin de fichier en paramètre et renvoyant son contenu sous forme de nombre.

Plusieurs exceptions peuvent survenir comme on l'a vu : le fichier peut ne pas exister ou ne pas avoir les bonnes permissions (`OSError`), peut contenir une valeur invalide (`ValueError`) et d'autres encore.

```python
def get_score(path):
    try:
        with open(path) as f:
            return int(f.read())
    except OSError:
        print("Impossible d'ouvrir le fichier")
    except ValueError:
        print('Score invalide')
```

Maintenant voilà ce que l'on obtient avec un fichier `score.txt` contenant `42` et un fichier `hello.txt` quelconque.

```python
>>> get_score('score.txt')
42
>>> get_score('hello.txt')
Score invalide
>>> get_score('not_found.txt')
Impossible d'ouvrir le fichier
```

Bien sûr, les blocs `except` ne peuvent attraper que les exceptions qui surviendraient pendant l'exécution du `try`.
Toute exception survenue avant leur échapperait.

```python
def get_score(path):
    with open(path) as f:
        try:
            return int(f.read())
        except OSError:
            print("Impossible d'ouvrir le fichier")
        except ValueError:
            print('Score invalide')
```

Dans l'exemple précédent, la conversion du contenu du fichier en nombre a toujours lieu dans le `try` donc l'erreur sur `hello.txt` serait bien traitée.
Mais l'ouverture du fichier se situe en dehors, nous ne gérons donc pas l'erreur `OSError` sur `not_found.txt`.

```python
>>> get_score('score.txt')
42
>>> get_score('hello.txt')
Score invalide
>>> get_score('not_found.txt')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in get_score
FileNotFoundError: [Errno 2] No such file or directory: 'not_found.txt'
```

Aussi, l'exécution du bloc `try` s'arrête à la première erreur rencontrée.
Cela signifie que tout son contenu n'est pas nécessairement exécuté, donc certaines variables définies dans le `try` n'existent peut-être pas.

```python
def get_score(path):
    try:
        with open(path) as f:
            content = f.read()
            score = int(content)
    except OSError:
        print("Impossible d'ouvrir le fichier")
    except ValueError:
        print('Score invalide')
    return score
```

Par exemple la fonction qui précède gère mal les exceptions : `score` ne sera jamais définie si une erreur est survenue, et donc le `return` échouera car accèdera à une variable inexistante.  
Quant aux variables `f` et `content` on ne sait pas si elles existent car cela dépend de l'endroit précis où est survenu l'erreur.
Pour une erreur à l'ouverture du fichier `content` ne sera pas définie, mais s'il s'agit d'une erreur lors de la conversion alors `content` contiendra sa bonne valeur.

Pour s'assurer que ces variables existent, il nous faut alors les définir dans tous les cas.
Soit en le faisant avant le `try` (puisque c'est du code qui sera toujours exécuté), soit en répétant la définition dans chaque clause `except`.

```python
def get_score(path):
    score = None

    try:
        with open(path) as f:
            content = f.read()
            score = int(content)
    except OSError:
        print("Impossible d'ouvrir le fichier")
    except ValueError:
        print('Score invalide')

    return score
```

#### Remontée d'erreurs

* Mécanisme de la remontée d'erreur
* Placer judicieusement les except
