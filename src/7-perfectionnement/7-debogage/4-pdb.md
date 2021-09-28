### Utilisation d'un débogueur (Pdb)

Vous avez peut-être remarqué un autre bug dans notre programme : le jeu ne s'arrête pas quand le premier joueur est censé être KO.

```shell
% python battle.py
Monstre: (pythachu/pythard/ponytha) pythachu
PV du monstre: 100
Monstre: (pythachu/pythard/ponytha) ponytha
PV du monstre: 120
Pythachu vs Ponytha
Pythachu 100 PV
Ponytha 120 PV
Attaque de Pythachu: (charge/tonnerre) charge
Pythachu utilise Charge : Ponytha perd 20 PV
Attaque de Ponytha: (charge/jet-de-flamme) jet-de-flamme
Ponytha utilise Jet de flamme : Pythachu perd 60 PV
Pythachu 40 PV
Ponytha 100 PV
Attaque de Pythachu: (charge/tonnerre) charge
Pythachu utilise Charge : Ponytha perd 20 PV
Attaque de Ponytha: (charge/jet-de-flamme) jet-de-flamme
Ponytha utilise Jet de flamme : Pythachu perd 60 PV
Pythachu -20 PV
Ponytha 80 PV
Attaque de Pythachu: (charge/tonnerre) charge
Pythachu utilise Charge : Ponytha perd 20 PV
Attaque de Ponytha: (charge/jet-de-flamme) jet-de-flamme
Ponytha utilise Jet de flamme : Pythachu perd 60 PV
Pythachu -80 PV
Ponytha 60 PV
[...]
```

Pour déceler son origine, nous allons cette fois-ci faire appel à un débogueur, j'ai nommé Pdb (pour _Python Debugger_).

#### Lancer un programme pas-à-pas avec Pdb

Pour commencer, on va lancer l'exécution de notre programme pas-à-pas à l'aide de Pdb, en l'exécutant via `python -m pdb battle.py`.

```shell
% python -m pdb battle.py
> /.../battle.py(1)<module>()
-> import json
(Pdb) 
```

Pdb nous indique quel fichier est exécuté (`battle.py`) et quelle ligne (`import json`).
Puis on se retrouve face à un prompt qui attend nos ordres pour continuer l'exécution.
Ce prompt comprend plusieurs commandes que nous allons voir ici.

Premièrement nous pouvons lui demander un peu de contexte.
Cela se fait avec la commande `list` (ou simplement `l`) qui va afficher les lignes autour de nous.

```python
(Pdb) l
  1  ->	import json
  2  	
  3  	
  4  	def input_choice(prompt, choices):
  5  	    value = None
  6  	    prompt += '(' + '/'.join(choices) + ') '
  7  	    while value not in choices:
  8  	        if value is not None:
  9  	            print('Valeur invalide')
 10  	        value = input(prompt)
 11  	    return value
```

On peut continuer l'exécution jusqu'à l'instruction suivante à l'aide de la commande `next` (ou `n`).

```python
(Pdb) n
> /.../battle.py(4)<module>()
-> def input_choice(prompt, choices):
(Pdb) n
> /.../battle.py(14)<module>()
-> def input_int(prompt):
(Pdb) n
> /../battle.py(22)<module>()
-> with open('data.json') as f:
```

Mais on se rend vite compte que c'est un peu long à avancer. On pourrait plutôt se rendre directement là où ça nous intéresse : au début de la boucle de jeu.  
Pour cela il existe la commande `until` (ou `unt`) qui prend en argument un numéro de ligne, le programme continuera alors son exécution jusqu'à cette ligne.

Mais comment connaître le numéro de ligne que l'on souhaite atteindre ?
Si vous avez le fichier ouvert en parallèle, vous pouvez voir que le `while` se trouve ligne 52.
Sinon, un appel à la commande `longlist` (ou `ll`) permet d'afficher toutes les lignes du fichier.

```python
(Pdb) ll
[...]
 47  	if __name__ == '__main__':
 48  	    player1 = input_player()
 49  	    player2 = input_player()
 50  	    print(player1['monster']['name'], 'vs', player2['monster']['name'])
 51  	
 52  	    while player1['pv'] and player2['pv'] > 0:
 53  	        print(player1['monster']['name'], player1['pv'], 'PV')
 54  	        print(player2['monster']['name'], player2['pv'], 'PV')
[...]
```

On va maintenant pouvoir entrer la commande `until 52` pour avancer jusqu'à notre boucle.
Là notre programme reprend son exécution normale sur les lignes intermédiaires, et nous demande alors d'entrer les informations sur les joueurs.

```python
(Pdb) until 52
Monstre: (pythachu/pythard/ponytha) pythachu
PV du monstre: 100
Monstre: (pythachu/pythard/ponytha) ponytha
PV du monstre: 120
Pythachu vs Ponytha
> /.../battle.py(52)<module>()
-> while player1['pv'] and player2['pv'] > 0:
(Pdb)
```

Nous entrons maintenant dans la boucle et nous pouvons reprendre l'exécution pas-à-pas à l'aide de `next`.

[[i]]
| Petite astuce : il est possible d'utiliser les flèches haut/bas de votre clavier pour naviguer dans l'historique des commandes entrées à Pdb.

```python
> /.../battle.py(52)<module>()
-> while player1['pv'] and player2['pv'] > 0:
(Pdb) next
> /.../battle.py(53)<module>()
-> print(player1['monster']['name'], player1['pv'], 'PV')
(Pdb) next
Pythachu 100 PV
> /.../battle.py(54)<module>()
-> print(player2['monster']['name'], player2['pv'], 'PV')
(Pdb) next
Ponytha 120 PV
> /.../battle.py(56)<module>()
-> attack = input_attack(player1)
(Pdb) next
Attaque de Pythachu: (charge/tonnerre) charge
> /.../battle.py(57)<module>()
-> apply_attack(player1, player2, attack)
(Pdb) next
Pythachu utilise Charge : Ponytha perd 20 PV
> /.../battle.py(59)<module>()
-> if player2['pv'] > 0:
(Pdb) next
> /.../battle.py(60)<module>()
-> attack = input_attack(player2)
(Pdb) next
Attaque de Ponytha: (charge/jet-de-flamme) jet-de-flamme
> /.../battle.py(61)<module>()
-> apply_attack(player2, player1, attack)
(Pdb) next
Ponytha utilise Jet de flamme : Pythachu perd 60 PV
> /.../battle.py(52)<module>()
-> while player1['pv'] and player2['pv'] > 0:
(Pdb)
```

On a fait un tour de boucle et on ne voit rien d'anormal pour le moment.
On peut afficher à l'aide de la commande `pp` (_pretty-print_) les valeurs de certaines variables pour vérifier que tout va bien.

```python
(Pdb) pp player1
{'monster': {'attacks': ['charge', 'tonnerre'], 'name': 'Pythachu'}, 'pv': 40}
(Pdb) pp player2
{'monster': {'attacks': ['charge', 'jet-de-flamme'], 'name': 'Ponytha'},
 'pv': 100}
```

On pourrait alors recommencer les mêmes opérations pour effectuer un tour de boucle supplémentaire, mais comme nous l'avons vu c'est un peu long.  
Nous allons donc utiliser une autre fonctionnalité offerte par Pdb : les points d'arrêts (ou _breakpoints_).
Il s'agit de points dans le programme qui provoqueront sa mise en pause chaque fois qu'ils seront atteints.

C'est notre boucle qui nous intéresse, et nous posons donc un point d'arrêt sur la ligne 52 à l'aide de la commande `break 52`.

```python
(Pdb) break 52
Breakpoint 1 at /.../battle.py:52
```

Pdb nous informe bien qu'un _breakpoint_ a été posé.
La commande `break` utilisée sans argument nous permet de lister tous les _breakpoints_.

```python
(Pdb) break
Num Type         Disp Enb   Where
1   breakpoint   keep yes   at /.../battle.py:52
```

Nous pouvons maintenant demander à Pdb de continuer normalement l'exécution du programme à l'aide de la commande `continue` (abrégée en `cont` ou `c`).
Le programme reprendra alors son cours normal jusqu'à la prochaine interruption (notre point d'arrêt).

```python
(Pdb) c
Pythachu 40 PV
Ponytha 100 PV
Attaque de Pythachu: (charge/tonnerre) charge
Pythachu utilise Charge : Ponytha perd 20 PV
Attaque de Ponytha: (charge/jet-de-flamme) jet-de-flamme
Ponytha utilise Jet de flamme : Pythachu perd 60 PV
> /.../battle.py(52)<module>()
-> while player1['pv'] and player2['pv'] > 0:
(Pdb)
```

Nous sommes bien revenus à la condition de notre boucle, et cette fois Pythachu est censé être KO, donc nous devrions en sortir.
On va s'en assurer à l'aide d'un simple `next` : nous verrons tout de suite où nous emmène la prochaine instruction.

```python
(Pdb) next
> /.../battle.py(53)<module>()
-> print(player1['monster']['name'], player1['pv'], 'PV')
```

Et là c'est le drame.
La boucle ne s'est pas arrêtée comme ça aurait dû être le cas.
On peut jeter un œil à la valeur de `player1` pour essayer de comprendre.

```python
(Pdb) pp player1
{'monster': {'attacks': ['charge', 'tonnerre'], 'name': 'Pythachu'}, 'pv': -20}
```

Les PV sont négatifs, la condition de boucle aurait alors dû être fausse.
`pp` n'accepte pas seulement une variable en argument mais n'importe quelle expression.
On peut alors exécuter `pp` sur la condition de notre boucle pour voir ce qui cloche.

```python
(Pdb) pp player1['pv'] and player2['pv'] > 0
True
```

Malgré les points de vie du joueur 1 négatifs, cette condition est tout de même considérée comme vraie.
La source de notre bug se trouve donc ici.

Et effectivement, si nous analysons notre condition de plus près, nous pouvons voir qu'elle est équivalente à `(player1['pv']) and (player2['pv'] > 0)`.  
On ne teste donc jamais si les points de vie du premier joueur sont positifs, mais seulement s'ils ne sont pas nuls.

Il ne nous reste plus qu'à corriger notre programme dans l'éditeur de texte pour utiliser la condition `player1['pv'] > 0 and player2['pv'] > 0` et à recommencer le débogage une fois notre fichier enregistré à l'aide de la commande `restart`.

Le programme repart alors de zéro depuis la première ligne, on peut entrer la commande `continue` pour continuer l'exécution jusqu'au point d'arrêt.  
On refait deux tours d'attaque comme précédemment pour revenir sur la condition de notre boucle qui doit maintenant être fausse.

```python
Ponytha utilise Jet de flamme : Pythachu perd 60 PV
> /.../battle.py(52)<module>()
-> while player1['pv'] > 0 and player2['pv'] > 0:
(Pdb) pp player1
{'monster': {'attacks': ['charge', 'tonnerre'], 'name': 'Pythachu'}, 'pv': -20}
(Pdb) pp player1['pv'] > 0 and player2['pv'] > 0
False
```

On peut alors exécuter `next` et vérifier que l'on sort bien de la boucle.

```python
(Pdb) next
> /.../battle.py(63)<module>()
-> if player1['pv'] > 0:
```

Le bug en question est donc corrigé !

#### Invoquer Pdb depuis le programme

Mais ce mode d'utilisation de Pdb n'est pas le plus intuitif.
Généralement on a déjà constaté le bug en dehors du débogueur et on sait donc à peu près à quel endroit il va se produire.
On pourrait alors directement poser notre point d'arrêt dans le programme pour invoquer Pdb.

Cela est rendu possible à l'aide de la fonction `breakpoint` de Python, appelable depuis n'importe où dans le programme.
On lancera alors notre jeu normalement, et la fonction aura pour effet de le mettre en pause et de nous amener sur une console Pdb.

[[i]]
| Avant Python 3.7, la fonction `breakpoint` n'existait pas.
| Il fallait alors écrire `import pdb; pdb.set_trace()` dans le code pour placer un point d'arrêt.

Vous avez peut-être pu constater un autre bug dans le jeu en utilisant le monstre Pythard, celui-ci se produit quand on essaie d'utiliser l'attaque _jet-de-flotte_.

```shell
% python battle.py
Monstre: (pythachu/pythard/ponytha) pythard
PV du monstre: 100
Monstre: (pythachu/pythard/ponytha) pythachu
PV du monstre: 100
Pythard vs Pythachu
Pythard 100 PV
Pythachu 100 PV
Attaque de Pythard: (charge/jet-de-flotte) jet-de-flotte
Traceback (most recent call last):
  File "/.../battle.py", line 57, in <module>
    apply_attack(player1, player2, attack)
  File "/.../battle.py", line 43, in apply_attack
    target['monster']['name'], 'perd', attack['damage'], 'PV')
KeyError: 'damage'
```

On constate donc que le bug survient dans la fonction `apply_attack` et l'on va pouvoir placer un point d'arrêt directement dans cette fonction.

```python linenostart=41
def apply_attack(attacker, target, attack):
    breakpoint()
    print(attacker['monster']['name'], 'utilise', attack['name'], ':',
          target['monster']['name'], 'perd', attack['damage'], 'PV')
    target['pv'] -= attack['damage']
```

Il nous suffit ensuite de relancer normalement notre programme.
Et après avoir saisi les informations de jeu, on se retrouve interrompu par notre _breakpoint_.

```shell
% python battle.py
Monstre: (pythachu/pythard/ponytha) pythard
PV du monstre: 100
Monstre: (pythachu/pythard/ponytha) pythachu
PV du monstre: 100
Pythard vs Pythachu
Pythard 100 PV
Pythachu 100 PV
Attaque de Pythard: (charge/jet-de-flotte) jet-de-flotte
> /.../battle.py(43)apply_attack()
-> print(attacker['monster']['name'], 'utilise', attack['name'], ':',
(Pdb)
```

Nous pouvons alors reprendre notre attirail de commandes et essayer de comprendre le problème en inspectant les différentes valeurs.

```python
(Pdb) pp attacker
{'monster': {'attacks': ['charge', 'jet-de-flotte'], 'name': 'Pythard'},
 'pv': 100}
(Pdb) pp attack
{'damages': 50, 'name': 'Jet de flotte'}
(Pdb) pp target
{'monster': {'attacks': ['charge', 'tonnerre'], 'name': 'Pythachu'}, 'pv': 100}
```

Rien qui ne saute forcément aux yeux pour l'instant, donc on continue l'exécution avec `next`.

```python
(Pdb) next
> /.../battle.py(44)apply_attack()
-> target['monster']['name'], 'perd', attack['damage'], 'PV')
(Pdb) next
KeyError: 'damage'
> /.../battle.py(44)apply_attack()
-> target['monster']['name'], 'perd', attack['damage'], 'PV')
```

Là on voit bien l'erreur `KeyError` qui se produit et la ligne fautive est pointée.
On se rend alors compte qu'on a utilisé dans notre JSON la clé `'damages'` plutôt que `'damage'` pour l'attaque _jet-de-flotte_. Encore une fois l'erreur venait donc de nos données.  
On peut directement quitter le programme pour aller corriger notre fichier `data.json`.

Par acquis de conscience, on le relance ensuite dans les mêmes conditions pour vérifier que tout se passe bien.

```python
Attaque de Pythard: (charge/jet-de-flotte) jet-de-flotte
> /.../battle.py(43)apply_attack()
-> print(attacker['monster']['name'], 'utilise', attack['name'], ':',
(Pdb) 
```

On est à nouveau interrompu par notre _breakpoint_ et on avance alors pas-à-pas pour nous assurer du bon fonctionnement.

```python
(Pdb) next
> /.../battle.py(44)apply_attack()
-> target['monster']['name'], 'perd', attack['damage'], 'PV')
(Pdb) next
> /.../battle.py(43)apply_attack()
-> print(attacker['monster']['name'], 'utilise', attack['name'], ':',
(Pdb) continue
Pythard utilise Jet de flotte : Pythachu perd 50 PV
Attaque de Pythachu: (charge/tonnerre)
```

Cette fois-ci c'est bon, le problème semble bien résolu. Mais le point d'arrêt reste toujours présent et continuera de nous interrompre.
Il nous suffira de retirer la ligne `breakpoint()` dans le programme pour le supprimer.

[[i]]
| La fonction `breakpoint` peut aussi directement s'utiliser depuis des fonctions de test, et ainsi être invoquée lors de l'exécution des tests.

Pour plus d'informations sur les commandes comprises par Pdb, je vous invite à consulte [sa page de documentation](https://docs.python.org/fr/3/library/pdb.html).
