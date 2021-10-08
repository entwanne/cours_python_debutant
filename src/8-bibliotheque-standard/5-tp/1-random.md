### L'aléatoire à la rescousse !

On va donc intégrer quelques doses d'aléatoire dans notre jeu, à différents niveaux :

* Pour le choix de monstre, l'ordinateur réalisera un choix aléatoire, de même pour son nombre de PV.
* Pour connaître l'ordre d'attaque entre les deux monstres, on pourra faire un tirage aléatoire (savoir qui commence).
* À chaque tour, l'ordinateur sélectionnera une attaque aléatoire pour son monstre. Ce choix pourra être pondéré selon les dégâts infligés par chaque attaque.

Pour plus de généricité, on aimerait ne pas avoir à gérer l'ordinateur comme un cas spécifique, et donc ne pas faire de différence de traitement entre nos deux joueurs.

Pour cela, je vous propose de modifier la structure des joueurs (le dictionnaire tel que renvoyé par la fonction `get_player`) pour y ajouter une fonction (un _callback_) associée à la clé `'chose_attack_func'`, qui pourra être appelée depuis la boucle de jeu pour demander au joueur de sélectionner une attaque.  
Dans le cas d'un joueur humain, cette fonction fera appel à `input`, et dans le cas de l'ordinateur elle opérera une sélection aléatoire. Mais la boucle de jeu n'en saura rien, ce sera totalement abstrait pour elle.

```python
attack = player['chose_attack_func'](player)
apply_attack(player, opponent)
```

En bonus, on pourrait ajouter un choix pour permettre au 2ème joueur d'être un humain ou un robot, voire que les deux joueurs soient des ordinateurs pour les observer combattre. :D

#### Solution

Je vous propose la solution suivante, n'hésitez pas à regarder plus en détails le mécanisme de _callback_.
J'ai aussi utilisé une interface commune entre les modules `players` et `ia`, avec une fonction `get_player` prenant un identifiant en argument et renvoyant un dictionnaire décrivant le joueur.

Pour la sélection du nombre de PV par l'ordinateur, j'ai utilisé une distribution normale, mais tout autre tirage serait correct.

Enfin, pour alléger le code, j'ai supprimé ce qui était relatif à la sauvegarde du jeu car ça n'est plus utile ici.

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
| import random
| 
| from .definitions import attacks
| from .prompt import get_choice_input
| from .players import get_player as get_real_player
| from .ia import get_player as get_ia_player
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
|     attack = player['chose_attack_func'](player)
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
|     players = [get_real_player(1), get_ia_player(2)]
|     random.shuffle(players)
|     player1, player2 = players
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
| import random
| 
| from .definitions import attacks, monsters
| 
| 
| def chose_monster():
|     values = list(monsters.values())
|     monster = random.choice(values)
|     return monster
| 
| 
| def chose_attack(player):
|     monster = player['monster']
|     weights = [attacks[name]['damages'] for name in monster['attacks']]
|     att_name = random.choices(monster['attacks'], weights=weights)[0]
|     print(f"Le joueur {player['id']} utilise {att_name}")
|     return attacks[att_name]
| 
| 
| def get_player(player_id):
|     monster = chose_monster()
|     pv = int(random.normalvariate(100, 10))
|     print(f"Le joueur {player_id} choisit {monster['name']} ({pv} PV)")
| 
|     return {
|         'id': player_id,
|         'monster': monster,
|         'pv': pv,
|         'chose_attack_func': chose_attack,
|     }
| ```
| Code: `tp/ia.py`
|
| ```python
| from .definitions import attacks, monsters
| from .prompt import get_choice_input
| 
| 
| def chose_attack(player):
|     print('Joueur', player['id'], 'quelle attaque utilisez-vous ?')
|     for name in player['monster']['attacks']:
|         print('-', name.capitalize(), -attacks[name]['damages'], 'PV')
| 
|     return get_choice_input(attacks, 'Attaque invalide')
| 
| 
| def get_player(player_id):
|     print('Monstres disponibles :')
|     for monster in monsters.values():
|         print('-', monster['name'])
| 
|     print('Joueur', player_id, 'quel monstre choisissez-vous ?')
|     monster = get_choice_input(monsters, 'Monstre invalide')
|     pv = int(input('Quel est son nombre de PV ? '))
|     return {
|         'id': player_id,
|         'monster': monster,
|         'pv': pv,
|         'chose_attack_func': chose_attack,
|     }
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
