### Généralités

Une valeur en Python peut-être le résultat de n'importe quelle expression (opération, appel de fonction, accès à une variable, etc.).
Toute valeur possède un type qui définit les opérations qui lui sont applicables.

#### Conversions

Certaines valeurs peuvent être converties d'un type vers un autre.
Pour cela, les types s'utilisent comme des fonctions, où la valeur à convertir est donnée en argument.

```pycon
>>> int('123')
123
>>> float(42)
42.0
>>> list('abc')
['a', 'b', 'c']
>>> str(1.5)
'1.5'
```

#### Comparaisons

Les opérateurs d'égalité (`==`) et de différence (`!=`) sont applicables à tous les types.

```pycon
>>> 2 == 2
True
>>> 1.5 == 3.7
False
>>> 'abc' != 'def'
True
>>> [1, 2, 3] == [1, 2, 3]
True
```

Ces opérations sont de plus compatibles entre valeurs de types différents.

```pycon
>>> 2 == 2.0
True
>>> 2 == 2.5
False
>>> 2 != '2'
True
>>> 2 == [2]
False
```
