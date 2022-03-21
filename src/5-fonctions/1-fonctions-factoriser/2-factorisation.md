### Factoriser

La question va maintenant être de savoir comment identifier et réunir les portions logiques pour éviter les répétitions.

Mais souvent, on ne sera pas face à deux codes strictement identiques, ils seront simplement similaires.
L'idée sera alors de travailler à les rendre identiques afin de les factoriser en une unique fonction.
Pour cela, il faudra identifier les paramètres variables qui agissent sur le code et le font se différencier.
Une fois ces paramètres isolés et placés dans des variables avant la portion concernée, le code deviendra factorisable.

Prenons l'exemple suivant, qui affiche les tables de multiplication de `3` et de `5`.

```python
for i in range(1, 11):
    print(3, '×', i, '=', 3*i)

for i in range(1, 11):
    print(5, '×', i, '=', 5*i)
```

On a deux boucles très semblables qui ne sont pourtant pas identiques.
Un paramètre diffère entre les deux, le nombre par lequel on multiplie.
Si l'on isole ce nombre dans une variable, on constate que nos deux boucles deviennent identiques.

```python
n = 3
for i in range(1, 11):
    print(n, '×', i, '=', n*i)

n = 5
for i in range(1, 11):
    print(n, '×', i, '=', n*i)
```

On pourrait alors écrire une fonction pour réaliser ces opérations, paramétrée selon la valeur de `n`.

C'est donc en ça que consiste le travail de factorisation : œuvrer pour que des codes similaires mais différents puisse utiliser une fonction commune.

#### Identifier les portions logiques dans un code plus complet

Pour s'exercer sur un cas d'usage réel, on peut reprendre le code du dernier TP que je réinsère ci-dessous.
Notre travail va alors être d'identifier les différentes sections qui composent notre programme et qui pourront donc être séparées en fonctions.

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

À sa lecture on distingue ainsi plusieurs blocs avec des logiques bien distinctes :
* Lignes 1 à 21, la définition de nos données.
* Lignes 23 à 25, l'affichage des monstres existants.
* Lignes 27 à 44, la sélection des joueurs, et plus particulièrement :
    * Lignes 34 à 40, la sélection d'un joueur.
    * Lignes 34 à 37, la validation des monstres.
    * Lignes 42 à 44, l'affichage des monstres en jeu.
* Lignes 46 à 50, la définition des tours de jeu.
* Lignes 52 à 77, la boucle jeu et le déroulement des combats, notamment :
    * Lignes 57 à 77, le déroulement du combat pour un joueur.
    * Lignes 57 à 65, le choix d'une attaque.
    * Lignes 67 à 77, l'application d'une attaque (avec affichage).
* Lignes 79 à 84, la désignation du vainqueur.

L'écriture des fonctions correspondant à ces différentes logiques sera l'objet du prochain TP.
