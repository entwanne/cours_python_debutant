### Sérialisation binaire

Python possède un format de sérialisation qui lui est propre, disponible via le module `pickle`, capable de gérer à peu près tous les types Python.
C'est donc un format très pratique pour enregistrer l'état d'un programme.

Étant un format binaire, je ne vais pas décrire à quoi il ressemble, ça serait juste un tas d'octets illisibles.
Sachez juste que le format gère de nombreux objets Python, pour peu que leur type soit connu par le programme qui chargera les données, en inspectant ce qui est contenu dans ces objets.

#### Module `pickle`

Le module utilise l'interface dont je vous avais parlé plus tôt pour `json`, et propose donc les fonctions `load`, `loads`, `dump` et `dumps`.

##### Écriture

Puisqu'il nous est impossible de partir d'un fichier existant, nous débuterons cette fois par l'écriture.
Elle se fait donc à l'aider des fonctions `dump` et `dumps`.

`dump` prend en argument un objet Python et un fichier (ouvert en écriture) vers lequel le sérialiser.  
Il est possible d'enchaîner les appels à `dump` pour écrire plusieurs objets dans le fichier.

```python
with open('game.dat', 'wb') as f:
    monsters = {
        '001': {
            'name': 'Pythachu',
            'attaques': ['charge', 'tonnerre'],
        },
        '002': {
            'name': 'Pythard',
            'attaques': ['charge', 'jet-de-flotte'],
        },
    }
    pickle.dump(monsters, f)
    attacks = [
        {'name': 'charge', 'type': 'normal', 'damage': 20},
        {'name': 'tonnerre', 'type': 'foudre', 'damage': 50},
        {'name': 'jet-de-flotte', 'type': 'aquatique', 'damage': 50},
    ]
    pickle.dump(attacks, f)
```

La méthode `dumps` prend simplement un objet et renvoie une chaîne d'octets qui sera compatible avec `loads`.

```python
>>> pickle.dumps([1, 2, 3])
b'\x80\x04\x95\x0b\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02K\x03e.'
>>> pickle.dumps(2+1j)
b'\x80\x04\x95.\x00\x00\x00\x00\x00\x00\x00\x8c\x08builtins\x94\x8c\x07complex\x94\x93\x94G@\x00\x00\x00\x00\x00\x00\x00G?\xf0\x00\x00\x00\x00\x00\x00\x86\x94R\x94.'
```

##### Lecture

La méthode `loads` prend donc en argument une chaîne d'octets, reconsruit l'objet Python représenté et le renvoie.

```python
>>> pickle.loads(b'\x80\x04\x95\x0b\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02K\x03e.')
[1, 2, 3]
>>> pickle.loads(b'\x80\x04\x95.\x00\x00\x00\x00\x00\x00\x00\x8c\x08builtins\x94\x8c\x07complex\x94\x93\x94G@\x00\x00\x00\x00\x00\x00\x00G?\xf0\x00\x00\x00\x00\x00\x00\x86\x94R\x94.')
(2+1j)
```

`load` prend elle un fichier et renvoie aussi l'objet qui y est contenu. Comme pour `dump`, il est possible d'appeler `load` plusieurs fois de suite sur un même fichier (pour y lire les différents objets écrits).

```python
>>> with open('game.dat', 'rb') as f:
...     print('monstres :', pickle.load(f))
...     print('attaques :', pickle.load(f))
... 
monstres : {'001': {'name': 'Pythachu', 'attaques': ['charge', 'tonnerre']}, '002': {'name': 'Pythard', 'attaques': ['charge', 'jet-de-flotte']}}
attaques : [{'name': 'charge', 'type': 'normal', 'damage': 20}, {'name': 'tonnerre', 'type': 'foudre', 'damage': 50}, {'name': 'jet-de-flotte', 'type': 'aquatique', 'damage': 50}]
```

#### Avantages et inconvénients

Vous l'aurez compris, `pickle` est un format très pratique en Python, puisqu'il permet de tout représenter ou presque.
Il n'est en revanche pas interopérable puisque applicable seulement à Python.

De plus, il permet l'exécution de code arbitraire ce qui présente donc une grosse faille de sécurité sur des données non sûres, il est donc à bannir pour tout ce qui reçoit des données distantes sans couche supplémentaire de sécurité.

Dans notre cas d'une sauvegarde de l'état d'un programme, c'est un assez bon choix.
