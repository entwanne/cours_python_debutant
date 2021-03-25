### Déboguer pas à pas

Maintenant que nous sommes en mesure de nous dépatouiller pour inspecter les valeurs, il est temps de comprendre comment elles évoluent au cours du programme pour mener jusqu'au bug.

#### Suivre et comprendre les exceptions

Une manière courante de procéder au débogage, bien qu'elle ne soit pas des plus efficaces, est de placer des appels à `print` à plusieurs en droits du programme afn d'afficher des informations de debug.

Par exemple si l'on reprend le programme présenté en introduction, on remarque que le premier problème que l'on rencontre est que le programme affiche sans cesse « Valeur invalide » avant même que l'on ait entré quelque chose.  
Pour comprendre ce qui se passe, on peut donc ajouter un `print` pour afficher ce que l'on connaît, la valeur de `value` et celle de `choices`.

```python linenostart=4
def input_choice(prompt, choices):
    value = None
    prompt += '(' + '/'.join(choices) + ') '
    while value not in choices:
        print('debug', repr(value), repr(choices))
        print('Valeur invalide')
        value = input(prompt)
    return value
```
Code: battle.py

```shell
% python battle.py
debug None {'pythachu': {'name': 'Pythachu', 'attacks': ['charge', 'tonnerre', 'eclair']}, 'pythard': {'name': 'Pythard', 'attacks': ['charge', 'jet-de-flotte']}, 'ponytha': {'name': 'Ponytha', 'attacks': ['charge', 'jet-de-flamme']}}
Valeur invalide
Monstre: (pythachu/pythard/ponytha)
```

On peut déjà s'interroger sur le fait que `choices` soit un dictionnaire mais c'est normal : on lui passe directement l'objet `monsters` de notre JSON, et comme le `in` sur un dictionnaire fait une recherche sur les clés ça ne pose pas de problème.

Non le problème vient de ce `None`, la valeur initiale de notre variable, qui n'est effectivement pas dans les choix.
On peut donc conditionner l'affichage du message d'erreur au fait que `value` ne soit pas `None` pour résoudre le premier problème.

```python linenostart=7
    while value not in choices:
        if value is not None:
            print('Valeur invalide')
        value = input(prompt)
```
Code: battle.py

Une autre erreur que l'on remarque, c'est le plantage à la fin après avoir sélectionné l'attaque « éclair ».
C'est une erreur qui se produit systématiquement dans le cas où l'on choisit cette attaque, et qui n'arrive pas autrement.  
On peut donc facilement la reproduire pour l'analyser.

Là encore, on peut afficher quelques informations au moment où l'on manipule cette information pour comprendre ce qu'il se passe.  
La trace de l'erreur nous dit déjà que celle-ci se produit dans la fonction `input_attack`, c'est donc à cette fonction que nous allons nous intéresser en premier.

De la même manière que précdemment, on peut vérifier les différentes valeurs que l'on manipule pour s'assurer qu'elles correspondent à ce que l'on attend, notammant `player`, `monster`, `name` et `attacks`.

[[i]]
| Pour nous aider à afficher nos valeurs, on peut s'appuyer sur le module `pprint`.  
| Ce module fournit une fonction `pprint` (pour _pretty print_, soit _affichage joli_) qui donne un rendu plus aéré que `print`.

```python linenostart=35
def input_attack(player):
    from pprint import pprint
    print('player')
    pprint(player)
    monster = player['monster']
    print('monster')
    pprint(monster)
    name = input_choice(f"Attaque de {monster['name']}: ", monster['attacks'])
    print('name', repr(name))
    print('attacks')
    pprint(attacks)
    return attacks[name]
```
Code: battle.py

On obtient alors le résultat suivant en relançant le programme.

```
player
{'monster': {'attacks': ['charge', 'tonnerre', 'eclair'], 'name': 'Pythachu'},
 'pv': 10}
monster
{'attacks': ['charge', 'tonnerre', 'eclair'], 'name': 'Pythachu'}
Attaque de Pythachu: (charge/tonnerre/eclair) eclair
name 'eclair'
attacks
{'charge': {'damage': 20, 'name': 'Charge'},
 'jet-de-flamme': {'damage': 60, 'name': 'Jet de flamme'},
 'jet-de-flotte': {'damages': 50, 'name': 'Jet de flotte'},
 'tonnerre': {'damage': 50, 'name': 'Tonnerre'}}
Traceback (most recent call last):
  File "battle.py", line 61, in <module>
    attack1 = input_attack(player1)
  File "battle.py", line 50, in input_attack
    return attacks[name]
KeyError: 'eclair'
```

Et là on constate que l'attaque `eclair` proposée pour le monstre n'existe pas dans le dictionnaire des attaques car elle n'est pas encore implémentée : on a donc simplement renseigné une mauvaise valeur dans notre JSON.  
Il nous suffit de corriger ce dernier et supprimer `eclair` pour corriger l'erreur, on peut alors retirer tous les `print` de debug de notre programme.

```js linenostart=9
	"pythachu": {
	    "name": "Pythachu",
	    "attacks": ["charge", "tonnerre"]
	},
```
Code: data.json


#### S'appuyer sur des tests unitaires

Mais on le voit, utiliser `print` pour déboguer peut être assez fastidieux.
Heureusement un autre outil peut nous venir en aide : un ensemble de tests unitaires.

Je vous en parlais d'ailleurs [plus tôt](), les tests unitaires nous permettent de déceler des bugs dans nos fonctions en vérifiant que le retour correspond à ce qui est attendu.  
C'est pourquoi je ne peux que vous reconseiller de découper vos programmes en fonctions afin de plus facilement pouvoir les déboguer.
L'idéal serait aussi de disposer les fonctions en différents modules pour pouvoir tester unitairement chacun des modules.

Mais revenons-en à notre code. Il possède peu de fonctions que nous pouvons tester en l'état car beaucoup reposent sur des entrées utilisateurs que nous ne savons pas simuler[^mock].  
Il n'y a en fait que la fonction `apply_attack` qui est déterministe : elle doit toujours faire la même chose quand on lui renseigne les mêmes arguments.

[^mock]: Nous apprendrons à le faire par la suite à l'aide de _mocks_ intégré aux _frameworks_ de tests, mais ce n'est pas l'objet de ce chapitre.

Pour la tester, il faut alors que l'on donne à la fonction des données dans le format qu'elle attend (deux joueurs et une attaque) puis que l'on vérifie son retour.
Ici la fonction ne renvoie rien mais elle peut altérer ses paramètres, c'est donc sur ceux-ci que nous ferons nos assertions afin de vérifier que les points de vie sont bien mis à jour (en l'occurence que les dégâts sont retirés du second monstre).

Les paramètres n'ont pas besoin d'être exhaustifs mais simplement de contenir les informations qui seront utilisées par la fonction.
Ici les joueurs n'ont besoin de n'avoir par exemple qu'un nombre de points de vie et un nom de monstre, et l'attaque seulement un nom et un nombre de dégâts.

```python
from battle import apply_attack


def test_apply_attack():
    p1 = {
        'monster': {'name': 'Pythachu'},
        'pv': 50,
    }
    p2 = {
        'monster': {'name': 'Ponytha'},
        'pv': 100,
    }
    attack = {'name': 'électrocution', 'damage': 30}

    apply_attack(p1, p2, attack)
    assert p2['pv'] == 70


if __name__ == '__main__':
    test_apply_attack()
```
Code: test_battle.py

Et là… c'est le drame !

```shell
% python test_battle.py
Pythachu utilise électrocution : Ponytha perd 30 PV
Traceback (most recent call last):
  File "test_battle.py", line 20, in <module>
    test_apply_attack()
  File "test_battle.py", line 16, in test_apply_attack
    assert p2['pv'] == 70
AssertionError
```

Notre assertion échoue parce que les PV du second joueur ne valent pas 70 comme attendu.  
Sans plus d'outils à notre disposition pour le moment, on peut associer à nos tests un `print` comme précédemment avant d'obtenir plus d'informations.

```python linenostart=15
    apply_attack(p1, p2, attack)
    print('résultat', p2['pv'])
    assert p2['pv'] == 70
```
Code: test_battle.py

À l'exécution du test on comprend mieux le problème : les PV du deuxième jour n'ont pas bougé.

```shell
% python test_battle.py
résultat 100
Traceback (most recent call last):
  File "test_battle.py", line 21, in <module>
    test_apply_attack()
  File "test_battle.py", line 17, in test_apply_attack
    assert p2['pv'] == 70
AssertionError
```

On peut alors se demander où sont retirés les PV, et logiquement ajouter une assertion sur le premier joueur.

```python linenostart=15
    apply_attack(p1, p2, attack)
    print('résultat', p1['pv'], p2['pv'])
    assert p1['pv'] == 50
    assert p2['pv'] == 70
```
Code: test_battle.py

```shell
% python test_battle.py
Pythachu utilise électrocution : Ponytha perd 30 PV
résultat 20 100
Traceback (most recent call last):
  File "test_battle.py", line 22, in <module>
    test_apply_attack()
  File "test_battle.py", line 17, in test_apply_attack
    assert p1['pv'] == 50
AssertionError
```

Cette fois-ci c'est clair : les dégâts sont appliqués au premier joueur plutôt qu'au deuxième.
Et à regarder notre fonction `apply_attack`, c'est vrai que les noms des paramètres `player1` et `player2` prêtent à confusion.

Nous leur préférerons alors respectivement les noms plus descriptifs de `attacker` (attaquant) et `target` (cible).

```python linenostart=41
def apply_attack(attacker, target, attack):
    print(attacker['monster']['name'], 'utilise', attack['name'], ':',
          target['monster']['name'], 'perd', attack['damage'], 'PV')
    target['pv'] -= attack['damage']
```
Code: battle.py

On peut alors exécuter à nouveau nos tests et constater que tout se passe bien.

```shell
% python test_battle.py
Pythachu utilise électrocution : Ponytha perd 30 PV
résultat 50 70
```
