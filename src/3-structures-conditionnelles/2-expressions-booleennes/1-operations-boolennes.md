### Opérations booléennes

#### Vocabulaire

Pour rappel, un test d'égalité peut s'évaluer à `True` (vrai) ou `False` (faux).
Il s'agit de deux valeurs qui forment un nouveau type de données, le type booléen (`bool` en Python).  
Ce nom provient de George Boole qui a introduit ce concept d'une valeur ne pouvant avoir que deux états, vrai ou faux.

C'est pourquoi on parle généralement d'opération ou d'expression booléenne pour qualifier une expression s'évaluant en un booléen.

Derrière les structures conditionnelles se cache aussi la notion de prédicat.
C'est le nom que l'on donne à l'expression booléenne qui conditionne la suite de l'exécution du bloc.  
Typiquement, un prédicat peut correspondre à une vérification d'une entrée utilisateur, pour s'assurer qu'un mot de passe est correct ou qu'un nombre se situe bien dans un certain intervalle.

#### Opérateurs

Outre l'égalité (`==`), plusieurs opérateurs de comparaison permettent d'obtenir des booléens.
On trouve ainsi l'opérateur de différence, `!=`, qui teste si deux valeurs sont différentes l'une de l'autre.

Cet opérateur s'utilise de la même manière que l'égalité, sur des valeurs de tous types.

```pycon
>>> 1 != 1
False
>>> 1 != 2
True
>>> 1 != 'abc'
True
>>> 1 != '1'
True
```

Sont aussi présents les opérateurs d'inégalités `<` et `>` pour tester les relations d'ordre :

* `a < b` teste si `a` est strictement inférieur à `b` ;
* `a > b` teste si `a` est strictement supérieur à `b`.

```pycon
>>> 1 < 2
True
>>> 1 > 2
False
```

Cette fois-ci l'opération n'est possible qu'entre deux valeurs compatibles, c'est-à-dire ordonnables l'une par rapport à l'autre.
Ce qui est par exemple le cas des entiers et des flottants.

```pycon
>>> 5 < 5.1
True
>>> 1.9 > 3
False
```

Les chaînes de caractères sont ordonnables les unes par rapport aux autres, selon un ordre appelé « ordre lexicographique », une extension au classique ordre alphabétique.  
Il est ainsi possible de tester les inégalités entre deux chaînes de caractères.

```pycon
>>> 'renard' > 'loup'
True
>>> 'loup' < 'lama'
False
```

L'ordre lexicographique définit explicitement l'ordre de tous les caractères, selon la table unicode.
Il faut savoir par exemple que bien que les lettres soient dans l'ordre alphabétique, les majuscules sont considérées comme inférieures aux minuscules, et les lettres accentuées supérieures aux autres.

```pycon
>>> 'Loup' < 'lama'
True
>>> 'léopard' > 'loup'
True
```

Il n'est en revanche pas possible de comparer un nombre avec une chaîne de caractères, car aucune relation d'ordre n'existe entre ces deux types.

```pycon
>>> 5 > '4'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '>' not supported between instances of 'int' and 'str'
```

Enfin ces deux opérateurs possèdent des variantes `<=` et `>=` correspondant aux opérations « inférieur ou égal » et « supérieur ou égal » en mathématiques.

```pycon
>>> 1 < 1
False
>>> 1 <= 1
True
>>> 'abc' <= 'abc'
True
```

#### Priorités des opérateurs

La priorité entre opérateurs ne concerne pas que les opérations arithmétiques, les opérateurs de comparaison sont eux aussi concernés.
Tous ces opérateurs possèdent la même priorité, qui se situe juste en-dessous de l'addition.
Ainsi, toutes les opérations arithmétiques sont prioritaires sur les opérations de comparaison.

On a donc `3 + 5 == 2 * 4` qui est équivalent à `(3 + 5) == (2 * 4)`.

```pycon
>>> 3 + 5 == 2 * 4
True
>>> (3 + 5) == (2 * 4)
True
```

Les opérations booléennes étant des expressions comme les autres, il est tout à fait possible d'en stocker le résultat dans des variables.
Il est alors courant d'entourer l'expression de parenthèses pour bien la distinguer de l'opérateur `=` d'assignation.

```pycon
>>> equal = (5 == 8)
>>> equal
False
>>> inferior = ('abc' < 'def')
>>> inferior
True
```
