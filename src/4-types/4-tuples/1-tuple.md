### Les tuples

Les tuples (parfois traduits en n-uplets) sont des équivalents non modifiables des listes.
C'est-à-dire des séquences d'un nombre fixe d'éléments : après la définition, on ne peut ni ajouter, ni supprimer, ni remplacer d'élément.

Un tuple est généralement défini par une paire de parenthèses contenant les éléments séparés par des virgules.
Comme une liste, un tuple peut contenir des éléments de types différents.

```python
>>> (1, 2, 3)
(1, 2, 3)
>>> ('a', 'b', 'c')
('a', 'b', 'c')
>>> (42, '!')
(42, '!')
```

On notera tout de même que les parenthèses sont facultatives, c'est la virgule qui définit réellement un tuple.
Comme pour les opérations arithmétiques, les parenthèses servent en fait à gérer les priorités.

```python
>>> 1, 2, 3
(1, 2, 3)
>>> 1, 2, 3 * 3
(1, 2, 9)
>>> (1, 2, 3) * 3
(1, 2, 3, 1, 2, 3, 1, 2, 3)
```

Il faut bien penser à cette virgule lorsque l'on cherche à définir un tuple contenant un unique élément.
En effet, `(1)` étant une notation équivalente à `1`, il est nécessaire d'en ajouter une pour expliciter le tuple.

```python
>>> (1)
1
>>> (1,)
(1,)
>>> 1,
(1,)
```

Par ailleurs, il est possible de définir un tuple vide à l'aide d'une simple paire de parenthèses (il n'y a dans ce cas pas de confusion avec d'autres utilisations possibles des parenthèses).

```python
>>> ()
()
```

J'utiliserai principalement le terme de tuple, mais il faut savoir qu'on rencontre parfois d'autres noms suivant la taille du tuple.
On parle ainsi parfois de couple pour des tuples de 2 éléments, des triplets pour 3, etc.

Par exemple il est courant de dire que la méthode `items` des dictionnaires renvoie des couples clé/valeur.

```python
>>> phonebook = {'Alice': '0633432380', 'Bob': '0663621029', 'Alex': '0714381809'}
>>> for couple in phonebook.items():
...     print(couple)
... 
('Alice', '0633432380')
('Bob', '0663621029')
('Alex', '0714381809')
```

#### Utilisations des tuples

On peut parfois se demander quand utiliser un tuple et quand utiliser une liste.
Le tuple étant comparable à une liste non modifiable, il peut donc être utilisé pour toutes les opérations attendant une liste et ne cherchant pas à la modifier.
Il est même préférable si l'on sait qu'il ne sera jamais question de modification, ou encore que l'on veut l'empêcher.

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

Attention cependant, un tuple qui contient un élément modifiable pourra lui aussi être indirectement altéré.
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

On appelle cette seconde opération (assigner plusieurs variables depuis un tuple) l'_unpacking_, mais nous y reviendrons plus tard.
