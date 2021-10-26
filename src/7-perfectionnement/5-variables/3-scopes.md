### Scopes

Je vais être assez bref sur ce sujet car je ne souhaite pas vous inonder d'informations compliquées, mais je pense qu'il est temps de parler un peu des scopes.

On a vu plus tôt que les fonctions définissaient un espace de noms (un scope) : les variable définies dans une fonction n'existent pas à l'extérieur.
L'inverse n'est pas vrai, les mécanismes de Python permettent d'accéder depuis une fonction à une variable définie à l'extérieur.

```pycon
>>> x = 5
>>>
>>> def get_x():
...     print('x vaut', x)
...
>>> get_x()
x vaut 5
```

On a vu aussi qu'il était possible depuis une fonction de définir une variable locale du même nom qu'une variable extérieur, sans que cela ne provoque d'erreur ou d'interférence.

```pycon
>>> def set_x():
...     x = 12
...     print('x vaut', x)
... 
>>> set_x()
x vaut 12
>>> x
5
```

On a vu enfin que cela pouvait poser problème si l'on tente d'accéder à une variable extérieure avant de la redéfinir, Python croyant avoir affaire à une variable locale qui n'a pas encore été définie.

```pycon
>>> def set_x():
...     print('x vaut', x)
...     x = 12
... 
>>> set_x()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in set_x
UnboundLocalError: local variable 'x' referenced before assignment
```

Ces points mènent à une question : est-il possible de redéfinir une variable extérieure depuis une fonction Python ?
La réponse est oui, mais à l'aide de mots-clés spécifiques.

#### Variables globales

Dans notre exemple, `x` est appelée une variable globale, car elle est définie à la racine (au plus haut espace de noms) du module courant, et est donc accessible dans tout le module.
Pour redéfinir une variable globale depuis une fonction du module, il nous faut la déclarer au sein de la fonction.
La déclarer c'est indiquer à Python que la variable existe quelque part et lui permettre de la retrouver, afin de la distinguer d'une variable locale.

Ici, on va utiliser le mot-clé `global` pour indiquer que la variable existe dans le scope global du module.
Après, il nous sera possible de l'utiliser comme une variable locale, et donc même de la redéfinir.

```pycon
>>> def set_x():
...     global x
...     x = 12
...     print('x vaut', 12)
... 
>>> x
5
>>> set_x()
x vaut 12
>>> x
12
```

Bien sûr, l'instruction `global x` doit être exécutée dans la fonction avant toute utilisation de la variable `x`.

`global` peut aussi être utilisé avec une variable n'existant pas encore dans le scope global.
Mais cela signifie à Python que c'est dans ce scope qu'il faudra la définir.

```pycon
>>> def set_y():
...     global y
...     y = 17
... 
>>> set_y()
>>> y
17
```

[[a]]
| L'utilisation de `global` induit naturellement des effets de bord et rend le flux d'exécution du programme plus difficile à suivre.
| Dans la mesure du possible, évitez donc de l'utiliser à moins d'être sûrs de ce que vous faites.

On notera aussi que le mot-clé `global` n'est utile que pour redéfinir une variable globale, il n'est pas nécessaire pour y accéder ni même pour la modifier.

```pycon
>>> items = []
>>>
>>> def add_item(value):
...     items.append(value)
...     print(items)
... 
>>> add_item(3)
[3]
>>> add_item(5)
[3, 5]
>>> add_item(8)
[3, 5, 8]
```

#### Fonctions imbriquées

En Python les fonctions sont des valeurs de premier ordre, c'est-à-dire des valeurs à part entière comme le sont les nombres ou les chaînes de caractères.
Il est donc possible de les manipuler, de les mettre dans des variables, d'utiliser ces variables comme des fonctions etc.

```pycon
>>> func = print
>>> func('toto')
toto
```

Et donc naturellement, il est aussi possible de renvoyer des fonctions depuis des fonctions.

```pycon
>>> def get_print():
...     return print
...
>>> p = get_print()
>>> p('toto')
toto
>>> get_print()('tata')
tata
```

Mais mieux encore, il est possible de définir des fonctions au sein d'autres fonctions.
Ces fonctions seront comme toutes les variables locales, perdues si elles ne sont pas renvoyées par la fonction mère.

```pycon
>>> def get_print():
...     def special_print(*args):
...         print(':', *args)
...     return special_print
... 
>>> p = get_print()
>>> p('toto')
: toto
```

#### Variables non-locales

Le sujet des scopes ne se résume donc pas aux variables locales et globales : avec les fonctions imbriquées, les scopes s'imbriquent eux aussi.
Il existe alors des variables intermédiaires qui ne sont ni locales (appartenant au scope le plus bas) ni globales (scope le plus haut), que l'on appelle variables non-locales.

```python
def add_by(a):
    def inner(b):
        return a + b
    return inner
```

Cet exemple permet de générer des fonctions pour additionner par un nombre en particulier.

```pycon
>>> add_by_3 = add_by(3)
>>> add_by_3(5)
8
>>> add_by_3(10)
13
```

Das l'exemple, `b` est une variable locale à la fonction `inner`, et `a` lui est une variable non-locale.
Mais la définition dépend toujours du scope dans lequel on regarde : `a` est aussi une variable locale de `add_by`.  
Et d'ailleurs, une variable globale n'est rien de plus qu'une variable locale à un module.

De la même manière que pour les globales, il est possible de redéfinir les variables non-locales.
Mais cela dépasse le cadre de ce cours, et je vous conseille alors de vous diriger vers mon tutoriel [Variables, scopes et closures en Python](https://zestedesavoir.com/tutoriels/3163/variables-scopes-et-closures-en-python/) si vous souhaitez en apprendre plus sur ces variables, et découvrir les mécanismes de capture.
