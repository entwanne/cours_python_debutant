### Introspection

#### Informations sur la valeur

Avant d'en venir proprement au débogage de notre programme, faisons un tour des outils qui sont à notre disposition pour examiner notre programme.
Il s'agit de fonctions proposées par Python pour inspecter différentes valeurs du programme.  
On parle d'outils d'introspection car ils permettent au programme de s'examiner lui-même.

La première information, toute bête, c'est la valeur en elle-même, ou plutôt sa représentation.
C'est ce que l'on obtient quand on tape juste le nom de la variable dans l'interpréteur interactif par exemple.

```python
>>> value = 'toto'
>>> value
'toto'
```

Cette représentation est fournie par la fonction `repr`, qui renvoie donc une chaîne de caractères représentant la valeur.
Souvent, cette représentation va être la manière dont il est possible de définir cette valeur en Python,
c'est pour ça que des guillemets apparaissent autour des chaînes de caractères.  
Elle peut tout à fait être appelée depuis un programme pour afficher (avec `print`) l'état d'une variable.

```python
>>> print(repr(value))
'toto'
>>> print(repr(10))
10
>>> print(repr([1, 2, 'abc']))
[1, 2, 'abc']
```

Grâce à cette simple information, on identifie déjà à quoi correspond notre valeur.

Mais une autre information pertinente que l'on connaît déjà sur notre valeur, c'est son type, renvoyé par la fonction `type`.  
Cela nous permet, pour peu que l'on connaisse le type, de s'avoir quelles opérations et méthodes sont applicables à notre objet.

```python
>>> type(value)
<class 'str'>
>>> type([])
<class 'list'>
```

Et si on ne connaît pas ce type, on peut toujours se documenter dessus.
Soit en consultant la documentation en ligne, soit à l'aide de la fonction `help` que j'ai présentée plus tôt.

On sait que cette fonction peut prendre un type en argument, il est donc tout à fait possible de lui donner directement le retour de la fonction `type`.

```python
>>> help(type(value))
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |  [...]
>>> help(type([]))
Help on class list in module builtins:

class list(object)
 |  list(iterable=(), /)
 |  [...]
```

Mais plus simple encore : on peut directement donner à `help` la valeur sur laquelle on a besoin d'aide, la fonction s'occupera de renvoyer la documentation du type correspondant.

```python
>>> help([])
Help on list object:

class list(object)
 |  list(iterable=(), /)
 | [...]
```

[[a]]
| Attention, cela fonctionne pour toutes les valeurs sauf les chaînes de caractères.
|
| En effet, la fonction `help` interprète les chaînes comme un sujet d'aide en particulier :
| help('NUMBERS') affichera de l'aide sur les nombres en Python et pas sur le type `str`.

```python
>>> help('NUMBERS')
Numeric literals
****************

There are three types of numeric literals: integers, floating point
numbers, and imaginary numbers.
[...]
>>> help('toto')
No Python documentation found for 'toto'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.
```

Par ailleurs, il est possible de connaître tous les sujets sur lesquels `help` est capable de fournir de l'aide avec l'appel `help('topics')`.

#### Contenu de la valeur

* Examiner une valeur (objet, fonction, module) avec `dir`, `vars`

#### Suivre et comprendre les exceptions

* Débogage à l'aide de `print`
* Débogage à l'aide de tests (assertions)
