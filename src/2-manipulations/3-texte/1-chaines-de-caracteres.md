### Chaînes de caractères

Nous n'avons jusqu'ici manipulé que des nombres, mais ce ne sont pas les seuls types de données utilisables en Python, bien heureusement.
Bien que la mémoire de l'ordinateur ne sache traiter que des nombres, les langages de programmation offrent des abstractions pour représenter d'autres données.

Ainsi Python sait associer chaque lettre ou chaque caractère à un nombre grâce aux tables d'encodage.
Et le texte, ce n'est au final qu'une suite de lettres, une séquence de caractères.
On parle alors d'une chaîne de caractères.

On définit une chaîne de caractères à l'aide d'une paire de guillemets (_double-quotes_), entre lesquels on place le texte voulu.

```pycon
>>> "Salut les gens !"
'Salut les gens !'
```

On voit Python nous répondre par cette même chaîne délimitée par des apostrophes (_quotes_).
Il s'agit juste de deux syntaxes équivalentes pour représenter la même chose : une chaîne peut être délimitée par des apostrophes ou des guillemets, cela revient au même.

```pycon
>>> 'toto'
'toto'
>>> "toto"
'toto'
```

Les chaînes de caractères sont un type de valeur et donc des expressions, qu'il est possible d'assigner à des variables.

```pycon
>>> text = 'toto'
```

Si l'on appelle `print` sur une chaîne de caractères, son contenu est simplement affiché sur le terminal, sans les délimiteurs.

```pycon
>>> print(text)
toto
>>> print('Salut les gens !')
Salut les gens !
```

L'avantage des deux syntaxes pour délimiter les chaînes, c'est qu'il est possible d'entourer la chaîne d'apostrophes pour lui faire contenir des guillemets, et inversement.

```pycon
>>> 'Il a dit "salut"'
'Il a dit "salut"'
>>> "Oui il l'a dit"
"Oui il l'a dit"
```

Autrement, on aurait le droit à de belles erreurs car Python penserait en rencontrant le premier guillemet que l'on termine la chaîne, et il ne comprendrait donc pas les caractères qui suivraient.

```pycon
>>> "Il a dit "salut""
  File "<stdin>", line 1
    "Il a dit "salut""
                   ^
SyntaxError: invalid syntax
```

Mais comment alors représenter une chaîne de caractères possédant à la fois des apostrophes et des guillemets (telle que `J'ai dit "salut"`) ?
La solution se situe au niveau de l'échappement.
Il suffit de faire précéder un caractère d'un _backslash_ (ou _antislash_, `\`) pour qu'il ne soit pas interprété par Python comme un caractère de délimitation.

```pycon
>>> 'J\'ai dit "salut"'
'J\'ai dit "salut"'
```

Ces échappements, comme les délimiteurs, disparaissent lorsque le texte est affiché à l'aide d'un `print`.

```pycon
>>> print('J\'ai dit "salut"')
J'ai dit "salut"
```

D'autres séquences d'échappement sont disponibles, comme `\t` pour représenter une tabulation (alinéa) ou `\n` pour un saut de ligne (_n_ comme _newline_, soit _nouvelle ligne_).
Il n'est en effet pas possible de revenir à la ligne dans une chaîne de caractères, et le `\n` est donc nécessaire pour insérer un saut de ligne.

```pycon
>>> print('Elle a dit :\t"Salut"')
Elle a dit :	"Salut"
>>> print('Première ligne\nDeuxième ligne')
Première ligne
Deuxième ligne
```

[[a]]
| Certains systèmes d'exploitation comme Windows pourraient ne pas bien interpréter le `\n` comme un saut de ligne et demander à ce qu'il soit précédé du caractère « retour-chariot » (`\r`) pour fonctionner.
|
| ```pycon
| >>> print('Une\r\nDeux')
| Une
| Deux
| ```
|
| C'est un héritage de l'époque des machines à écrire où il fallait à la fois passer à la ligne suivante (nouvelle ligne) et revenir en début de ligne (retour chariot).

Et enfin, le _backslash_ étant lui-même un caractère spécial, il est nécessaire de l'échapper (donc le doubler) si on veut l'insérer dans une chaîne.
Comme par exemple pour un chemin de fichier sous Windows :

```pycon
>>> print('C:\\Python\\projet\\example.py')
C:\Python\projet\example.py
```

Afin de moins avoir recours aux séquences d'échappement, il est aussi possible d'utiliser des _triple-quotes_ pour définir une chaîne de caractères.
Il s'agit de délimiter notre chaîne par trois apostrophes (ou trois guillemets) de chaque côté, lui permettant alors d'utiliser librement apostrophes et guillemets à l'intérieur, mais aussi des retours à la ligne.

```pycon
>>> print('''J'ai dit "salut"''')
J'ai dit "salut"
>>> print("""Une chaîne sur
... plusieurs lignes
... avec des ' et des " dedans""")
Une chaîne sur
plusieurs lignes
avec des ' et des " dedans
```

[[i]]
| On voit des `...` apparaître à la place des `>>>` dans l'interpréteur interactif.  
| Cela signifie que l'interpréteur ne peut pas exécuter telle quelle la ligne de code entrée et qu'il attend pour cela les lignes suivantes, qui complèteront le code.
