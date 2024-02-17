### Conventions

Un nom de variable ne peut pas être composé de n'importe quels caractères.
Il ne doit contenir que des lettres (minuscules ou majuscules), des chiffres et des _underscores_ (caractère `_`).
La seconde règle est que le nom ne peut pas commencer par un chiffre.

Ainsi, un nom ne peut pas contenir d'espaces ou de caractères spéciaux, contrevenir à ces règles produira des erreurs de syntaxe.

```pycon
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
Il est donc impossible de nommer une variable avec l'un des noms présents dans le tableau suivant.

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

```pycon
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

Les lettres majuscules sont par contre conventionnelles pour des variables définies dans le fichier et dont la valeur ne change jamais.
Par exemple une variable `MAX_POINTS_VIE` qui contient le nombre maximum absolu de points de vie possible.
On parle alors habituellement de constante même si ce concept n'existe pas en tant que tel en Python.

[[i]]
| On notera tout de même que les variables sont sensibles à la casse, c'est-à-dire qu'elles distinguent majuscules et minuscules.
| Ainsi `points_vie` et `POINTS_VIE` peuvent être définies comme deux variables distinctes et ne seront jamais mélangées.
|
| ```pycon
| >>> points_vie = 10
| >>> POINTS_VIE = 20
| >>> points_vie
| 10
| >>> POINTS_VIE
| 20
| ```

Aussi, il est déconseillé de nommer une variable d'un même nom qu'une fonction de Python, comme `abs`, `min` ou `max`.

On évitera enfin les noms `l`, `O` ou `I` qui portent à confusion car ne sont pas bien distinguables de 1 ou 0 avec certaines polices de caractères.

[[i]]
| Les différentes règles de style à appliquer en Python sont décrites dans la [PEP8](https://www.python.org/dev/peps/pep-0008/).  
| Il s'agit initialement d'un guide écrit par les développeurs de Python pour expliquer quelles sont les règles en vigueur dans le projet Python.
| Ce guide est ensuite devenu une référence pour de nombreux projets et aujourd'hui considéré comme un standard.
|
| Une section de la PEP8 est particulièrement dédiée au nommage : <https://www.python.org/dev/peps/pep-0008/#naming-conventions>.

#### La variable `_`

Autre convention, il est courant d'appeler `_` une variable dont on n'utilise pas le résultat.
Cela est utile dans des cas où il est nécessaire de préciser un nom de variable mais dont on ne veut pas vraiment conserver la valeur.
On verra ça par la suite avec les assignations multiples où `_` pourra servir à combler les trous.

La variable `_` a aussi un sens spécial dans l'interpréteur interactif : elle garde la trace de la dernière expression calculée et affichée.

```pycon
>>> 1 + 2
3
>>> _
3
>>> _ + 1
4
>>> _ + 1
5
```
