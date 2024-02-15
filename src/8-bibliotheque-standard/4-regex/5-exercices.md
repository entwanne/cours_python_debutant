### Quelques exercices

Je vous propose maintenant de nous entraîner à construire des _regex_ pour résoudre différents problèmes.

Pour vous aider, vous pouvez utiliser des sites web tels que [regex101](https://regex101.com/) ou [regexr](https://regexr.com/) afin de tester et voir en temps réel comment sont interprétées vos _regex_.

##### Reconnaître un nombre pair

On veut ici identifier un nombre pair (en représentation décimale).  
Qu'est-ce qu'un nombre pair ? Un nombre qui se termine par un chiffre pair.

[[s]]
| ```python
| >>> pattern = re.compile(r'[+-]?[0-9]*[02468]')
| >>> pattern.fullmatch('42')
| <re.Match object; span=(0, 2), match='42'>
| >>> pattern.fullmatch('-108')
| <re.Match object; span=(0, 4), match='-108'>
| >>> pattern.fullmatch('0')
| <re.Match object; span=(0, 1), match='0'>
| >>> pattern.fullmatch('17')
| >>> pattern.fullmatch('abc')
| ```

##### Reconnaître un identifiant Python

On sait qu'un identifiant (nom de variable ou fonction) en Python est composé de lettres, de chiffres et de caractères `_`, et que le premier caractère ne peut pas être un chiffre.

[[s]]
| ```pycon
| >>> pattern = re.compile(r'[a-z_][a-z0-9_]*', re.IGNORECASE)
| >>> pattern.fullmatch('foo')
| <re.Match object; span=(0, 3), match='foo'>
| >>> pattern.fullmatch('BAR')
| <re.Match object; span=(0, 3), match='BAR'>
| >>> pattern.fullmatch('item1')
| <re.Match object; span=(0, 5), match='item1'>
| >>> pattern.fullmatch('1item')
| ```
|
| [[i]]
| | Cette solution ne reconnaît cependant pas certains identifiants valides comme `prénom`, mais nous ne souhaitons pas traiter ce cas ici comme ce nom n'est pas recommandé en Python.
| |
| | ```pycon
| | >>> pattern.fullmatch('prénom')
| | ```

##### Découper les mots d'une chaîne

Nous voulons maintenant découper tous les mots d'une chaîne de caractère, en considérant les mots comme des suites de lettres/chiffres et en ignorant tout le reste.

[[s]]
| On serait tenté d'utiliser la méthode `findall` avec une _regex_ `r'\w+'` mais `\w` ne reconnaît pas seulement les chiffres et les lettres, il inclut aussi le caractère de soulignement (`_`).
|
| ```pycon
| >>> pattern = re.compile(r'\w+')
| >>> pattern.findall("Et sous la pluie _I feel sorry_")
| ['Et', 'sous', 'la', 'pluie', '_I', 'feel', 'sorry_']
| ```
|
| On peut alors penser à une _regex_ du genre `r'[a-zA-Z0-9]+` mais on perdrait l'usage des caractères accentués.
| Au final la meilleure solution est de prendre le problème à l'envers : on veut exclure tous les caractères qui ne sont ni des chiffres ni des lettres. On sait que `\W` identifie tout ce qui n'est pas chiffre/lettre/_underscore_, il suffit alors d'ajouter explicitement le `_` et de prendre la négation (avec `^`) de la classe de caractères.  
| On trouve ainsi `r'[^\W_]+'`.
|
| ```pycon
| >>> pattern = re.compile(r'[^\W_]+')
| >>> pattern.findall("Et sous la pluie _I feel sorry_")
| ['Et', 'sous', 'la', 'pluie', 'I', 'feel', 'sorry']
| >>> pattern.findall("Adieu l'Émile je t'aimais bien.")
| ['Adieu', 'l', 'Émile', 'je', 't', 'aimais', 'bien']
| >>> pattern.findall("Regarde ta montre il est déjà 8h !")
| ['Regarde', 'ta', 'montre', 'il', 'est', 'déjà', '8h']
| ```

##### Mettre des mots en évidence

Ensuite on aimerait passer en majuscules tous les mots (lettres/chiffres/_underscores_) contenant la lettre « t » dans un texte.

[[s]]
| ```pycon
| >>> def upperize(match_obj):
| ...     return match_obj[0].upper()
| ... 
| >>> pattern = re.compile(r'\w*[tT]\w*')
| >>> pattern.sub(upperize, "Quand tu traverses la pièce, en silence que tu passes devant moi")
| 'Quand TU TRAVERSES la pièce, en silence que TU passes DEVANT moi'
| ```

##### Identifier un palindrome

Enfin on voudrait utiliser une _regex_ pour reconnaître un palindrome, c'est-à-dire un mot qui peut se lire dans les deux sens comme « ressasser ».

[[i]]
| Vous ne trouvez pas ? C'est normal : les _regex_ ne disposant pas de mémoire, il n'est pas possible de se souvenir du début de la chaîne quand on en analyse la fin. Nous verrons cela plus en détails dans les limitations des _regex_.
