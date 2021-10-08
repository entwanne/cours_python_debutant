### f-strings

Les _f-strings_ ou chaînes de formatage sont une nouveauté apportée par Python 3.6 qui simplifie la création de chaînes de caractères dynamiques (se construisant à partir d'autres valeurs).
Elles se caractérisent par un préfixe `f` placé avant les guillemets délimitant la chaîne.

```python
>>> f'abc'
'abc'
```

Il ne s'agit pas d'un type particulier, on le voit car notre expression a juste renvoyé la chaîne `'abc'`.
Le préfixe signale simplement qu'il peut y avoir des choses à interpréter à l'intérieur de notre chaîne.

Et ces choses, elles sont similaires à ce que l'on faisait avec `str.format`.
Dans les chaînes de formatage, on va pouvoir trouver des séquences entre accolades pour signaler où l'on souhaite insérer des valeurs.

Ainsi, `'{} + {} = {}'.format(3, 5, 3 + 5)` deviendra `f'{3} + {5} = {3 + 5}'`. Plus court et plus clair.

Ici il n'est donc pas question de préciser des positions entre les accolades, mais des expressions.
Il est ainsi possible de capturer des variables pour les utiliser dans la chaîne.

```python
>>> a = 3
>>> b = 5
>>> f'{a} + {b} = {a+b}'
'3 + 5 = 8'
```

Bien sûr, tous les types de données y sont utilisables.

```python
>>> name = 'Max'
>>> f'Salut {name} !'
'Salut Max !'
```

Et tous types d'expressions sont valides à l'intérieur de ces accolades.
Il faut juste faire attention à ne pas s'emmêler les pinceaux avec les guillemets : on ne peut pas placer d'apostrophe dans une chaîne délimitée par des apostrophes par exemple.

```python
>>> fruits = {'a': 'abricot', 'b': 'banane'}
>>> f"{fruits['b']}, {len(fruits)}"
'banane, 2'
```

Entre accolades, on peut aussi placer un `:` et y ajouter toutes les options de formatage disponibles avec `str.format`.

```python
>>> f'{a} + {b} = {a+b:+}'
'3 + 5 = +8'
>>> f'Salut {name:10} !'
'Salut Max        !'
```
