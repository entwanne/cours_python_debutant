### Des séquences de valeurs

Une liste en Python peut être vue comme une séquence de valeurs.
Imaginez une simple ligne de tableau avec des cases, chaque case contenant une valeur.

+---+---+---+---+---+---+---+
| 5 | 3 | 2 | 8 | 6 | 7 | 3 |
+---+---+---+---+---+---+---+

Ceci est la représentation d'une liste de 7 nombres entiers.
On la noterait en Python de la manière suivante :

```python
numbers = [5, 3, 2, 8, 6, 7, 3]
```

On utilise donc des crochets pour délimiter la liste, et des virgules pour séparer les valeurs les unes des autres.

Chaque case de la liste est associée à une position (ou index). Ainsi la case en première position contient la valeur 5, celle en deuxième position contient la valeur 3, etc.
L'ordre des éléments dans une liste est donc important, et celui-ci est libre (mes valeurs n'ont par exemple pas besoin d'être rangées en ordre croissant).

```python
>>> [1, 2, 3]
[1, 2, 3]
>>> [2, 3, 1]
[2, 3, 1]
```

On note que la case en septième (dernière) position contient aussi la valeur 3. Une même valeur peut être présente dans la liste à plusieurs positions.

La liste peut être vue comme une généralisation des chaînes de caractères : là où la chaîne est une séquance de caractères, la liste peut contenir des valeurs de tous types.
L'exemple précédent ne montre qu'une liste composée de nombres entiers (`int`), mais n'importe quelle valeur peut être contenue dans une liste.

```python
>>> ['abc', 'def']
['abc', 'def']
>>> [4.5, 1.8, -3.2]
[4.5, 1.8, -3.2]
```

Il faut voir les listes comme des ensembles de valeurs distinctes les unes des autres mais qui forment un tout.
Elles sont le reflet même des listes de la vie courante : une liste de courses, une liste d'élèves, une liste de notes, etc.

```python
courses = ['pain', 'œufs', 'lait', 'pâtes', 'tomates']
eleves = ['Julie', 'Martin', 'Sami', 'Natacha']
notes = [12, 9, 16, 13]
```

On peut aussi construire une liste composée de valeurs de types différents.
On verra par la suite que l'important est d'avoir une manière unique de traiter l'ensemble des éléments.

```python
notes = [12, 8.5, 16, 12.5]
items = ['salut', 42, True, 1.5]
```

Une liste peut aussi ne contenir aucun élément (liste vide), on la définit alors à l'aide d'une simple paire de crochets `[]`.  
Un autre cas particulier est celui des listes contenant un seul élément, où la virgule est facultative puisqu'il n'y a pas de valeurs à séparer.

```python
>>> []
[]
>>> [4]
[4]
>>> ['salut',]
['salut']
```

Quand on initialise une liste avec beaucoup d'éléments, il arrive que la ligne de définition soit assez longue.

```python
words = ['sur', 'zeste', 'de', 'savoir', 'vous', 'pouvez', 'trouver', 'des', 'contenus', 'sur', 'des', 'sujets', 'variés']
```

Il est alors intéressant d'aérer le tout pour que ça devienne plus lisible.
Python permet d'effectuer des retours à la ligne dans la définition d'une liste, entre les valeurs.  
Attention, un retour à la ligne ne remplace pas la virgule séparant les valeurs, qui reste obligatoire.

On prendra l'habitude d'indenter les valeurs par rapport à la ligne d'ouverture de la liste.

```python
words = [
    'sur',
    'zeste',
    'de',
    'savoir',
    'vous',
    'pouvez',
    'trouver',
    'des',
    'contenus',
    'sur',
    'des',
    'sujets',
    'variés',
]
```

Seule la dernière virgule, puisque suivie d'aucune valeur, est facultative.
Je la laisse par commodité et pour ne pas faire de différences entre les lignes.

Une liste se définit aussi par le nombre d'éléments qu'elle contient, sa taille.
Cette taille sera amenée à évoluer au cours du déroulement du programme, la liste pouvant gagner ou perdre des élémentss suivant certaines opérations.
