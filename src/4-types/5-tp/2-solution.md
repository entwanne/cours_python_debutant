### Solution

On retrouve maintenant la solution à ce TP, qui se rapproche de plus en plus d'un vrai système de combat.

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
| print('Monstres disponibles :')
| for monster in monsters.values():
|     print('-', monster['name'])
| 
| players = []
| 
| # Boucle pour créer 2 joueurs sans se répéter
| for i in range(2):
|     player_id = i + 1
|     print('Joueur', player_id, 'quel monstre choisissez-vous ?')
| 
|     name = input('> ').lower()
|     while name not in monsters:
|         print('Monstre invalide')
|         name = input('> ').lower()
| 
|     pv = int(input('Quel est son nombre de PV ? '))
|     players.append({'id': player_id, 'monster': monsters[name], 'pv': pv})
| 
| print()
| print(players[0]['monster']['name'], 'affronte', players[1]['monster']['name'])
| print()
| 
| # Représente les tours de jeu, liste de couples (joueur, opposant)
| turns = [
|     (players[0], players[1]),
|     (players[1], players[0]),
| ]
| 
| while players[0]['pv'] > 0 and players[1]['pv'] > 0:
|     # On effectue les deux tours de jeu
|     for player, opponent in turns:
|         # Le joueur ne peut jouer que s'il n'est pas KO
|         if player['pv'] > 0:
|             print('Joueur', player['id'], 'quelle attaque utilisez-vous ?')
|             for name in player['monster']['attacks']:
|                 print('-', name.capitalize(), -attacks[name]['damages'], 'PV')
| 
|             att_name = input('> ').lower()
|             while att_name not in attacks:
|                 print('Attaque invalide')
|                 att_name = input('> ').lower()
|             attack = attacks[att_name]
| 
|             opponent['pv'] -= attack['damages']
| 
|             print(
|                 player['monster']['name'],
|                 'attaque',
|                 opponent['monster']['name'],
|                 'qui perd',
|                 attack['damages'],
|                 'PV, il lui en reste',
|                 opponent['pv'],
|             )
| 
| if players[0]['pv'] > players[1]['pv']:
|     winner = players[0]
| else:
|     winner = players[1]
| 
| print('Le joueur', winner['id'], 'remporte le combat avec', winner['monster']['name'])
| ```

À l'exécution, on a bien quelque chose d'assez clair sur le déroulement du jeu.

```text
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

Joueur 1 quelle attaque utilisez-vous ?
- Tonnerre -50 PV
- Charge -20 PV
> tonnerre
Pythachu attaque Ponytha qui perd 50 PV, il lui en reste 70
Joueur 2 quelle attaque utilisez-vous ?
- Brûlure -40 PV
- Charge -20 PV
> charge
Ponytha attaque Pythachu qui perd 20 PV, il lui en reste 80
Joueur 1 quelle attaque utilisez-vous ?
- Tonnerre -50 PV
- Charge -20 PV
> charge
Pythachu attaque Ponytha qui perd 20 PV, il lui en reste 50
Joueur 2 quelle attaque utilisez-vous ?
- Brûlure -40 PV
- Charge -20 PV
> brulure
Attaque invalide
> brûlure
Ponytha attaque Pythachu qui perd 40 PV, il lui en reste 40
Joueur 1 quelle attaque utilisez-vous ?
- Tonnerre -50 PV
- Charge -20 PV
> tonnerre
Pythachu attaque Ponytha qui perd 50 PV, il lui en reste 0
Le joueur 1 remporte le combat avec Pythachu
```
