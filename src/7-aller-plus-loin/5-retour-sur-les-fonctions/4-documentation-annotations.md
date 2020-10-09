### Documentation et annotations

* Docstring
* Annotation de type (paramètres et retour)
* Module `typing` (introduction aux types courants : `List[...]`, `Tuple[...]` et leur utilité)

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
