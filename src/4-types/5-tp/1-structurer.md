### Structurer les données

Un monstre devient alors une structure avec un nom et une liste d'attaques.
Et une attaque se compose simplement d'un nombre de dégâts.

Dans le chapitre sur les dictionnaires, je présentais comment les utiliser pour former des données composites, avec un exemple correspondant à notre TP.
En repartant de cet exemple on va pouvoir structurer facilement nos monstres et nos attaques.

```python
monsters = {
    'pythachu': {
        'name': 'Pythachu',
        'attacks': ['tonnerre', 'charge'],
    },
    'pythard': {
        'name': 'Pythard',
        'attacks': ['jet-de-flotte', 'charge'],
    },
    'ponytha': {
        'name': 'Ponytha',
        'attacks': ['brûlure', 'charge'],
    },
}

attacks = {
    'charge': {'damages': 20},
    'tonnerre': {'damages': 50},
    'jet-de-flotte': {'damages': 40},
    'brûlure': {'damages': 40},
}
```

L'avantage de cette structure c'est que les attaques sont pleinement séparées des monstres, ce qui permet de ne pas les répéter quand elles sont partagées entre plusieurs monstres.

Le second avantage c'est qu'on est maintenant en mesure de définir précisément quel monstre peut utiliser quelle attaque, et donc d'avoir une meilleure validation à ce niveau.

Pour commencer le jeu, on demandera toujours aux deux joueurs de choisir leur monstre et d'indiquer les points de vie associés, mais on pourra maintenant vérifier qu'il s'agit d'un monstre que l'on connaît.

```python
print('Monstres disponibles :')
for monster in monsters.values():
    print('-', monster['name'])

players = []

print('Joueur 1, quel monstre choisissez-vous ?')
name = input('> ').lower()
while name not in monsters:
    print('Monstre invalide')
    name = input('> ').lower()
pv = int(input('Quel est son nombre de PV ? '))
players.append({'id': '1', 'monster': name, 'pv': pv})
```

Le fait d'utiliser des dictionnaires pour représenter nos joueurs nous permet aussi de les stocker dans une liste plutôt que dans deux variables distinctes, et donc d'éviter les répétitions que l'on avait dans nos traitements (puisque l'on va pouvoir appliquer une boucle sur cette liste).
