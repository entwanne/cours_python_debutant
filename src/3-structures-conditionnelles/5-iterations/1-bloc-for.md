### Le bloc for

Une liste possède donc un nombre « indéterminé » de valeurs -- on connaît sa taille au moment de l'exécution mais pas quand on écrit le code.
Pour réaliser un traitement (par exemple afficher un message) pour chacune des valeurs de la liste, il nous faudrait alors pouvoir la parcourir d'élément en élément.

En programmation ce genre de construction s'appelle une boucle, soit un bloc de code qui sera répété un certain nombre de fois.
Ici un bloc exécuté pour chaque élément de notre liste.

On a pour cela en Python le bloc `for` qui permet de parcourir une liste, d'itérer sur ses éléments.  
Sa syntaxe est la suivante :

```python
for element in values:
    ...
```

`values` étant ici notre liste, et `element` une variable qui sera successivement (à chaque tour de boucle) assignée à chaque élément de la liste.

`for` introduit un bloc, la ligne se termine donc par un `:` et est suivie d'un bloc indenté.

```pycon
>>> numbers = [1, 1, 2, 3, 5, 8, 13]
>>> for elem in numbers:
...     print('Nombre actuel :', elem)
... 
Nombre actuel : 1
Nombre actuel : 1
Nombre actuel : 2
Nombre actuel : 3
Nombre actuel : 5
Nombre actuel : 8
Nombre actuel : 13
```

On peut voir l'itération comme un curseur qui se déplace le long de notre liste.

`elem` est à l'intérieur de la boucle une variable tout ce qu'il y a de plus standard, on peut l'utiliser dans toutes nos opérations usuelles.

```pycon
>>> for elem in numbers:
...     result = 2 * elem + 1
...     print(result)
... 
3
3
5
7
11
17
27
```

Comme toute variable, il nous est aussi possible de la redéfinir, mais attention : il ne s'agit que d'une variable assignée à un élément de la liste, elle n'est en aucune manière liée à la liste.  
Donc redéfinir la variable n'aura aucun effet sur la liste qui restera inchangée.
Et le redéfinition n'est que temporaire, puisque la variable sera assignée à une nouvelle valeur de la liste à la prochaine itération.

```pycon
>>> for elem in numbers:
...     elem += 1
...     print(elem)
... 
2
2
3
4
6
9
14
>>> numbers
[1, 1, 2, 3, 5, 8, 13]
```
