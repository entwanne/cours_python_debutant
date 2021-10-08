### Sauvegarde

Venons-en maintenant à l'objectif de ce TP : la sauvegarde du jeu.  
On pourra pour cela ajouter un fichier `save.py` à notre paquet contenant une fonction `load_game(filename)` pour charger une sauvegarde depuis un fichier, renvoyant les deux joueurs ainsi chargés, et une fonction `save_game(filename, player1, player2)` pour enregistrer la sauvegarde (l'état des deux joueurs) dans un fichier.

Dans la boucle principale de notre jeu, on ajoutera donc une question pour demander à l'utilisateur s'il souhaite continuer ou s'arrêter.
En cas d'arrêt, on lui demandera alors s'il souhaite sauvegarder la partie et dans quel fichier.

```text
% python -m tp
Monstres disponibles :
- Pythachu
- Pythard
- Ponytha
Joueur 1 quel monstre choisissez-vous ?
> Pythachu
Quel est son nombre de PV ? 100
Joueur 2 quel monstre choisissez-vous ?
> Ponytha
Quel est son nombre de PV ? 120

Pythachu affronte Ponytha

Voulez-vous continuer ? [O/n] o
Joueur 1 quelle attaque utilisez-vous ?
- Tonnerre -50 PV
- Charge -20 PV
> tonnerre
Pythachu attaque Ponytha qui perd 50 PV, il lui en reste 70
Joueur 2 quelle attaque utilisez-vous ?
- Brûlure -40 PV
- Charge -20 PV
> brûlure
Ponytha attaque Pythachu qui perd 40 PV, il lui en reste 60
Voulez-vous continuer ? [O/n] n
Voulez-vous sauvegarder ? [o/N] o
Dans quel fichier sauvegarder ? game.dat
```

Dans l'autre sens, on permettra au programme de prendre un argument pour charger le jeu depuis la sauvegarde pointée par ce fichier.

```text
% python -m tp game.dat
Pythachu affronte Ponytha

Voulez-vous continuer ? [O/n] 
Joueur 1 quelle attaque utilisez-vous ?
- Tonnerre -50 PV
- Charge -20 PV
> tonnerre
Pythachu attaque Ponytha qui perd 50 PV, il lui en reste 20
[...]
```

On privilégiera le format JSON pour le fichier de sauvegarde.

#### Solution

Voici maintenant la solution à cet exercice, qui repose principalement sur le fichier `tp/save.py`, dont les fonctions sont appelées dans le module `game`.

On peut voir aussi la fonction `get_yesno_input` dans le module `prompt`.
C'est une fonction qui permet de poser une question qui attend pour réponse oui ou non (`[O/n]`).
Elle propose aussi de définir une valeur par défaut, reconnaissable à la lettre en majuscule (`O` ici pour `Oui`).  
Ainsi si l'utilisateur entre une ligne vide, c'est cette valeur par défaut qui sera utilisée.

[[s]]
| ```python
| ```
| Code: `tp/__init__.py`
|
| ```python
| from . import game
| 
| 
| if __name__ == '__main__':
|     game.main()
| ```
| Code: `tp/__main__.py`
|
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
| ```
| Code: `tp/definitions.py`
|
| ```python
| import sys
| 
| from .definitions import attacks
| from .players import get_players
| from .prompt import get_choice_input, get_yesno_input
| from .save import load_game, save_game
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
| def main():
|     if len(sys.argv) > 1:
|         filename = sys.argv[1]
|         try:
|             # Chargement de la sauvegarde
|             player1, player2 = load_game(filename)
|         except:
|             print('Échec du chargement de la sauvegarde', filename, file=sys.stderr)
|             return
|     else:
|         player1, player2 = get_players()
| 
|     print()
|     print(player1['monster']['name'], 'affronte', player2['monster']['name'])
|     print()
| 
|     while player1['pv'] > 0 and player2['pv'] > 0:
|         if not get_yesno_input('Voulez-vous continuer ? ', True):
|             if get_yesno_input('Voulez-vous sauvegarder ? ', False):
|                 filename = input('Dans quel fichier sauvegarder ? ')
|                 save_game(filename, player1, player2)
|             return
| 
|         game_turn(player1, player2)
|         game_turn(player2, player1)
| 
|     winner = get_winner(player1, player2)
|     print('Le joueur', winner['id'], 'remporte le combat avec', winner['monster']['name'])
| ```
| Code: `tp/game.py`
|
| ```python
| from .definitions import monsters
| from .prompt import get_choice_input
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
| ```
| Code: `tp/players.py`
|
| ```python
| def get_choice_input(choices, error_message):
|     entry = input('> ').lower()
|     while entry not in choices:
|         print(error_message)
|         entry = input('> ').lower()
|     return choices[entry]
| 
| 
| def get_yesno_input(prompt, default):
|     if default:
|         prompt += '[O/n] '
|     else:
|         prompt += '[o/N] '
| 
|     resp = input(prompt).lower()
|     if resp.startswith('o'):
|         return True
|     elif resp.startswith('n'):
|         return False
|     return default
| ```
| Code: `tp/prompt.py`
|
| ```python
| import json
| 
| from .definitions import monsters
| 
| 
| def load_game(filename):
|     with open(filename) as f:
|         player1, player2 = json.load(f)
|     # On récupère les monstres à partir de leurs noms
|     player1['monster'] = monsters[player1['monster']]
|     player2['monster'] = monsters[player2['monster']]
|     return player1, player2
| 
| 
| def save_game(filename, player1, player2):
|     player1 = dict(player1)
|     player2 = dict(player2)
|     # On enregistre seulement le nom des monstres
|     player1['monster'] = player1['monster']['name'].lower()
|     player2['monster'] = player2['monster']['name'].lower()
|     with open(filename, 'w') as f:
|         json.dump([player1, player2], f)
| ```
| Code: `tp/save.py`
