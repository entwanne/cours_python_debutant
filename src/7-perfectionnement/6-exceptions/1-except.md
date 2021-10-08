### Bloc except

Précédemment nous avons vu le bloc `except` qui, associé à un `try`, permet de traiter une exception qui surviendrait au cours de l'exécution.

```python
def get_10th(seq):
    try:
        return seq[10]
    except IndexError:
        return None
```

```python
>>> get_10th('abcdefghijkl')
'k'
>>> get_10th('abcd')
```

L'idée étant que le contenu du `try` peut lever une erreur qui sera attrapée par le bloc `except` si son type correspond (`IndexError` ici).

Plusieurs blocs `except` peuvent être placés à la suite sur des types d'erreurs différents pour leur offrir un traitement particulier.

```python
def get_10th(seq):
    try:
        return seq[10]
    except IndexError:
        return None
    except KeyError:
        return None
```

```python
>>> get_10th({5: 'a', 10: 'b'})
'b'
>>> get_10th({})
```

Mais on le voit ici, il peut arriver que le traitement soit le même pour différentes erreurs.  
Dans ce cas, il est possible de spécifier les différents types d'exceptions au sein d'une même clause `except`, simplement en les plaçant dans un tuple.

```python
def get_10th(seq):
    try:
        return seq[10]
    except (IndexError, KeyError):
        return None
```

#### Données complémentaires des exceptions

Une exception possède certes un type pour expliciter la cause de l'erreur, mais d'autres informations complémentaires sont aussi accessibles.

En effet, une exception n'est rien d'autre qu'un objet Python, qui possède donc des attributs et des méthodes.
Pour récupérer l'objet de cette exception, il suffit de placer un `as nom_de_la_variable` derrière le `except` afin de l'affecter à une variable `nom_de_la_variable`.  
Variable que l'on a tendance à appeler `error` / `exception`, ou plus simplement `err`, `exc` ou `e`.

```python
>>> seq = []
>>> try:
...     seq[10]
... except IndexError as e:
...     print(e)
...
list index out of range
```

On voit qu'ici dans le cas d'une `IndexError`, l'exception contient un message nous expliquant la raison de l'erreur (l'index choisi est en dehors des bornes).  
Ce message est un argument de l'exception, il est accessible via son attribut `args`.

```python
>>> try:
...     seq[10]
... except IndexError as e:
...     print(e.args)
...     msg, = e.args
...     print(msg)
...
('list index out of range',)
list index out of range
```

Dans le cas d'une `KeyError` (clé invalide sur un dictionnaire), l'argument de l'erreur est simplement la clé.

```python
>>> dic = {}
>>> try:
...     dic['abc']
... except KeyError as e:
...     print(e.args)
... 
('abc',)
```

Et c'est ce qui peut être un peu difficile avec le traitement des erreurs : chaque type d'exception présente des métadonnées qui lui sont propres, sans qu'il n'y ait forcément beaucoup de cohérence entre les types.

On notera que le `as ...` est aussi possible quand un tuple de types est précisé au `except` et s'utilise de la même manière.

```python
def get_10th(seq):
    try:
        return seq[10]
    except (IndexError, KeyError) as e:
        return e.args
```

```python
>>> get_10th([])
('list index out of range',)
>>> get_10th({})
(10,)
```
