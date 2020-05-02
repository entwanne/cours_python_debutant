### Solution

```python
name1 = input('Entrez le nom du 1er joueur : ').capitalize()
pv1 = int(input('Et son nombre de PV : '))

name2 = input('Entrez le nom du 2ème joueur : ').capitalize()
pv2 = int(input('Et son nombre de PV : '))

print()
print(name1, 'affronte', name2)
print()

menu = '''quelle attaque voulez-vous utiliser ?
1. Charge (-20 PV)
2. Tonnerre (-50 PV)'''

# Joueur 1

print(name1, menu)
att1 = input('> ')

if att1 == '1':
    damages = 20
elif att1 == '2':
    damages = 50
else:
    print('Erreur de saisie')
    damages = 0

pv2 -= damages
print(name1, 'attaque', name2, 'qui perd', damages, 'PV')

# Joueur 2

print(name2, menu)
att1 = input('> ')

if att1 == '1':
    damages = 20
elif att1 == '2':
    damages = 50
else:
    print('Erreur de saisie')
    damages = 0

pv1 -= damages
print(name2, 'attaque', name1, 'qui perd', damages, 'PV')

if pv1 == pv2:
    print('Match nul')
elif pv1 > pv2:
    print(name1, 'remporte le combat')
else:
    print(name2, 'remporte le combat')
```

On voit encore beaucoup de répétitions dans ce code, mais pas d'inquiétudes, nous corrigerons bientôt cela.
