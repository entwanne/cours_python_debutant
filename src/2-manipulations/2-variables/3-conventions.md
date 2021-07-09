### Conventions

Un nom de variable ne peut pas être composé de n'importe quels caractères.
Il ne doit contenir que des lettres (minuscules ou majuscules), des chiffres et des _underscores_ (caractère `_`).
L'autre règle est que le nom ne peut pas commencer par un chiffre.

C'est-à-dire que le nom de peut pas contenir d'espaces ou de caractères spéciaux, contrevenir à ces règles produira des erreurs de syntaxe.

```python
>>> 0x = 1
  File "<stdin>", line 1
    0x = 1
     ^
SyntaxError: invalid token
>>> x y = 1
  File "<stdin>", line 1
    x y = 1
      ^
SyntaxError: invalid syntax
>>> x! = 1
  File "<stdin>", line 1
    x! = 1
     ^
SyntaxError: invalid syntax
```

Certains noms sont aussi réservés, car ils correspondent à des mots-clés Python.
Il est ainsi impossible de nommer une variable avec l'un des noms présent dans le tableau suivant.

+----------+------------+-----------+------------+----------+
| `False`  | `await`    | `else`    | `import`   | `pass`   |
+----------+------------+-----------+------------+----------+
| `None`   | `break`    | `except`  | `in`       | `raise`  |
+----------+------------+-----------+------------+----------+
| `True`   | `class`    | `finally` | `is`       | `return` |
+----------+------------+-----------+------------+----------+
| `and`    | `continue` | `for`     | `lambda`   | `try`    |
+----------+------------+-----------+------------+----------+
| `as`     | `def`      | `from`    | `nonlocal` | `while`  |
+----------+------------+-----------+------------+----------+
| `assert` | `del`      | `global`  | `not`      | `with`   |
+----------+------------+-----------+------------+----------+
| `async`  | `elif`     | `if`      | `or`       | `yield`  |
+----------+------------+-----------+------------+----------+

```python
Type "help", "copyright", "credits" or "license" for more information.
>>> def = 10
  File "<stdin>", line 1
    def = 10
        ^
SyntaxError: invalid syntax
```

--------------------

Il faut ajouter à cela quelques conventions de style.
Il est ainsi conseillé d'éviter les lettres majuscules et accentuées dans les noms de variables.
Par exemple, pour un nom de variable composé de plusieurs mots, on préfèrera `points_vie` à `pointsVie`.  
Mais on préférera souvent utiliser l'anglais pour garder une cohérence avec les mots-clés du langage et faciliter les collaborations, notre variable se nommerait donc plutôt `health_points`.

Aussi, il est déconseillé de nommer une variable d'une même nom qu'une fonction de Python, comme `abs`, `min` ou `max`.

On évitera enfin les noms `l`, `O` ou `I` qui portent à confusion car ne sont pas bien distingables de 1 ou 0 avec certaines polices de caractères.

Les différentes règles de style à appliquer en Python sont décrites dans la [PEP8](https://www.python.org/dev/peps/pep-0008/).
Il s'agit d'un guide écrit par les créateurs de Python pour aider à comprendre ces conventions.  
Une section de la PEP8 est particulièrement dédiée au nommage : <https://www.python.org/dev/peps/pep-0008/#naming-conventions>.

#### La variable `_`

Autre convention, il est courant d'appeler `_` une variable dont on n'utilise pas le résultat.
Cela est utile dans des cas où il est nécessaire de préciser un nom de variable mais dont on ne veut pas vraiment conserver la valeur.
On verra ça par la suite avec les assignations multiples où `_` pourra servir à combler les trous.

La variable `_` a aussi un sens spécial dans l'interpréteur interactif : elle garde la trace de la dernière expression calculée et affichée.

```python
>>> 1 + 2
3
>>> _
3
>>> _ + 1
4
>>> _ + 1
5
```
