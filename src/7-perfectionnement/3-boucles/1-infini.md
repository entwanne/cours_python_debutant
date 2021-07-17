### Cas des boucles infinies

Nous avons vu les boucles `for` pour itérer sur des données, puis les boucles `while` pour boucler sur une condition.
Et nous avons vu que, volontairement ou non, nous pouvions tomber dans des cas de boucles infinies.

```python
while True:
    print("Vers l'infini et au-delà !")
```

[[i]]
| Pour rappel, utilisez la combinaison de touches ||Ctrl+C|| pour couper le programme.

Volontairement, ça peut être pour laisser tourner un programme en tâche de fond -- un serveur par exemple -- qui s'exécuterait continuellement pour traiter des requêtes.
Et dans ce cas des dispositifs seront mis en place pour terminer proprement le programme quand on le souhaite.

Mais il y a d'autres cas d'usages légitimes de boucles a priori infinies, car il existe d'autres moyens de terminer une boucle en cours d'exécution.

En effet, la condition d'un `while` est parfois difficile à exprimer, d'autant plus si elle repose sur des événements tels que des `input`.
Dans ce cas, un idiome courant est d'écrire une boucle infinie et d'utiliser un autre moyen de sortir de la boucle : le mot-clé `break`.  
Ce mot-clé, quand il est rencontré, a pour effet de stopper immédiatement la boucle en cours, sans repasser par la condition.

```python
while True:
    value = input('Entrez un nombre: ')
    if value.isdigit():
        value = int(value)
        break
    else:
        print('Nombre invalide')
```

Avec cette boucle, nous attendons que l'entrée ne soit composée que de chiffres, auquel cas on rentre dans le `if` et l'on atteint le `break`.
Sinon, on continue de boucler en redemandant à l'utilisateur de saisir un nouveau nombre.

La boucle, infinie en apparence (`while True`), possède en fait une condition de fin exprimée par un `if`.
