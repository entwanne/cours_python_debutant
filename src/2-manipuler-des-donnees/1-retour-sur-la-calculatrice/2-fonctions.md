### Fonctions

Mais notre calculatrice ne s'arrête pas à ces simples opérateurs, elle est aussi capable d'appliquer des fonctions sur nos nombres.
Une fonction est une opération à laquelle on va donner une valeur et qui va en renvoyer une nouvelle.

Par exemple, `abs` est la fonction qui calcule la valeur absolue d'un nombre (il s'agit grossièrement de la valeur de ce nombre sans le signe `+` ou `-`).  
Pour appliquer une fonction sur une valeur, on écrit le nom de la fonction suivi d'une paire de parenthèses, entre lesquelles on place notre valeur.

```python
>>> abs(-5)
5
>>> abs(3.2)
3.2
```

Une autre fonction mathématique de Python est `round` qui permet de calculer l'arrondi à l'entier d'un nombre flottant.

```python
>>> round(1.4)
1
>>> round(1.5)
2
```

Ces fonctions sont prédictibles : pour une même valeur en entrée le résultat sera toujours le même.
Le résultat d'une fonction est une valeur que l'on peut utiliser au sein d'autres opérations.

```python
>>> abs(-2) * (round(3.7) - 1)
6
```

On parle d'une « expression » pour désigner une ligne de Python qui peut s'évaluer et produire une valeur.
Les expressions peuvent se composer de sous-expressions et de divers opérateurs.
Un appel de fonction est donc une expression comme une autre.

La valeur que l'on envoie à la fonction est appelée un argument. `abs(-5)` se lit « appel de la fonction `abs` avec l'argument `-5` », et `5` est la valeur de retour de la fonction.
Les exemples précédents présentaient des appels avec un unique argument.
Mais certaines fonctions vont pouvoir recevoir plusieurs arguments, qui devront alors être séparés par des virgules lors de l'appel.

C'est le cas de la fonction `round`, qui prend un deuxième argument optionnel permettant de préciser combien de chiffres après la virgule on souhaite conserver.
Par défaut on n'en conserve aucun.

```python
>>> round(2.3456)
2
>>> round(2.3456, 1)
2.3
>>> round(2.3456, 2)
2.35
>>> round(2.3456, 3)
2.346
>>> round(2.3456, 4)
2.3456
```

D'autres fonctions vont recevoir plusieurs arguments, c'est le cas par exemple de `min`, qui renvoie la plus petite valeur de ses arguments.
À l'inverse, `max` renvoie la plus grande valeur.

```python
>>> min(4, 9, -2, 7)
-2
>>> max(4, 9, -2, 7)
9
```

Une fonction est toujours associée à un « ensemble de définition », on ne peut que lui donner des arguments qui sont cohérents avec le calcul qu'elle doit réaliser.
`abs(1, 2)` et `min(1)` sont par exemple des appels qui n'ont pas de sens et qui produiront des erreurs.

```python
>>> abs(1, 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: abs() takes exactly one argument (2 given)
>>> min(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not iterable
```

Nous verrons par la suite ce que signifient précisément ces erreurs.
Pour l'instant, retenez qu'une fonction attend un certain nombre d'arguments, de certains types. Et que déroger à ces règles produit des erreurs.
