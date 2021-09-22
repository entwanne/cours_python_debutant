### Découpage en fonctions

On le sait, et je le répète depuis le début : le code actuel de notre TP est très répétitif.
Le but ici va donc être de le factoriser pour enfin gagner en lisibilité.

Pour cela on va se donner les différents objectifs suivants :

* Diviser et grouper les différentes commandes de saisie et de validation en fonctions.
* Ajouter une fonction pour initialiser un nouveau joueur.
* Ajouter une fonction pour réaliser un tour de jeu (joueur courant contre adversaire).
* Ajouter une fonction dédiée à l'application d'une attaque.
* Ajouter une fonction pour identifier le gagnant.
* Paramétrer ces fonctions selon les besoins.

Cette liste d'objectifs est bien sûr donnée à titre indicatif, n'hésitez pas à ajouter d'autres fonctions si vous les trouvez utiles.

#### Solution

Voici la solution que je propose pour ce TP.
Elle repose sur plusieurs fonctions, notamment `get_choice_input(choices, error_message)` qui permet de demander une saisie à l'utilisateur et de la vérifier en fonction des choix prévus, et `game_turn(player, opponent)` qui exécute un tour de jeu (sélection et application d'une attaque).

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
| player1, player2 = get_players()
| 
| print()
| print(player1['monster']['name'], 'affronte', player2['monster']['name'])
| print()
| 
| while player1['pv'] > 0 and player2['pv'] > 0:
|     game_turn(player1, player2)
|     game_turn(player2, player1)
| 
| winner = get_winner(player1, player2)
| print('Le joueur', winner['id'], 'remporte le combat avec', winner['monster']['name'])
| ```
