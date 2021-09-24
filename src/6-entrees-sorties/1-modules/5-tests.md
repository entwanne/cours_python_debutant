### Modules de tests

Revenons-en à notre dernier TP.
Il serait intéressant dans un premier temps de séparer les tests du reste du code.
Ils n'ont en effet pas de raison particulière d'être placés là.

Dans un fichiers `tests.py`, on va donc placer toutes les fonctions `test_*`.
Mais ce module `tests` n'aura par défaut pas accès aux fonctions à tester, il va donc nous falloir les importer.
Au début du module `tests`, on placera donc les lignes d'import suivantes.

```python
from game import ...
from game import ...
```

Aussi, vous vous souvenez de notre fonction pour réunir tous les tests ?
Elle n'a maintenant plus lieu d'être, étant donné que nous sommes dans un module à part nous savons que son code ne sera pas exécuté par erreur.

On peut donc placer les appels des fonctions de tests à la toute fin de notre module.
Enfin pas tout à fait, on va inclure nos appels dans un bloc conditionnel `if __name__ == '__main__':`.

```python
if __name__ == '__main__':
    test_...()
    test_...()
```

Cette ligne obscure permet de savoir si on exécute directement le module ou si on l'importe.
En effet, la variable spéciale `__name__` contient le nom du module.
Dans le cas où le module est exécuté directement par Python (`python tests.py`), ce nom vaudra `'__main__'` (il s'agira sinon de `'tests'` lors d'un import).

Par cette ligne, nous nous assurons donc que les fonctions de tests ne seront pas exécutées lors d'un import.
Ce n'est pas très important pour un module de tests qui n'a pas vocation à être importé, mais ça reste un outil pratique pour qu'un script soit importable.
C'est donc toujours une bonne habitude à prendre.

```python
print('A')

if __name__ == '__main__':
    print('B')
```
Code: foo.by

```bash
$ python foo.by
A
B
```

```python
>>> import foo
A
```

Nous allons d'ailleurs aussi modifier le code de notre TP pour ajouter une telle condition `if __name__ == '__main__':` et y placer le code qui ne figure dans aucune fonction.
Ça nous évitera d'avoir le code du jeu qui s'exécute lors d'un `import game` depuis les tests.

[[s]]
| ```python
| monsters = {
|     'pythachu': {
|         'name': 'Pythachu',
|         'attacks': ['tonnerre', 'charge'],
|     },
|     'pythard': {
|         'name': 'Pythard',
|         'attacks': ['jet-de-flotte', 'charge'],
|     },
|     'ponytha': {
|         'name': 'Ponytha',
|         'attacks': ['brûlure', 'charge'],
|     },
| }
| 
| attacks = {
|     'charge': {'damages': 20},
|     'tonnerre': {'damages': 50},
|     'jet-de-flotte': {'damages': 40},
|     'brûlure': {'damages': 40},
| }
| 
| 
| def get_choice_input(choices, error_message):
|     entry = input('> ').lower()
|     while entry not in choices:
|         print(error_message)
|         entry = input('> ').lower()
|     return choices[entry]
| 
| 
| def get_player(player_id):
|     print('Joueur', player_id, 'quel monstre choisissez-vous ?')
|     monster = get_choice_input(monsters, 'Monstre invalide')
|     pv = int(input('Quel est son nombre de PV ? '))
|     return {'id': player_id, 'monster': monster, 'pv': pv}
| 
| 
| def get_players():
|     print('Monstres disponibles :')
|     for monster in monsters.values():
|         print('-', monster['name'])
|     return get_player(1), get_player(2)
| 
| 
| def apply_attack(attack, opponent):
|     opponent['pv'] -= attack['damages']
|     if opponent['pv'] < 0:
|         opponent['pv'] = 0
| 
| 
| def game_turn(player, opponent):
|     # Si le joueur est KO, il n'attaque pas
|     if player['pv'] <= 0:
|         return
| 
|     print('Joueur', player['id'], 'quelle attaque utilisez-vous ?')
|     for name in player['monster']['attacks']:
|         print('-', name.capitalize(), -attacks[name]['damages'], 'PV')
| 
|     attack = get_choice_input(attacks, 'Attaque invalide')
|     apply_attack(attack, opponent)
| 
|     print(
|         player['monster']['name'],
|         'attaque',
|         opponent['monster']['name'],
|         'qui perd',
|         attack['damages'],
|         'PV, il lui en reste',
|         opponent['pv'],
|     )
| 
| 
| def get_winner(player1, player2):
|     if player1['pv'] > player2['pv']:
|         return player1
|     else:
|         return player2
| 
| 
| if __name__ == '__main__':
|     player1, player2 = get_players()
| 
|     print()
|     print(player1['monster']['name'], 'affronte', player2['monster']['name'])
|     print()
| 
|     while player1['pv'] > 0 and player2['pv'] > 0:
|         game_turn(player1, player2)
|         game_turn(player2, player1)
| 
|     winner = get_winner(player1, player2)
|     print('Le joueur', winner['id'], 'remporte le combat avec', winner['monster']['name'])
| ```
