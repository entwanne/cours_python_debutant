### Tests

On va maintenant ajouter quelques tests à notre jeu, pour vérifier le bon comportement de certaines fonctions.  
Malheureusement, beaucoup de nos fonctions attendent des saisies de l'utilisateur, et nous ne sommes pas en mesure de les tester automatiquement pour le moment.

Nos tests vont donc se résumer aux fonctions qui n'intéragissent pas avec l'utilisateur : dans ma solution il s'agit des fonctions `apply_attack` et `get_winner`.
Pour les autres fonctions, il faudra pour l'instant se contenter de tests manuels en exécutant le code du TP.

Pour la fonction `apply_attack`, nous voulons nous assurer que les dégâts correspondants à l'attaque sont bien soustraits aux points de vie du joueur adverse.
Nous souhaitons aussi vérifier que les points de vie ne descendent jamais en dessous de zéro.

Pour ce qui est de `get_winner`, on cherche à contrôler que c'est le joueur avec le plus de points de vie qui est identifié comme gagnant.
Le cas de l'égalité entre joueurs ne nous intéresse pas vraiment, car il ne peut pas se produire en jeu, mais on peut toujours le vérifier pour s'assurer que la fonction est cohérente (renvoie toujours le deuxième joueur par exemple).

#### Solution

Voilà donc les deux fonctions de tests que l'on peut ajouter et exécuter dans notre TP pour vérifier le comportement de nos fonctions.

[[s]]
| ```python
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
| ```
