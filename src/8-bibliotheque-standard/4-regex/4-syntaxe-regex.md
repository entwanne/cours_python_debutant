### Syntaxe des regex

Maintenant que nous connaissons les fonctions du module, voyons voir quelques autres éléments de syntaxe des _regex_.

#### Chaînes brutes (_raw strings_)

Il est d'usage, pour représenter des expressions rationnelles, de ne pas utiliser des chaînes de caractères telles quelles mais d'utiliser ce qu'on appelle des chaînes brutes (ou _raw strings_).
On les reconnaît au caractère `r` qui les préfixe.

```pycon
>>> r'abc'
'abc'
```

Celles-ci ne forment pas un type particulier, on voit d'ailleurs que l'objet évalué est une chaîne de caractère tout à fait normale.
Non la différence se trouve au niveau de l'analyse de l'entrée par l'interpréteur, la façon dont il interprète les caractères écrits pour former l'objet `str`.

On le sait, les chaînes de caractères permettent d'utiliser des séquences d'échappement telles que `\t` ou `\n` pour représenter des caractères spéciaux.

```pycon
>>> print('abc\tdef\nghi')
abc	def
ghi
```

Ce comportement est rendu possible par l'interpréteur qui quand il lit la séquence de caractères `\t` dans le code la transforme en caractère « tabulation ».

Mais il ne le fait pas pour les chaînes brutes, qui conservent alors toutes les séquences d'échappement sans les interpréter comme des caractères spéciaux.

```pycon
>>> print(r'abc\tdef\nghi')
abc\tdef\nghi
```

Pour les _regex_, on préfère ainsi utiliser des chaînes brutes pour ne pas générer de conflits avec des motifs qui pourraient être interprétés comme des séquences d'échappement.

```pycon
>>> re.fullmatch(r'[0-9]+', '1234')
<re.Match object; span=(0, 4), match='1234'>
```

#### Syntaxe des motifs

On a déjà vu de nombreux motifs dans le début du chapitre, mais laissez-moi ici vous les présenter de façon plus détaillée.

##### Échappement (`\`)

L'antislash utilisé devant un caractère spécial du motif permet de lui faire faire son aspect spécial et de l'utiliser comme un caractère normal. `\+` identifie le caractère `+`.

```pycon
>>> re.match(r'\.\+\$', '.+$')
<re.Match object; span=(0, 3), match='.+$'>
>>> re.match(r'\.\+\$', 'toto')
>>> re.match(r'.+$', 'toto')
<re.Match object; span=(0, 4), match='toto'>
```

##### Joker (`.`)

`.` est le caractère joker, il correspond à n'importe quel caractère du texte (hors retours à la ligne).
Il correspond toujours à un et un seul caractère.

```pycon
>>> re.match(r'.', 'a')
<re.Match object; span=(0, 1), match='a'>
>>> re.match(r'.', '@')
<re.Match object; span=(0, 1), match='@'>
>>> re.match(r'.', '')
>>> re.match(r'.', 'ab')
<re.Match object; span=(0, 1), match='a'>
```

Par défaut, le caractère de retour à la ligne (`\n`) n'est pas reconnu par ce motif mais on verra avec l'option `DOTALL` comment y remédier.

```pycon
>>> re.match(r'.', '\n')
```

##### Classes de caractères (`[...]`)

Les crochets identifient les classes de caractères, une classe pouvant alors correspondre à n'importe lequel des caractères qu'elle contient. `[abc]` pourra correspondre aux caractères `a`, `b` ou `c` (toujours un et un seul).

Il est possible de préciser dans cette classe des intervalles de chiffres ou de lettres à l'aide d'un tiret (`-`).
`[0-9]` identifie ainsi un chiffre et `[0-0A-Za-z]` un caractère alphanumérique.

Pour contenir le caractère `-` en lui-même, il est possible de l'échapper (le précéder d'un `\`) ou le placer au tout début ou à la fin de la classe : `[0-91-Za-z_-]` identifie un caractère alphanumérique, un caractère de soulignement (`_`) ou un tiret (`-`).

Un `^` placé en début de classe fait office de négation, ainsi la classe `[^0-9]` reconnaît les caractères qui ne sont pas des chiffres.

Les autres symboles que nous avons pu voir perdent leur signification spéciale à l'intérieur d'une classe de caractères.
Seul le caractère `]` a besoin d'être échappé pour éviter de fermer la classe prématurément.

##### Quantificateurs (`?`, `+`, `*`, `{...}`)

Les quantificateurs sont différents symboles qui s'appliquent au motif qui précède afin d'en préciser la quantité attendue.

* `?` rend le motif optionnel. Il s'agit alors d'un quantificateur 0 ou 1 fois.
* `+` permet de répéter le motif. Il s'agit alors d'un quantificateur 1 fois ou plus.
* `*` est un quantificateur 0 ou plus, il combine alors `?` et `+`.

Les accolades (`{...}`) permettent d'appliquer un quantificateur personnalisé au motif qui précède.
On précise à l'intérieur de ces accolades le nombre de répétitions voulues, ou l'intervalle de répétitions acceptées (sous forme de deux nombres séparés d'une virgule).

Par exemple `x{3}` identifie la chaîne `xxx` et `x{2,4}` correspond aux chaînes `xx`, `xxx` et `xxxx`.

Il est possible d'omettre l'une ou l'autre des bornes de l'intervalle. `{,n}` sera alors équivalent à `{0,n}` et `{n,}` signifiera un motif répété au moins `n` fois.

##### Groupes (`(...)`)

Les parenthèses permettent de prioriser une sous-expression mais aussi de former un groupe de capture.
Lors d'un appel valide à `re.fullmatch` par exemple, l'objet `re.Match` renvoyé permet d'accéder aux différentes valeurs des groupes capturés.  
Chaque groupe est identifié par un nombre correspondant à sa position dans l'expression, et le groupe 0 correspond à la chaîne entière.

```pycon
>>> match = re.fullmatch('([0-9]+)\+([0-9]+)=([0-9]+)', '13+25=38')
>>> match[0]
'13+25=38'
>>> match[1]
'13'
>>> match[2]
'25'
>>> match[3]
'38'
```

L'objet `re.Match` possède aussi une méthode `groups` pour renvoyer tous les groupes capturés dans le texte.

```pycon
>>> match.groups()
('13', '25', '38')
```

[[i]]
| Pour bénéficier de la priorisation des parenthèses sans créer de groupe de capture, il est possible d'utiliser un `?:` à l'intérieur des parenthèses (`(?:...)`), Python comprendra alors que ces parenthèses ne correspondent pas à un groupe.
|
| ```pycon
| >>> re.fullmatch('(ab)+', 'ababab')
| <re.Match object; span=(0, 6), match='ababab'>
| >>> _.groups()
| ('ab',)
| >>> re.fullmatch('(?:ab)+', 'ababab')
| <re.Match object; span=(0, 6), match='ababab'>
| >>> _.groups()
| ()
| ```

##### Unions (`|`)

Les quantificateurs nous permettent de représenter un choix entre plusieurs alternatives suivant le nombre de fois qu'un motif est répété.
Cette notion de choix est au cœur des automates finis puisqu'ils représentent les différents chemins qui partent d'un même nœud.

Pour représenter un choix simple, on utilise l'opérateur d'union (`|`), celui-ci offrant deux possibilités pour évaluer la chaîne : soit le motif de gauche, soit celui de droite.
Ainsi l'expression `ab|cd` correspond aux deux chaînes `'ab'` et `'cd'`.

```pycon
>>> re.fullmatch(r'ab|cd', 'ab')
<re.Match object; span=(0, 2), match='ab'>
>>> re.fullmatch(r'ab|cd', 'cd')
<re.Match object; span=(0, 2), match='cd'>
>>> re.fullmatch(r'ab|cd', 'abcd')
```

L'opérateur d'union a une priorité plus faible que l'ensemble des autres opérateurs, à l'exception des parenthèses qui permettent donc de prioriser une union.  
L'expression `a(b|c)d` correspond alors aux chaînes `'abd'` et `'acd'`.

```pycon
>>> re.fullmatch(r'a(b|c)d', 'abd')
<re.Match object; span=(0, 3), match='abd'>
>>> re.fullmatch(r'a(b|c)d', 'acd')
<re.Match object; span=(0, 3), match='acd'>
>>> re.fullmatch(r'a(b|c)d', 'ab')
```

Un quantificateur peut évidemment être appliqué à une union, deux choix possibles seront alors à opérer à chaque répétition du motif.
`(ab|ba)+` représente une chaîne comprenant une suite de mots `ab` ou `ba`.

```pycon
>>> re.fullmatch('(ab|ba)+', 'ababab')
<re.Match object; span=(0, 6), match='ababab'>
>>> re.fullmatch('(ab|ba)+', 'baba')
<re.Match object; span=(0, 4), match='baba'>
>>> re.fullmatch('(ab|ba)+', 'abba')
<re.Match object; span=(0, 4), match='abba'>
>>> re.fullmatch('(ab|ba)+', 'abbb')
```

Enfin, il est possible d'utiliser plusieurs `|` successifs pour représenter un choix entre plus de deux motifs.
`ab|bc|cd` identifie le motif `ab`, `bc` ou `cd`.

```pycon
<re.Match object; span=(0, 2), match='ab'>
>>> re.fullmatch('ab|bc|cd', 'bc')
<re.Match object; span=(0, 2), match='bc'>
>>> re.fullmatch('ab|bc|cd', 'cd')
<re.Match object; span=(0, 2), match='cd'>
>>> re.fullmatch('ab|bc|cd', 'ac')
```

[[i]]
| On note que les unions permettent de représenter différemment des motifs que l'on connaissait déjà.
| Par exemple `X|XY` est équivalent à `XY?` et `a|b|c` est équivalent à `[abc]`.

##### Marqueurs d'extrémités (`^` et `$`)

Les caractères `^` et `$` permettent respectivement d'identifier le début et la fin du texte (ou de la ligne suivant le mode, voir les options plus bas).

Ces marqueurs n'ont pas d'intérêt avec `re.fullmatch` qui les ajoute implicitement mais s'avèrent utiles pour les autres fonctions du module.
Un motif débutant par `^` indique qu'il doit se trouver au début du texte, tandis qu'un motif se terminant par `$` indique qu'il doit se trouver à la fin du texte.

```pycon
>>> re.search(r'^a', 'bac')
>>> re.search(r'^a', 'abc')
<re.Match object; span=(0, 1), match='a'>
>>> re.search(r'a$', 'bac')
>>> re.search(r'a$', 'bca')
<re.Match object; span=(2, 3), match='a'>
```

Ces marqueurs sont moins prioritaires que l'union, il est donc parfaitement possible par exemple de représenter l'ensemble des chaînes qui commencent par « zeste » ou terminent par « savoir » avec `^zeste|savoir$`.

```pycon
>>> re.search(r'^zeste|savoir$', 'zeste de savoir')
<re.Match object; span=(0, 5), match='zeste'>
>>> re.search(r'^zeste|savoir$', 'concentré de savoir')
<re.Match object; span=(13, 19), match='savoir'>
>>> re.search(r'^zeste|savoir$', 'zeste de citron')
<re.Match object; span=(0, 5), match='zeste'>
>>> re.search(r'^zeste|savoir$', 'concentré de citron')
```

[[i]]
| On remarque que lorsque les deux motifs d'une union correspondent au texte, c'est celui de gauche qui l'emporte (« zeste de savoir » _matche_ sur `^zeste` avant `savoir$`).

##### Séquences spéciales

On trouve aussi quelques séquences d'échappement particulières pour représenter facilement certaines classes de caractères.

Ainsi, `\d` identifie un chiffre (à la manière de `[0-9]` mais en plus large car identifie tous les caractères reconnus comme tels par le standard Unicode).

```pycon
>>> re.fullmatch(r'\d+', '123')
<re.Match object; span=(0, 3), match='123'>
>>> re.fullmatch(r'\d+', 'abc')
>>> re.fullmatch(r'\d+', '١٢٣')
<re.Match object; span=(0, 3), match='١٢٣'>
```

À l'inverse, `\D` identifie ce qui n'est pas un chiffre.

```pycon
>>> re.fullmatch(r'\D+', '123')
>>> re.fullmatch(r'\D+', 'abc')
<re.Match object; span=(0, 3), match='abc'>
```

La séquence `\w` correspond aux caractères alphanumériques unicodes (chiffres, lettres et caractères de soulignement comme `_`).
Là encore, `\W` (notez la majuscule) identifie le motif inverse, soit les caractères non alphanumériques.

```pycon
>>> re.fullmatch(r'\w+', 'Ab_12')
<re.Match object; span=(0, 5), match='Ab_12'>
>>> re.fullmatch(r'\w+', 'Àƀ_١٢')
<re.Match object; span=(0, 5), match='Àƀ_١٢'>
>>> re.fullmatch(r'\w+', '.?')
>>> re.fullmatch(r'\W+', '.?')
<re.Match object; span=(0, 2), match='.?'>
```

La séquence `\s` identifie un caractère d'espacement, et `\S` un autre caractère.

```pycon
>>> re.fullmatch(r'\s', ' ')
<re.Match object; span=(0, 1), match=' '>
>>> re.fullmatch(r'\s', '\n')
<re.Match object; span=(0, 1), match='\n'>
>>> re.fullmatch(r'\s', '\t')
<re.Match object; span=(0, 1), match='\t'>
>>> re.fullmatch(r'\s', 'x')
>>> re.fullmatch(r'\S', 'x')
<re.Match object; span=(0, 1), match='x'>
```

----------

D'autres motifs et séquences d'échappement ne sont pas abordés ici et je vous invite à les retrouver dans [la documentation du mode `re`](https://docs.python.org/fr/3/library/re.html).

#### Options

Les fonctions de recherche du module `re` acceptent un argument `flags` qui permet de préciser des options sur la recherche, que je vais vous décrire ici.

##### `re.IGNORECASE` (ou `re.I`)

Cette option permet simplement d'ignorer la casse des caractères de la chaîne à analyser, ainsi le motif ne fera pas de différence entre caractères en minuscules ou en capitales.

```pycon
>>> re.match('[a-z]+', 'ToTo', re.IGNORECASE)
<re.Match object; span=(0, 4), match='ToTo'>
>>> re.match('[a-z]+', 'ToTo')
```

##### `re.ASCII` (`re.A`)

Par défaut les _regex_ en Python expriment des motifs unicode, c'est-à-dire qu'elles gèrent les caractères accentués et spéciaux.  
Comme on l'a vu, le motif `\w` permet par exemple de reconnaître des chiffres et des lettres quelle que soit leur forme (différents alphabets, différentes diacritiques).

Mais il est possible de restreindre ces motifs à la seule table des caractères ASCII (cf [le tableau dans le chapitre dédié aux _bytes_](https://zestedesavoir.com/tutoriels/2514/un-zeste-de-python/6-entrees-sorties/7-formatage/#5-5-bytes)) avec l'option `ASCII` et ainsi n'accepter par exemple que les lettres de l'alphabet latin.

```pycon
>>> re.match('\w+', 'été', re.ASCII)
>>> re.match('\w+', 'ete', re.ASCII)
<re.Match object; span=(0, 3), match='ete'>
>>> re.match('\w+', 'été')
<re.Match object; span=(0, 3), match='été'>
```

##### `re.DOTALL` (`re.S`)

On a vu précédemment que le motif joker (`*`) ne reconnaissait pas le caractère de retour à la ligne dans le mode par défaut.
Il est possible de changer ce comportement à l'aide de l'option `DOTALL`.

```pycon
>>> re.match(r'.', '\n', re.DOTALL)
<re.Match object; span=(0, 1), match='\n'>
>>> re.match(r'.', '\n')
```

##### `re.MULTILINE` (`re.M`)

Enfin, l'option `MULTILINE` est une option qui permet de gérer différemment les textes sur plusieurs lignes.

Par défaut, une chaîne de caractères contenant des retours à la ligne (`\n`) est gérée comme les autres chaînes, sans traitement particulier pour les sauts de ligne.  
Cette option permet de différencier les lignes les unes des autres et d'avoir un traitement différencié.
Ainsi les marqueurs `^` et `$` n'identifieront plus seulement le début et la fin du texte mais aussi le début et la fin de chaque ligne.

```pycon
>>> re.findall(r'^.+$', 'abc\ndef\nghi', re.MULTILINE)
['abc', 'def', 'ghi']
>>> re.findall(r'^.+$', 'abc\ndef\nghi')
[]
```

[[a]]
| Le traitement n'est pas le même qu'avec l'option `DOTALL` qui elle ne reconnaît simplement pas les sauts de ligne comme des caractères spéciaux.
|
| ```pycon
| >>> re.findall(r'^.+$', 'abc\ndef\nghi', re.DOTALL)
| ['abc\ndef\nghi']
| ```

##### Composition d'options

Les options ne sont pas exclusives et peuvent être composées les unes avec les autres.  
On utilise pour cela la notation d'union afin d'assembler différentes options entre elles.

```pycon
>>> re.findall(r'^[a-z]\w+', 'abc\nDEF\nghî', re.ASCII | re.MULTILINE | re.IGNORECASE)
['abc', 'DEF', 'gh']
```

Ainsi le code qui précède permet de faire une recherche ascii multiligne ignorant la casse.

On pourra bien sûr enregistrer ces options dans une variable si on est amenés à les réutiliser.

```pycon
>>> flags = re.ASCII | re.IGNORECASE
>>> re.fullmatch(r'zds_\w+', 'zds_foo', flags)
<re.Match object; span=(0, 7), match='zds_foo'>
>>> re.fullmatch(r'zds_\w+', 'ZDS_BAR', flags)
<re.Match object; span=(0, 7), match='ZDS_BAR'>
>>> re.fullmatch(r'zds_\w+', 'zds_été', flags)
```

[[i]]
| L'ordre des opérandes autour des `|` n'a pas d'importance, puisqu'il s'agit d'une union de tous les éléments.  
| On remarque d'ailleurs que l'ordre n'est pas conservé dans le résultat de l'union.
|
| ```pycon
| >>> re.MULTILINE | re.ASCII
| re.ASCII|re.MULTILINE
| ```
