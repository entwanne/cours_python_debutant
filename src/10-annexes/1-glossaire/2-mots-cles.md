### Tableau des mots-clés

Voici le tableau de l'ensemble des mots-clés de Python :

+------------+------------+------------+------------+------------+
| `False`    | `await`    | `else`     | `import`   | `pass`     |
+------------+------------+------------+------------+------------+
| `None`     | `break`    | `except`   | `in`       | `raise`    |
+------------+------------+------------+------------+------------+
| `True`     | `class`    | `finally`  | `is`       | `return`   |
+------------+------------+------------+------------+------------+
| `and`      | `continue` | `for`      | `lambda`   | `try`      |
+------------+------------+------------+------------+------------+
| `as`       | `def`      | `from`     | `nonlocal` | `while`    |
+------------+------------+------------+------------+------------+
| `assert`   | `del`      | `global`   | `not`      | `with`     |
+------------+------------+------------+------------+------------+
| `async`    | `elif`     | `if`       | `or`       | `yield`    |
+------------+------------+------------+------------+------------+

À cela on pourrait aussi ajouter les mots-clés `match` et `case`, qui sont bien des mots-clés mais pas des noms réservés (vous pouvez nommer une variable `match` ou `case` sans soucis).

* `False` : Valeur `False` du type booléen.
* `None` : Valeur `None`, qui représente l'absence de valeur.
* `True` : Valeur `True` du type booléen.
* `and` : Opération booléenne ET (conjonction).
  ```python
  >>> True and False
  False
  ```
* `as` : Permet une assignation si couplé à un autre mot-clé. (`import`, `with`, `except`).
  ```python
  import math as m
  ```
  ```python
  with open('file') as f:
      ...
  ```
  ```python
  try:
      ...
  except ValueError as e:
      ...
  ```
* `assert` : Assertion, échoue si l'expression donnée est fausse (les assertions ne sont pas exécutées si Python est lancé en mode optimisé `-O`).
  ```python
  assert 5 == 4 + 1
  ```
* `async` : Introduit une fonction asynchrone (`async def`)[^python_35][^non_aborde].
* `await` : Attend un résultat asynchrone (depuis une fonction asynchrone)[^python_35][^non_aborde].
* `break` : Permet de sortir immédiatement d'une boucle. En cas de boucles imbriquées, le mot-clé affecte la boucle intérieure uniquement.
  ```python
  while condition:
      ...
      break
  ```
* `case` : Introduit un motif de filtrage dans un bloc `match`[^python_310][^non_aborde].
* `class` : Définit une classe en programmation orientée objet[^class].
* `continue` : Permet de passer à l'itération suivante de la boucle. En cas de boucles imbriquées, le mot-clé affecte la boucle intérieure uniquement.
  ```python
  while condition:
      ...
      continue
  ```
* `def` : Définit une fonction.
  ```python
  def func(a, b):
      ...
  ```
* `del` : Supprime une variable ou un élément d'un conteneur.
  ```python
  del var
  ```
  ```python
  del container[key]
  ```
* `elif` : Condition _sinon-si_ dans un bloc conditionnel.
  ```python
  if condition:
      ...
  elif other_condition:
      ...
  ```
* `else` : Condition _sinon_ dans un bloc conditionnel, ou deuxième clause d'une expression conditionnelle.
  ```python
  if condition:
      ...
  else:
      ...
  ```
  ```python
  true_val if condition else false_val
  ```
  Peut aussi se placer après un bloc `for`/`while` (réagir en cas de sortie de boucle prématurée) ou `try` (réagir si tout s'est bien passé).
* `except` : Attrape une exception après un bloc `try`.
  ```python
  try:
      ...
  except ValueError:
      ...
  ```
* `finally` : Exécute des instructions dans tous les cas après un bloc `try`.
  ```python
  try:
      ...
  finally:
      ...
  ```
* `for` : Introduit une boucle d'itération. Peut aussi introduire une intension (liste, ensemble, etc.).
  ```python
  for item in iterable:
      ...
  ```
  ```python
  [... for item in iterable]
  ```
* `from` : Réalise un import dans l'espace de nom courant, conjointement avec `import` (`from ... import`).
  ```python
  from collections import Counter
  ```
* `global` : Déclare une variable comme étant globale.
  ```python
  global var
  ```
* `if` : Introduit un bloc conditionnel avec une condition _si_. Peut aussi introduire une expression conditionnelle ou une condition de filtrage dans une intension.
  ```python
  if condition:
      ...
  ```
  ```python
  true_val if condition else false_val
  ```
  ```python
  [... for item in iterable if condition]
  ```
* `import` : Réalise un import, utilisé seul (import simple) ou conjointement avec `from` (`from ... import`).
  ```python
  import math
  ```
  ```python
  from collections import Counter
  ```
* `in` : Opérateur d'appartenance, teste si une valeur est présente dans un conteneur.
  ```python
  value in container
  ```
* `not in` : Opérateur de non-appartenance, teste si une valeur est absente d'un conteneur.
  ```python
  value not in container
  ```
* `is` : Opérateur d'identité.
  ```python
  value is None
  ```
* `is not` : Opérateur de non-identité.
  ```python
  value is not None
  ```
* `lambda` : Introduit une fonction lambda.
  ```python
  lambda x: x**2
  ```
* `match` : Introduit un bloc de filtrage par motif[^python_310][^non_aborde].
* `nonlocal` : Déclare une variable comme non-locale[^nonlocal].
* `not` : Opération booléenne NON (négation).
  ```python
  >>> not True
  False
  ```
* `or` : Opération booléenne OU (disjontion).
  ```python
  >>> True or False
  True
  ```
* `pass` : Ne fait rien, ne renvoie rien (utile quand un bloc indenté est attendu).
  ```python
  if True:
      pass
  ```
* `raise` : Lève une exception.
  ```python
  raise ValueError()
  ```
* `return` : Renvoie une valeur depuis une fonction (la fonction se termine au premier `return`).
  ```python
  def f(a, b):
      return ...
  ```
* `try` : Introduit un bloc de traitement d'exception.
  ```python
  try:
      ...
  except:
      ...
  ```
* `while` : Introduit une boucle sur une condition.
  ```python
  while condition:
      ...
  ```
* `with` : Introduit un gestionnaire de contexte (pour ouvrir un fichier par exemple).
  ```python
  with open('file') as f:
      ...
  ```
* `yield` : Produit une valeur depuis un générateur[^non_aborde].

[^python_35]: Introduit en [Python 3.5](https://zestedesavoir.com/articles/175/sortie-de-python-3-5/).
[^python_310]: Introduit en [Python 3.10](https://zestedesavoir.com/articles/4041/sortie-de-python-3-10/).
[^non_aborde]: Non abordé dans ce cours.
[^class]: Non abordé, mais c'est l'objet du cours [sur la programmation objet en Python](https://zestedesavoir.com/tutoriels/1253/la-programmation-orientee-objet-en-python/).
[^nonlocal]: Non abordé, mais introduit dans [ce tutoriel sur les scopes](https://zestedesavoir.com/tutoriels/3163/variables-scopes-et-closures-en-python/).
