### Tout ne se passe pas comme prévu

On a déjà rencontré des exceptions, ce sont les erreurs qui se produisent quand une opération échoue (conversion impossible, élément inexistant dans un dictionnaire, ouverture d'un fichier introuvable, etc.).
L'erreur survient alors sous la forme d'une exception avec un type particulier (`ValueError`, `TypeError`, `KeyError`, etc.).

Le souci c'est que cela coupe l'exécution de la fonction et du programme (hors interpréteur interactif).

Imaginons que nous souhaitions au chargement de notre jeu regarder si une sauvegarde existe.
On essaierait alors d'ouvrir le fichier de sauvegarde, et s'il n'existe pas on obtiendrait une exception.

```python
with open('game.sav') as save:
    state = load_game(save.read())

print('Jeu en cours...')
```
Code: game.py

À l'exécution :

```python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'game.sav'
```

Ainsi, le programme s'arrête à l'exception, ce qui est plutôt embêtant.
Notre jeu devrait être en mesure de démarrer sans sauvegarde existante, de traiter l'erreur et de continuer.

Pour autant une exception peut être un comportement attendu, d'autant plus si elle provient d'une valeur entrée par l'utilisateur.
Dans une calculatrice, on ne veut pas que le programme plante si l'utilisateur demande une division par zéro.
De même dans un annuaire si un nom n'est pas trouvé.

```python
def calculatrice(a, op, b):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        return a / b
    print('Calcul impossible')
```

```pycon
>>> calculatrice(3, '+', 0)
3
>>> calculatrice(3, '/', 0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 9, in calculatrice
ZeroDivisionError: division by zero
```

Comment alors peut-on gérer ces erreurs pour éviter cela ?
