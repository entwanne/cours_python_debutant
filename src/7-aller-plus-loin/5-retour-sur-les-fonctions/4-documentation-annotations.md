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
Une _docstring_ c'est simple une chaîne de caractères placée au début de notre fonction, sans assignation ni rien.

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

#### Annotations de type

La _docstring_ n'est pas l'uniquement manière de documenter une fonction, d'autres informations peuvent être apportées par les annotations de types.
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

Il est aussi possible de préciser une annotation sur la fonction en elle-même pour en indiquer le type de la valeur de retour.
Pour cela, on utilise un `->` derrière la liste des paramètres, suivi du type de retour.

```python
def operation(op: str, a: int, b: int) -> int:
    ...
```

[[a]]
| Les annotations ne changent rien lors de l'exécution du programme, la fonction peut être appelée avec d'autre type que ceux précisés sans que cela ne provoque d'erreur.

On le constate d'ailleurs si l'on appelle notre fonction avec des nombres flottants.

```python
>>> operation('+', 1.2, 3.4)
4.6
```

#### Module `typing`

* typing.Union[...], typing.Any
* Module typing: typing.List[...], typing.Tuple[...] -> Python 3.9
