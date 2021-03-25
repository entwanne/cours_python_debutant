### Arguments optionnels

Nous savons déclarer une fonction avec des paramètres simples, et leur associer des arguments lors de l'appel, qu'ils soient positionnels ou nommés.

```python
>>> def log(message, component, level):
...     print(f'[{level}] {component}: {message}')
... 
>>> log('Une erreur est survenue', 'system', 'error')
[error] system: Une erreur est survenue
>>> log('Une erreur est survenue', 'system', level='error')
[error] system: Une erreur est survenue
```

Nous obtenons un message d'erreur si nous omettons un des arguments.

```python
>>> log('Une erreur est survenue', 'system')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: log() missing 1 required positional argument: 'level'
```

Pourtant nous avons vu qu'il existait dans la bilbiothèque standard des fonctions avec des arguments optionnels, comment font-elles ?
Cela se passe au moment de la définition des paramètres de la fonction, ou une valeur par défaut est donnée à certains paramètres.
Les arguments optionnels correspondent simplement aux paramètres ayant une valeur par défaut.

Pour définir une valeur par défaut à un paramètre, il suffit d'écrire `parametre=valeur` plutôt que `parametre` dans la liste des paramètres de la fonction.
Voici ainsi une version plus évoluée de notre fonction `log`, s'appuyant sur des valeurs par défaut.

```python
>>> def log(message, component=None, level='info'):
...     if component is None:
...         print(f'[{level}] {message}')
...     else:
...         print(f'[{level}] {component}: {message}')
...
>>> log('Une erreur est survenue', 'system', 'error')
[error] system: Une erreur est survenue
>>> log("Message d'information")
[info] Message d'information
>>> log('Fonction dépréciée', level='warning')
[warning] Fonction dépréciée
```

#### Paramètres par défaut mutables

C'est aussi simple que cela… ou presque !
Il y a une chose à laquelle il faut faire attention, comme toujours, les types mutables.  
Eh oui, les valeurs par défaut sont définies une seule fois pour toutes, quand la fonction elle-même est définie.
C'est-à-dire que ces valeurs seront partagées entre tous les appels à la fonction.

Pour les valeurs immutables, pas de problème, il n'y a pas de risque d'effets de bord.
Mais pour les mutables, faites bien attention à ce que vous faites, on arrive rapidement à des situations problématiques.

```python
>>> def get_monster(name, attacks=[]):
...     return {'name': name, 'attacks': attacks}
... 
>>> pythachu = get_monster('Pythachu')
>>> pythachu['attacks'].append('tonnerre')
>>> pythachu
{'name': 'Pythachu', 'attacks': ['tonnerre']}
>>> pythard = get_monster('Pythard')
>>> pythard
{'name': 'Pythard', 'attacks': ['tonnerre']}
```

Et oui, la même liste d'attaque a été utilisée et donc partagée entre nos deux dictionnaires, d'où le bug.
C'est pourquoi il est généralement conseillé d'éviter les mutables comme valeurs par défaut de paramètres.

Pour cela, on utilisera une valeur comme `None` (appellée sentinelle) qui indiquera l'absence de valeur et permettra donc d'instancier un objet (ici une liste) dans le corps de la fonction, évitant le problème de l'instance partagée.

```python
>>> def get_monster(name, attacks=None):
...     if attacks is None:
...         attacks = []
...     return {'name': name, 'attacks': attacks}
... 
>>> pythachu = get_monster('Pythachu')
>>> pythachu['attacks'].append('tonnerre')
>>> pythachu
{'name': 'Pythachu', 'attacks': ['tonnerre']}
>>> pythard = get_monster('Pythard')
>>> pythard
{'name': 'Pythard', 'attacks': []}
```

Je dis « généralement » car il y a des cas où c'est le comportement voulu, cela permet de mettre en place facilement un mécanisme de cache[^cache] sur une fonction par exemple.

[^cache]: Un cache est une mémoire associée à une fonction, pour éviter de réexécuter des calculs coûteux.

```python
>>> def compute(x, cache={}):
...     if x in cache:
...         return cache[x]
...     print('Calcul complexe...')
...     ret = x**3 - x**2
...     cache[x] = ret
...     return ret
... 
>>> compute(2)
Calcul complexe...
4
>>> compute(3)
Calcul complexe...
18
>>> compute(2) # Réutilisation du cache
4
>>> compute(5)
Calcul complexe...
100
```

#### Ordre de placement des paramètres

Nous l'avions vu, lors d'un appel de fonction les arguments positionnels doivent toujours être placés avant les arguments nommés.
C'est ce qui permet à Python de faire correctement la correspondance entre arguments et paramètres.

```python
>>> log(level='warning', 'Avertissement')
  File "<stdin>", line 1
SyntaxError: positional argument follows keyword argument
```

Une règle similaire existe pour les paramètres : ceux qui prennent une valeur par défaut doivent se placer après les autres.
Cela est logique puisqu'ils sont optionnels, et qu'on ne pourrait pas savoir dans le cas contraire à quel paramètre est censé correspondre un argument.

```python
>>> def log(component=None, level='info', message):
...     pass
... 
  File "<stdin>", line 1
SyntaxError: non-default argument follows default argument
```
