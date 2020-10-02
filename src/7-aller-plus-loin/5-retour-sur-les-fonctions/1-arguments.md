### Types d'arguments

* Valeurs par défaut des paramètres (attention aux mutables)

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
>>> log('Une erreur est survenue', 'system', 'error')
[error] system: Une erreur est survenue
>>> log("Message d'information")
[info] Message d'information
>>> log('Fonction dépréciée', level='warning')
[warning] Fonction dépréciée
```

C'est aussi simple que cela… ou presque !
Il y a une chose à laquelle il faut faire attention, comme toujours, les types mutables.  
Eh oui, les valeurs par défaut sont définies une seule fois pour toutes, quand la fonction elle-même est définie.
C'est-à-dire que ces valeurs seront partagées entre tous les appels à la fonction.

Pour les valeurs immutables, pas de problème, il n'y a pas de risque d'effets de bord.
Mais pour les mutables, faites bien attention à ce que vous faites, on arrive rapidement à des situations problématiques.

```python
```

C'est pourquoi il est généralement conseillé d'éviter les mutables comme valeurs par défaut de paramètres.
Je dis généralement car il y a des cas où c'est le comportement voulu, cela permet de mettre en place facilement un mécanisme de cache[^cache] sur une fonction par exemple.

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

* Arguments uniquement nommés (`*`)
* Arguments uniquement positionnels (`/`)

* Ordre de placement des arguments
* Ordre lors de l'appel
