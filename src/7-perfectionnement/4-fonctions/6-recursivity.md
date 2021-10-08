### Fonctions récursives

Deux grands modèles s'opposent en informatique lorsqu'il est question de répéter des tâches : le modèle itératif et le modèle récursif.

Le modèle itératif, nous le connaissons, c'est celui des boucles.
On place notre tâche dans une boucle et celle-ci sera donc répétée un certain nombre de fois.

Le modèle récursif est assez différent dans sa conception, il repose sur des fonctions.
L'idée étant que la fonction s'appelle elle-même, provoquant ainsi une répétition, on parle alors de fonction récursive.

> En mode itératif, marcher c'est mettre un pied devant l'autre et recommencer. En mode récursif, marcher c'est mettre un pied devant l'autre et marcher.
Source: <https://twitter.com/framaka/status/1327220641150496768>

C'est un concept issu des mathématiques qui se définit assez bien et intuitivement, nous l'appliquons même généralement sans le savoir.  
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
    return 1 + my_len(s[1:])
```

Là encore, nous avons oublié de prévoir la condition de fin (renvoyer 0 sur une chaîne vide), et patatra !

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

En fait, chaque appel récursif occupe un peu de mémoire dans notre programme, pour stocker le contexte de la fonction (les arguments qui lui sont passés par exemple).
Quand nous empilons les appels récursifs, la mémoire utilisée croît, jusqu'à atteindre une limite.
En Python c'est l'interpréteur qui fixe arbitrairement une limite de 1000 appels.

[[i]]
| Certains langages (les langages fonctionnels notamment) mettent en œuvre des optimisations pour supprimer cette limite, mais ce n'est pas le cas de Python qui est assez peu porté sur le modèle récursif.


#### Récursions croisées

La récursivité ne se limite pas à une fonction seule, il est aussi possible de croiser des fonctions qui s'appelleraient les unes les autres.

Par exemple, comment déterminer si un nombre `n` est impair ? En regardant si `n-1` est pair !
Et pour savoir si `n-1` est pair on teste si `n-2` est impair.
On répète cela jusqu'à zéro que l'on sait pair (et donc non impair).

En Python, cela nous donnerait les deux fonctions suivantes.

```python
def odd(n): # impair
    if n == 0:
        return False
    return even(n - 1)

def even(n): # pair
    if n == 0:
        return True
    return odd(n - 1)
```

Qui se comportent bien comme on veut pour calculer la parité des nombres.

```python
>>> odd(5)
True
>>> even(5)
False
>>> odd(4)
False
>>> even(4)
True
```

Bien sûr je ne présente ces fonctions qu'à titre d'exemple.
Les fonctions récursives étant déjà assez rares en Python pour les raisons expliquées plus haut, les récursions croisées le sont encore plus.  
Et l'exemple présenté ci-dessus est particulièrement inefficace (on peut directement tester la parité d'un nombre avec `n % 2`).

Aussi, préférez dans la mesure du possible opter pour des solutions itératives.
