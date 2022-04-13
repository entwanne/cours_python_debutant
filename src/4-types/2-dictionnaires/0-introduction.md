## Les dictionnaires

Les listes permettent de stocker un ensemble d'éléments en associant chaque élément à un index numérique.

Mais cela n'est pas adapté à toutes les données, toutes ne représentent pas une séquence de valeurs.

Comment par exemple représenter un répertoire téléphonique ? Avec une liste de listes où chaque sous-liste serait composée de deux éléments : un nom et un numéro ?

Par exemple on pourrait avoir

```python
phonebook = [['Alice', '0633432380'], ['Bob', '0663621029'], ['Alex', '0714381809']]
```

Ça fonctionnerait mais c'est loin d'être idéal, il faudrait se souvenir d'utiliser `[0]` pour le nom et `[1]` pour le numéro, et ça demanderait de parcourir toute la liste chaque fois que l'on voudrait chercher un numéro.

Heureusement pour nous, les dictionnaires sont une structure de données bien plus adaptée à ce genre de problématique.
