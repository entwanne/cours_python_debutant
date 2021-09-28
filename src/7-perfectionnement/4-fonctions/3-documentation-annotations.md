### Documentation et annotations

Je vous ai présenté plus tôt la fonction `help` qui permet d'obtenir des informations sur un module ou une fonction.
Mais pour avoir accès à ces informations il faut que celles-ci aient été renseignées, que les fonctions aient été documentées.

C'est le cas dans la bibliothèque standard et c'est pourquoi nous obtenons des pages d'aide si complètes.
Mais qu'en est-il de nos propres fonctions ?

Prenons cette fonction `operation` capable d'appliquer différentes opérations arithmétiques à deux valeurs.

```python
def operation(op, a, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    print('error')
    return -1
```

La gestion d'erreurs est nulle mais ce n'est pas le sujet ici, nous y reviendrons plus tard. :)  
Voyons pour le moment à quoi ressemble la page d'aide de notre fonction.

```python
>>> help(operation)
Help on function operation in module __main__:

operation(op, a, b)
```

C'est… succinct.
D'un côté, on n'a rien renseigné d'autre à notre fonction, et il serait difficile à Python de nous donner plus d'informations.

#### Docstring

Une première étape vers la documentation est de rédiger une _docstring_ dans notre fonction.
Une _docstring_ c'est simplement une chaîne de caractères placée au début de notre fonction, sans assignation ni rien.

```python
def operation(op, a, b):
    "Renvoie le résultat de l'opération a (op) b"
    ...
```

Dans le déroulement de notre fonction ça ne change rien puisqu'une telle chaîne de caractères n'a aucun effet.
Mais Python la détecte et la rend accessible comme documentation de notre fonction.

```python
>>> help(operation)
Help on function operation in module __main__:

operation(op, a, b)
    Renvoie le résultat de l'opération a (op) b
```

Mais la documentation ne se résume généralement pas en une ligne.
Aussi, on trouvera souvent une chaîne multi-lignes délimitée par des triple-guillemets pour documenter notre fonction.

```python
def operation(op, a, b):
    """
    Renvoie le résultat de l'opération a (op) b
    
    Avec op l'un des opérateurs suivants :
    +: addition
    -: soustraction
    *: multiplication
    /: division
    """
    ...
```

Ne vous inquiétez pas pour les retours à la ligne introduits au début et à la fin de la chaîne, ils disparaissent dans la documentation.

```python
>>> help(operation)
Help on function operation in module __main__:

operation(op, a, b)
    Renvoie le résultat de l'opération a (op) b
    
    Avec op l'un des opérateurs suivants :
    +: addition
    -: soustraction
    *: multiplication
    /: division
```

#### Comment documenter ?

Dans notre documentation, on ne va pas définir en détails ce que fait notre fonction, expliquer toutes les conditions qui y sont faites, ça n'aurait pas trop d'intérêt.
Non, le but d'une documentation est de décrire l'usage : comment utiliser notre fonction et à quoi s'attendre en retour.

Si notre fonction a des comportements particuliers (erreurs qu'elle gère ou pas, astuces d'optimisation, etc.), il est bon aussi de les indiquer dans la documentation.

Pour notre fonction `operation`, la documentation devrait indiquer que notre fonction réalise des opérations arithmétiques de 4 types (addition, soustraction, multiplication et division flottante) et renvoie le résultat de l'opération, l'opération à effectuer et les deux opérandes étant récupérés depuis les paramètres.  
Il serait ajouté que la fonction affiche un message d'erreur en cas d'opération inconnue (en renvoyant `-1`), et qu'elle ne traite pas l'erreur de division par zéro.

#### Annotations de types

La _docstring_ n'est pas l'unique manière de documenter une fonction, d'autres informations peuvent être apportées par les annotations de types.
Comme leur nom l'indique, ces annotations servent à décrire les types des paramètres de la fonction.

[[i]]
| Les annotations sont parfaitement facultatives, elles sont utiles à la documentation et pour des outils d'analyse statique (tel que `mypy` présenté en annexe).  
| Elles existent et vous pouvez donc en rencontrer dans un code, c'est pourquoi je vous les présente, mais ne vous sentez pas obligé de les utiliser si vous n'en ressentez pas le besoin.

Notre fonction peut s'annoter simplement : le premier paramètre est une chaîne de caractère, et les deux suivants sont des nombres, que l'on va pour le moment considérer comme des `int`.
Pour annoter un paramètre, on le fait suivre d'un `:` et du type que l'on veut préciser.

```python
def operation(op: str, a: int, b: int):
    ...
```

Ces informations sont ajoutées à la signature de la fonction dans la documentation fournie par `help`.

```python
>>> help(operation)
Help on function operation in module __main__:

operation(op: str, a: int, b: int)
...
```

Il est aussi possible de préciser une annotation sur la fonction en elle-même pour indiquer le type de la valeur de retour.
Pour cela, on utilise un `->` derrière la liste des paramètres, suivi du type de retour.

```python
def operation(op: str, a: int, b: int) -> int:
    ...
```

[[a]]
| Les annotations ne changent rien lors de l'exécution du programme, elles sont là à titre indicatif, la fonction peut être appelée avec d'autres types que ceux précisés sans que cela ne provoque d'erreur.

On le constate d'ailleurs si l'on appelle notre fonction avec des nombres flottants.

```python
>>> operation('+', 1.2, 3.4)
4.6
```

#### Module `typing`

Cela nous pose tout de même un problème : notre fonction est documentée pour être utilisée avec des `int`, mais on aimerait pouvoir l'appeler avec des `float`.
On pourrait la documenter avec des `float` mais se poserait alors le problème inverse.

Heureusement, il existe un module Python pour travailler et modeler ces annotations de types, le module `typing`.
Celui-ci contient des outils qui vont nous être utiles pour préciser des cas plus complexes d'utilisation des types, comme ici avec le choix entre deux types.

Pour ce problème il existe donc `typing.Union`, un objet particulier qui comme son nom l'indique permet de créer des unions (au sens mathématique) de types.
Il s'utilise à l'aide de crochets à l'intérieur desquels sont précisés les types autorisés.  
Dans notre cas on aurait `typing.Union[int, float]`.

Cet objet définit une forme spéciale de typage, et s'utilise donc directement en tant qu'annotation.
Un paramètre annoté ainsi sera considéré comme pouvant être de n'importe lequel des types précisés.

```python
import typing

def operation(op: str, a: typing.Union[int, float], b: typing.Union[int, float]) -> typing.Union[int, float]:
    ...
```

Ce type n'a pas pour but d'être instancié, et vous obtiendrez d'ailleurs une erreur si vous essayez de le faire.
Il n'est utile que pour renseigner des annotations.

On notera qu'il est possible de créer un alias à notre type particulier, de façon à le renseigner plus facilement, tout simplement en l'assignant à une variable.

```python
Number = typing.Union[int, float]

def operation(op: str, a: Number, b: Number) -> Number:
    ...
```

[[i]]
| En l'occurrence dans un cas comme celui-ci on utiliserait plutôt le type `Number` du module `numbers` présenté dans la partie suivante.
| Il est plus générique que notre solution avec `typing.Union` puisqu'il autorise aussi les complexes et d'autres types encore.

--------------------

D'autres problèmes peuvent se poser lorsque l'on cherche à documenter les types d'une fonction.
Par exemple prenons la fonction `my_sum` suivante, équivalente à la fonction `sum` de la bibliothèque standard, pour calculer une somme de nombres.

```python
def my_sum(values, start=0):
    "Calcule et renvoie les somme des éléments de `values`"
    for value in values:
        start += value
    return start
```

Comment l'annoter de façon à préciser que l'on attend une liste de nombres comme premier argument ?
On ne peut pas simplement utiliser `list` qui serait bien trop générique, autorisant des éléments d'autres types et mêmes des listes disparates (composées d'éléments de types différents).

`typing` vient à la rescousse en proposant un `typing.List` que l'on spécialise avec le type voulu, ici le type spécial `Number` défini plus haut.

```python
def my_sum(values: typing.List[Number], start : typing.Number = 0) -> typing.Number:
    ...
```

On pourrait aussi utiliser `typing.Iterable[Number]` qui aurait l'intérêt d'autoriser tout type d'itérable (tuple, range, etc.) et non uniquement les listes.

[[i]]
| Depuis Python 3.9, le type `list` est directement spécialisable comme annotation de type, rendant `typing.List` obsolète.
| On peut ainsi simplement utiliser `list[int]` pour indiquer une liste de nombres entiers.  
| C'est le cas aussi pour les autres conteneurs de la bibliothèque standard tels `tuple` et `dict`.
|
| Encore une fois, ces types particuliers n'ont pas pour but d'être instanciés et n'apporteraient aucune garantie sur leurs objets.
| Ils ne sont utiles qu'à des fins d'annotations.

Le module `typing` comprend de nombreuses choses, certaines dépassant le cadre de ce cours, et je ne vais donc pas m'appesentir sur sa présentation.
Pour terminer, sachez simplement qu'il existe un type spécial `typing.Any`, pour préciser qu'un paramètre peut accepter une valeur de n'importe quel type.

```python
def print(value: typing.Any):
    ...
```
