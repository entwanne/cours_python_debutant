### Éviter l'exception

Une solution pour éviter les erreurs est d'empêcher qu'elles se produisent.
Ainsi, avant d'exécuter une action, on va tester différents cas d'erreurs pour les écarter.
C'est la stratégie dite *LBYL* (*Look before you leap*, soit *réfléchis avant d'agir*).

Par exemple pour une calculatrice dans le cadre d'une division, on testerait si le quotient n'est pas nul avant de réaliser l'opération.


```python
def calculatrice(a, op, b):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/' and b != 0:
        return a / b
    print('Calcul impossible')
```

```python
>>> calculatrice(3, '/', 2)
1.5
>>> calculatrice(3, '/', 0)
Calcul impossible
```

Pour notre problématique de sauvegarde, il faudrait donc être en mesure de tester si un fichier existe.
Une telle fonctionnalité est disponible dans le module `pathlib`.
Ce module propose un type `Path` représentant un chemin sur le système de fichiers, et bénéficiant naturellement d'une méthode `exists` renvoyant un booléen pour tester si le chemin existe ou non.

```python
>>> from pathlib import Path
>>> p = Path('hello.txt')
>>> p.exists()
True
>>> p = Path('game.sav')
>>> p.exists()
False
```

Ainsi, on peut remplacer notre code de chargement par :

```python
from pathlib import Path

if Path('game.sav').exists():
    with open('game.sav') as save:
        state = load_game(save.read())
else:
    state = None
```

On notera que les objets `Path` possèdent aussi une méthode `open` équivalente à la fonction du même nom : `Path(foo).open()` revient à écrire `open(foo)`.
On peut alors améliorer notre code précédent pour éviter les répétitions.

```python
save_path = Path('game.sav')

if save_path.exists():
    with save_path.open() as save:
        state = load_game(save.read())
else:
    state = None
```

#### Limites

La stratégie *LBYL* est cependant limitée.
Déjà, il est difficile d'envisager tous les cas d'erreurs : on pourrait obtenir une exception parce que le fichier est un répertoire, parce que les permissions ne sont pas suffisantes pour le lire, etc.

Mais considérons que l'on arrive à anticiper toutes les erreurs possibles, il resterait un problème.
Quand on demande au système si un fichier existe, il le vérifie à l'instant *t* ; mais quand on l'ouvre nous sommes à l'instant *t+1*.  
Pendant ce très court laps de temps le fichier a pu être supprimé, déplacé, ses permissions modifiées, et donc on n'échapperait pas à l'exception.

Il va alors nous falloir adopter une autre stratégie, dite *EAFP* (*Easier to ask for forgiveness than permission*, *il est plus simple de demander pardon que demander la permission*). C'est-à-dire laisser l'exception se produire et la traiter ensuite, comme nous allons le voir tout de suite.

Pour autant, la stratégie *LBYL* n'est pas à jeter, il reste des cas où elle est parfaitement adaptée, quand les conditions ne sont pas amenées à changer entre les pré-conditions et l'opération.
C'est le cas par exemple du test pour le quotient nul dans la division, s'il est non-nul à l'instant *t*, il sera toujours à *t+1*.
