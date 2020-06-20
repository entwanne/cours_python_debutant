### Rappel sur les types mutables

On a vu que certains types étaient modifiables (mutables) et d'autres non.
Les types mutables que nous avons étudiés sont les listes et les dictionnaires.

Cela signifie qu'une fois ces objets instanciés, il est possible d'en modifier la valeur.
Ce qui n'est pas la même chose que réaffecter une variable car cela affecte toutes les références de l'objet.

````python
>>> a = b = {}
>>> a[0] = True
>>> a
{0: True}
>>> b
{0: True}
```

Cela n'est pas possible avec un nombre, une chaîne de caractères ou un tuple.

Ainsi, toute référence vers un objet mutable va permettre d'en modifier le contenu, ce sera donc le cas aussi pour ces objets passés en arguments à des fonctions.
Il faudra alors être très attentif sur ceux-ci.
