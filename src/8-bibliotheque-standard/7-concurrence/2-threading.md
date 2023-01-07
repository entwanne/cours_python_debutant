### Programmation multi-thread

Le premier mécanisme que nous allons voir est celui des _threads_, aussi appelés fils d'exécution[^exétron].

[^exétron]: Et plus rarement « exétrons » (pour unités d'exécution).

D'un point de vue système un programme prend la forme d'un processus : c'est une entité qui regroupe les instructions du programme, sa mémoire et un curseur pour se déplacer dans les instructions.  
Chaque processus possède en effet sa propre zone mémoire pour des raisons de sécurité, on ne voudrait pas que notre navigateur web puisse lire la mémoire de notre logiciel de messagerie par exemple.

Mais les processus peuvent aussi se diviser en fils d'exécution (_threads_), chaque fil étant un curseur différent dans les instructions du programme et l'ensemble des fils partageant une mémoire commune.
On a donc ainsi plusieurs tâches qui s'exécutent simultanément au sein d'un même processus.

En Python les fils d'exécution nous permettent de faire de la programmation concurrente.
Ils sont mis en œuvre par le module `threading` de la bibliothèque standard qui fournit l'interface pour les manipuler.

Ce module met à disposition un type `Thread` afin de créer de nouveaux fils.
On l'instancie en lui précisant un argument `target` qui sera la fonction à exécuter dans ce nouveau _thread_.

```pycon
>>> import time
>>> 
>>> def worker(n=10):
...     for i in range(n):
...         print(i)
...         time.sleep(1)
... 
>>> import threading
>>> thr = threading.Thread(target=worker)
```

Il est aussi possible à l'aide des argument `args` et `kwargs` de préciser les arguments qui seront passés à la fonction cible.

```python
thr = threading.Thread(target=worker, args=[5])
thr = threading.Thread(target=worker, kwargs={'n': 5})
```

À ce moment-là, le fil ne tourne pas encore, nous disposons simplement d'un objet _thread_.
Pour le démarrer, il faut ensuite appeler sa méthode `start`.

```pycon
>>> thr.start()
0
>>> 1
2
3
4
```

On voit alors que le fil démarre et qu'il interfère avec le fil principal dans lequel nous nous trouvons.
On constate aussi que la console n'est pas bloquée et qu'il est possible d'exécuter d'autres opérations pendant que le fil continue sa route.

```pycon
>>> thr = threading.Thread(target=worker, args=[5])
>>> thr.start()
0
>>> print('hello')
hello
1
>>> 2
3
4
```

Un objet _thread_ possède aussi une méthode `join` qui permet d'attendre que le fil se termine.
Cette méthode s'interrompt immédiatement si le fil est déjà terminé.

```pycon
>>> thr.join()
```

```pycon
>>> thr = threading.Thread(target=worker)
>>> thr.start()
0
>>> thr.join()
1
2
3
4
5
6
7
8
9
>>>
```

Elle est utile pour s'assurer que chacun des fils lancés est bien terminé et pour fermer proprement le programme.

Les _threads_ sont donc un mécanisme assez simple à mettre en place.  
Ils sont notamment utiles pour réaliser des programmes avec des interactions réseau bloquantes, sans que l'on doive pour autant figer l'interface du programme le temps que ces actions se terminent.
C'est par exemple le cas des clients de messagerie.

Voici un tel programme écrit en Python, avec un simple serveur de messagerie inversant et renvoyant les messages reçus.

```python
import threading
import time

running = True
server_queue = []
client_queue = []


def server():
    while running:
        if server_queue:
            msg = server_queue.pop(0)
            client_queue.append(msg[::-1])

def client_consumer():
    while running:
        if client_queue:
            msg = client_queue.pop(0)
            print('Received', msg)

def client_producer():
    global running
    try:
        while msg := input('> '):
            server_queue.append(msg)
            time.sleep(0.1)
    except EOFError:
        pass
    finally:
        running = False


threads = [
    threading.Thread(target=server),
    threading.Thread(target=client_consumer),
    threading.Thread(target=client_producer),
]
for thr in threads:
    thr.start()
for thr in threads:
    thr.join()
```
Code: `messenger.py`

```
> Hello World!
Received !dlroW olleH
> J'utilise des threads
Received sdaerht sed esilitu'J
```

Il faut aussi noter qu'il n'y a pas de limite sur le nombre de fils que l'on peut exécuter en même temps dans un programme.  
En revanche, gardez à l'esprit qu'on ne prévoit pas quel fil va être exécuté à quel moment, il faut donc concevoir nos programmes de façon à ce que les variations dans l'ordre d'exécution ne le fassent pas planter.

```python
import threading
import time

values = list(range(100))
result = []


def worker(n):
    while values:
        result.append(values[0])
        print(n, values[0])
        del values[0]


threads = [
    threading.Thread(target=worker, args=[n])
    for n in range(3)
]
for thr in threads:
    thr.start()
for thr in threads:
    thr.join()

print(result)
```

À l'exécution on a des chances de rencontrer une erreur ligne 12 comme quoi la liste est vide, et des doublons dans la liste `result` ligne 24 : en effet comme la fonction met un certain temps à s'exécuter, l'état de la liste a pu changer plusieurs fois entre les lignes 9 et 12. Rien n'assure que la liste contient toujours des éléments une fois la ligne 12 atteinte, ni que le premier élément est le même qu'à la ligne précédente.  
On parle de problèmes de concurrence (ou _race-condition_) pour qualifier de tels bugs, et on dit d'un programme qui les gère correctement qu'il est _thread-safe_.

**ILLUSTRATION DU PROBLÈME**

Il y a plusieurs manières de gérer ce genre de problème.

Premièrement on peut ajouter un `try/except` autour du `del` pour éviter de provoquer une erreur en cas de liste vide, c'est un cas simple à gérer et qui ne pose pas de plus gros problème de concurrence au-delà de ça (le traitement s'arrête de toute façon en cas de liste vide).

```python linenostart=8
def worker(n):
    while values:
        try:
            result.append(values[0])
            print(n, values[0])
            del values[0]
        except IndexError:
            break
```

Le problème des doublons est plus gênant car il s'agit clairement d'une erreur dans le comportement du programme.
D'autres solutions s'offrent alors à nous.

La plus simple, quand cela est possible, est d'utiliser des opérations qui sont elles-mêmes _thread-safe_ pour le problème rencontré, voire des opérations atomiques.  
Une opération atomique est une opération indivisible, qui ne peut pas être interrompue en cours de route et donc dont on a l'assurance qu'elle ne rencontrera pas de problème de concurrence.
C'est par exemple le cas [de la méthode `pop` des listes](https://docs.python.org/fr/3/faq/library.html#what-kinds-of-global-value-mutation-are-thread-safe) pour récupérer une valeur de la liste tout en la supprimant.

On pourrait ainsi réécrire le code précédent en utilisant un unique appel à `pop` plutôt qu'une récupération de l'élément suivie d'un `del`.
Cet appel lève toujours une exception `IndexError` en cas de liste vide qu'il nous faut encore ignorer.

```python linenostart=8
def worker(n):
    while values:
        try:
            item = values.pop(0)
        except IndexError:
            break
        print(n, item)
        result.append(item)
```

Le problème des doublons est bien résolu mais on remarque en revanche que l'ordre des éléments dans `result` n'est pas conservé par rapport à `values`.
En effet bien que les opérations `pop` et `append` en elles-mêmes soient atomiques, le fil peut-être suspendu par Python entre ces deux opérations, faisant qu'un autre fil ajoutera une valeur plus tôt.

**ILLUSTRATION DU PROBLÈME**

Pour résoudre ceci, on peut alors faire appel à un verrou logiciel.
C'est un mécanisme de programmation concurrente qui permet de s'assurer qu'un bloc de code n'est exécuté que par un et un seul fil en même temps.  
Ce fil se charge en effet de prendre possession d'un verrou en début de bloc (si ce verrou est disponible, sinon il attend) puis de le libérer en fin de bloc (permettant à un autre fil de l'obtenir etc.).

En Python dans le cas du _threading_ ils prennent la forme d'un objet `threading.Lock` et s'utilisent avec un bloc `with`.
Le verrou a besoin d'être partagé entre tous les _threads_ et donc d'être défini en dehors de la fonction `worker`.

[[i]]
| On parle aussi de _mutex_ pour ces verrous, signifiant _mutual exclusion_ soit exclusion mutuelle.

```python linenostart=4
values = list(range(100))
result = []
lock = threading.Lock()


def worker(n):
    while values:
        with lock:
            try:
                item = values.pop(0)
            except IndexError:
                break
            print(n, item)
            result.append(item)
```

**ILLUSTRATION DE LA SOLUTION**

* dead-lock

[[i]]
| Au niveau du système d'exploitation les _threads_ sont un mécanisme de programmation parallèle, pouvant s'exécuter sur différents cœurs du processeur.  
| C'est l'interpréteur Python qui empêche ce parallélisme en ajoutant un verrou global (_Global Interpretor Lock_, ou _GIL_) qui fait qu'un seul fil peut s'exécuter à la fois pour préserver l'intégrité des données manipulées.
