### Généralités

Une valeur en Python peut-être le résultat de n'importe quel expression (opération, appel de fonction, accès à une variable, etc.)
Toute valeur possède un type qui définit ses opérations.

#### Conversions

Certaines valeurs peuvent être converties d'un type vers un autre.
Pour cela, les types s'utilisent comme des fonctions, où la valeur à convertir est donnée en argument.

#### Comparaisons

Les opérateurs d'égalité (`==`) et de différence (`!=`) sont applicables à tous les types.

```python
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

```python
>>> 2 == 2.0
True
>>> 2 == 2.5
False
>>> 2 != '2'
True
>>> 2 == [2]
False
```
