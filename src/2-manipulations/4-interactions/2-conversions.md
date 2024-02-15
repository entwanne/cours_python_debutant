### Conversions de types

Comme indiqué, `input` renvoie toujours une chaîne de caractères.
Comment faire alors pour demander à l'utilisateur un nombre afin de l'utiliser dans un calcul ?

Il y a pour cela des mécanismes pour convertir (dans la mesure du possible) une valeur d'un type vers un autre.
Je n'ai pour le moment présenté les types que comme des catégories regroupant des valeurs, mais ils ont en fait une existence propre en Python.  
Les nombres entiers correspondent ainsi au type `int` (pour _integer_, entier), les nombres à virgule au type `float` (flottant) et les chaînes de caractère au type `str` (pour _string_, chaîne).

Chacun de ces types peut être vu et utilisé comme une fonction permettant de convertir des données vers ce type.

```pycon
>>> int(4.2)
4
>>> float(4)
4.0
>>> str(4)
'4'
>>> int('10')
10
```

On voit dans ce dernier exemple que `'10'` et `10` sont des valeurs de types différents, la première est une chaîne de caractères et la seconde un nombre.
Il ne s'agit donc pas de la même chose, on ne peut pas exécuter les mêmes opérations sur les deux.

```pycon
>>> 10 + 1
11
>>> 10 + '1'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> '10' + '1'
'101'
```

Ainsi, pour en revenir à la demande initiale, afin traiter une entrée de l'utilisateur comme un nombre, il convient alors de convertir en `int` le retour d'`input`.

```pycon
>>> n = int(input('Choisis un nombre : '))
Choisis un nombre : 5
>>> print('Le double de', n, 'vaut', n * 2)
Le double de 5 vaut 10
```

Cependant, toute valeur n'est pas convertible d'un type vers un autre, par exemple la chaîne de caractères `'toto'` ne correspond à aucun nombre.
Lorsque la conversion est impossible, on verra survenir lors de l'appel une erreur explicitant le problème.

```pycon
>>> int('toto')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'toto'
```
