### Construction d'un paquet

Pour créer notre propre paquet, on peut alors simplement créer un nouveau répertoire dans lequel on placera nos fichiers Python (nos modules).

Créons par exemple un dossier `operations` depuis le répertoire courant, avec deux fichiers `addition.py` et `soustraction.py` :

```python
def addition(a, b):
    return a + b
```
Code: `operations/addition.py`

```python
def soustraction(a, b):
    return a - b
```
Code: `operations/soustraction.py`

Nous voilà maintenant avec un nouveau paquet `operations`.
Ce paquet forme un espace de noms supplémentaire autour de nos modules, et nous devons donc les préfixer de `operations.` pour les importer.

```python
>>> from operations import addition
>>> # on a importé le module addition
>>> addition.addition(1, 2)
3
>>> from operations.soustraction import soustraction
>>> # on a importé directement la fonction soustraction
>>> soustraction(1, 2)
-1
```

[[w]]
| Pensez à bien vous placer depuis le répertoire contenant le dossier `operations` et non dans le dossier `operations` lui-même pour exécuter ce code.  
| Par exemple si votre dossier `operations` se trouve dans un dossier `projet`, il faut que vous exécutiez l'interpréteur depuis ce dossier `projet` sans quoi Python ne serait pas en mesure de trouver le paquet.

On remarque que l'on ne peut pas simplement faire `import operations` puis utiliser par exemple `operations.addition.addition(1, 2)` comme on le ferait avec des modules.
C'est parce que les modules d'un paquet ne sont pas directement chargés quand le paquet est importé, mais nous verrons ensuite comment y parvenir.

#### Imports relatifs

Il peut arriver depuis un paquet que nous ayons besoin d'accéder à d'autres modules du même paquet.
Par exemple, notre fonction `soustraction` pourrait vouloir faire appel à la fonction `addition`.  
Pour cela, on va pouvoir importer la fonction `addition` dans le module `soustraction`, comme on vient de le faire dans l'interpréteur interactif.

```python
from operations.addition import addition

def soustraction(a, b):
    return addition(a, -b)
```
Code: `operations/soustraction.py`

Et tout fonctionne comme prévu :

```python
>>> from operations.soustraction import soustraction
>>> soustraction(8, 5)
3
```

Mais la syntaxe peut paraître lourde, pourquoi avoir besoin de préciser `operations` alors qu'on est déjà dans ce paquet ?
Python a prévu une réponse à ça : les imports relatifs.

Ainsi, pour un import au sein d'un même paquet, on peut simplement référencer un autre module en le préfixant d'un `.` sans indiquer explicitement le paquet (qui sera donc le paquet courant).

```python
from .addition import addition

def soustraction(a, b):
    return addition(a, -b)
```
Code: `operations/soustraction.py`

Et l'on peut vérifier en important le module `operations.soustraction` que tout fonctionne toujours correctement.

[[a]]
| Attention cependant, cette syntaxe d'imports relatifs n'est valable que dans le cas d'un `from ... import ...`.
| Il n'est ainsi pas possible d'écrire simplement `import .addition` pour importer le module `addition`.  
| En revanche la syntaxe `from . import addition` est valide (équivalente à `from operations import addition`).
