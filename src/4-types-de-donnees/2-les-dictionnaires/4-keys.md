### Clés de dictionnaires

* Les clés de dictionnaires ne se limitent pas aux chaînes de caractères
* Il y a par contre des restrictions, les listes ou dictionnaires ne peuvent pas être des clés (car modifiables, donc impossible de retrouver la valeur)

Jusqu'ici, je n'ai présenté que des chaînes de caractères comme clés de dictionnaire, par soucis de simplicité.

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

```python
>>> choices[True]
'OK'
>>> choices[False] = 'erreur'
>>> diviseurs[8]
[1, 2, 4]
>>> diviseurs.get(5, [1])
[1]
```

En revanche, tout type de données n'est pas accepté comme clé de dictionnaire.
Vous avez vu vous en rendre compte si vous avez essayé d'y placer une liste ou un dictionnaire.

```python
>>> {[]: 0}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

Nous reviendrons plus tard sur cette erreur et ce qu'elle signifie, mais retenez pour le moment que dans les types que nous connaissons seuls les non-modifiables peuvent être utilisés en tant que clés.
