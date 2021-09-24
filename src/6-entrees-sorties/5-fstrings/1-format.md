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
Déjà, cela peut servir à spécifier l'argument que l'on souhaite utiliser : il peut arriver qu'on veuille afficher le deuxième argument avant le premier par exemple.
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

On peut aussi accéder directement aux attributs ou éléments de l'argument positionnel ou nommé, en utilisant le point pour les attributs et les crochets pour les éléments.

```python
>>> '{0.real}-{items[1]}'.format(1+2j, items=['a', 'b', 'c'])
'1.0-b'
```

Voilà pour le placement des arguments mais ce n'est pas tout : le principal intérêt de cette méthode `format` est de pouvoir… formater les valeurs, leur donner le format que l'on souhaite.

#### Options de formatage

Il existe pour cela un mini-langage dédié aux options de formatage.
Ces options se placeront toujours derrière un signe `:` entre les accolades.

Par exemple, il est possible en utilisant un nombre comme option d'aligner le texte sur un certain nombre de caractères.
On l'appelle la largeur de champ.

```python
>>> '{:10}'.format('abc')
'abc       '
```

Par défaut le texte sera aligné à gauche (espaces ajoutées à droite).
Il est possible d'être explicite là-dessus en faisant précéder le nombre d'un `<`.  
Mais on peut aussi utiliser `>` ou `^` pour l'aligner à droite ou le centrer.

```python
>>> '{:<10}'.format('abc')
'abc       '
>>> '{:>10}'.format('abc')
'       abc'
>>> '{:^10}'.format('abc')
'   abc    '
```

Pour le formatage des nombres, on peut préciser l'option ` ` (espace) qui a pour effet d'ajouter une espace avant les nombres positifs, de façon à les aligner avec les négatifs (qui commencent par un caractère `-`).  
De même on peut utiliser l'option `+` pour afficher explicitement le `+` des nombres positifs.

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

Pour les nombres entiers, on peut utiliser les caractères `x`, `o` ou `b` comme options pour choisir la base dans laquelle le nombre sera écrit.
Avec `x`, le nombre sera écrit en hexadécimal, en octal avec `o` et en binaire avec `b`.

```python
>>> '{:x}'.format(42)
'2a'
>>> '{:o}'.format(42)
'52'
>>> '{:b}'.format(42)
'101010'
```

On peut ajouter un `#` avant ce caractère pour insérer un préfixe indiquant la base utilisée.

```python
>>> '{:#x}'.format(42)
'0x2a'
>>> '{:#b}'.format(42)
'0b101010'
```

La largeur de champ est aussi utilisable pour les nombres, ils seront par défaut alignés à droite.
On peut préfixer cette largeur de champ d'un `0` pour compléter le nombre avec des zéros plutôt qu'avec des espaces.

```python
>>> '{:5}'.format(123)
'  123'
>>> '{:05}'.format(123)
'00123'
```

Pour ce qui est des nombres flottants, on peut utiliser l'option `.` suivie d'un nombre pour indiquer la précision.
Ce nombre correspond au nombre maximum de chiffres que l'on veut afficher, cela compte les chiffres avant et après la virgule (sauf les zéros initiaux)

```python
>>> '{}'.format(0.1+0.2)
'0.30000000000000004'
>>> '{:.1}'.format(0.1+0.2)
'0.3'
>>> '{}'.format(1/3)
'0.3333333333333333'
>>> '{:.5}'.format(1/3)
'0.33333'
>>> '{:.5}'.format(4/3)
'1.3333'
>>> '{:.5}'.format(1/30)
'0.033333'
```

Il existe aussi une option `%` pour afficher un nombre flottant sous la forme d'un pourcentage.
On peut ajouter une précision (avec un point) à ce pourcentage, qui cette fois-ci précise le nombre de chiffres après la virgule uniquement.

```python
>>> '{:%}'.format(1/2)
'50.000000%'
>>> '{:.1%}'.format(1/3)
'33.3%'
```

Étant donné que les accolades ont un effet bien particulier au sein des chaînes de formatage, il est nécessaire de les échapper pour les ajouter en tant que caractères.
Il faut pour cela les doubler. `{{` correspondra au caractère `{` dans une chaîne de formatage, et `}}` au caractère `}`.

```python
>>> '{} {{}} {}'.format(1, 2)
'1 {} 2'
```

Ces options de formatage ne sont pas exhaustives, et vous les trouverez plus en détails dans la [documentation détaillée](https://docs.python.org/fr/3/library/string.html#formatspec) ou  en annexe.

Vous pouvez aussi obtenir plus d'aide sur le formatage à l'aide de l'appel `help('FORMATTING')` depuis l'interpréteur interactif.

#### Operateur `%`

Une autre méthode de formatage plus ancienne existe aussi en Python, elle utilise l'opérateur `%`.

On applique donc cet opérateur à une chaîne (à gauche) en lui donnant un tuple d'arguments (à droite).
Comme précédemment, la chaîne suit un certain format pour définir où seront insérés les arguments.

Ici, le format est celui utilisé par la fonction `printf` en C, où l'on identifie les valeurs par leur type : `%s` pour une chaîne de caractère, `%d` pour un nombre entier ou encore `%f` pour un flottant.
Les arguments seront toujours pris successivement dans le tuple qui les fournit (comme les arguments positionnels avec `{}`).

En pratique, on a donc quelque chose de la sorte :

```python
>>> '%s dit à %s: tu me dois %d€' % ('Bob', 'Alice', 20)
'Bob dit à Alice: tu me dois 20€'
```

On trouve aussi la possibilité de préciser des options telle que la largeur de champ ou la précision, en les insérant entre le `%` et le caractère représentant le type.

```python
>>> '%10s répond: il ne me reste que %.2f€' % ('Alice', 18.5)
'     Alice répond: il ne me reste que 18.50€'

```

Et il existe encore d'autres possibilités (types et options).
Mais cette syntaxe est de moins en moins utilisée en Python, c'est pourquoi je n'en parlerai pas plus longuement.
Vous trouverez cependant plus d'informations à son sujet [dans la documentation](https://docs.python.org/fr/3/library/stdtypes.html#printf-style-string-formatting).

Sachez que tout ce qu'il est possible de faire sur les chaînes de caractères avec `%` est aussi réalisable avec la méthode `format`.
Et nous allons maintenant voir une forme encore plus simple d'utilisation.
