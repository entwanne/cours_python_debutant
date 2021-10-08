### Tour de jeu

Un tour de jeu se divise en deux manches, d'abord le premier monstre attaque le second, puis l'inverse.

Nous ne sommes pour l'instant pas en mesure de traiter une liste d'attaques, nous demanderons alors simplement aux joueurs d'entrer le nombre de dégâts qu'ils souhaitent infliger à l'adversaire.
Comme précédemment, on utilisera pour ça la fonction `input` et la conversion dans le type voulu.

À partir de ces dégâts, on calculera alors le nombre de points de vie restants du monstre cible, afin de les afficher dans un récapitulatif.
Nous utiliserons toutes les données recueillies pour fournir le plus d'informations possibles aux joueurs.

À la suite de nos deux manches, on pourra afficher un résumé de la partie.

Voici ce à quoi pourrait ressembler un tour de jeu.

```
Pythachu, combien de dégâts infligez-vous à Pythard ? 30

+++++++++++++++++++++++++++++++++++++++++++
+ Pythachu attaque Pythard qui perd 30 PV +
+ Pythard a maintenant 10 PV              +
+++++++++++++++++++++++++++++++++++++++++++

Pythard, combien de dégâts infligez-vous à Pythachu ? 15

+++++++++++++++++++++++++++++++++++++++++++
+ Pythard attaque Pythachu qui perd 15 PV +
+ Pythachu a maintenant 35 PV             +
+++++++++++++++++++++++++++++++++++++++++++

+++++++++++++++++++++++
+ Résulat du combat : +
+ Pythachu a 35 PV    +
+ Pythard a 10 PV     +
+++++++++++++++++++++++
```


#### Solution

L'affichage correct du cadre autour des messages pourrait vous donner du fil à retordre, pensez à la fonction `max` pour en connaître la taille.

Je vous propose la solution suivante à cette deuxième partie, mais prenez d'abord le temps de compléter la vôtre.

[[s]]
| ```python
| att1 = int(input(name1 + ', combien de PV infligez-vous à ' + name2 + ' ? '))
|
| print()
|
| pv2 -= att1
| msg1 = name1 + ' attaque ' + name2 + ' qui perd ' + str(att1) + ' PV'
| msg2 = name2 + ' a maintenant ' + str(pv2) + ' PV'
| max_size = max(len(msg1), len(msg2))
| msg1 += ' ' * (max_size - len(msg1))
| msg2 += ' ' * (max_size - len(msg2))
| print('+' * (max_size+4))
| print('+', msg1, '+')
| print('+', msg2, '+')
| print('+' * (max_size+4))
|
| print()
|
| att2 = int(input(name2 + ', combien de PV infligez-vous à ' + name1 + ' ? '))
|
| print()
|
| pv1 -= att2
| msg1 = name2 + ' attaque ' + name1 + ' qui perd ' + str(att2) + ' PV'
| msg2 = name1 + ' a maintenant ' + str(pv1) + ' PV'
| max_size = max(len(msg1), len(msg2))
| msg1 += ' ' * (max_size - len(msg1))
| msg2 += ' ' * (max_size - len(msg2))
| print('+' * (max_size+4))
| print('+', msg1, '+')
| print('+', msg2, '+')
| print('+' * (max_size+4))
|
| print()
|
| msg1 = 'Résulat du combat :'
| msg2 = name1 + ' a ' + str(pv1) + ' PV'
| msg3 = name2 + ' a ' + str(pv2) + ' PV'
| max_size = max(len(msg1), len(msg2), len(msg3))
| msg1 += ' ' * (max_size - len(msg1))
| msg2 += ' ' * (max_size - len(msg2))
| msg3 += ' ' * (max_size - len(msg3))
| print('+' * (max_size+4))
| print('+', msg1, '+')
| print('+', msg2, '+')
| print('+', msg3, '+')
| print('+' * (max_size+4))
| ```
|
| * On appelle `input` avec un message formaté à l'aide de concaténations, on prend soin d'en convertir le retour en `int`.
| * Ce nombre de dégâts est ensuite utilisé pour décrémenter les PV de l'ennemi.
| * Pour l'affichage du cadre, celui-ci contient maintenant deux lignes différentes. Il faut alors calculer la taille maximale (`max_size`) à l'aide de la fonction `max` pour connaître la taille des lignes haute et basse.
| * La longueur maximale sert aussi à calculer les marges pour que nos deux lignes s'intègrent correctement dans le cadre, en ajoutant autant d'espaces que besoin. On n'a pas peur pour cela de multiplier notre chaîne `' '` par un nombre négatif.
| * On remarque pas mal de répétitions dans le code, ce n'est pas idéal et on verra comment y remédier dans un prochain chapitre.
