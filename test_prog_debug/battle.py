import json


# bugs:
# erreurs dans data.json (damages à la place de damage, attaque inexistante)
# input_choice qui plante (value non définie) puis affiche un message d'erreur trop tôt (avant la première saisie)
# condition de boucle : a and b > 0 plutôt que a > 0 and b > 0
# déduction de pv depuis le mauvais player

def input_choice(prompt, choices):
    value=None
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


player1 = input_player()
player2 = input_player()
print(player1['monster']['name'], 'vs', player2['monster']['name'])

while player1['pv'] and player2['pv'] > 0:
    print(player1['monster']['name'], player1['pv'], 'PV')
    print(player2['monster']['name'], player2['pv'], 'PV')

    attack1 = input_attack(player1)
    print(player1['monster']['name'], 'utilise', attack1['name'], ':', player2['monster']['name'], 'perd', attack1['damage'], 'PV')
    player1['pv'] -= attack1['damage']

    if player2['pv'] > 0:
        attack2 = input_attack(player2)
        print(player2['monster']['name'], 'utilise', attack2['name'], ':', player1['monster']['name'], 'perd', attack2['damage'], 'PV')
        player1['pv'] -= attack2['damage']

if player1['pv'] > 0:
    print(player1['monster']['name'], 'gagne')
else:
    print(player2['monster']['name'], 'gagne')
