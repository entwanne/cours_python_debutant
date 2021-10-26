### Glossaire

##### annotation de type

Information facultative sur le **type** d'une **variable**, d'une **fonction** ou d'un **paramètre**.
Utilisée par des outils tels que _mypy_ pour vérifier la cohérence du code.

##### argument

**Valeur** envoyée à une **fonction**, qui sera assignée à un **paramètre**. Les arguments peuvent être positionnels (une simple valeur dans la liste des arguments) ou nommés (préfixés du nom du paramètre : `end='\n'`).

##### assertion

**Prédicat** évalué avec le **mot-clé** `assert` qui lève une **exception** s'il est faux.

##### assignation

Affectation d'une **valeur** à une **variable**.

```python
variable = 42
```

##### attribut

Champ contenu dans un **objet**, données relatives à l'objet (`obj.attr`).

##### bibliothèque standard (_stdlib_)

Ensemble des **modules**, **paquets** et **fonctions natives** embarquées avec Python par défaut.

##### bloc

Élément de syntaxe qui réunit plusieurs lignes de code dans une même entité, introduit par une **instruction** particulière (**boucle**, **condition**, etc.) suivie d'un `:`.

##### booléen

**Type** de **valeur** à deux états, _vrai_ (`True`) ou _faux_ (`False`).

##### boucle

**Bloc** de code répété un certain nombre de fois (pour **itérer** avec une boucle `for` ou selon une **condition** **booléenne** avec un `while`).

```python
while condition:
    ...

for item in iterable:
    ...
```

##### boucle infinie

**Boucle** dont la condition de fin n'est jamais atteinte, qui ne s'arrête jamais.

##### _bytes_

**Valeur** semblable aux **chaînes de caractères** pour représenter des **séquences** d'octets (des nombres entre 0 et 255).
`b'a\x01b\x02'` est de type _bytes_.

##### _callable_

**Objet** que l'on peut appeler, tel qu'une **fonction**.

```pycon
>>> min(3, 4)
3
>>> int('123')
123
```

##### chaîne de caractères (_string_)

**Valeur** représentant du texte, une **séquence** de caractères (`'abcdef'` par exemple).

##### chemin (_path_)

_Adresse_ d'un **fichier** sur le système d'exploitation.

##### clé

Identifiant d'une **valeur** dans un **dictionnaire**. Seuls les types de données **_hashables_** peuvent être utilisés en tant que clés.

##### condition

**Bloc** de code exécuté selon la **valeur** d'une **expression** **booléenne**.

```python
if condition:
    ...
```

##### conteneur

**Objet** contenant des éléments (des **valeurs**), auxquels on peut généralement accéder par **itération** ou via l'opérateur `container[key]`.

##### débogueur

Outil permettant de déceler pas-à-pas les bugs dans le code d'un programme.

##### décorateur

Élément de syntaxe permettant de modifier le comportement d'une **fonction**, introduit par un `@` suivi du nom du décorateur avant la définition de la fonction (`@cache` par exemple).

```python
@cache
def addition(a, b):
    return a + b
```

##### dictionnaire

Table d'association, pour associer des **valeurs** à des **clés**.

```python
{'a': 'foo', 2: 3}
```

##### docstring

**Chaîne de caractères** en en-tête d'une **fonction** pour documenter son comportement.

```python
def addition(a, b):
    "Addition entre deux nombres"
    return a + b
```

##### _EAFP_

_Easier to Ask Forgiveness than Permission_ (_il est plus simple de demander pardon que demander la permission_), mécanisme de traitement des erreurs qui préconise de laisser se produire les **exceptions** pour les attraper ensuite (_demander pardon_).  
_EAFP_ s'oppose à **_LBYL_**.

##### éditeur de texte

Logiciel permettant de modifier des **fichiers** texte (ou fichiers de code) sur le système d'exploitation.

##### encodage

Norme de codage des caractères dans une **chaîne de caractères**, associe chaque caractère (lettres, chiffres, symbole, accents, etc.) à un nombre.

##### ensemble (_set_)

**Conteneur** non-ordonné composé de **valeurs** uniques et **hashables**.

```python
{'a', 'b', 'c'}
```

##### entrée standard

Flux de données en entrée du programme, le terminal par défaut, sollicité par la **fonction** `input`.
Correspond à `sys.stdin`.

##### environnement virtuel

Répertoire cloisonné de **paquets** Python.

##### exception

Comportement permettant de remonter des erreurs dans le programme afin de les traiter.

##### expression

Ensemble d'opérations Python qui produisent une **valeur**.

```pycon
>>> (1 + 2 * 3) / 5 + round(1/3, 2)
1.73
```

##### fichier

Document sur le système d'exploitation (adressé par un **chemin**), représenté en Python par un **objet** qui permet d'interagir avec lui (lire son contenu, écrire dans le fichier, etc.).

##### fonction

Opération recevant des **arguments** et renvoyant une nouvelle **valeur** en fonction de ceux-ci (fonctions mathématiques par exemple : `round`, `abs`).

```pycon
>>> round(3.5)
4
>>> abs(-2)
2
```

##### fonction native (_builtin_)

**Fonction** disponible directement dans l'interpréteur, sans **import**.

##### fonction récursive

**Fonction** qui se rappelle elle-même pour mettre en place un mécanisme de répétition.

```python
def my_len(s):
    if s:
        return 1 + len(s[1:])
    return 0
```

##### formatage

Action d'obtenir une **représentation** d'une **valeur** dans un format voulu.

##### _f-string_

Chaîne de **formatage**, élément de syntaxe permettant de composer facilement des **chaines de caractères**.

```pycon
>>> f"1 + 3 = {1+3}"
'1 + 3 = 4'
```

##### gestionnaire de contexte

**Bloc** permettant de gérer des ressources (telles que des **fichiers**).

```python
with open('file.txt') as finput:
    ...
```

##### _hashable_

**Valeur** qui peut être utilisée en tant que **clé** de **dictionnaire** ou contenue dans un **ensemble**.
Le _hash_ est un « code-barre » généré à partir de la valeur, qui permet de la retrouver : le _hash_ d'un objet ne doit pas changer et deux valeurs égales doivent avoir le même _hash_.

Les **types** **immutables** natifs de Python sont _hashables_ tandis que les **mutables** ne le sont pas.

##### _IDLE_

_Interactive DeveLopment Environment_, l'environnement de développement fourni avec Python.

##### import

**Instruction** qui permet de charger le code d'un **module** Python.

```python
import math
```

##### instruction

Élément de syntaxe de Python au sens large, souvent équivalent à une ligne de code.

##### intension

Manière de créer des **listes** / **ensembles** / **dictionnaires** par **itération**.

```pycon
>>> [i**2 for i in range(5)]
[0, 1, 4, 9, 16]
>>> {i**2 for i in range(5)}
{0, 1, 4, 9, 16}
>>> {i**2: i for i in range(5)}
{0: 0, 1: 1, 4: 2, 9: 3, 16: 4}
```

##### interpréteur interactif / _REPL_

Mode de l'interpréteur de Python qui permet d'entrer les **instructions** et de les exécuter directement, en affichant les **valeurs** des **expressions**.  
_REPL_ pour _Read-Eval-Print-Loop_, soit _boucle qui lit, évalue et affiche_.

##### introspection

Caractéristique d'un programme qui est capable de s'inspecter lui-même (parcourir les **attributs** de ses objets, explorer les **méthodes**, etc.).

##### itérable

**Valeur** sur laquelle on peut **itérer** à l'aide d'une **boucle** `for`, appliquer un traitement sur chacun des éléments.

```python
for item in [3, 2, 5, 8]:
    ...
```

##### itérateur

Curseur le long d'un **itérable**, utilisé par les **boucles** `for` pour les parcourir.

##### itération / itérer

Action de parcourir les éléments d'un **itérable** avec un **itérateur**.

##### _LBYL_

_Look Before You Leap_ (_réfléchis avant d'agir_), mécanisme de traitement des erreurs qui préconise d'empêcher les erreurs en vérifiant les conditions de réussite au préalable.  
_LBYL_ s'oppose à **_EAFP_**.

##### liste

**Séquence** **mutable** d'élements de **types** variables.

```python
[1, 2, 3, 4]
['a', 42, 1.5, [0]]
```

##### littéral

Élément de syntaxe de base qui possède une **valeur**, comme les **chaînes de caractères**, les **listes** ou les **dictionnaires**.

##### méthode

**Fonction** intégrée à un **objet**, opération spécifique à un **type**.

```pycon
>>> [1, 2, 3].pop()
3
```

##### module

Fichier de code Python, que l'on peut charger à l'aide d'un **import**.

##### mot-clé

Élément de syntaxe formé de lettres correspondant à une **instruction** ou un **opérateur** du langage.
Les mots-clés ne peuvent pas être utilisés comme noms de **variables**.

##### mutable / immutable

Une **valeur** mutable est une valeur modifiable, que l'on peut altérer (les **listes** par exemple) contrairement à une valeur immutable (comme les **tuples**).

```pycon
>>> values = [1, 2, 3]
>>> values[0] = 4
>>> values
[4, 2, 3]
>>> values = (1, 2, 3)
>>> values[0] = 4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

##### nombre complexe

Représentation d'un nombre complexe en Python, formé de deux **flottants** (partie réelle et partie imaginaire suffixée d'un `j`) comme `3.2+5j`.

##### nombre entier

Représentation d'un nombre entier relatif (positif ou négatif) en Python.
Suite de chiffres potentiellement précédée d'un `+` ou d'un `-`, comme `101` ou `-42`.

##### nombre flottant

Représentation d'un nombre réel en Python, formé d'une partie entière et d'une partie décimale, comme `10.0`, `8.3` ou `5e2`.

##### objet / valeur

Résultat d'une **expression**, qui peut être stocké dans une **variable**.
Toute valeur Python est un objet, et peut posséder des **attributs** et **méthodes**.

##### opérateur

Élément de syntaxe (**mot-clé** ou caractères spéciaux) représentant une opération en Python, comme `+` pour l'addition.

##### paquet (_package_)

Niveau d'indirection au-dessus du **module** : un module qui contient des modules.  
S'utilise aussi pour parler des bibliothèques tierces, installables via `pip` (gestionnaire de paquets).

##### paramètre

**Variable** d'une **fonction** dont la **valeur** sera automatiquement **assignée** selon un **argument**.
Un paramètre peut choisir d'accepter les arguments positionnels ou nommés, et posséder une valeur par défaut.

```python
def func(param1, param2=None):
    pass
```

##### _PEP_

_Python Enhancement Proposal_, soit _Proposition d'amélioration pour Python_, c'est par là que passent les demandes de fonctionnalités au langage, avant d'être acceptées ou non.

##### prédicat

**Expression** booléenne, utilisée dans une condition.

##### pythonique

Qualificatif de ce qui est idomatique en Python, qui correspond à la philosophie du langage.
Voir [cet article](https://zestedesavoir.com/articles/1079/les-secrets-dun-code-pythonique/) à propos du code pythonique.

##### représentation

**Chaîne de caractères** obtenue à partir d'une **valeur**, qui permet d'en décrire le contenu.

##### retour

**Valeur** renvoyée par une **fonction**.
Donne sa valeur à l'**expression** d'appel de la fonction.

```pycon
>>> x = abs(-1)
>>> x
1
```

##### séquence

**Conteneur** dont les clés sont des nombres entiers de `0` à `N-1` (avec `N` la taille du conteneur).

##### scope

Espace de noms, là où sont déclarées les **variables**.

##### _slicing_

Découpage d'une séquence selon un intervalle.

```pycon
>>> 'abcdefghi'[1:-1:2]
'bdfh'
>>> [1, 2, 3, 4][1:]
[2, 3, 4]
```

##### sortie d'erreur

Flux de données en sortie du programme dédié aux erreurs, le terminal par défaut.
Correspond à `sys.stderr`.

##### sortie standard

Flux de données en sortie du programme où sont affichés les messages (par appel à `print` par exemple), le terminal par défaut.
Correspond à `sys.stdout`.

##### test

**Fonction** composée d'**assertions** pour vérifier le bon comportement d'un code.

##### tuple

**Séquence** **immutable** d'éléments de **types** variables.

```python
(1, 2, 3, 4)
('a', 42, 1.5, [0])
```

##### tuple nommé

**tuple** dont les éléments peuvent aussi être accédés via des **atributs**.

```python
from collections import namedtuple
Point = namedtuple('Point', ('x', 'y'))
p = Point(3, 5)
print(p.x, p.y)
```

##### type

Toute **valeur** en Python possède un type, qui décrit les opérations et **méthodes** qui lui sont applicables.

##### variable

Étiquette posée sur une **valeur** par **assignation**.
Plusieurs variables peuvent correspondre à la même valeur.

```python
variable = 42
```

##### zen

_Zen of Python_, ou **PEP** 20, sorte de poème qui décrit la philosophie du langage : <https://www.python.org/dev/peps/pep-0020/> ([traduction](https://zestedesavoir.com/articles/1079/les-secrets-dun-code-pythonique/#1-zen-of-python)).
