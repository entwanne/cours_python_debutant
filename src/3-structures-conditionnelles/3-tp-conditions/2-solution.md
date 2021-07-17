### Solution

J'ai ici volontairement allégé le programme par rapport à la solution du précédent TP, en retirant tout ce qui avait trait au formatage des chaînes de caractères.
Mais n'hésitez pas à reprendre votre programme précédent pour le compléter avec ces nouvelles fonctionnalités.

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
| menu = '''quelle attaque voulez-vous utiliser ?
| 1. Charge (-20 PV)
| 2. Tonnerre (-50 PV)'''
| 
| # Joueur 1
| 
| print(name1, menu)
| att1 = input('> ').lower()
| 
| if att1 == '1' or att1 == 'charge':
|     damages = 20
| elif att1 == '2' or att1 == 'tonnerre':
|     damages = 50
| else:
|     print('Erreur de saisie')
|     damages = 0
| 
| pv2 -= damages
| print(name1, 'attaque', name2, 'qui perd', damages, 'PV')
| 
| # Joueur 2
| 
| print(name2, menu)
| att2 = input('> ').lower()
| 
| if att2 == '1' or att2 == 'charge':
|     damages = 20
| elif att2 == '2' or att2 == 'tonnerre':
|     damages = 50
| else:
|     print('Erreur de saisie')
|     damages = 0
| 
| pv1 -= damages
| print(name2, 'attaque', name1, 'qui perd', damages, 'PV')
| 
| if pv1 == pv2:
|     print('Match nul')
| elif pv1 > pv2:
|     print(name1, 'remporte le combat')
| else:
|     print(name2, 'remporte le combat')
| ```

Et à l'utilisation, on a bien un programme de combat un peu plus dynamique.

```
Entrez le nom du 1er joueur : Pythachu
Et son nombre de PV : 100
Entrez le nom du 2ème joueur : Ponytha
Et son nombre de PV : 100

Pythachu affronte Ponytha

Pythachu quelle attaque voulez-vous utiliser ?
1. Charge (-20 PV)
2. Tonnerre (-50 PV)
> 2
Pythachu attaque Ponytha qui perd 50 PV
Ponytha quelle attaque voulez-vous utiliser ?
1. Charge (-20 PV)
2. Tonnerre (-50 PV)
> Charge
Ponytha attaque Pythachu qui perd 20 PV
Pythachu remporte le combat
```

Mais il est difficile avec le code actuel d'ajouter de nouvelles attaques et l'on voit encore beaucoup de répétitions dans ce code.
Pas d'inquiétudes, nous corrigerons tout cela dans les chapitres qui viennent.
