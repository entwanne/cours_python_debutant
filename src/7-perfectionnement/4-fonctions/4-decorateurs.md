### Décorateurs

Les décorateurs c'est fait pour décorer.
Enfin pas exactement, il faut comprendre le terme comme « envelopper ».
Un décorateur, c'est un objet que l'on va appliquer à une fonction pour en changer le comportement.

Le décorateur est indépendant et extérieur à la fonction, il se contente de l'envelopper.  
Lors des appels à notre fonction, c'est le décorateur qui prendra le pas et choisira les opérations à effectuer.
Il pourra choisir d'appeler notre fonction ou non, d'exécuter des opérations avant ou après, etc.

Par exeple, plus tôt dans ce chapitre nous avons vu un mécanisme de cache (mémoïsation) appliqué à une fonction, à l'aide de la valeur par défaut d'un paramètre.
Ce mécanisme aurait pu être implémenté à l'aide d'un décorateur, celui-ci décidant si l'appel à la fonction est nécessaire ou non, en fonction de ce qu'il a dans son cache, puis se chargerait d'y enregistrer les résultats reçus.

Il s'agit de l'application directe du [patron de conception décorateur](https://fr.wikipedia.org/wiki/D%C3%A9corateur_(patron_de_conception)).

La syntaxe pour appliquer un décorateur à une fonction est très simple, il suffit de précéder la définition de notre fonction par une ligne composée d'un `@` et du nom du décorateur.

```python
@decorator
def function(a, b):
    ...
```

En pratique, on notera que ce code est équivalent au suivant, l'application à l'aide de l'`@` n'étant que du sucre syntaxique apporté par Python.

```python
def function(a, b):
    ...

function = decorator(function)
```

Le mécanisme de cache dont je parlais est fourni par le décorateur `lru_cache` du module `functools`.
Appliqué à une fonction, il permettra donc de garder en mémoire les résultats de la fonction et éviter de réexécuter des calculs coûteux.

```python
from functools import lru_cache

@lru_cache
def addition(a, b):
    print(f'Calcul de {a} + {b}...')
    return a + b
```

On le voit à l'utilisation, la fonction est appelée que si son résultat n'est pas déjà connu.

```python
>>> addition(3, 5)
Calcul de 3 + 5...
8
>>> addition(1, 2)
Calcul de 1 + 2...
3
>>> addition(3, 5)
8
```

Un tel mécanisme par décorateur a l'intérêt de ne rien changer au code de la fonction, qui reste le même que si le décorateur n'était pas là.

#### Décorateur paramétré

Mais que signifie ce _lru_ dans `lru_cache` ?
Il s'agit du sigle _Least Recently Used_ (_Utilisés le Plus Récemment_ en français) explicitant le comportement du cache.

En effet, votre ordinateur a une mémoire limitée et le cache cherche donc à minimiser son empreinte.
Pour cela, il ne conservera pas tous les résultats en mémoire mais seulement ceux qu'ils jugent prioritaires.
C'est là qu'intervient le mécanisme _LRU_ qui signifie simplement que les résultats prioritaires sont ceux utilisés le plus récemment.  
Cela signifie aussi que les résultats les plus anciens finiront par disparaître du cache lorsque celui-ci aura été rempli par d'autres valeurs.

La taille maximale par défaut du cache est de 128 résultats, mais il est possible d'en changer en paramétrant le décorateur.  
Comme une fonction, un décorateur peut-être suivi de parenthèses contenant des arguments pour le paramétrer et donc influer sur son comportement.

```python
@decorator('foo', 5)
def function(a, b):
    ...
```

Ici, la taille du cache est un paramètre du décorateur.
Nous allons d'ailleurs voir le mécanisme _LRU_ en action en réduisant la taille allouée à ce cache, disons à 3.

```python
@lru_cache(3)
def addition(a, b):
    print(f'Calcul de {a} + {b}...')
    return a + b
```

Et maintenant, regardez bien ce qu'il se passe quand la taille maximale est atteinte.

```python
>>> addition(3, 5)
Calcul de 3 + 5...
8
>>> addition(1, 2)
Calcul de 1 + 2...
3
>>> addition(4, 7)
Calcul de 4 + 7...
11
>>> addition(3, 5) # la valeur est toujours en cache
8
>>> addition(9, 6)
Calcul de 9 + 6...
15
>>> addition(1, 2) # la valeur est sortie du cache
Calcul de 1 + 2...
3
```

Notre cache est limité à 3 résultats, pour enregistrer `9 + 6` il doit donc faire de la place.
Le résultat le plus anciennement utilisé, ici `1 + 2`, est donc supprimé.

Attention, je dis bien plus anciennement utilisé et non calculé.
Car le résultat le plus anciennement calculé est `3 + 5`, mais on l'a redemandé par la suite à la fonction, signifiant au cache qu'il était à nouveau utilisé.
Le résultat supprimé est celui auquel on a accédé le moins récemment.

Il est aussi parfaitement possible de se passer de ce mécanisme _LRU_ et donc de conserver tous les résultats sans limite de taille (autre que celle de l'ordinateur), en spécifiant `None` comme taille maximale au décorateur.

```python
@lru_cache(None)
def addition(a, b):
    print(f'Calcul de {a} + {b}...')
    return a + b
```

[[i]]
| On notera que depuis Python 3.9 il existe aussi le décorateur `cache` remplissant le rôle de cache illimité (`lru_cache(None)`).
|
| ```python
| from functools import cache
|
| @cache
| def addition(a, b):
|     print(f'Calcul de {a} + {b}...')
|     return a + b
| ```
