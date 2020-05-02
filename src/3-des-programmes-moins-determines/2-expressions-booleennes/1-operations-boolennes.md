### Opérations booléennes

#### Booléens

Au chapitre précédent nous avons appris à créer des conditions basées sur l'égalité entre deux valeurs.
Mais l'égalité n'est pas l'unique expression conditionnelle possible et c'est ce que nous allons voir ici.

Pour rappel, un test d'égalité peut s'évaluer à `True` (vrai) ou `False` (faux).
Il s'agit de deux valeurs qui forment un nouveau type de données, le type booléen (`bool`).
C'est aussi pourquoi on parle plus généralement d'expression booléenne pour qualifier une expression s'évaluant en un booléen.

Derrière les structures conditionnelles se cache aussi la notion de prédicat.
C'est le nom que l'on donne au test qui peut être vrai ou faux et qui conditionne la suite de l'exécution.
Typiquement, un prédicat peut correspondre à une vérification d'une entrée utilisateur, pour vérifier qu'un mot de passe est correct, qu'un nombre se situe bien dans un certain intervalle, etc.

#### Opérateurs

Outre l'égalité (`==`), plusieurs opérateurs de comparaison permettent d'obtenir des booléens.
On retrouve par exemple de la même manière l'opérateur `!=` pour tester si deux valeurs sont différentes.

Cette opérateur s'utilise de la même manière que l'égalité, sur des valeurs de tous types.

```python
>>> 1 != 1
False
>>> 1 != 'abc'
True
```

Sont aussi présents les opérateurs d'inégalités `<` et `>` pour tester les relations d'ordre :

* `a < b` teste si `a` est strictement inférieur à `b` ;
* `a > b` teste si `a` est strictement supérieur à `b`.

```python
>>> 1 < 2
True
>>> 1 > 2
False
```

Cette fois-ci l'opération n'est possible qu'entre deux valeurs compatibles, c'est-à-dire ordonnables l'une par rapport à l'autre.
Mais c'est par exemple le cas des entiers et des flottants.

```python
>>> 5 < 5.1
True
```

Il est aussi possible de tester l'inégalité entre deux chaînes de caractères, ce qui aura pour effet de les comparer selon l'ordre lexicographique (une extension de l'ordre alphabétique).

```python
>>> 'renard' > 'loup'
True
>>> 'loup' < 'lama'
False
```

Il n'est en revanche pas possible de comparer un nombre avec une chaîne de caractères, car aucune relation d'ordre n'existe entre ces deux types.

```python
>>> 5 > '4'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '>' not supported between instances of 'int' and 'str'
```

Enfin ces deux opérateurs possèdent des variantes `<=` et `>=` correspondant aux opérations « inférieur ou égal » et « supérieur ou égal » en mathématiques.

```python
>>> 1 < 1
False
>>> 1 <= 1
True
```

#### Priorités des opérateurs

La priorité entre opérateurs ne concerne pas que les opérations arithmétiques, les opérateurs de comparaison sont eux aussi concernés.
Tous ces opérateurs possèdent la même priorité, qui se situe juste en-dessous de l'addition.
Ainsi, toutes les opérations arithmétiques sont prioritaires sur les opérations de comparaison.

On a donc `3 + 5 == 2 * 4` qui est équivalent à `(3 + 5) == (4 * 4)`.
