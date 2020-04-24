### Opérations sur les listes

#### Opérations élémentaires

Tout comme les chaînes de caractères, les listes possèdent donc une taille.
Là encore, il est possible de connaître cette taille à l'aide d'un appel à la fonction `len`.

```python
>>> len(words)
13
```

Comme pour les chaînes toujours, il est possible d'accéder aux éléments de la liste à l'aide de l'opérateur `[]` associé à une position.
0 correspondant à la première position, 1 à la deuxième, etc.

```python
>>> print(words[8])
contenus
```

Les index négatifs sont aussi acceptés.

```python
>>> print(words[-2])
sujets
```

Et les listes sont aussi concaténables les unes aux autres, permettant de construire une grande liste en aggrégeant des plus petites.

```python
>>> [1, 1, 2, 3] + [5, 8, 13] + [21]
[1, 1, 2, 3, 5, 8, 13, 21]
```

Les listes possèdent différentes méthodes, par exemple pour rechercher et compter les éléments :

* `index` renvoie la première position trouvée pour un élément (et produit une erreur si l'élément n'est pas trouvé).
* `count` renvoie le nombre d'occurrences d'un élément dans la liste (donc 0 si l'élément n'est pas présent).

```python
>>> numbers = [5, 3, 2, 8, 6, 7, 3]
>>> numbers.index(2)
2
>>> numbers.index(3)
1
>>> numbers.index(7)
5
>>> numbers.count(3)
2
>>> numbers.count(8)
1
>>> numbers.count(9)
0
```

#### Mutabilité

Les listes sont des objets dits mutables, c'est-à-dire modifiables, ce qui n'est pas le cas des autres types que nous avons vu jusqu'ici.
En effet, sur les précédentes données que nous manipulions, leur valeur ne pouvait pas changer une fois qu'elles avaient été définies.  
Nous pouvions redéfinir une variable vers une nouvelle valeur (`a = 10; a += 1`), mais la valeur en question restait inchangée (`10` valait toujours `10`).

Sur les listes, nous pouvons librement remplacer certains éléments par d'autres, grâce à l'opérateur d'indexation (`[]`) couplé à une affectation (`=`).

```python
>>> words = ['salut', 'les', 'amis']
>>> words[2] = 'copains'
>>> words
['salut', 'les', 'copains']
```

Ici c'est bien la valeur même de la liste qui a été modifiée : on a altéré son contenu pour remplacer un élément, mais `words` est toujours la même liste.

On peut le mettre encore plus en évidence si l'on a deux variables qui référencent la même liste.

```python
>>> numbers = copy = [1, 2, 3, 4]
>>> numbers[0] = 10
>>> numbers
[10, 2, 3, 4]
>>> copy
[10, 2, 3, 4]
```

Et c'est d'ailleurs un comportement qui est souvent perçu comme une erreur par les débutants, mais il faut bien comprendre que `numbers` et `copy` sont deux étiquettes sur une même liste.
Ainsi, une modification de `numbers` est aussi une modification de `copy`.

Nos listes étant modifiables, elles possèdent certaines opérations pour insérer ou supprimer des éléments.

La méthode `append` permet comme son nom l'indique d'ajouter un nouvel élément en fin de liste (à la dernière position), augmentant donc de 1 la taille de la liste.

```python
>>> letters = ['a', 'b', 'c', 'd']
>>> len(letters)
4
>>> letters.append('e')
>>> letters
['a', 'b', 'c', 'd', 'e']
>>> len(letters)
5
```

Plus généralement, on trouve la méthode `insert` qui permet d'insérer un élément à une position (un index) particulière dans la liste, décalant ainsi s'il y en a les éléments à sa droite d'un cran.

```python
>>> letters.insert(0, 'à')
>>> letters
['à', 'a', 'b', 'c', 'd', 'e']
>>> letters.insert(6, 'é')
>>> letters
['à', 'a', 'b', 'c', 'd', 'e', 'é']
>>> letters.insert(3, 'ĉ')
>>> letters
['à', 'a', 'b', 'ĉ', 'c', 'd', 'e', 'é']
>>> letters.insert(-2, 'đ')
>>> letters
['à', 'a', 'b', 'ĉ', 'c', 'd', 'đ', 'e', 'é']
```

Comme vous le voyez, les index négatifs sont aussi acceptés.
Si la position est plus grande que la taille de la liste, la valeur sera insérée la fin.
De même, la valeur sera insérée au début pour une position négative dépassant la limite.

```python
>>> letters.insert(20, 'f')
>>> letters
['à', 'a', 'b', 'ĉ', 'c', 'd', 'đ', 'e', 'é', 'f']
>>> letters.insert(-50, 'å')
>>> letters
['å', 'à', 'a', 'b', 'ĉ', 'c', 'd', 'đ', 'e', 'é', 'f']
```

La méthode `pop` sert quant à elle à supprimer un élément de la liste.
Utilisée sans argument, elle en supprimera le dernier élément.
La méthode renvoie l'élément qui vient d'être supprimé, ce qui permet de le conserver dans une variable par exemple.

```python
>>> letters.pop()
'f'
>>> deleted = letters.pop()
>>> print(deleted, 'a été supprimée')
é a été supprimée
>>> letters
['å', 'à', 'a', 'b', 'ĉ', 'c', 'd', 'đ', 'e']
```

Mais la méthode peut aussi être appelée avec une position en argument, pour supprimer une valeur à un index particulier.

```python
>>> letters.pop(0)
'å'
>>> letters
['à', 'a', 'b', 'ĉ', 'c', 'd', 'đ', 'e']
```

On notera aussi l'opérateur `del` permettant lui aussi de supprimer une valeur mais sans la renvoyer.

```python
>>> del letters[3]
>>> letters
['à', 'a', 'b', 'c', 'd', 'đ', 'e']
```

#### Slicing

Nous avons vu pour l'instant comment accéder facilement à un élément d'une liste à partir de son index, grâce à l'opérateur d'indexation (`[]`).
Mais cet opérateur est plus puissant que cela et permet des utilisations plus avancées.

Il est en effet possible d'extraire plusieurs éléments en un seul appel, à l'aide d'une syntaxe particulière.
Il s'agit de préciser entre les crochets une position de début et une position de fin, séparées par un signe `:`.

La valeur renvoyée sera la liste des éléments compris entre ces deux positions (démarrant à la position de début et s'arrêtant juste avant la position de fin).

```python
>>> numbers = [1, 1, 2, 3, 5, 8, 13, 21]
>>> numbers[1:4]
[1, 2, 3]
>>> numbers[0:7]
[1, 1, 2, 3, 5, 8, 13]
```

On voit bien que `numbers[1:4]` nous renvoie la liste des éléments d'index compris entre 1 et 3 (inclus).
Ces opérations n'affectent pas la liste d'origine qui reste inchangée.

```python
>>> numbers
[1, 1, 2, 3, 5, 8, 13, 21]
```

Une fois de plus, il est possible d'utiliser des index négatifs pour se positionner à partir de la fin de la liste.

```python
>>> numbers[-5:-1]
[3, 5, 8, 13]
>>> numbers[1:-2]
[1, 2, 3, 5, 8]
```

Enfin, une autre facilité et que l'on peut omettre la position de début ou la position de fin.
Sans position de début on considère que l'on part du début de la liste (index `0`) et sans fin que l'on va jusqu'à la fin (index `len(numbers)`).

```python
>>> numbers[3:]
[3, 5, 8, 13, 21]
>>> numbers[:-3]
[1, 1, 2, 3, 5]
```

Si l'on omet le début et la fin, on récupère une liste contenant tous les éléments de la liste d'origine.

```python
>>> numbers[:]
[1, 1, 2, 3, 5, 8, 13, 21]
```

On peut aussi préciser une troisième valeur qui est le pas (par défaut de 1).
Ce pas indique combien d'index on passe entre chaque élément.

Ainsi, `[1:8:3]` correspondra aux index 1, 4 et 7 (3 de différence entre chaque index)

```python
>>> numbers[1:8:3]
[1, 5, 21]
```

Ou encore `[::2]` permettra d'extraire un élément sur deux.

```python
>>> numbers[::2]
[1, 2, 5, 13]
>>> numbers[1::2]
[1, 3, 8, 21]
```

Voilà pour ce qui est des accès en lecture, mais ces opérations sont aussi possibles pour la modification.

```python
>>> numbers[:2] = [2, 0]
>>> numbers
[2, 0, 2, 3, 5, 8, 13, 21]
```

La liste que l'on assigne n'a pas besoin de faire la même taille que le nombre d'éléments concernés par le _slicing_, ce qui peut alors modifier la longueur de la liste d'origine.

```python
>>> numbers[-1:] = [21, 34, 55]
>>> numbers
[2, 0, 2, 3, 5, 8, 13, 21, 34, 55]
>>> numbers[1:5] = []
>>> numbers
[2, 8, 13, 21, 34, 55]
```

Et ces opérations concernent aussi l'opérateur `del`.

```python
>>> del numbers[1:-1]
>>> numbers
[2, 55]
```

Enfin, l'opération de _slicing_ (en lecture seulement) est aussi disponible sur les chaînes de caractères, renvoyant donc une chaîne composée des caractères aux positions comprises dans l'intervalle..

```python
>>> 'pouetpouet'[3:-2]
'etpou'
```

Pour plus d'informations sur le _slicing_ en Python, je vous invite à découvrir ce tutoriel : <>.

#### Listes à plusieurs dimensions

* Imbriquer des listes dans des listes

Les listes précédentes ne contenaient que des types de données simples, nombres ou chaînes de caractères.
On pouvait alors les voir comme des tableaux de données à une dimension (une seule ligne).

Mais les listes peuvent contenir toutes sortes de données, même des plus complexes comme… des listes.

```
>>> items = [1, 2, [3, [4]]]
>>> items
[1, 2, [3, [4]]]
```

Pour accéder aux éléments des sous-listes, on pourra simplement chaîner les opérateurs `[]`.

```python
>>> items[2][1][0]
4
>>> items[2][0] = 5
>>> items
[1, 2, [5, [4]]]
```

Quand une liste est composée uniquement de sous-listes, elle peut alors prendre la forme d'un tableau à plusieurs dimensions.
Comme ici avec une liste représentant un plateau de morpion (tableau à 2 dimensions, lignes et colonnes).

```python
morpion = [
    ['x', ' ', ' '],
    ['o', 'o', ' '],
    ['x', ' ', ' '],
]
```
