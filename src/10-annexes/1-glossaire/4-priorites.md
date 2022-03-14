### Priorité des opérateurs

#### Ordre d'évaluation des expressions

Les expressions en Python sont toujours évaluées de la gauche vers la droite, à l'exception près des assignations où la partie droite sera évaluée avant la partie gauche.

Ainsi, dans les exemples fictifs suivants, `expr1` sera toujours évaluée avant `expr2`, elle-même avant `expr3`, etc. jusque `expr5`.

```python
expr1, expr2, expr3, expr4
(expr1, expr2, expr3, expr4)
{expr1: expr2, expr3: expr4}
expr1 + expr2 * (expr3 - expr4)
expr1(expr2, expr3, *expr4, **expr5)
expr3, expr4 = expr1, expr2
```

#### Tableau des priorités

Aussi, dans une même expression, les opérations seront exécutées par ordre de priorité.
Dans le tableau suivant, les opérations de rang inférieur seront exécutées prioritairement à celles de rang supérieur (`**` est évalué avant `/`).

+------+-----------------------+--------------------------------------------------+
| Rang | Opérateur             | Description                                      |
+======+=======================+==================================================+
|  1   | `(...)`, `[...]`,     | Expressions entre parenthèses, crochets (listes) |
|      | `{...}`               | ou accolades (dictionnaires, ensembles)          |
+------+-----------------------+--------------------------------------------------+
|  2   | `x(...)`, `x[...]`,   | Appels, accès aux éléments et attributs          |
|      | `x.attr`              |                                                  |
+------+-----------------------+--------------------------------------------------+
|  3   | `await`               | Expressions `await`                              |
+------+-----------------------+--------------------------------------------------+
|  4   | `**`                  | Exponentiations[^exponentiation]                 |
+------+-----------------------+--------------------------------------------------+
|  5   | `+`, `-`, `~`         | Opérateurs unaires                               |
+------+-----------------------+--------------------------------------------------+
|  6   | `*`, `@`, `/`, `//`,  | Opérateurs binaires de multiplications/divisions |
|      | `%`                   |                                                  |
+------+-----------------------+--------------------------------------------------+
|  7   | `+`, `-`              | Opérateurs binaires d'addition/soustraction      |
+------+-----------------------+--------------------------------------------------+
|  8   | `<<`, `>>`            | Décalages de bits                                |
+------+-----------------------+--------------------------------------------------+
|  9   | `&`                   | Conjonctions bit-à-bit, intersections            |
+------+-----------------------+--------------------------------------------------+
| 10   | `^`                   | _XOR_ bit-à-bit, différences symétriques         |
+------+-----------------------+--------------------------------------------------+
| 11   | `|`                   | Disjonctions bit-à-bit, unions                   |
+------+-----------------------+--------------------------------------------------+
| 12   | `in`, `not in`, `is`, | Comparaisons, tests d'appartenance et d'identité |
|      | `is not`, `<`, `<=`,  |                                                  |
|      | `>`, `>=`, `!=`, `==` |                                                  |
+------+-----------------------+--------------------------------------------------+
| 13   | `not`                 | Négations booléennes                             |
+------+-----------------------+--------------------------------------------------+
| 14   | `and`                 | Conjonctions booléennes                          |
+------+-----------------------+--------------------------------------------------+
| 15   | `or`                  | Disjonctions booléennes                          |
+------+-----------------------+--------------------------------------------------+
| 16   | `if - else`           | Expressions conditionnelles                      |
+------+-----------------------+--------------------------------------------------+
| 17   | `lambda`              | Fonctions lambda                                 |
+------+-----------------------+--------------------------------------------------+
| 18   | `:=`                  | Expressions d'assignation                        |
+------+-----------------------+--------------------------------------------------+
| 19   | `,`                   | Séparateurs, tuples                              |
+------+-----------------------+--------------------------------------------------+

[^exponentiation]: On note cependant que l'opérateur `**` est moins prioritaire qu'un opérateur unaire sur son opérande de droite.
Ainsi `10**-2` s'évalue comme `10**(-2)` (mais `-10**2` s'évalue bien comme `-(10**2)`).

--------------------

Les exemples de cette section sont tirés de la page de documentation [Référence sur les expressions](https://docs.python.org/fr/3/reference/expressions.html), sur laquelle vous trouverez plus d'informations au sujet des expressions et des priorités des opérateurs.
