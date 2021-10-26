### Lever une exception

Les exceptions ont deux faces.
D'un côté il s'agit de les attraper pour faire un traitement correct des erreurs, ce qui était l'objet des précédentes parties.  
Mais de l'autre il est aussi question de lever des exceptions pour signaler les erreurs.

Souvenez-vous de notre factorielle qui ne gérait pas correctement les nombres négatifs en entrée, ce qui pouvait mener à des bugs[^boucles].

[^boucles]: Voir chapitre [Boucler sur une condition (`while`)](https://zestedesavoir.com/tutoriels/2514/un-zeste-de-python/3-structures-conditionnelles/6-boucles/).

La factorielle d'un nombre négatif n'a pas de sens et notre fonction ne devrait même pas les accepter.
Elle devrait lever une exception quand un tel nombre lui est donné, pour que l'appelant sache que la valeur passée est problématique.

Cela se fait avec le mot-clé `raise`.
Celui-ci peut simplement être suivi du type de l'exception à lever.
Il a pour effet de lever immédiatement l'exception voulue, et donc de couper tout traitement en cours.  
L'exception remontera ensuite la pile d'exécution du programme jusqu'à être attrapée.

```python
def factorielle(n):
    if n < 0:
        raise ValueError

    ret = 1
    for i in range(2, n + 1):
        ret *= i
    return ret
```

Nous utilisons ici une `ValueError` pour signaler qu'il s'agit d'un problème avec la valeur en elle-même.
Lors de l'appel, nous obtenons bien une exception `ValueError` en cas de valeur invalide.

```pycon
>>> factorielle(5)
120
>>> factorielle(-1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in factorielle
ValueError
```

Mais l'erreur n'est pas très explicite.
Nous savons par le type d'erreur qu'il est question de la valeur, mais aucune autre information ne nous est donnée.  
Parce que lors du `raise` nous avons simplement précisé un type sans plus d'informations.

Il est en fait possible d'appeler un type d'exception pour l'instancier, en lui donnant les arguments que l'on veut (généralement un message d'erreur), et d'utiliser cette instance pour le `raise`.
Les arguments seront accessibles via l'attribut `args` de l'exception reçue comme nous l'avons vu précédemment, et affichés si l'erreur est imprimée à l'écran.

Ainsi, on peut modifier notre `raise` pour ajouter à l'exception un message d'erreur.

```python
if n < 0:
    raise ValueError('Le nombre doit être positif')
```

```pycon
>>> factorielle(-1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in factorielle
ValueError: Le nombre doit être positif
```

On peut aller encore plus loin et générer un message d'erreur précis en ajoutant d'autres informations.

```python
if n < 0:
    raise ValueError(f'Le nombre doit être positif ({n} est négatif)')
```

```pycon
>>> factorielle(-1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in factorielle
ValueError: Le nombre doit être positif (-1 est négatif)
```

#### Hiérarchie des exceptions

Nous avons rencontré plusieurs types d'exceptions pour coller à différentes situations.
Il faut savoir que ces types sont hiérarchisés, afin de pouvoir traiter plus ou moins finement les erreurs qui surviennent.  
Ainsi, faire un `except` sur un type d'exception arrêtera les exceptions de ce type mais aussi de tous les types qui en descendent.

Par exemple, toutes les exceptions que nous avons vues descendent d'un même type `Exception` : cela signifie qu'il suffit d'attraper `Exception` pour les attraper toutes.[^chen]

[^chen]: Allez dire ça au Professeur Chen, il sera vert.

`TypeError` et `ValueError` sont alors deux des principales exceptions, la première indiquant une erreur dans le type des données et la seconde sur la valeur elle-même (le type correspond mais la valeur est incohérente).
`ValueError` rassemble aussi des exceptions plus précises telles que `UnicodeDecodeError` et `UnicodeEncodeError` que nous avons déjà rencontrées.

`IndexError` et `KeyError` que l'on a beaucoup utilisées dans ce chapitre descendent d'une même exception `LookupError` qui attrape donc toutes les erreurs liées à la recherche dans un conteneur.

```python
def get_10th(seq):
    try:
        return seq[10]
    except LookupError as e:
        print('erreur', e)
```

```pycon
>>> get_10th([])
erreur list index out of range
>>> get_10th({})
erreur 10
```

On trouve aussi une grande famille d'erreurs sous `OSError` qui regroupe toutes les exceptions liées aux entrées/sorties, comme `FileNotFoundError`, `FileExistsError` ou `PermissionError`.

Voici un bref aperçu de cette hiérarchie :

```text
Exception
 +-- TypeError
 +-- ValueError
 |    +-- UnicodeError
 |         +-- UnicodeDecodeError
 |         +-- UnicodeEncodeError
 +-- ArithmeticError
 |    +-- ZeroDivisionError
 +-- NameError
 |    +-- UnboundLocalError
 +-- LookupError
 |    +-- IndexError
 |    +-- KeyError
 +-- OSError
 |    +-- FileNotFoundError
 |    +-- FileExistsError
 |    +-- PermissionError
 +-- SyntaxError
 +-- AssertionError
 +-- RuntimeError
      +-- RecursionError
```

La hiérarchie complète des exceptions Python peut être trouvée à l'adresse suivante : <https://docs.python.org/fr/3/library/exceptions.html#exception-hierarchy>.
