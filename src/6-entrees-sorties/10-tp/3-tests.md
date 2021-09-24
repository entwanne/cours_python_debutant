### Tests

Maintenant que l'on a un paquet dédié à notre TP, il va être plus simple de le tester depuis l'extérieur.
On va pouvoir déplacer nos tests dans un fichier `test_tp.py` à l'extérieur du paquet.  
Depuis ce fichier, on importera les différentes fonctions que l'on souhaite tester.

À notre module, on va ajouter des fonctions pour tester nos fonctions de sauvegarde.
Vérifier qu'une sauvegarde se fait correctement vers le fichier et qu'il est possible d'en charger une ensuite.

#### Solution

Retrouvez maintenant ci-dessous la solution que je propose pour ce TP.

[[s]]
| ```python
| import json
| 
| from tp.definitions import monsters, attacks
| from tp.game import apply_attack, get_winner
| from tp.save import load_game, save_game
| 
| 
| def test_apply_attack():
|     player = {'id': 0, 'monster': monsters['pythachu'], 'pv': 100}
| 
|     apply_attack(attacks['brûlure'], player)
|     assert player['pv'] == 60
| 
|     apply_attack(attacks['tonnerre'], player)
|     assert player['pv'] == 10
| 
|     apply_attack(attacks['charge'], player)
|     assert player['pv'] == 0
| 
| 
| def test_get_winner():
|     player1 = {'id': 0, 'monster': monsters['pythachu'], 'pv': 100}
|     player2 = {'id': 0, 'monster': monsters['pythard'], 'pv': 0}
|     assert get_winner(player1, player2) == player1
|     assert get_winner(player2, player1) == player1
| 
|     player2['pv'] = 120
|     assert get_winner(player1, player2) == player2
|     assert get_winner(player2, player1) == player2
| 
|     player1['pv'] = player2['pv'] = 0
|     assert get_winner(player1, player2) == player2
|     assert get_winner(player2, player1) == player1
| 
| 
| def test_load_game():
|     filename = 'test_game.dat'
|     with open(filename, 'w') as f:
|         json.dump([
|             {'id': 1, 'monster': 'pythachu', 'pv': 50},
|             {'id': 2, 'monster': 'pythard', 'pv': 40},
|         ], f)
| 
|     p1, p2 = load_game(filename)
|     assert p1 == {
|         'id': 1,
|         'monster': monsters['pythachu'],
|         'pv': 50,
|     }
|     assert p2 == {
|         'id': 2,
|         'monster': monsters['pythard'],
|         'pv': 40,
|     }
| 
| 
| def test_save_game():
|     filename = 'test_game.dat'
|     player1 = {
|         'id': 1,
|         'monster': monsters['pythachu'],
|         'pv': 30,
|     }
|     player2 = {
|         'id': 2,
|         'monster': monsters['ponytha'],
|         'pv': 20,
|     }
|     save_game(filename, player1, player2)
| 
|     with open(filename) as f:
|         doc = json.load(f)
| 
|     assert doc == [
|         {'id': 1, 'monster': 'pythachu', 'pv': 30},
|         {'id': 2, 'monster': 'ponytha', 'pv': 20},
|     ]
| 
| 
| if __name__ == '__main__':
|     test_apply_attack()
|     test_get_winner()
|     test_load_game()
|     test_save_game()
| ```
| Code: `test_tp.py`

[[w]]
| On remarque qu'après l'exécution de nos tests, un fichier `test_game.dat` persiste dans le répertoire courant.
| Ce n'est pas très grave pour l'instant mais ce n'est pas très propre non plus.
|
| Il existe une manière d'éviter cela à l'aide [du module `tempfile`](https://docs.python.org/fr/3/library/tempfile.html) de la bibliothèque standard pour créer un fichier temporaire.
