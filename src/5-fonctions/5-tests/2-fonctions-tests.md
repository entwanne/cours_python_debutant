### Fonctions de tests

#### Assertions

Il existe en Python un mot-clé, `assert`, qui permet de tester une expression booléenne.  
Si cette expression s'évalue à `True`, il ne se passe rien.

```pycon
>>> assert 1 == 1
```

Mais si l'expression s'évalue à `False`, alors une erreur de type `AssertionError` est levée.

```pycon
>>> assert 1 == 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
```

[[a]]
| Attention cependant, les assertions ne doivent avoir un rôle que lors du développement.
| Elles peuvent en effet être désactivées (et donc n'avoir aucun effet même si évaluées à `False`) en production (notamment si les optimisations de l'interpréteur sont activées).  
| Aucun problème pour des tests puisqu'ils seront exécutés dans un environnement de développement ou de tests.

[[i]]
| Vous pouvez d'ailleurs essayer en lançant un script contenant des assertions avec `python -O script.py`, celles-ci n'ont alors plus aucun effet.

#### Tests unitaires

Le but maintenant va être de réaliser des assertions sur des appels à notre fonction.
On veut que pour une entrée donnée on obtienne le retour attendu.  
Par exemple `assert my_sum([1, 2, 3]) == 6`.

Afin d'avoir quelque chose de facilement reproductible, on va placer notre assertion dans une fonction `test_my_sum` qu'il nous suffira de réexécuter pour lancer la suite de tests.
On va en profiter pour ajouter quelques autres assertions.

```python
def test_my_sum():
    assert my_sum([1, 2, 3]) == 6
    assert my_sum([-1, 0, 1]) == 0
    assert my_sum([42]) == 42
```

Puis on l'exécute.

```pycon
>>> test_my_sum()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in test_my_sum
AssertionError
```

Voilà déjà une première erreur, sur la première assertion (_line 2_).
Et en effet, si on regarde de plus près, on voit que la fonction ne renvoie rien.

```pycon
>>> my_sum([1, 2, 3])
```

On corrige donc en ajoutant un `return result` en fin de fonction, et on relance les tests.

```python
def my_sum(numbers):
    result = numbers[0]
    size = len(numbers) - 1
    for i in range(1, size):
        result += numbers[i]
    return result
```

```pycon
>>> test_my_sum()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in test_my_sum
AssertionError
```

Toujours une erreur sur la même assertion, quel est le soucis cette fois ?
Nous verrons plus loin quelques outils d'aide au débugage, on va pour le moment regarder « manuellement ».

```pycon
>>> my_sum([1, 2, 3])
3
>>> my_sum([1, 2, 3, 4])
6
>>> my_sum([1, 2, 3, 4, 5])
10
>>> my_sum([11, 2, 3, 4, 5])
20
```

Il semble bien que c'est le dernier élément de la liste qui est ignoré.  
On peut ajouter un `print(i)` dans la boucle de notre fonction pour nous en assurer.

Quel est le soucis ? On a oublié que `range(a, b)` itérait sur les entiers `i` tels que `a <= i < b` et non `a <= i <= b`.
On a donc calculé `size = len(numbers) - 1` comme index du dernier élément alors qu'il aurait fallu l'index après le dernier, simplement `size = len(numbers)`.
Ce genre d'erreur est très courant et porte un nom, c'est une _off-by-one error_, une erreur de décalage de 1.

On corrige le code de notre fonction, et on relance.

```python
def my_sum(numbers):
    result = numbers[0]
    size = len(numbers)
    for i in range(1, size):
        result += numbers[i]
    return result
```

```pycon
>>> test_my_sum()
```

Cette fois-ci, il ne se passe rien, c'est donc que toutes les assertions sont bonnes et que les tests sont validés.  
Est-ce que pour autant notre fonction est bonne ?
Cela dépend justement des tests.

Quand on teste, il est important d'identifier quels cas peuvent potentiellement être problématiques.
Ici on a testé avec des listes de nombres entiers positifs, des négatifs, zéro, c'est très bien.  
Mais on n'a pas testé de nombres flottants, on n'a pas testé de tuples.
On n'a pas non plus testé le cas d'une liste vide.

Pour ne pas trop surcharger notre fonction `test_my_sum` de cas en tous genres, on va la découper en plusieurs petites fonctions pour séparer les cas bien précis.
Il sera ainsi plus facile d'identifier quel genre de problème fait buguer notre fonction.

Par commodité on gardera pour le moment une fonction `test_my_sum` générale pour appeler toutes nos autres fonctions et avoir ainsi un unique point d'entrée.
On verra par la suite qu'il est possible d'avoir beaucoup mieux avec les bons outils de tests.

```python
def test_my_sum_int():
    assert my_sum([1, 2, 3]) == 6
    assert my_sum([-1, 0, 1]) == 0
    assert my_sum([42]) == 42

def test_my_sum_float():
    assert my_sum([1.0, 2.0, 3.0]) == 6.0
    assert my_sum([0.1, 0.2, 0.3]) == 0.6

def test_my_sum_tuple():
    assert my_sum((1, 2, 3)) == 6

def test_my_sum_empty():
    assert my_sum([]) == 0
    assert my_sum(()) == 0

def test_my_sum():
    test_my_sum_int()
    test_my_sum_float()
    test_my_sum_tuple()
    test_my_sum_empty()
```

C'est l'heure du test !

```pycon
>>> test_my_sum()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in test_my_sum
  File "<stdin>", line 3, in test_my_sum_float
AssertionError
```

Ah, la deuxième assertion (_line 3_) des tests sur les flottants ne fonctionne pas.

```pycon
>>> my_sum([0.1, 0.2, 0.3])
0.6000000000000001
```

Et oui, souvenez-vous, l'arithmétique sur les flottants n'est pas la même chose que l'arithmétique sur les nombres décimaux.
Ici c'est notre test qui est faux, il s'attend à obtenir `0.6` alors que `0.1 + 0.2 + 0.3 == 0.6000000000000001`.

Il existe des fonctions pour tester l'égalité entre flottants avec un seuil de tolérace, nous découvrirons ça dans un prochain chapitre.
Pour le moment, on va simplement comparer notre résultat avec celui d'une addition entre flottants.

```python
def test_my_sum_float():
    assert my_sum([1.0, 2.0, 3.0]) == 1.0 + 2.0 + 3.0
    assert my_sum([0.1, 0.2, 0.3]) == 0.1 + 0.2 + 0.3
```

Mais c'est aussi quelque chose à quoi il faudra faire attention, les problèmes peuvent aussi bien se situer dans la fonction à tester que dans les tests eux-mêmes.

On relance une nouvelle fois nos tests.

```pycon
>>> test_my_sum()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 5, in test_my_sum
  File "<stdin>", line 2, in test_my_sum_empty
  File "<stdin>", line 2, in my_sum
IndexError: list index out of range
```

Maintenant, c'est le test sur la liste vide qui plante.
Mais on n'obtient pas une `AssertionError`, c'est une `IndexError` qui est levée.
Parce que ce n'est pas l'assertion qui a échoué, une erreur est survenue avant.

Si on regarde à la ligne indiquée dans la fonction `my_sum`, on voit `result = numbers[0]`.
En effet, sur une liste vide il n'y a pas de premier élément (index 0), d'où l'erreur `IndexError`.

Comme correction, on pourrait apporter une pré-condition en début de fonction pour traiter explicitement le cas de la liste vide en renvoyant directement zéro.
Ainsi, la suite de la fonction ne serait pas exécutée et on éviterait de rencontrer l'erreur.

```python
def my_sum(numbers):
    if not numbers: # une liste vide s'évalue à False
        return 0
    result = numbers[0]
    size = len(numbers)
    for i in range(1, size):
        result += numbers[i]
    return result
```

Et maintenant, ça marche.

```pycon
>>> test_my_sum()
```

Cette fois-ci, nous couvrons l'ensemble des cas que nous souhaitions vérifier.
Nous ne testons pas la fonction sur une chaîne de caractères ou d'autres types incohérents car nous savons qu'elle n'est pas prévue pour fonctionner dans ces conditions.

[[i]]
| Bien sûr, la fonction `my_sum` est inutilement compliquée, elle n'était là que dans un but d'exercice pour montrer comment apparaissaient les erreurs et quelles stratégies on pouvait adopter pour les corriger.
| En voici une autre version bien plus lisible et elle aussi dépourvue de bugs.

```python
def my_sum(numbers):
    result = 0
    for number in numbers:
        result += number
    return result
```

```pycon
>>> test_my_sum()
```
