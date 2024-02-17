### Booléens

Le type booléen (`bool`) permet de représenter les valeurs `True` (vrai) et `False` (faux).
Ces valeurs peuvent être le résultat d'une opération booléenne comme les opérateurs de comparaison (`==`, `!=`, `<`, etc.).

#### Conversions

Toute valeur Python peut être interprétée comme un booléen (par conversion implicite) :

* Le nombre zéro (`0`, `0.0`) vaut `False`.
* Les conteneurs vides (chaîne vide, liste vide) valent `False`.
* Toute valeur qui ne vaut pas explicitement `False` vaut `True`.

Il est aussi possible de convertir explicitement une valeur en booléen en faisant appel au type booléen.
Les règles de conversion sont les mêmes que celles énoncées ci-dessus.

```pycon
>>> bool(5)
True
>>> bool(0.0)
False
>>> bool('abc')
True
>>> bool([])
False
```

#### Opérations

Trois opérateurs existent sur les booléens : `not` (unaire), `and` et `or` (binaires), répondant chacun à une table de vérité.

  `a`   | `not a`
--------|--------
`True`  | `False`
`False` | `True`

  `a`   |   `b`   | `a and b`
--------|---------|----------
`True`  | `True`  | `True`
`True`  | `False` | `False`
`False` | `True`  | `False`
`False` | `False` | `False`

  `a`   |   `b`   | `a or b`
--------|---------|----------
`True`  | `True`  | `True`
`True`  | `False` | `True`
`False` | `True`  | `True`
`False` | `False` | `False`

Ces opérateurs sont présentés comme renvoyant toujours `True` ou `False`, mais ce n'est en vérité pas toujours le cas.
Étant donné que toute valeur peut être vue comme un booléen, il suffit de renvoyer une valeur qui sera interprétée comme `True` ou `False`.

Prenons le cas de `and` avec une opération `a and b` :

* Si `a` vaut `False`, le résultat sera forcément `False`. Donc `and` fait un raccourci et ne regarde même pas `b`. Dans ce cas la valeur renvoyée est `a` (qui peut être interprétée comme `False`).
* Si `a` vaut `True`, alors `and` renverra simplement `b`, puisque la conversion de `b` en booléen sera le résultat de l'opération.

```pycon
>>> [] and 5
[]
>>> ['foo'] and 5
5
>>> ['foo'] and 0
0
>>> 5 and True
True
```

Le même genre de raccourci existe pour `or`, qui renvoie `a` si `a` vaut `True` et `b` sinon.

```pycon
>>> ['foo'] or 5
['foo']
>>> [] or 5
5
>>> [] or 0
0
>>> 0 or True
True
```

On notera enfin en termes de conversions que les booléens eux-mêmes sont aussi implicitement convertis en nombres lorsque utilisés comme tels.
On aura ainsi `True` converti en `1` et `False` en `0`.

```pycon
>>> False + 2 * True
2
```
