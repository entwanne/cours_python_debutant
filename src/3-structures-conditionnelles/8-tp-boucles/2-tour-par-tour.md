### Un jeu au tour par tour

On va enfin vraiment avoir un jeu en tour par tour !

Grâce au `while`, il nous est en effet possible de répéter le processus de jeu jusqu'à ce que l'un des monstres soit KO.
Une ébauche était présentée dans le chapitre sur les boucles `while` et il nous suffit de la compléter ici.

On souhaiterait donc que notre programme boucle tant que les deux monstres ont encore des points de vie, c'est-à-dire que leurs PV sont strictement supérieurs à zéro.
À l'intérieur de la boucle, on saura donc que nos deux montres sont encore en vie.

Un petit détail auquel il nous faudra cependant penser : le premier monstre attaque avant le second et lui retire des points de vie.
Lors du tour du second monstre il est donc possible qu'il soit déjà KO, ce qui est censé l'empêcher d'attaquer.
On ajoutera donc une condition pour éviter de rencontrer un bug avec ce cas.

En fin de jeu, on peut aussi retirer la condition de match nul puisque celle-ci ne pourra plus se produire : un monstre sera forcément KO avant l'autre.

On se permettra enfin d'ajouter un récapitulatif après chaque attaque pour nous rappeler où nous en sommes dans les points de vie.

#### Solution

Voici sans plus attendre la solution de notre jeu qui en est maintenant vrailent un. :)

[[s]]
| ```python
| name1 = input('Entrez le nom du 1er joueur : ').capitalize()
| pv1 = int(input('Et son nombre de PV : '))
| 
| name2 = input('Entrez le nom du 2ème joueur : ').capitalize()
| pv2 = int(input('Et son nombre de PV : '))
| 
| print()
| print(name1, 'affronte', name2)
| print()
| 
| attack_names = ['charge', 'tonnerre']
| attack_damages = [20, 50]
| 
| menu = 'quelle attaque voulez-vous utiliser ?'
| 
| while pv1 > 0 and pv2 > 0:
|     # Joueur 1
| 
|     print(name1, menu)
|     i = 1
|     for name in attack_names:
|         print(i, name.capitalize(), -attack_damages[i - 1], 'PV')
|         i += 1
| 
|     att1 = input('> ')
|     while not att1.isdigit() or not 1 <= int(att1) <= len(attack_names):
|         print('Attaque invalide, veuillez resaisir le numéro')
|         att1 = input('> ')
| 
|     att1_idx = int(att1) - 1
|     damages = attack_damages[att1_idx]
| 
|     pv2 -= damages
|     print(name1, 'attaque', name2, 'qui perd', damages, 'PV, il lui en reste', pv2)
| 
|     # Joueur 2
|     if pv2 > 0:
|         print(name2, menu)
|         i = 1
|         for name in attack_names:
|             print(i, name.capitalize(), -attack_damages[i - 1], 'PV')
|             i += 1
| 
|         att2 = input('> ')
|         while not att2.isdigit() or not 1 <= int(att1) <= len(attack_names):
|             print('Attaque invalide, veuillez resaisir le numéro')
|             att1 = input('> ')
| 
|         att2_idx = int(att2) - 1
|         damages = attack_damages[att2_idx]
| 
|         pv1 -= damages
|         print(name2, 'attaque', name1, 'qui perd', damages, 'PV, il lui en reste', pv1)
| 
| if pv1 > pv2:
|     print(name1, 'remporte le combat')
| else:
|     print(name2, 'remporte le combat')
| ```

[[i]]
| Si vous faites bien attention, vous remarquerez que l'on peut arriver dans un cas où les PV d'un monstre sont négatifs.  
| Ce n'est pas très grave parce que cela ne change rien au déroulement du jeu, mais cela peut facilement se régler à l'aide
| d'une condition ou d'un appel à la fonction `max` : `pv2 = max(pv2 - damanges, 0)`.
