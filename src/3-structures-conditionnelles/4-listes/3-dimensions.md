### Listes à plusieurs dimensions

Je présentais en introduction les listes comme des séquences, des lignes d'éléments.
L'analogie est bonne, d'autant que nos listes précédentes ne contenaient que des types de données simples : nombres ou chaînes de caractères.

Mais les listes peuvent contenir toutes sortes de données, même des plus complexes comme… d'autres listes.

```
>>> items = [1, 2, [3, [4]]]
>>> items
[1, 2, [3, [4]]]
```

Pour accéder aux éléments des sous-listes, on pourra simplement chaîner les opérateurs `[]`.

```pycon
>>> items[2][1][0]
4
>>> items[2][0] = 5
>>> items
[1, 2, [5, [4]]]
```

Quand une liste est composée uniquement de sous-listes, elle peut alors prendre la forme d'un tableau.
Comme ici avec une liste représentant un plateau de morpion.

```python
morpion = [
    ['x', ' ', ' '],
    ['o', 'o', ' '],
    ['x', ' ', ' '],
]
```

Que l'on peut représenter sous la forme du tableau suivant.

+-------+-------+-------+
| `'x'` | `' '` | `' '` |
+-------+-------+-------+
| `'o'` | `'o'` | `' '` |
+-------+-------+-------+
| `'x'` | `' '` | `' '` |
+-------+-------+-------+

Il s'agit ici d'un tableau à deux dimensions (lignes et colonnes).
Mais les listes n'ont pas de limite et l'on pourrait alors voir d'autres subdivisions s'il y avait un niveau supplémentaire de listes.

#### Problème de la multiplication

[[q]]
| Je vous parlais de l'opérateur de multiplication des listes pour les concaténer, mais que se passe-t-il si on l'utiliste sur des listes à plusieurs dimensions ?

Et bien ça ne fonctionne pas comme prévu !  
En effet cet opérateur ne crée pas de copies mais duplique les références à une même valeur.
La même sous-liste est alors répétée plusieurs fois dans la liste, provoquant des comportements intattendus en cas de modifications.

```pycon
>>> grid = [[1, 2, 3]] * 2
>>> grid
[[1, 2, 3], [1, 2, 3]]
>>> grid[0].append(4)
>>> grid
[[1, 2, 3, 4], [1, 2, 3, 4]]
```

Le code précédent étant en fait équivalent à :

```pycon
>>> line = [1, 2, 3]
>>> grid = [line, line]
>>> grid
[[1, 2, 3], [1, 2, 3]]
>>> line.append(4)
>>> grid
[[1, 2, 3, 4], [1, 2, 3, 4]]
```

Ce comportement de duplication des références n'est pas propre aux listes multi-dimensionnelles.  
Une code tel que `[0] * 10` duplique aussi 10 fois la référence à la valeur `0`, mais cela ne pose pas de problème particulier car les nombres ne sont pas des valeurs modifiables.
Le comportement apparaît donc problématique dans le cas des sous-listes en raison de leur mutabilité.

Nous verrons dans le chapitre prochain comment contrer ce problème en construisant nos listes itérativement, en attendant je vous conseille de simplement ne pas utiliser la multiplication dans des cas comme celui-ci.

```pycon
>>> grid = [[1, 2, 3], [1, 2, 3]]
>>> grid[0].append(4)
>>> grid
[[1, 2, 3, 4], [1, 2, 3]]
```
