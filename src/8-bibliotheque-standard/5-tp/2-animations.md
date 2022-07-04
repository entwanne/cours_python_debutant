### Animations

Un tout petit exercice avant de finir.

L'ordinateur est un peu trop rapide à jouer, on a à peine le temps de voir ce qui se passe.
On serait alors tenté d'ajouter un simple `time.sleep(1)` pour ralentir l'exécution, mais on se demanderait alors ce qui se passe.

Une autre idée serait d'ajouter des animations pendant les choix de l'ordinateur, afin de voir qu'il se passe quelque chose sans que ça ne se passe trop vite.

Et pour cela, on va simplement utiliser les fonctions `print` et `time.sleep`.

Par exemple comment représenter une barre de progression en animation ?
On peut afficher un caractère, attendre, afficher un autre caractère, etc.  
Pour cela, on va appeler `print` avec l'argument `end=''` (pour ne pas afficher de retour à la ligne) dans une boucle.
En sortie de boucle, on s'occupera de revenir à la ligne pour finaliser la barre.

```python
import time

for _ in range(10):
    print('-', end='')
    time.sleep(0.1)

print()
```

Si vous exécutez ce code, vous verrez probablement la barre complète s'afficher d'un seul coup au bout d'une seconde, sans aucune animation.

Cela est dû au mécanisme de _flush_ (mémoire tampon) dont je vous avais parlé : en l'absence de retour à la ligne, `print` a simplement placé le texte en mémoire tampon mais n'a rien écrit réellement sur le terminal.
On corrige ça an ajoutant l'argument `flush=True` à l'appel.

```python
import time

for _ in range(10):
    print('-', end='', flush=True)
    time.sleep(0.1)

print()
```

[[i]]
| Pour aller plus loin, on peut aussi utiliser le caractère spécial `\b` qui permet de revenir en arrière sur la ligne et donc d'effacer le dernier caractère imprimé.

#### Solution

Rien de bien méchant, je présente ici le fichier `tp/ia.py` uniquement qui est le seul à changer.

[[s]]
| ```python
| import random
| import time
| 
| from .definitions import attacks, monsters
| 
| 
| def wait(steps, step_duration=0.1):
|     print('[', end='', flush=True)
|     for _ in range(steps):
|         print('>', end='', flush=True)
|         time.sleep(step_duration)
|         print('\b#', end='', flush=True)
|     print(']')
| 
| 
| def chose_monster():
|     values = list(monsters.values())
|     monster = random.choice(values)
|     wait(10)
|     return monster
| 
| 
| def chose_attack(player):
|     monster = player['monster']
|     weights = [attacks[name]['damages'] for name in monster['attacks']]
|     att_name = random.choices(monster['attacks'], weights=weights)[0]
| 
|     wait(10)
|     print(f"Le joueur {player['id']} utilise {att_name}")
|     return attacks[att_name]
| 
| 
| def get_player(player_id):
|     monster = chose_monster()
|     pv = int(random.normalvariate(100, 10))
|     print(f"Le joueur {player_id} choisit {monster['name']} ({pv} PV)")
| 
|     return {
|         'id': player_id,
|         'monster': monster,
|         'pv': pv,
|         'chose_attack_func': chose_attack,
|     }
| ```
| Code: `tp/ia.py`

Si les animations dans le terminal vous intéressent et que vous souhaitez aller plus loin, je vous conseille de regarder du côté [du module `curses`](https://docs.python.org/3/library/curses.html) de Python, qui permet de dessiner dans le terminal plus simplement qu'avec `print` et `'\b'`.

La bibliothèque tierce [`prompt_toolkit`](https://github.com/prompt-toolkit/python-prompt-toolkit) peut aussi être un bon point d'entrée.
