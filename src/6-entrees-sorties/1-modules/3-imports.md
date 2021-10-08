### Imports

Il y a différentes manières d'importer un module, et nous allons ici voir en quoi elles consistent.

Déjà, on a vu le simple `import foo` qui crée un nouvel objet `foo` représentant notre module et donc contenant les fonctions du module `foo.addition` et `foo.soustraction`.

Il est possible lors de l'import de choisir un autre nom que `foo` pour l'objet créé (par exemple pour opter pour un nom plus court) à l'aide du mot-clé `as` suivi du nom souhaité.

```python
>>> import foo as oof
>>> foo
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'foo' is not defined
>>> oof
<module 'foo' from '/tmp/foo.py'>
>>> oof.addition(1, 2)
3
```

Une autre syntaxe permet d'importer directement les objets que l'on veut depuis le module, sans créer d'objet pour le module, il s'agit de `from ... import ...`.

```python
>>> from foo import addition
>>> addition
<function addition at 0x7feb439c34c0>
>>> addition(3, 5)
8
>>> soustraction
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'soustraction' is not defined
>>> foo
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'foo' is not defined
```

Comme on le voit, cette syntaxe permet de rendre accessible la fonction `addition` directement, et uniquement elle.

Il est aussi possible de préciser plusieurs objets à importer en les séparant par des virgules.

```python
>>> from foo import addition, soustraction
>>> addition(3, 5)
8
>>> soustraction(8, 2)
6
```

Enfin, il peut arriver que vous rencontriez des `from foo import *`.
Cela permet d'importer tous les noms présents dans le module `foo` (ici `addition` et `soustraction`) et de les rendre directement accessibles comme s'ils étaient tous précisés explicitement.

C'est une syntaxe pratique pour des tests rapides dans l'interpréteur mais qui est peu recommandable généralement, parce qu'elle pollue inutilement l'espace de noms courant avec tout le contenu du module (et peut effacer des objets s'il y a un conflit entre les noms).
Comme on dit, l'explicite est préférable à l'implicite.
