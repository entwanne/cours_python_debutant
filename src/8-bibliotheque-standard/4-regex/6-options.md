### Options

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
Comme on l'a vu, le motif `\w` permet par exemple de reconnaître des chiffres et des lettres quelle que soit leur forme (différents alphabets, différents diacritiques).

Mais il est possible de restreindre ces motifs à la seule table des caractères ASCII (cf [le tableau dans le chapitre dédié aux _bytes_](https://zestedesavoir.com/tutoriels/2514/un-zeste-de-python/6-entrees-sorties/7-formatage/#5-5-bytes)) avec l'option `ASCII` et ainsi n'accepter par exemple que les lettres de l'alphabet latin.

```pycon
>>> re.match('\w+', 'été', re.ASCII)
>>> re.match('\w+', 'ete', re.ASCII)
<re.Match object; span=(0, 3), match='ete'>
>>> re.match('\w+', 'été')
<re.Match object; span=(0, 3), match='été'>
```

##### `re.DOTALL` (`re.S`)

On a vu précédemment que le motif joker (`.`) ne reconnaissait pas le caractère de retour à la ligne dans le mode par défaut.
Il est possible de changer ce comportement à l'aide de l'option `DOTALL`.

```pycon
>>> re.match(r'.', '\n', re.DOTALL)
<re.Match object; span=(0, 1), match='\n'>
>>> re.match(r'.', '\n')
```

##### `re.MULTILINE` (`re.M`)

Enfin, l'option `MULTILINE` est une option qui permet de gérer différemment les textes sur plusieurs lignes.

Par défaut, une chaîne de caractères contenant des retours à la ligne (`\n`) est gérée comme les autres chaînes, sans traitement particulier pour les sauts de ligne.  
Cette option permet de différencier les lignes les unes des autres et d'avoir un traitement adapté.
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

#### Composition d'options

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
