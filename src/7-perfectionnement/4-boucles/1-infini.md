### Vers l'infini et au-delà

Nous avons vu les boucles `for` pour itérer sur des données, puis les boucles `while` pour boucler sur une condition.
Dans tous nos cas, nous considérions que nos boucles étaient finies, qu'elles se termineraient forcément après un certain nombre de tours.
Mais ce n'est pas toujours le cas, et volontairement ou non on peut tomber dans des cas de boucle infinie.

```python
while True:
    print("Vers l'infini et au-delà !")
```

[[i]]
| Utilisez la combinaison de touches ||Ctrl+C|| pour couper le programme.

Volontairement, ça peut être pour laisser tourner un programme en tâche de fond -- un serveur par exemple -- qui tournerait continuellement pour traiter des requêtes.
Et dans ce cas des dispositifs seront mis en place pour terminer proprement le programme quand on le souhaite.

Involontairement c'est plus problématique, et ça peut arriver avec une boucle `while` dont la condition serait toujours vraie.
Le cas précédent est flagrant mais ça ne l'est pas toujours autant.

```python
def factorielle(n):
    ret = 1
    while n != 0:
        ret *= n
        n -= 1
    return ret
```

Cette fonction de calcul de factorielle[^factorielle] paraît parfaitement innocente, pourtant appelée avec un nombre négatif elle provoque une boucle infinie.

[^factorielle]: La factorielle est la fonction mathélatique renvoyant le produit des nombres entiers de 1 à n.

```python
>>> factorielle(5)
120
>>> factorielle(0)
1
>>> factorielle(-1)
^CTraceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in factorielle
KeyboardInterrupt
```

Dans l'idéal il faudrait traiter les nombres négatifs comme une erreur, mais nous ne savons pas encore faire cela alors on peut se dire que `1` serait un résultat acceptable en cas d'argument négatif.

Il nous aurait alors fallu utiliser une condition de boucle telle que `n > 0` (ou même `n > 1`) pour éviter cela.
Mais le plus simple aurait encore été d'utiliser une boucle `for`.

```python
def factorielle(n):
    ret = 1
    for i in range(2, n + 1):
        ret *= i
    return ret
```

Le soucis c'est qu'à l'exécution il n'est théoriquement pas possible de savoir si une boucle va s'arrêter ou non, c'est un problème indécidable (théorème de l'arrêt).
En effet, dans le cas précédent on ne sait pas avec quelles valeurs pourra être appelée la fonction, surtout si ces valeurs dépendent de saisies de l'utilisateur.  
Ainsi, il faut être prudent et faire très attentions aux conditions utilisées pour les `while`, ou utiliser autant que possible des boucles `for`, plus facilement prédictibles.

Toutefois, la condition d'un `while` est parfois difficile à exprimer, d'autant plus si elle repose sur des événements tels que des `input`.
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
