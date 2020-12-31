### Autres mots-clés

* Réagir quand tout va bien : `else`
* Réagir dans tous les cas : `finally`

Le mot-clé `try` ne s'accompagne pas uniquement de `except`.
D'autres blocs sont aussi disponibles pour réagir à différents types de situations.

Par exemple, le bloc `else` permet de traiter le cas où tout s'est bien passé et qu'aucune exception n'a été levée (attrapée ou non).

```python
def get_10th(seq):
    try:
        seq[10]
    except IndexError:
        print("erreur d'index")
    else:
        print("pas d'erreur")
```

```python
>>> get_10th([])
erreur d'index
>>> get_10th({})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in get_10th
KeyError: 10
>>> get_10th([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
pas d'erreur
>>> get_10th({10: 'foo'})
pas d'erreur
```

Cela est utile dans le cas d'une action qui dépendrait d'un traitement précédent, par exemple voici comment on pourrait implémenter la méthode `pop` des dictionnaires.
Pour rappel, cette méthode permet de supprimer une clé d'un dictionnaire et d'en renvoyer la valeur, et permet de renvoyer une valeur par défaut si la clé n'existe pas (ce que nous ferons par défaut dans notre implémentation).

```python
def dict_pop(dic, key, default=None):
    try:
        value = dic[key]
    except KeyError:
        value = default
    else:
        del dic[key]
    return value
```

```python
>>> dic = {'a': 42}
>>> dict_pop(dic, 'a')
42
>>> dic
{}
>>> dict_pop(dic, 'a')
>>> dict_pop(dic, 'a', 'pouet')
'pouet'
```

Le bloc `finally` permet lui de réagir dans tous les cas, qu'une erreur soit survenue ou non, qu'elle ait été attrapée ou non.

```python
def get_10th(seq):
    try:
        seq[10]
    except IndexError:
        print("erreur d'index")
    finally:
        print("traitement final")
```

```python
>>> get_10th([])
erreur d'index
traitement final
>>> get_10th({})
traitement final
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in get_10th
KeyError: 10
>>> get_10th([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
traitement final
>>> get_10th({10: 'foo'})
traitement final
```

On l'utilise par exemple pour la libération d'une ressource qui aurait été acquise avant le `try`[^with].

[^with]: Même si l'on verra plus généralement un bloc `with` dans ce cas, qui permet de faire la même chose.

```python
def read_int(path):
    f = open(path)
    try:
        return int(f.read())
    finally:
        f.close()
```

Avec les fichiers suivants :

```
salut
```
Code: hello.txt

```
123
```
Code: number.txt

On aurait alors le traitement voulu.

```python
```

Attention, cela est différent de placer un traitement à l'extérieur du bloc d'exception, qui lui ne sera pas exécuté en cas d'exception non attrapée.

```python
```
