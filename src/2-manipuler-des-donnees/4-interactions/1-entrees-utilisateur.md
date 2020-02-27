### Entrées utilisateur

Nous avons déjà vu la commande `print('message')` qui permet d'écrire un message sur le terminal.
Il s'agit en fait d'une fonction prenant un nombre variable d'arguments et les affichant successivement.
Les arguments passés peuvent être de n'importe quel type.

```python
>>> print(10, 'text', 4.2)
10 text 4.2
```

Par défaut, les valeurs sont séparées par une espace.
Il est possible de choisir un autre séparateur en ajoutant un argument `sep='xxx'` après tous les autres.

```python
>>> print(10, 'text', 4.2, sep=' - ')
10 - text - 4.2
```

Contrairement aux autres arguments, il est ici nécessaire de préciser un nom (`sep`) pour que Python fasse la différence avec les valeurs à afficher. On parle alors d'argument nommé.

À l'inverse de `print`, il existe aussi une fonction `input` pour lire une chaîne de caractères depuis le terminal.

```python
>>> input()
coucou
'coucou'
```

Après avoir entré la commande `input()`, on est invité à écrire une ligne de texte.
Cette ligne est ensuite renvoyée, sous forme d'une chaîne de caractères, par la fonction `input`.

`input` prend aussi un argument optionnel permettant d'afficher un message juste avant de demander la saisie, comme dans l'exemple suivant.

```python
>>> name = input('Quel est ton nom ? ')
Quel est ton nom ? entwanne
>>> print("Tu t'appelles", name)
Tu t'appelles entwanne
```

On comprend ainsi tout l'intérêt des variables.
Jusqu'ici nous ne manipulions que des données connues du programme et les variables pouvaient sembler futiles.
Mais elles vont maintenant nous servir à stocker des données venant de l'extérieur, inconnues au lancement du programme.
