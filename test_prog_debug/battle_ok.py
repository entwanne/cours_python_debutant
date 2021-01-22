import json


def input_choice(prompt, choices):
    value = None
    prompt += '(' + '/'.join(choices) + ') '
    while value not in choices:
        if value is not None:
            print('Valeur invalide')
        value = input(prompt)
    return value


def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Nombre invalide')


with open('data_ok.json') as f:
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


player1 = input_player()
player2 = input_player()
print(player1['monster']['name'], 'vs', player2['monster']['name'])

while player1['pv'] > 0 and player2['pv'] > 0:
    print(player1['monster']['name'], player1['pv'], 'PV')
    print(player2['monster']['name'], player2['pv'], 'PV')

    attack1 = input_attack(player1)
    print(player1['monster']['name'], 'utilise', attack1['name'], ':', player2['monster']['name'], 'perd', attack1['damage'], 'PV')
    player2['pv'] -= attack1['damage']

    if player2['pv'] > 0:
        attack2 = input_attack(player2)
        print(player2['monster']['name'], 'utilise', attack2['name'], ':', player1['monster']['name'], 'perd', attack2['damage'], 'PV')
        player1['pv'] -= attack2['damage']

if player1['pv'] > 0:
    print(player1['monster']['name'], 'gagne')
else:
    print(player2['monster']['name'], 'gagne')
