### Opérations de formatage

#### Méthode `format`

La méthode `write` des fichiers textes ne comprend que les chaînes de caractères.
Nous avons vu qu'il était possible avec `print` d'écrire d'autres types de données, mais les options de formatage sont relativement limitées.

Par exemple il ne nous est pas possible de choisir combien de chiffres après la virgule on veut afficher pour les décimaux (souvenez-vous des erreurs d'arrondis qui donnent parfois des résultats inattendus) ni gérer facilement les espacements.

Tout cela relève du formatage, et il existe une méthode dédiée : la méthode `format` des chaînes de caractères.
C'est une méthode qui permet de générer une nouvelle chaîne à partir d'un patron (la chaîne d'origine) et d'arguments.

Pour cela, une syntaxe particulière est utilisée dans le chaîne faisant office de patron pour définir où seront insérés les arguments (on parle de _placeholders_).
Cette syntaxe, c'est `{}`.  
Lors d'un appel à `format` sur une chaîne de caractères, les `{}` seront repérés dans la chaîne et remplacés par les arguments.

```python
>>> '{}'.format(10)
'10'
>>> '{}'.format(1.5)
'1.5'
>>> '{}'.format('abc')
'abc'
```

Chaque `{}` correspond à la valeur suivante dans la liste des arguments.

```python
>>> '{}-{}'.format(10, 'abc')
'10-abc'
>>> '{} dit à {} : {}'.format('Alice', 'Bob', 'Salut')
'Alice dit à Bob : Salut'
```

Mais ces accolades ne sont pas destinées à rester éternellement vides, on peut y préciser différents types de choses.
Déjà, cela peut servir à spécifier l'argument que l'on souhaite utiliser : il peut arriver qu'on veuille afficher le deuxième argument avant le premeir par exemple.
On entre donc simplement le numéro de l'argument positionnel entre les accolades pour y faire référence (`0` étant le premier argument, `1` le deuxième, etc.).

```python
>>> '{0}-{1}'.format(10, 'abc')
'10-abc'
>>> '{1}-{0}'.format(10, 'abc')
'abc-10'
```

La méthode `format` ne se limite pas aux arguments positionnels mais accepte aussi les arguments nommés, ce qui permet de gagner en clarté.
Pour utiliser un argument nommé, il faudra nécessairement préciser son nom entre les accolades.

```python
>>> '{number}-{name}'.format(number=10, name='abc')
'10-abc'
>>> '{speaker} dit à {listener} : {sentence}'.format(listener='Alice', speaker='Bob', sentence='Salut')
'Bob dit à Alice : Salut'
```

Il est possible de mixer arguments positionnels et nommés, mais attention à ne pas perdre en lisibilité.

```python
>>> '{0}-{name}'.format(10, name='abc')
'10-abc'
```

* Accéder aux attributs (nombres complexes) / éléments (list / dict) de l'argument positionnel/nommé

Voilà pour le placement des arguments mais ce n'est pas tout : le principal intérêt de cette méthode `format` est de pouvoir… formater les valeurs, leur donner le format que l'on souhaite.

#### Options de formatage

* Mini-langage

```python
>>> '{:10}'.format('abc')
'abc       '
>>> '{:<10}'.format('abc')
'abc       '
>>> '{:>10}'.format('abc')
'       abc'
>>> '{:^10}'.format('abc')
'   abc    '
```

```python
>>> '{: }'.format(5)
' 5'
>>> '{: }'.format(-5)
'-5'
>>> '{:+}'.format(5)
'+5'
>>> '{:+}'.format(-5)
'-5'
```

```python
>>> '{:x}'.format(42)
'2a'
>>> '{:o}'.format(42)
'52'
>>> '{:b}'.format(42)
'101010'
>>> '{:#x}'.format(42)
'0x2a'
```

```python
>>> '{}'.format(0.1+0.2)
'0.30000000000000004'
>>> '{:.1}'.format(0.1+0.2)
'0.3'
>>> '{}'.format(1/3)
'0.3333333333333333'
>>> '{:.5}'.format(1/3)
'0.33333'
```

```python
>>> '{:%}'.format(1/2)
'50.000000%'
>>> '{:.0%}'.format(1/3)
'33%'
```

* Doubler les accodales pour les échapper

```python
>>> '{} {{}} {}'.format(1, 2)
'1 {} 2'
```

* flags de formatage reçus depuis les arguments
* d'autres objets pourront avoir leurs propres options de formatage

```python
help('FORMATTING')
```

* https://docs.python.org/fr/3/library/string.html#formatspec
* ± annexe
    * `!r`, `!a`

#### Operateur `%`

Une autre méthode plus ancienne existe aussi en Python, elle utilise l'opérateur `%`.

On applique donc cet opérateur à une chaîne (à gauche) en lui donnant un tuple d'arguments (à droite).
Comme précédemment, la chaîne suit un certain format pour définir où seront insérés les arguments.

Ici, le format est celui utilisé par la fonction `printf` en C, où l'on identifie les valeurs par leur type : `%s` pour une chaîne de caractère, `%d` pour un nombre entier ou encore `%f` pour un flottant.
Les arguments seront toujours pris successivement dans le tuple qui les fournit (comme les arguments positionnels avec `{}`).

En pratique, on a donc quelque chose de la sorte :

```python
>>> '%s dit à %s: tu me dois %d€' % ('Bob', 'Alice', 20)
'Bob dit à Alice: tu me dois 20€'
```

On trouve aussi la possibilité de préciser des options telle que la largeur ou la précision, en les insérant entre le `%` et le caractère représentant le type.

```python
>>> '%10s répond: il ne me reste que %.2f€' % ('Alice', 18.5)
'     Alice répond: il ne me reste que 18.50€'

```

Et il existe encore d'autres possibilités (types et options).
Mais cette syntaxe est de moins en moins utilisée en Python, c'est pourquoi je n'en parlerai pas plus longuement.
Vous trouverez cependant plus d'informations à son sujet [dans la documentation](https://docs.python.org/fr/3/library/stdtypes.html#printf-style-string-formatting).

Sachez que tout ce qu'il est possible de faire sur les chaînes de caractères avec `%` est aussi réalisable avec la méthode `format`.
Et nous allons maintenant voir une forme encore plus simple d'utilisation.
