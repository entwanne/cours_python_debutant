### Les modules

Les modules forment un espace de noms et permettent ainsi de regrouper les définitions de fonctions et variables, en les liant à une même entité.

Ils prennent la forme de fichiers Python (un nom et une extension `.py`) et doivent suivre une nomenclature particulière (la même que pour les noms de variables ou de fonction) : uniquement composés de lettres, de chiffres et d'_underscores_ (`_`), et ne commençant pas par un chiffre.  
Ainsi, un fichier `foo.py` correspondra à un module `foo`.

```python
def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b
```
Code: foo.py

Pour charger le code d'un module (le code du fichier associé) et avoir accès à ses définitions, il est nécessaire de l'importer.
On utilise pour cela le mot-clé `import` de Python suivi du nom du module (`foo` dans notre exemple).

```pycon
>>> import foo
```

Rien ne se passe.
En fait, le code de notre fichier `foo.py` a bien été exécuté, mais comme il ne fait que définir des fonctions c'est invisible pour nous.

Avec le fichier `bar.py` suivant :

```python
print('Je suis le module bar')
```
Code: bar.py

On constate bien que son code est exécuté à l'import.

```pycon
>>> import bar
Je suis le module bar
```

Mais revenons-en à notre premier module, `foo`.
C'est bien beau de l'avoir importé, mais on aimerait pouvoir en exécuter les fonctions.
Si vous avez tenté d'appeler `addition` ou `soustraction` vous avez remarqué que les fonctions n'existaient pas et obtenu une erreur `NameError`.

C'est parce que les fonctions existent mais dans l'espace de noms (_namespace_) du module `foo`.
Il faut alors les préfixer de `foo.` pour y accéder : `foo.addition` ou `foo.soustraction`.
L'opérateur `.` signifiant « accède au nom contenu dans ».

```pycon
>>> foo.addition(3, 5)
8
>>> foo.soustraction(12, 42)
-30
```

`foo` en lui-même est un objet d'un nouveau type représentant le module importé.

```pycon
>>> foo
<module 'foo' from '/.../foo.py'>
```

#### La fonction `help`

Une fonction de Python est très utile pour se documenter sur un module, il s'agit de la fonction `help`.
On appelle la fonction depuis l'interpréteur interactif en lui donnant l'objet-module en argument (il faut donc l'avoir importé au préalable).

```pycon
>>> help(foo)
```

Le terminal affiche alors un écran d'aide détaillant le contenu du module.
Appuyez sur la touche ||Q|| pour quitter cet écran et revenir à l'interpréteur.

```
Help on module foo:

NAME
    foo

FUNCTIONS
    addition(a, b)
    
    soustraction(a, b)

FILE
    /.../foo.py

(END)
```

C'est très succinct pour le moment, nous verrons par la suite comment étayer tout cela en ajoutant de la documentation à notre module.

Notez que la fonction `help` n'est pas utile uniquement pour les modules, elle permet aussi de se documenter sur une fonction ou un type.

```pycon
>>> help(abs)

>>> help(int)

```

Vous pouvez faire défiler l'écran à l'aide des flèches haut/bas ou page-up/page-down, ainsi que la touche espace pour naviguer de page en page.

La fonction s'utilise aussi avec une chaîne de caractères en argument pour rechercher de l'aide sur un sujet précis.
Par exemple `help('keywords')` pour obtenir la liste des mots-clés de Python.

Enfin, on peut utiliser la fonction sans argument pour entrer dans une interface d'aide où chaque ligne entrée sera exécutée comme un nouvel appel à la fonction `help`.

```pycon
>>> help()

Welcome to Python 3.9's help utility!

[...]

help>
```
