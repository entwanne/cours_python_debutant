### Utilisations des tuples

On peut parfois se demander quand utiliser un tuple et quand utiliser une liste.
Le tuple étant comparable à une liste non modifiable, il peut donc être utilisé pour toutes les opérations attendant une liste et ne cherchant pas à la modifier.
Il est même préférable de l'utiliser si l'on sait qu'il ne sera jamais question de modification, ou si l'on veut empêcher toute modification.

Mais il y a aussi des opérations qui ne sont possibles qu'avec les tuples.
Étant non modifiables, ils peuvent être utilisés en tant que clés de dictionnaires.

```python
>>> cells = {(0, 0): 'x', (0, 1): '.', (1, 0): '.', (1, 1): 'x'}
>>> cells[(1, 0)]
'.'
>>> cells[(1, 1)] = ' '
>>> cells
{(0, 0): 'x', (0, 1): '.', (1, 0): '.', (1, 1): ' '}
```

Les parenthèses sont encore une fois facultatives lors des accès.

```python
>>> cells[0, 0]
'x'
```

Cette structure permet ainsi de représenter d'une grille de données où chaque case est associée à ses coordonnées.

--------------------

[[a]]
| Attention cependant, un tuple qui contient un élément modifiable pourra lui aussi être indirectement altéré.

Par exemple si un tuple contient une liste, rien n'empêche d'ajouter des éléments à cette liste.

```python
>>> events = ('29/05/2019', ['anniversaire', 'soirée'])
>>> events[1].append('rdv coiffeur')
>>> events
('29/05/2019', ['anniversaire', 'soirée', 'rdv coiffeur'])
```

Un tel tuple ne pourra donc pas être utilisé comme clé de dictionnaire, parce qu'il contient une liste qui ne peut pas être utilisée comme tel.

```python
>>> {events: None}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

Mais beaucoup d'utilisations des tuples sont tous simplement implicites.
C'est en effet une manière de faire des assignations multiples de variables.

```python
>>> a, b = 1, 2
>>> a
1
>>> b
2
```

Techniquement, cela revient à écrire `(a, b) = (1, 2)`, ou encore :

```python
>>> tmp = (1, 2)
>>> (a, b) = tmp
```

[[i]]
| On appelle cette seconde opération (assigner plusieurs variables depuis un tuple) l'_unpacking_, mais nous y reviendrons plus tard.
