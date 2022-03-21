### Minimum d'une liste

On a déjà réalisé quelques algorithmes dans les derniers chapitres.
Pour illustrer les boucles `for` je vous montrais par exemple comment identifier le maximum d'une liste.
Identifier le minimum suit donc le même principe.

On avait imaginé deux solutions au problème.
La première consisterait à itérer sur tous les éléments de la liste, et à vérifier pour chaque élément qu'il est le minimum en le comparant avec les autres éléments.  
S'il existe un autre élément plus petit, alors l'élément courant ne peut pas être le minimum.

```python
numbers = [3, 2, 5, 8, 4, 7, 9, 1, 6]
minimum = numbers[0]

for i in numbers[1:]:
    is_minimum = True
    for j in numbers:
        if j < i:
            is_minimum = False
    if is_minimum:
        minimum = i

print('Le minimum est', minimum)
```

Cet algorithme fonctionne mais est particulièrement inefficace : il nous faut re-parcourir la liste complète pour chaque élément.
Cela revient à dire que pour une liste de N éléments on va devoir effectuer un total de N² comparaisons.

L'autre algorithme que nous avions implémenté était bien meilleur.
On pouvait simplement ne comparer chaque élément qu'avec les éléments précédents.  
Et comme le minimum des éléments précédents est déjà connu à chaque instant, on peut juste comparer chaque élément avec le minimum déjà connu.

```python
numbers = [3, 2, 5, 8, 4, 7, 9, 1, 6]
minimum = numbers[0]

for i in numbers[1:]:
    if i < minimum:
        minimum = i

print('Le minimum est', minimum)
```

En plus d'être plus efficace (on ne réalise ici que N comparaisons pour une liste de taille N), le code est bien plus concis est lisible.

Même si la différence de performances ne saute pas aux yeux, parce que nos listes sont de tailles modestes, cela peut devenir problématique quand on commence à beaucoup l'utiliser ou l'appliquer à des données en plus grande quantité.  
Cette notion de nombre d'opérations effectuées en fonction du nombre d'éléments en entrée est ce que l'on appelle la complexité algorithmique[^complexite].

On dit de notre premier algorithme qu'il a une complexité quadratique (N² opérations pour N éléments), et du second qu'il a une complexité linéaire (N opérations).

[[i]]
| Cet algorithme n'est présenté que comme un exercice, dans la vie de tous les jours il serait bien sûr inutile puisque Python possède déjà une fonction `min` qui fait le boulot.

[^complexite]: Pour en apprendre davantage sur la complexité algorithmique, je vous invite à consulter [ce tutoriel](https://zestedesavoir.com/tutoriels/621/algorithmique-pour-lapprenti-programmeur/399_presentation-de-la-notion-de-complexite-algorithmique/2020_la-notion-de-complexite/).
