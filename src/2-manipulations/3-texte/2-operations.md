### Opérations sur les chaînes

Une chaîne de caractères est une valeur à part entière, et comme toute valeur elle a certaines opérations qui lui sont applicables.

Pour commencer, la fonction `len` est une fonction de base de Python, qui peut être appelée avec une chaîne de caractères en argument.
La fonction renvoie un nombre entier représentant la longueur de la chaîne, c'est-à-dire le nombre de caractères qu'elle contient.

```pycon
>>> len('Hello')
5
>>> len('Hello World!')
12
```

C'est une fonction assez utile puisqu'elle nous permet par exemple de calculer l'espace occupé à l'écran par notre texte.

Mais d'autres opérations agissent directement sur le texte.
C'est le cas de l'opérateur d'addition (`+`) que nous avons vu pour les nombres et qui existe aussi pour le texte, mais pour lequel il a un sens un peu différent.

On ne va en effet pas additionner deux chaînes de caractères, ça n'aurait pas de sens, mais on va les mettre l'une à la suite de l'autre.
On appelle cette opération une concaténation.

```pycon
>>> 'Hello' + ' ' + 'World' + '!'
'Hello World!'
```

Les délimitateurs ne faisant pas partie de la chaîne, il est bien sûr possible de mixer des chaînes délimitées par des apostrophes avec d'autres délimitées par des guillemets.

```pycon
>>> 'abc' + "def"
'abcdef'
```

Nous retrouvons aussi l'opérateur de multiplication `*` pour représenter un autre type de concaténation : la répétition d'une chaîne un certain nombre de fois.
`'to' * 3` est ainsi équivalent à `'to' + 'to' + 'to'`.

```pycon
>>> 'to' * 3
'tototo'
```

On peut multiplier un texte par un nombre nul ou négatif, cela a pour effet de produire une chaîne vide.
En revanche multiplier une chaîne par un nombre flottant n'a aucun sens, et Python nous le fait bien comprendre.

```pycon
>>> 'toto' * 0
''
>>> 'toto' * -10
''
>>> 'toto' * 1.5
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'float'
```

Toutes les facilités vues jusqu'ici avec les opérateurs d'assignation restent bien sûr valables.

```pycon
>>> msg = 'Salut '
>>> msg += 'tom'*2 + ' et ' + 'na'*2
>>> print(msg)
Salut tomtom et nana
```

Mais nous découvrons aussi d'autres opérateurs que nous n'avions pas vus jusque là, pour des opérations spécifiques à ce nouveau type de données.  
Les chaînes de caractères formant une séquence d'éléments (des caractères), il est possible d'accéder de façon directe à chacun de ces éléments.

Cela se fait à l'aide de crochets (`[ ]`) en indiquant entre-eux la position du caractère voulu, par exemple `msg[3]`.  
Il faut savoir que généralement en informatique on compte à partir de 0.
Le premier caractère d'une chaîne se trouve donc à la position 0 de la séquence, le deuxième caractère à la position 1, etc. jusqu'au n-ième caractère à la position *n-1*.

```pycon
>>> msg = 'Salut'
>>> msg[0]
'S'
>>> msg[0] + msg[1] + msg[2] + msg[3] + msg[4]
'Salut'
```

La valeur `'S'` renvoyée par `msg[0]` est un caractère, c'est-à-dire en Python une chaîne de taille 1.

On peut alors représenter notre chaîne de caractères `'Salut'` sous la forme d'un tableau, associant une position (un index) à chaque caractère de la chaîne :

Index | Caractère
------|----------
0     | 'S'
1     | 'a'
2     | 'l'
3     | 'u'
4     | 't'

Il est ainsi possible d'accéder à n'importe quel caractère de la chaîne à partir de son index, s'il est compris dans les bornes (de `0` à `len(msg)-1`).

```pycon
>>> msg[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
```

On observe qu'au-delà on obtient une erreur `IndexError`, soit un index invalide.
On peut en revanche utiliser des index négatifs pour prendre la chaîne en sens inverse : -1 correspond au dernier caractère, -2 à l'avant dernier, jusqu'à `-len(msg)` pour le premier.
Chaque caractère a ainsi deux positions possibles dans la chaîne.

```pycon
>>> msg[-1]
't'
>>> msg[-3]
'l'
>>> msg[-5]
'S'
```

Index | Caractère
------|----------
-5    | 'S'
-4    | 'a'
-3    | 'l'
-2    | 'u'
-1    | 't'
