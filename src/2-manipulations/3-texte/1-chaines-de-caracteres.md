### Chaînes de caractères

Nous n'avons jusqu'ici manipulé que des nombres, mais ce ne sont pas les seuls types de données utilisables en Python, bien heureusement.
Bien que la mémoire de l'ordinateur ne sache traiter que des nombres, les langages de programmation offrent des abstractions pour représenter d'autres données.

C'est le cas par exemple des chaînes de caractères, qui sont en fait des tableaux de caractères et permettent de représenter du texte.

On définit une chaîne de caractères à l'aide d'une paire de guillemets, et en plaçant le texte voulu entre.

```python
>>> "Salut les gens !"
'Salut les gens !'
```

On voit Python nous répondre par cette même chaîne délimitée par des apostrophes (_quotes_).
Il s'agit juste de deux syntaxes équivalentes pour représenter une même chaîne.

```python
>>> 'toto'
'toto'
>>> "toto"
'toto'
```

Si l'on appelle `print` sur une chaîne de caractères, son contenu est simplement affiché sur le terminal, sans les délimiteurs.

```python
>>> print('Salut les gens !')
Salut les gens !
```

L'avantage des deux syntaxes, c'est qu'il est possible d'entourer la chaîne d'apostrophe pour lui faire contenir des guillemets, et inversement.

```python
>>> 'Il a dit "salut"'
'Il a dit "salut"'
>>> "Oui il l'a dit"
"Oui il l'a dit"
```

Autrement, on aurait le droit à de belles erreurs car Python penserait en rencontrant le premier guillemet que l'on termine la chaîne, et il ne comprendrait alors pas les caractères qui suivraient.

```python
>>> "Il a dit "salut""
  File "<stdin>", line 1
    "Il a dit "salut""
                   ^
SyntaxError: invalid syntax
```

Mais comment alors représenter une chaîne de caractères possédant à la fois des apostrophes et des guillemets (telle que `J'ai dit "salut"`) ?
La solution se situe au niveau de l'échappement.
Il suffit de faire précéder un caractère d'un _backslash_ (`\\`) pour qu'il ne soit pas interprété par Python comme un caractère spécial.

```python
>>> 'J\'ai dit "salut"'
'J\'ai dit "salut"'
```

Ces échappements, comme les délimiteurs, disparaissent lorsque le texte est affiché à l'aide d'un `print`.

```python
>>> print('J\'ai dit "salut"')
J'ai dit "salut"
```

D'autres séquences d'échappement sont disponibles, comme `\n` pour représenter un saut de ligne.

```python
>>> print('Première ligne\nDeuxième ligne')
Première ligne
Deuxième ligne
```

Et enfin, le _backslash_ étant lui-même un caractère spécial, il est nécessaire de l'échapper (donc le doubler) si on veut l'insérer dans une chaîne.
Comme par exemple pour un chemin de fichier sous Windows :

```python
>>> print('C:\\Python\\projet\\example.py')
C:\Python\projet\example.py
```

* + triple quotes
