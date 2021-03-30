### Solution

```python
name1 = input('Entrez le nom du 1er joueur : ').capitalize()
pv1 = int(input('Et son nombre de PV : '))

name2 = input('Entrez le nom du 2ème joueur : ').capitalize()
pv2 = int(input('Et son nombre de PV : '))

print()

msg = name1 + ' (' + str(pv1) + ' PV) affronte ' + name2 + ' (' + str(pv2) + ' PV)'
print('+' * (len(msg)+4))
print('+', msg, '+')
print('+' * (len(msg)+4))

print()

att1 = int(input(name1 + ', combien de PV infligez-vous à ' + name2 + ' ? '))

print()

pv2 -= att1
msg1 = name1 + ' attaque ' + name2 + ' qui perd ' + str(att1) + ' PV'
msg2 = name2 + ' a maintenant ' + str(pv2) + ' PV'
max_size = max(len(msg1), len(msg2))
msg1 += ' ' * (max_size - len(msg1))
msg2 += ' ' * (max_size - len(msg2))
print('+' * (max_size+4))
print('+', msg1, '+')
print('+', msg2, '+')
print('+' * (max_size+4))

print()

att2 = int(input(name2 + ', combien de PV infligez-vous à ' + name1 + ' ? '))

print()

pv1 -= att2
msg1 = name2 + ' attaque ' + name1 + ' qui perd ' + str(att2) + ' PV'
msg2 = name1 + ' a maintenant ' + str(pv1) + ' PV'
max_size = max(len(msg1), len(msg2))
msg1 += ' ' * (max_size - len(msg1))
msg2 += ' ' * (max_size - len(msg2))
print('+' * (max_size+4))
print('+', msg1, '+')
print('+', msg2, '+')
print('+' * (max_size+4))

print()

msg1 = 'Résulat du combat :'
msg2 = name1 + ' a ' + str(pv1) + ' PV'
msg3 = name2 + ' a ' + str(pv2) + ' PV'
max_size = max(len(msg1), len(msg2), len(msg3))
msg1 += ' ' * (max_size - len(msg1))
msg2 += ' ' * (max_size - len(msg2))
msg3 += ' ' * (max_size - len(msg3))
print('+' * (max_size+4))
print('+', msg1, '+')
print('+', msg2, '+')
print('+', msg3, '+')
print('+' * (max_size+4))
```

Il serait possible de réaliser plusieurs tours de jeu en dupliquant la partie de code dédiée, mais ce n'est pas une bonne pratique.
Nous verrons par la suite comment faire cela proprement.
