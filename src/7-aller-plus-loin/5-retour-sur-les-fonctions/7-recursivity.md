### Fonctions récursives

Deux grands modèles s'opposent en informatique lorsqu'il est question de répéter des tâches : le modèle itératif et le modèle récursif.

Le modèle itératif, nous le connaissons, c'est celui des boucles.
On place notre tâche dans une boucle et celle-ci sera donc répétée un certain nombre de fois.

Le modèle récursif est assez différent dans sa conception, il repose sur des fonctions.
L'idée étant que la fonction s'appelle elle-même, provoquant ainsi une répétition, on parle alors de fonction récursive.

C'est un concept issu des mathématiques qui se défini assez bien et intuitivement, nous l'appliquons même généralement sans le savoir.  
Prenons par exemple la somme d'une liste de *N* nombres : de quoi s'agit-il ?
Simplement de l'addition entre le premier nombre de la liste et la somme des *N-1* autres nombres.

Par exemple `sum([1, 2, 3, 4, 5])` est égal à `1 + sum([2, 3, 4, 5])`, `sum([2, 3, 4, 5])` à `2 + sum([3, 4, 5])` et ainsi de suite.

Nous venons de définir la somme de manière récursive.
On a réduit une opération complexe (la somme de *N* nombres) à une succession d'opérations plus simples (une addition entre deux nombres) et un procédé récursif (exécuter à nouveau la procédure sur un ensemble restreint).

En Python, cela donnerait le code suivant.

```python
def my_sum(numbers):
    return numbers[0] + my_sum(numbers[1:])
```

Mais on remarque tout de suite un problème, on ne sait pas quand ça va s'arrêter. Cette fonction va-t-elle même s'arrêter ?
En l'occurrence oui, mais en provoquant une erreur.

```python
>>> my_sum([1, 2, 3, 4, 5])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in my_sum
  File "<stdin>", line 2, in my_sum
  File "<stdin>", line 2, in my_sum
  [Previous line repeated 3 more times]
IndexError: list index out of range
```

En effet, nos appels récursifs finissent par appeler `my_sum([])` qui échoue car n'a pas de premier élément (`numbers[0]`).

Le soucis c'est que c'est à nous de gérer explicitement la condition de fin et que nous ne l'avons pas fait.
Ici la condition de fin est facilement identifiable, la somme des nombres d'une liste vide est toujours nulle.
On devrait donc, dans le cas où l'on rencontre une liste vide, renvoyer directement zéro.

Nous pouvons ajouter cette condition à notre fonction récursive et constater que le comportement est alors bon.

```python
>>> def my_sum(numbers):
...     if not numbers:
...         return 0
...     return numbers[0] + my_sum(numbers[1:])
... 
>>> my_sum([1, 2, 3, 4, 5])
15
```

Mais il y a des cas où la condition de fin est moins évidente à trouver, cela pouvant mener à une récursion infinie.

#### Récursion infinie

Notre premier cas ne possédait pas de condition de fin mais s'est arrêté en raison d'une `IndexError`.
Que ce serat-il passé sans cette erreur ?

On peut prendre un cas assez similaire qui est de calculer la taille d'une chaîne de caractères.
Récursivement, la taille d'une chaîne se conçoit comme l'addition entre deux tailles de sous-chaînes, par exemple entre la taille du premier caractère (1) et la taille du reste.  
On a `len('abcdef')` égal à `1 + len('bcdef')`.

```python
def my_len(s):
    return s + my_len(s[1:])
```

Là encore, nous avons oublié de prévoir la condition de fin, et patatra !

```python
>>> my_len('abcdef')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in my_len
  File "<stdin>", line 2, in my_len
  File "<stdin>", line 2, in my_len
  [Previous line repeated 996 more times]
RecursionError: maximum recursion depth exceeded
```

Cette fois ce n'est pas une erreur dans notre code qui nous arrête, mais une erreur de Python lui-même qui nous indique que nous avons dépassé le nombre maximum de récursions.
Nous sommes entrés dans une récursion infinie.
