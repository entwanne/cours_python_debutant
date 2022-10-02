### Module re

En effet le graphe qui précède est bien joli, mais comment l'intégrer à notre programme pour pouvoir l'utiliser ?  
Ce graphe n'est qu'une représentation de l'expression rationnelle comme il en existe d'autres (notre fonction `is_number` en est une elle aussi).

Le plus souvent, on va représenter ces expressions sous la forme de chaînes de caractères, où des caractères spéciaux permettront de décrire des motifs (comme des boucles).
Il existe plusieurs standards pour cela, les plus connus étant POSIX et PCRE (_Perl-Compatible Regular Expressions_).  
Le standard POSIX est celui que l'on retrouvera dans des outils tels que `grep` ou `sed`.
En Python, c'est plutôt le standard PCRE qui est utilisé avec le module `re`.

Ce module regroupe les opérations permettant de travailler avec des expressions rationnelles, offrant différentes fonctions pour plusieurs usages (rechercher un motif, découper selon un motif, etc.).

#### Utilisation

On va y aller pas à pas pour construire une expression correspondant à notre besoin.
Nous allons tout d'abord importer le module `re` et nous intéresser à la fonction `re.fullmatch`.
C'est une fonction qui reçoit l'expression rationnelle (en premier argument) et le texte à analyser (en second) et qui renvoie un objet résultat ou `None` suivant si le texte correspond à l'expression ou non.

L'expression rationnelle peut être une chaîne de caractères toute simple (par exemple `'123'`) et la fonction va alors simplement vérifier que les caractères correspondent un à un.

```pycon
>>> import re
>>> re.fullmatch('123', '123')
<re.Match object; span=(0, 3), match='123'>
>>> re.fullmatch('123', '124')
```

On considère dans ce cas que la _regex_ se compose de motifs (`1`, `2`, `3`) qui ne peuvent chacun identifier qu'un seul caractère.

[[i]]
| On voit dans l'objet `re.Match` renvoyé par la fonction la zone qui a été identifiée dans le texte (la valeur `span` qui indique que le motif a été identifié entre les caractères 0 et 3) et l'extrait correspondant dans le texte (`match`, le texte complet dans notre cas).

Mais l'expression peut aussi contenir des caractères particuliers pour exprimer des motifs plus évolués. Ces motifs pouvant correspondre à plusieurs caractères dans notre texte.
Par exemple le caractère `.` utilisé dans une _regex_ signifie « n'importe quel caractère » (comme un joker).

```pycon
>>> re.fullmatch('12.', '123')
<re.Match object; span=(0, 3), match='123'>
>>> re.fullmatch('12.', '124')
<re.Match object; span=(0, 3), match='124'>
>>> re.fullmatch('12.', '134')
```

Un autre caractère particulier est le `+` qui indique que le motif qui précède peut être répété indéfiniment.
La _regex_ `'a+'` permet ainsi de reconnaître les suites de caractères `a` (minuscule, on note au passage que les _regex_ sont sensibles à la casse par défaut).

```pycon
>>> re.fullmatch('a+', 'a')
<re.Match object; span=(0, 1), match='a'>
>>> re.fullmatch('a+', 'aaaa')
<re.Match object; span=(0, 4), match='aaaa'>
>>> re.fullmatch('a+', 'aaab')
>>> re.fullmatch('a+', 'A')
```

[[i]]
| Il est parfaitement possible de combiner nos motifs spéciaux, ainsi `.+` identifie une suite de n'importe quels caractères : `'123'`, `'aaa'`, `'abcd'`, etc.
|
| ```pycon
| >>> re.fullmatch('.+', '123')
| <re.Match object; span=(0, 3), match='123'>
| >>> re.fullmatch('.+', 'aaa')
| <re.Match object; span=(0, 3), match='aaa'>
| >>> re.fullmatch('.+', 'abcd')
| <re.Match object; span=(0, 4), match='abcd'>
| ```

Dans le même genre que `+` on trouve aussi `?` pour indiquer un motif optionnel.
Un motif suivi d'un `?` peut donc être présent zéro ou une fois.

```pycon
>>> re.fullmatch('a?b', 'ab')
<re.Match object; span=(0, 2), match='ab'>
>>> re.fullmatch('a?b', 'b')
<re.Match object; span=(0, 1), match='b'>
>>> re.fullmatch('a?b', 'a')
```

On peut utiliser des parenthèses comme en mathématiques pour gérer les priorités : `(ab)?` correspondra ainsi à la chaîne `'ab'` ou à la chaîne vide, tandis que `ab?` correspond à `'a'` ou `'ab'`.

Dans notre cas initial, on cherche à pouvoir identifier des suites de chiffres.
Pour cela il va nous falloir utiliser des classes de caractères : ce sont des motifs qui peuvent correspondre à plusieurs caractères bien précis (ici des chiffres).

On définit une classe de caractère à l'aide d'une paire de crochets à l'intérieur de laquelle on fait figurer tous les caractères possibles.
Par exemple `[0123456789]` correspond à n'importe quel chiffre.  
Pour simplifier, il est possible d'utiliser un `-` pour définir un intervalle de caractères à l'intérieur de la classe : la syntaxe précédente devient alors équivalente à `[0-9]`.

```pycon
>>> re.fullmatch('[0-9]', '5')
<re.Match object; span=(0, 1), match='5'>
>>> re.fullmatch('[0-9]+', '123')
<re.Match object; span=(0, 3), match='123'>
```

#### `is_number`

Nous avons maintenant toutes les clefs en main pour recoder notre fonction `is_number`… ou presque !  
En effet, dans notre nombre nous voulons pouvoir identifier un caractère `.`, mais nous savons que ce caractère est un motif particulier dans une _regex_ qui fait office de joker.

Comment alors faire en sorte de n'identifier que le caractère `.` et lui seul ?
Il nous faut pour cela l'échapper, en le faisant précéder d'un _antislash_ (`\`).

```python
>>> re.fullmatch('\.', '.')
<re.Match object; span=(0, 1), match='.'>
>>> re.fullmatch('\.', 'a')
```

Reprenons maintenant le graphe de notre automate et décomposons-le.

![Automate](img/automate.png)
Figure: Automate `is_number` -- image générée par [regexper](https://regexper.com/)

Il commence par un état _Start of line_, c'est-à-dire le début de la ligne.
`re.fullmatch` s'occupe déjà de rechercher un motif au début du texte donné, donc nous n'avons pas à en tenir compte ici.

L'état suivant est optionnel puisqu'il existe un chemin qui le contourne, il teste si le caractère est un `+` ou un `-`.  
Cela correspond donc au motif `[+-]?` (à l'intérieur d'une classe de caractère, le `+` perd son statut de caractère spécial).

On voit que l'état suivant forme une boucle : il y a en effet un chemin qui part de la droite de l'état pour revenir à sa gauche, qui permet de le répéter indéfniment.  
Cette boucle correspond au symbole `+` que nous avons vu plus haut, qui signifie « au moins une fois ».

L'état en lui-même détaille que le caractère doit être entre `0` et `9`, soit `[0-9]`.
La _regex_ correspondant à ce motif est donc `[0-9]+`.

Les deux états qui suivent peuvent-être court-circuités pour arriver directement à la fin, cela veut dire qu'ils forment un groupe optionnel `(...)?`.

Le premier état est un simple point (`\.`) et le second est une nouvelle suite de chiffres (`[0-9]+`).
Le groupe s'exprime donc sous la forme `(\.[0-9]+)?`.

Enfin, l'état _End of line_ est lui aussi déjà géré par la fonction `fullmatch`.

En mettant tous ces extraits bout à bout, on forme la _regex_ finale qui identifie nos nombres : `[+-]?[0-9]+(\.[0-9]+)?`.

```pycon
>>> pattern = '[+-]?[0-9]+(\.[0-9]+)?'
>>> re.fullmatch(pattern, '123.456')
<re.Match object; span=(0, 7), match='123.456'>
>>> re.fullmatch(pattern, '-42')
<re.Match object; span=(0, 3), match='-42'>
>>> re.fullmatch(pattern, '100')
<re.Match object; span=(0, 3), match='100'>
>>> re.fullmatch(pattern, '0.0')
<re.Match object; span=(0, 3), match='0.0'>
>>> re.fullmatch(pattern, '.123')
>>> re.fullmatch(pattern, '123.')
>>> re.fullmatch(pattern, '.')
>>> re.fullmatch(pattern, 'abc')
```

La fonction `is_number` peut donc simplement être réécrite comme suit.

```python
import re

def is_number(my_string):
    result = re.fullmatch('[+-]?[0-9]+(\.[0-9]+)?', my_string)
    return result is not None
```

#### Autres fonctions du module

D'autres fonctions sont aussi proposées par le module `re` pour réaliser d'autres opérations.

##### `re.search`

`re.search` est une fonction similaire à `re.fullmatch` à la différence qu'elle permet de trouver un motif n'importe où dans la chaîne.

```pycon
>>> re.search('[0-9]+', 'abc123def')
<re.Match object; span=(3, 6), match='123'>
```

On remarque que les valeurs `span` et `match` du résultat correspondent à la zone où notre motif a été identifié dans le texte.
Cette valeur `match` est d'ailleurs récupérable en accédant au premier élément (`[0]`) de l'objet résultat.

```pycon
>>> result = re.search('[0-9]+', 'abc123def')
>>> result[0]
'123'
```

[[i]]
| Nous verrons par la suite que ce résultat peut en effet contenir plusieurs éléments.

Sachez qu'il existe les caractères spéciaux `^` et `$` pour reproduire le comportement de `fullmatch` avec `search` : un motif débutant par `^` signifie que le motif doit être trouvé au début du texte et un motif finissant par `$` signifie que le motif doit être trouvé à la fin.

```pycon
>>> re.search('^[0-9]+', 'abc123')
>>> re.search('^[0-9]+', '123abc')
<re.Match object; span=(0, 3), match='123'>
>>> re.search('[0-9]+$', '123abc')
>>> re.search('[0-9]+$', 'abc123')
<re.Match object; span=(3, 6), match='123'>
```

En combinant les deux, `re.search('^...$', ...)` est alors équivalent à `re.fullmatch('...', ...)`.

```pycon
>>> re.search('^[0-9]+$', 'abc123def')
>>> re.search('^[0-9]+$', '123')
<re.Match object; span=(0, 3), match='123'>
```

[[i]]
| On note qu'il existe aussi la fonction `re.match` qui recherche un motif au début du texte.
| Elle est ainsi équivalente à `re.search` avec un `^` systématique.

##### `re.findall`

Cette fonction est un peu plus intéressante : elle permet de trouver toutes les occurrences d'un motif dans le texte.
Elle renvoie la liste des extraits de texte ainsi trouvés.

```pycon
>>> re.findall('[0-9]+', "Nous sommes le 31 mars 2022 et il fait 10°C")
['31', '2022', '10']
```

Si le motif n'est jamais trouvé, la fonction renvoie simplement une liste vide.

```pycon
>>> re.findall('[0-9]+', "C'est bientôt le week-end")
[]
```

Dans la même veine, on trouve la fonction `re.finditer` qui ne renvoie pas une liste mais un itérateur pour parcourir les résultats.
Elle évite ainsi de parcourir le texte en entier dès le début et de constuire une liste.

```pycon
>>> for result in re.finditer('[0-9]+', "Nous sommes le 31 mars 2022 et il fait 10°C"):
...     print(result)
... 
<re.Match object; span=(15, 17), match='31'>
<re.Match object; span=(23, 27), match='2022'>
<re.Match object; span=(39, 41), match='10'>
```

##### `re.sub`

Cette fonction permet d'opérer des remplacements (ou comme son nom l'indique des substitutions) sur un texte, remplaçant chaque occurrence du motif par la valeur précisée.  
Elle prend donc en arguments la _regex_, la valeur par laquelle remplacer le motif, et le texte sur lequel opérer.
Et elle renvoie le texte après substitution.

```pycon
>>> re.sub('[0-9]+', '?', "Nous sommes le 31 mars 2022 et il fait 10°C")
'Nous sommes le ? mars ? et il fait ?°C'
```

Si le motif n'est pas trouvé, alors le texte est renvoyé inchangé.

```pycon
>>> re.sub('[0-9]+', '?', "C'est bientôt le week-end")
"C'est bientôt le week-end"
```

##### `re.split`

`re.split` est plus ou moins équivalente à la méthode `split` des chaînes de caractères, qui permet de découper la chaîne selon un séparateur, sauf qu'ici le séparateur est spécifié sous la forme d'une _regex_.

```pycon
>>> re.split('[ ,.?!:]+', 'Alors : ça décoiffe, hein ?')
['Alors', 'ça', 'décoiffe', 'hein', '']
```

[[i]]
| On constate qu'une chaîne vide est renvoyée dans le résultat si le texte termine par un séparateur.
| Mais on peut facilement la filtrer si elle ne nous intéresse pas.
|
| ```pycon
| >>> [s for s in re.split('[ ,.?!:]+', 'Alors : ça décoiffe, hein ?') if s]
| ['Alors', 'ça', 'décoiffe', 'hein']
| ```

##### `re.compile`

On notera enfin la présence de la fonction `re.compile` qui permet de créer un objet _regex_.
Cette fonction reçoit l'expression rationnelle sous forme d'une chaîne et renvoie un objet avec des méthodes `fullmatch`, `search`, `finditer`, `split`, etc.

Cea peut être plus pratique si l'on est amené à réutiliser plusieurs fois une même expression.

```python
>>> pattern = re.compile('[0-9]+')
>>> pattern.findall('3 + 5 = 8')
['3', '5', '8']
>>> pattern.sub('?', '3 + 5 = 8')
'? + ? = ?'
```
