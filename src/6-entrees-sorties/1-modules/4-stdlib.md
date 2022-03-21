### Bibliothèque standard

Python dispose par défaut de nombreux modules déjà prêts à être utilisés.
Ils sont regroupés dans ce qu'on appelle la bibliothèque standard (ou _stdlib_ pour _standard library_), c'est-à-dire les modules disponibles directement après l'installation de Python.

Ces modules apportent des fonctions concernant des domaines particuliers qui ne sont pas incluses dans l'espace de noms global pour ne pas le surcharger.
Ainsi on a par exemple un module `math` pour toutes les fonctions mathématiques usuelles (`sqrt`, `exp`, `cos`, `sin`) ainsi que les constantes (`pi`, `e`).

On importe donc le module comme on le faisait précédemment.

```pycon
>>> import math
```

Le module a beau ne pas se trouver dans le répertoire d'exécution, Python arrive à le trouver car il se situe dans un des répertoires d'installation.

[[a]]
| Attention d'ailleurs à la priorité des répertoires lors de la recherche d'un module : si nous avions un fichier `math.py` dans le répertoire d'exécution, c'est lui qui serait importé lors d'un `import math` plutôt que celui de la bibliothèque standard.
| Veillez donc toujours à ne pas utiliser de nom existant pour vos propres modules.

Comme annoncé, nous retrouvons dans ce module différentes constantes mathématiques.
Il s'agit de nombres flottants, avec donc la précision qui est la leur.

```pycon
>>> math.pi
3.141592653589793
>>> math.e
2.718281828459045
>>> math.inf
inf
```

Cette dernière représente l'infini, un nombre flottant supérieur à tout autre.

Question fonctions il ne sera pas possible de tout énumérer mais en voici quelques exemples.

```pycon
>>> math.sqrt(2) # Racine carrée
1.4142135623730951
>>> math.floor(1.5) # Arrondi à l'inférieur
1
>>> math.ceil(1.5) # Arrondi au supérieur
2
>>> math.cos(math.pi) # Cosinus (argument en radians)
-1.0
>>> math.sin(0) # Sinus (argument en radians)
0.0
>>> math.radians(180) # Conversion degrés -> radians
3.141592653589793
>>> math.degrees(math.pi) # Conversion radians -> degrés
180.0
>>> math.exp(1) # Exponentielle
2.718281828459045
>>> math.log(math.e) # Logarithme
1.0
>>> math.gcd(12, 8) # Calcul de PGCD
4
```

Encore une fois, pensez à `help(math)` si vous voulez un aperçu complet, ou à consulter [la documentation](https://docs.python.org/fr/3/library/math.html).

Je voudrais enfin attirer votre attention sur la fonction `isclose`.
Cette fonction permet de comparer deux nombres flottants avec une certaine marge d'erreur.

Pour rappel, il y a une certaine imprécision dans le stockage des flottants, et l'opérateur `==` est donc déconseillé.
`isclose` prend simplement les deux nombres en paramètres et renvoie un booléen indiquant s'ils sont « égaux » (disons très proches) ou non.

```pycon
>>> 0.1 + 0.2 == 0.3
False
>>> math.isclose(0.1 + 0.2, 0.3)
True
>>> math.isclose(0.2, 0.3)
False
```
