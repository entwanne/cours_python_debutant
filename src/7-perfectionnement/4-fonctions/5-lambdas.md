### Fonctions lambdas

Les conditions peuvent être des expressions, les boucles (`for`) peuvent être des expressions, les définitions de fonction peuvent aussi être des expressions.

Je dis bien les définitions car les fonctions en elles-mêmes, nous l'avons vu précédemment, sont déjà des valeurs et donc des expressions à part entière.

```python
>>> def add_one(n):
...     return n + 1
... 
>>> add_one
<function add_one at 0x7f662ecf61f0>
>>> x = add_one
>>> x(5)
6
```

Leur définition, c'est le bloc `def` qui définit leur nom, leurs paramètres et leur code ; lui ne peut pas être assigné à une variable ou passé en argument.

La solution se trouve du côté des fonctions lambdas (ou « fonctions anonymes ») introduites par le mot-clé `lambda`.
Ce mot-clé, suivi d'un `:` et d'une expression permet de définir une fonction sans nom, l'expression étant le code de la fonction.  
Une fonction lambda ne peut alors être composée que d'une unique expression.

```python
>>> lambda: 42
<function <lambda> at 0x7f616ffe93a0>
```

Il s'agit d'une fonction à part entière, et si nous l'appelons nous obtenons bien 42 comme réponse.

```python
>>> (lambda: 42)()
42
```

[[i]]
| Les parenthèses autour de la lambda sont nécessaires pour la gestion des priorités, `lambda: 42()` serait compris comme `lambda: (42())` et n'aurait pas de sens.

La lambda est une expression et peut donc être assignée à une variable.

```python
>>> get_42 = lambda: 42
>>> get_42
<function <lambda> at 0x7f616ffe9430>
>>> get_42()
42
```

Tout comme les fonctions, les lambdas peuvent recevoir des paramètres en tous genres, il suffit pour cela de préciser la liste des paramètres avant le signe `:`.

```python
>>> addition = lambda a, b: a + b
>>> addition(3, 5)
8
```

Mais l'intérêt principal des fonctions comme expressions réside dans le fait de pouvoir être passées comme arguments à d'autres fonctions.
Souvenez-vous par exemple de la fonction `sorted` et de son paramètre `key` recevant une fonction.  
Avec une lambda, il n'est pas nécessaire de définir une fonction au préalable : on peut directement passer l'expression de tri sous forme de lambda à la fonction.

Voici par exemple un tri de mots ne tenant pas compte de la casse (différence entre lettres minuscules et capitales), en s'appuyant sur la conversion en minuscules des chaînes.

```python
>>> words = ['poire', 'Ananas', 'banane', 'abricot', 'FRAISE']
>>> sorted(words, key=lambda w: w.lower())
['abricot', 'Ananas', 'banane', 'FRAISE', 'poire']
```
