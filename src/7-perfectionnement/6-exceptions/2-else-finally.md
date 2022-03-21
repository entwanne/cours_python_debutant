### Autres mots-clés

Le mot-clé `try` ne s'accompagne pas uniquement de `except`.
D'autres blocs sont aussi disponibles pour réagir à différents types de situations.

#### `else`

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

```pycon
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

```pycon
>>> dic = {'a': 42}
>>> dict_pop(dic, 'a')
42
>>> dic
{}
>>> dict_pop(dic, 'a')
>>> dict_pop(dic, 'a', 'pouet')
'pouet'
```

#### `finally`

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

```pycon
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

[^with]: Même si l'on verra plus généralement un bloc `with` dans ce cas, qui permet de faire la même chose sans se prendre la tête.

```python
def read_int(path):
    f = open(path)
    try:
        return int(f.read())
    finally:
        print('Fermeture')
        f.close()
```

Par exemple avec les fichiers suivants :

```
salut
```
Code: hello.txt

```
123
```
Code: number.txt

On constate bien que l'appel à `close` se fait dans tous les cas, même si une erreur survient.

```pycon
>>> read_int('number.txt')
Fermeture
123
>>> read_int('hello.txt')
Fermeture
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in read_int
ValueError: invalid literal for int() with base 10: 'salut\n'
```

On remarque aussi que le `finally` est exécuté même si un `return` est présent, il s'agit simplement d'un code exécuté à la toute fin de la fonction, mais qui n'en change pas la valeur de retour.

Attention, cela est bien sûr différent de placer un traitement à l'extérieur du bloc d'exception, qui lui ne sera pas exécuté en cas d'exception non attrapée.

```python
def get_10th(seq):
    try:
        seq[10]
    except IndexError:
        print("erreur d'index")
    finally:
        print("traitement final")
    print("Fin de la fonction")
```

```pycon
>>> get_10th([])
erreur d'index
traitement final
Fin de la fonction
>>> get_10th({})
traitement final
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in get_10th
KeyError: 10
```
