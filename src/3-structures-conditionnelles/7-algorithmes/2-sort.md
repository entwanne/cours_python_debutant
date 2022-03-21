### Tri d'une liste

Maintenant que l'on sait identifier le plus petit élément d'une liste on peut passer à un problème un peu plus compliqué, celui du tri d'une liste.
C'est un problème algorithmique très classique qui consiste à ranger dans l'ordre les éléments d'une liste.

Une approche simple consiste à trouver le minimum pour le retirer de la liste et l'ajouter à une nouvelle liste d'éléments triés.
L'opération est alors recommencée jusqu'à épuiser la liste de départ.  
C'est ce qu'on appelle le tri par sélection.

```python
numbers = [3, 2, 5, 8, 4, 7, 9, 1, 6]
sorted_numbers = []

while numbers:
    m = min(numbers)
    sorted_numbers.append(m)
    i = numbers.index(m)
    del numbers[i]

print(sorted_numbers)
```

Cet algorithme n'est pas le plus efficace puisqu'il effectue environ N² opérations (le calcul du minimum comptant comme N comparaisons) pour une liste de N éléments.
Il faut savoir que d'autres algorithmes plus performants existent tels que le tri rapide et le tri fusion, mais qui sont hors de portée pour le moment.

Python implémente lui-même son propre algorithme de tri inspiré des tris précédents, le _Tim sort_ (du nom de Tim Peters, contributeur de Python).
Ce tri est accessible par la fonction `sorted`.

```pycon
>>> numbers = [3, 2, 5, 8, 4, 7, 9, 1, 6]
>>> sorted(numbers)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

[[i]]
| Ainsi, avant de vous lancer tête baissée dans un algorithme, pensez à regarder si Python ne propose pas déjà une solution pour vous.
