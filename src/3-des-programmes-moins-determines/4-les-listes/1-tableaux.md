### Des tableaux de valeurs

* Définition multi-lignes

Une liste en Python peut être vue comme un tableau de valeurs.
Un tableau au sens basique du terme : imaginez une ligne avec des cases, chaque case contenant une valeur.

+---+---+---+---+---+---+---+
| 5 | 3 | 2 | 8 | 6 | 7 | 3 |
+---+---+---+---+---+---+---+

Cette liste se représente en Python de la manière suivante :

```python
numbers = [5, 3, 2, 8, 6, 7, 3]
```

On utilise donc des crochets pour délimiter la liste, et des virgules pour séparer les valeurs.

Chaque case de la liste est associée à une position (ou index). Ainsi la case en première position contient la valeur 5, celle en deuxième position contient la valeur 3, etc.
L'ordre des éléments dans une liste est donc important, et celui-ci est libre (mes valeurs n'ont par exemple pas besoin d'être rangées en ordre croissant).

On note que la case en septième (dernière) position contient aussi la valeur 3. Une même valeur peut être présente dans la liste à plusieurs positions.

La liste peut aussi être vue comme une généralisation des chaînes de caractères : plutôt que ne contenir uniquement des caractères, la liste peut contenir des valeurs de tous types.
L'exemple précédent ne montre qu'une liste composée de nombres entiers (`int`), mais n'importe quelle valeur peut être contenue dans une liste.  
On peut même construire une liste de valeurs de types différents (on verra par la suite que l'important est d'avoir une manière unique de traiter chacune de ces valeurs).

```python
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
Cette taille sera amenée à évoluer au cours du déroulement du programme, la liste pouvant gagner ou perdre des valeurs suivant certaines opérations.

* Insister sur l'utilité des listes : présenter un semble de valeurs, de façon à toutes les traiter de la même manière
* Exemples concrets de listes : liste de course, liste d'élèves dans une classe