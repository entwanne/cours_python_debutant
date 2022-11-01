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

values = list(range(10))


def worker(n):
    while values:
        time.sleep(1)
        print(f'[{n}] values: {values}')
        del values[0]


thr1 = threading.Thread(target=worker, args=[1])
thr2 = threading.Thread(target=worker, args=[2])
thr1.start()
thr2.start()
thr1.join()
thr2.join()
```

À l'exécution on a des chances de rencontrer une erreur ligne 11 comme quoi la liste est vide : en effet comme la fonction met un certain temps à s'exécuter, l'état de la liste a pu changer entre les lignes 8 et 11.  
On parle de problèmes de concurrence (ou _race-condition_) pour qualifier de tels bugs, et on dit d'un programme qui les gère correctement qu'il est _thread-safe_.

Il y a plusieurs manières de gérer ce genre de problème.

* opérations atomiques/thread-safe (values.pop avec except)
* mutex
    * dead-lock

[[i]]
| Au niveau du système d'exploitation les _threads_ sont un mécanisme de programmation parallèle, pouvant s'exécuter sur différents cœurs du processeur.  
| C'est l'interpréteur Python qui empêche ce parallélisme en ajoutant un verrou global (_Global Interpretor Lock_, ou _GIL_) qui fait qu'un seul fil peut s'exécuter à la fois pour préserver l'intégrité des données manipulées.
