## Débogage

Les bugs sont monnaie courante en programmation.
Une erreur d'inattention est vite arrivée, et hop, un bug se glisse dans le programme.

Ils peuvent prendre de multiples formes : parfois ils feront planter purement et simplement l'application, d'autres mèneront à des traitements incohérents voire à des failles de sécurité, d'autres encore pourront être invisibles.  
Mais quand un bug est repéré, il est encore loin d'être identifié : il faut trouver quelle fonction n'a pas eu un traitement correct et sur quelles données le problème survient.  
Il s'agit alors de tenter de reproduire l'erreur dans différentes conditions pour l'identifier, pour enfin être en mesure de la corriger.
C'est ce que l'on appelle le débogage !

Je ne peux que vous conseiller d'être attentif et de bien tester vos codes pour les éviter au maximum, malheureusement ce n'est pas toujours suffisant.  
Aussi, pour ne pas vous retrouver désemparé quand un bug survient (qu'il soit décelé lorsque l'application tourne ou lors de tests), voici un petit guide pour apprendre à trouver l'origine du bug et la corriger.

Nous prendrons pour exemple au long de ce chapitre le programme suivant de combat entre monstres et qui présente plusieurs bugs :

```python
import json


def input_choice(prompt, choices):
    value = None
    prompt += '(' + '/'.join(choices) + ') '
    while value not in choices:
        print('Valeur invalide')
        value = input(prompt)
    return value


def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Nombre invalide')


with open('data.json') as f:
    data = json.load(f)
    attacks = data['attacks']
    monsters = data['monsters']


def input_player():
    name = input_choice('Monstre: ', monsters)
    monster = monsters[name]
    pv = input_int('PV du monstre: ')
    return {'monster': monster, 'pv': pv}


def input_attack(player):
    monster = player['monster']
    name = input_choice(f"Attaque de {monster['name']}: ", monster['attacks'])
    return attacks[name]


def apply_attack(player1, player2, attack):
    print(player1['monster']['name'], 'utilise', attack['name'], ':',
          player2['monster']['name'], 'perd', attack['damage'], 'PV')
    player1['pv'] -= attack['damage']


if __name__ == '__main__':
    player1 = input_player()
    player2 = input_player()
    print(player1['monster']['name'], 'vs', player2['monster']['name'])

    while player1['pv'] and player2['pv'] > 0:
        print(player1['monster']['name'], player1['pv'], 'PV')
        print(player2['monster']['name'], player2['pv'], 'PV')

        attack = input_attack(player1)
        apply_attack(player1, player2, attack)

        if player2['pv'] > 0:
            attack = input_attack(player2)
            apply_attack(player1, player2, attack)

    if player1['pv'] > 0:
        print(player1['monster']['name'], 'gagne')
    else:
        print(player2['monster']['name'], 'gagne')
```
Code: battle.py

Il s'accompagne du fichier de données ci-dessous.

```js
{
    "attacks": {
	"charge": {"name": "Charge", "damage": 20},
	"tonnerre": {"name": "Tonnerre", "damage": 50},
	"jet-de-flotte": {"name": "Jet de flotte", "damages": 50},
	"jet-de-flamme": {"name": "Jet de flamme", "damage": 60}
    },
    "monsters": {
	"pythachu": {
	    "name": "Pythachu",
	    "attacks": ["charge", "tonnerre", "eclair"]
	},
	"pythard": {
	    "name": "Pythard",
	    "attacks": ["charge", "jet-de-flotte"]
	},
	"ponytha": {
	    "name": "Ponytha",
	    "attacks": ["charge", "jet-de-flamme"]
	}
    }
}
```
Code: data.json

Vous pouvez dores et déjà tenter d'exécuter le programme, et constater que celui-ci a un comportement incohérent voire lève une exception.

```shell
% python battle.py
Valeur invalide
Monstre: (pythachu/pythard/ponytha) pythachu
PV du monstre: 10
Valeur invalide
Monstre: (pythachu/pythard/ponytha) pythard
PV du monstre: 10
Pythachu vs Pythard
Pythachu 10 PV
Pythard 10 PV
Valeur invalide
Attaque de Pythachu: (charge/tonnerre/eclair) tonnerre
Pythachu utilise Tonnerre : Pythard perd 50 PV
Valeur invalide
Attaque de Pythard: (charge/jet-de-flotte) charge
Pythachu utilise Charge : Pythard perd 20 PV
Pythachu -60 PV
Pythard 10 PV
Valeur invalide
Attaque de Pythachu: (charge/tonnerre/eclair) eclair
Traceback (most recent call last):
  File "battle.py", line 55, in <module>
    attack = input_attack(player1)
  File "battle.py", line 37, in input_attack
    return attacks[name]
KeyError: 'eclair'
```
