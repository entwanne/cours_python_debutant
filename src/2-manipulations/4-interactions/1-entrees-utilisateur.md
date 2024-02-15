### Entrées utilisateur

Nous avons déjà vu la commande `print('message')` qui permet d'écrire un message sur le terminal.
Il s'agit en fait d'une fonction prenant un nombre variable d'arguments et les affichant successivement dans la fenêtre de l'interpréteur.
Les arguments passés peuvent être de n'importe quel type.

```pycon
>>> print(10, 'text', 4.2)
10 text 4.2
```

Par défaut, les valeurs sont séparées par une espace.
Il est toutefois possible de choisir un autre séparateur en ajoutant un argument `sep='xxx'` après tous les autres.

```pycon
>>> print(10, 'text', 4.2, sep=' - ')
10 - text - 4.2
```

Contrairement aux autres arguments, il est ici nécessaire de préciser un nom (`sep`) pour que Python fasse la différence avec les autres valeurs : il ne doit pas considérer `' - '` comme une valeur à afficher en plus des autres, mais comme le séparateur entre ces valeurs.
On parle alors d'argument nommé.

Sachez aussi que l'on peut appeler la fonction `print` sans lui passer aucun argument.
À quoi cela peut bien servir ? Juste à afficher une ligne vide.
Cela revient à appeler `print` avec une chaîne vide.

```pycon
>>> print()

>>> print('')

```

À l'inverse de `print`, il existe aussi une fonction `input` pour lire une chaîne de caractères depuis le terminal, selon ce qui est entré par l'utilisateur.

```pycon
>>> input()
coucou
'coucou'
```

Après avoir entré la commande `input()`, on est invité à écrire une ligne de texte en terminant par un retour à la ligne (||Entrée||).
Cette ligne est ensuite renvoyée, sous forme d'une chaîne de caractères, par la fonction `input`.

[[i]]
| Le texte qui s'affiche sous la ligne `>>> input()` dans l'exemple au-dessus est donc le texte entré dans le terminal par l'utilisateur.
| Je vous invite alors à essayer ces exemples chez vous pour bien voir comment ils se comportent.
| Vous pouvez y entrer ce que bon vous semble.

`input` prend aussi un argument optionnel permettant d'afficher un message juste avant de demander la saisie, comme dans l'exemple suivant.

```pycon
>>> name = input('Quel est ton nom ? ')
Quel est ton nom ? entwanne
>>> print("Tu t'appelles", name)
Tu t'appelles entwanne
```

On comprend ainsi tout l'intérêt des variables.
Jusqu'ici, nous ne manipulions que des données connues du programme et les variables pouvaient sembler futiles.
Mais elles vont maintenant nous servir à stocker et traiter des données venant de l'extérieur, inconnues au lancement du programme.
