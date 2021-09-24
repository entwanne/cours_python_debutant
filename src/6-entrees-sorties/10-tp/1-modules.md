### Découpage en modules

Une première étape dans l'avancement de notre TP va être de le découper en modules.
En effet, nous l'avons précédemment découpé en fonctions, mais ces fonctions cohabitent toutes ensembles dans un joyeux bordel.  
Nous pouvons donc aller plus loin et réunir ces fonctions en unité logiques dans un paquet.

Je vous propose pour cela un paquet `tp` contenant des modules pour les différentes parties de notre jeu : définitions des données, gestion des joueurs, gestion des entrées utilisateur.
On gardera aussi un module `game` pour les fonctions principales du jeu.

#### Solution

Un découpage possible est le suivant.

J'ai utilisé un module `definitions` pour stocker les dictionnaires `monsters` et `attacks`.
Ce module est assimilable à une base de données, il n'y a que lui à faire évoluer pour ajouter de nouveaux monstres ou de nouvelles atatques.

En plus de ça, un module `prompt` reprend la fonction `get_choice_input` et un module `get_players` est dédié à l'instanciation des joueurs.

J'ai aussi ajouté un fichier `__main__.py` pour exécuter notre TP avec `python -m tp`.

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
| from .definitions import attacks
| from .players import get_players
| from .prompt import get_choice_input
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
| ```
| Code: `tp/prompt.py`

[[i]]
| Comme vous le voyez, j'ai ici laissé un fichier `__init__.py` car il ne nous est pas utile.
