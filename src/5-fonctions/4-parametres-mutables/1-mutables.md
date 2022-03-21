### Rappel sur les types mutables

On a vu que certains types étaient modifiables (mutables) et d'autres non.
Les types mutables que nous avons étudiés sont les listes et les dictionnaires.

Cela signifie qu'une fois ces objets instanciés, il est possible d'en modifier la valeur.
Ce qui n'est pas la même chose que réassigner une variable car cela affecte toutes les références vers l'objet.

```pycon
>>> a = b = {}
>>> a[0] = True
>>> a
{0: True}
>>> b
{0: True}
```

Cela n'est pas possible avec un nombre, une chaîne de caractères ou un tuple, qui ne peuvent pas être modifiés en tant que tels.
Et la réassignation d'une variable la fait pointer vers une nouvelle valeur, sans affecter les autres références à l'ancienne valeur.

```pycon
>>> a = b = 3
>>> a = 5
>>> a
5
>>> b
3
```

Ainsi, toute référence vers un objet mutable va permettre d'en modifier le contenu, ce sera donc le cas aussi pour ces objets passés en arguments à des fonctions.
Il faudra alors être très attentif sur ceux-ci.
