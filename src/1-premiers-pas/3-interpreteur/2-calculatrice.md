### Une machine à calculer

Mais il ne se limite pas à cela, nous pouvons lui demander de calculer des opérations, comme une calculatrice.
Tout ce que nous avons à faire, c'est d'exprimer le calcul dans les termes qu'il comprend.

Nous avons de la chance, Python utilise la même notation que nous pour l'addition.

```python
>>> 5 + 3
8
```

Plus fort encore, on peut lui demander d'additionner plusieurs nombres !

```python
>>> 1 + 2 + 3
6
```

Je mets des espaces mais ceux-ci sont facultatifs. Ils sont néanmoins préférables pour une bonne lisibilité du code.

```python
>>> 1+2+3
6
```

Python connaît aussi la soustraction, et les nombres négatifs.

```python
>>> 8 - 5
3
>>> 1 - 10
-9
>>> 1 - -10
11
```

Autre opération courante, Python sait évaluer la multiplication entre deux nombres.
Mais il faut parler dans son langage, l'opérateur pour la multiplication est `*`.

```python
>>> 4 * 5
20
>>> 6 * 7 * -1
-42
```

Et bien sûr, les priorités entre les opérations sont gérées.
Quand en mathémtiques on écrit « 1 + 2 × 3 », la multiplication est prioritaire sur l'addition, donc elle est exécutée en premier, d'où le résultat de « 7 ».
Il en est de même en Python :

```python
>>> 1 + 2 * 3
7
```

Et comme en maths, on peut utiliser des parenthèses pour prioriser certaines opérations.

```python
>>> (1 + 2) * 3
9
```

Les parenthèses permettent aussi de jouer sur l'associativité des opérateurs, `1 - 2 - 3` n'est pas la même chose que `1 - (2 - 3)`

```python
>>> 1 - 2 - 3
-4
>>> 1 - (2 - 3)
2
```

Tout ce que nous demandons à Python doit être exprimé dans la syntaxe qu'il comprend -- ici des nombres et des opérations, mais nous verrons par la suite qu'il est possible de bien plus.  
Dans le cas contraire, Python nous annoncera gentilment qu'il ne comprend pas ce que nous lui demandons, que la syntaxe est incorrecte.

```python
>>> il fait beau aujourd'hui
  File "<stdin>", line 1
    il fait beau aujourd'hui
          ^
SyntaxError: invalid syntax
>>> 1!
  File "<stdin>", line 1
    1!
     ^
SyntaxError: invalid syntax
```
