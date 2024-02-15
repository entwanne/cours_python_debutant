### Booléens

Ainsi, le type `bool` est un type composé de seulement deux valeurs, `True` et `False`.
Ces valeurs répondent à ce que l'on appelle [algèbre de Boole](https://zestedesavoir.com/tutoriels/2256/de-la-logique-aux-processeurs/lalgebre-de-boole/), qui définit les opérations logiques possibles entre les booléens.

#### Algèbre de Boole

L'opération la plus élémentaire est la négation logique (« NON ») qui se note `not` en Python.
C'est un opérateur unaire (qui ne prend qu'un seul opérande), qui consiste à calculer l'inverse du booléen : `True` devient `False` et inversement.

```pycon
>>> not True
False
>>> not False
True
```

Il est courant de représenter les opérations booléennes sous forme de tables de vérité.
C'est-à-dire de présenter un tableau associant à chaque valeur le résultat de l'opération.

Voici donc la table de vérité de l'opérateur `not` :

  `a`   | `not a`
--------|--------
`True`  | `False`
`False` | `True`

La négation d'une égalité est alors la même chose que la différence.

```pycon
>>> not 'abc' == 'def'
True
>>> 'abc' != 'def'
True
```

Mais il est aussi possible de combiner plusieurs booléens entre eux, de différentes manières.

La première est la conjonction (« ET ») qui permet de tester si deux valeurs sont vraies.
Avec `a` et `b` deux booléens, l'expression « a ET b » est vraie si et seulement si `a` est vrai et que `b` l'est aussi.

En Python, cet opérateur binaire (à deux opérandes) se note `and`.

```pycon
>>> True and True
True
>>> True and False
False
>>> 'abc' == 'zzz' and 3 > 0
False
```

Et sa table de vérité est la suivante.

  `a`   |   `b`   | `a and b`
--------|---------|----------
`True`  | `True`  | `True`
`True`  | `False` | `False`
`False` | `True`  | `False`
`False` | `False` | `False`

Enfin, l'autre opération que l'on trouve en Python sur les booléens est la disjonction (« OU », soit `or` en Python).
L'expression « a OU B » étant vraie si `a` est vrai ou que `b` l'est.

```pycon
>>> True or False
True
>>> False or False
False
>>> 'abc' == 'zzz' or 3 > 0
True
```

On note que le « OU » est inclusif, ce qui peut se différencier de l'usage courant.  
En effet quand on dit « a OU b » on a tendance à imaginer que c'est soit l'un soit l'autre (exclusif) mais pas les deux.
En informatique on considère que « a OU b » est vraie aussi si `a` et `b` sont vrais.

```pycon
>>> True or True
True
```

Voici donc la table de vérité du `or`.

  `a`   |   `b`   | `a or b`
--------|---------|----------
`True`  | `True`  | `True`
`True`  | `False` | `True`
`False` | `True`  | `True`
`False` | `False` | `False`

Ces opérateurs sont bien sûr composables les uns avec les autres pour former des expressions plus complexes.
On utilisera généralement des parenthèses pour isoler les différentes opérations et ne pas avoir à se soucier de leur priorité (voir plus loin).

```pycon
>>> (True or False) and not (True and False)
True
```

#### Conditions et priorités

Ces trois opérateurs peuvent donc s'utiliser au sein d'expressions booléennes pour introduire des blocs conditionnels et ainsi combiner en une seule clause plusieurs sous-conditions.

```python
username = input("Nom d'utilisateur : ")
password = input("Mot de passe : ")

if username == 'admin' and password == 'nimda':
    print('Vous êtes connecté')
else:
    print('Échec de la connexion')
```

Il est à noter que `and`, `or` et `not` sont les opérateurs en Python ayant la plus faible priorité.
Plus faible encore que les opérateurs de comparaison (`==`, `!=`, etc.).  
C'est pourquoi l'expression dans le code qui précède est équivalente à `(username == 'admin') and (password == 'nimda')`.

Aussi, `not` est prioritaire sur `and` qui est lui-même prioritaire sur `or`, comme on peut le voir dans le code suivant.

```pycon
>>> not True and False
False
>>> True or True and False
True
```

Mais ce comportement peut différer d'un langage de programmation à un autre, c'est pourquoi on utilisera toujours des parenthèses autour des sous-expressions booléennes combinant ces différents opérateurs, pour plus de clarté.

```pycon
>>> (not True) and False
False
>>> True or (True and False)
True
```

#### Conversions implicites et explicites

Bien que nous n'ayons pour le moment utilisé de blocs `if` qu'avec des expressions booléennes, il faut savoir que ceux-ci acceptent n'importe quelle expression, par exemple ici avec un `int`.

```pycon
>>> if 5 + 3 * 4:
...     print('Ça marche')
... 
Ça marche
```

En fait, toute valeur Python est implicitement convertible en booléen, et c'est cette conversion qu'opère Python sur les expressions qu'il rencontre dans un bloc conditionnel.

Ainsi, le nombre zéro (`0` ou `0.0`) et la chaîne vide (`''`) s'évaluent à `False`.
Alors que tous les autres nombres (même négatifs) et chaînes de caractères s'évaluent à `True`

Cette facilité permet de simplifier certaines conditions, comme pour tester si une chaîne entrée n'est pas vide.

```python
name = input('Bonjour, qui est tu ? ')

if name:
    print('Bonjour', name)
else:
    print('Erreur de saisie')
```

Dans cet exemple, `if name:` est équivalent à `if name != ''`, car une chaîne vide s'évaluera toujours à `False`.
On préférera donc généralement utiliser cette version raccourcie plutôt qu'ajouter une comparaison inutile.

Il reste bien sûr possible -- quand cela est nécessaire -- de convertir explicitement une valeur en booléen, en utilisant le type `bool` comme une fonction sur la valeur que l'on souhaite convertir.  
La conversion se fera selon les mêmes règles que celles décrites au-dessus.

```pycon
>>> bool('hello')
True
>>> bool('')
False
>>> bool(-5.8)
True
>>> bool(0)
False
```

De la même manière, il n'est pas utile de comparer un booléen à `True` ou `False` dans une condition, ce qui ne fait que rallonger l'expression sans y apporter plus de sens.
Avec `result` le résultat d'une opération booléenne (`result = (name == 'admin')`), on écrira donc simplement `if result: ...` et jamais `if result == True: ...`.  
Et on écrira `if not result: ...` plutôt que `if result == False: ...`.

#### Comparaisons chaînées

Les opérateurs de comparaison que l'on a vus peuvent s'enchaîner afin de créer plus facilement des opérations booléennes entre plusieurs valeurs.

Par exemple, si l'on souhaite tester l'égalité entre trois valeurs `a`, `b` et `c`, on pourra écrire `a == b == c` plutôt que `a == b and b == c`.

```pycon
>>> 10 == 10 == 10
True
>>> 10 == 10 == 5
False
```

Ou encore pour tester une inégalité, `0 < temp < 100` est plus simple à lire que `0 < temp and temp < 100`.

```pycon
>>> 0 < 25 < 100
True
>>> 0 < -25 < 100
False
>>> 0 < 125 < 100
False
```
