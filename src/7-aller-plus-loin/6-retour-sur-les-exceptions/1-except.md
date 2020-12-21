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

L'idée étant que le contenu du `try` peut lever une erreur qui qui sera attrapée par le bloc `except` si son type correspond (`IndexError` ici).

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

* `except ... as`
