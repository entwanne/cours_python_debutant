### Clés de dictionnaires

Jusqu'ici, je n'ai présenté que des chaînes de caractères comme clés de dictionnaire, par souci de simplicité.

Mais ce ne sont pas les seuls types de clés possibles, les booléens ou les nombres sont aussi des clés valides.

```python
choices = {
    True: 'OK',
    False: 'KO',
}

diviseurs = {
    4: [1, 2],
    6: [1, 2, 3],
    8: [1, 2, 4],
    9: [1, 3],
    10: [1, 2, 5],
}
```

Qui s'utilisent de la même manière lors de l'indexation.

```pycon
>>> choices[True]
'OK'
>>> choices[False] = 'erreur'
>>> diviseurs[8]
[1, 2, 4]
>>> diviseurs.get(5, [1])
[1]
```

[[i]]
| Dans le cas de la construction d'un dictionnaire à l'aide d'un appel du type `dict(a=0, b=1)`, les clés seront forcément des chaînes de caractères et doivent correspondre à des noms valides.  
| Il n'est alors pas possible d'écrire quelque chose comme `dict(9=[1, 3])` puisque 9 n'est pas un nom d'argument valide.

--------------------

En revanche, tout type de données n'est pas accepté comme clé de dictionnaire.
Vous avez vu vous en rendre compte si vous avez essayé d'y placer une liste ou un dictionnaire.

```pycon
>>> {[]: 0}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

Nous reviendrons plus tard sur cette erreur et ce qu'elle signifie, mais retenez pour le moment que dans les types que nous connaissons seuls les non-modifiables peuvent être utilisés en tant que clés.

Les valeurs modifiables telles que les listes ou les dictionnaires ne peuvent pas être utilisées en tant que clés, car comment retrouverait-on la valeur associée si la clé est mise à jour ?
