### Chaînes de caractères

La chaîne de caractère est le type utilisé pour représenter du texte, on peut la voir comme un tableau contenant des caractères.

#### Conversions

Toute valeur Python est convertible en chaîne de caractères, en faisant appel à `str`.

```python
>>> str(True)
'True'
>>> str(4)
'4'
>>> str(1.5)
'1.5'
>>> str('foo')
'foo'
>>> str([1, 2, 3])
'[1, 2, 3]'
```

C'est ainsi que `print` procède d'ailleurs pour afficher n'importe quelle valeur.

#### Opérations

La longueur d'une chaîne peut être obtenue par un appel à la fonction `len`.

```python
>>> len('foo')
3
>>> len('hello world')
11
>>> len('')
0
```

##### Indexation

On peut accéder aux différents caractères de la chaîne à l'aide de l'opérateur d'indexation `[]` accompagné d'un index (une position dans la chaîne, à partir de 0).
Cet index peut être négatif pour parcourir la chaîne depuis la fin.

```python
>>> 'hello world'[1]
'e'
>>> 'hello world'[-3]
'r'
```

On peut préciser un intervalle d'index grâce au _slicing_ avec la syntaxe `debut:fin:pas` où chaque élément est optionnel.

```python
>>> 'hello world'[3:]
'lo world'
>>> 'hello world'[:-4]
'hello w'
>>> 'hello world'[1:8:2]
'el o'
```

##### Concaténation

Il est possible de concaténer (mettre à la suite) plusieurs chaînes de caractères avec l'opérateur `+`.

```python
>>> 'hello' + ' ' + 'world' + '!'
'hello world!'
```

On peut aussi « multiplier » une chaîne par un nombre entier _n_ pur obtenir _n_ concaténations de cette même chaîne.

```python
>>> 'hello ' * 3
'hello hello hello '
```

##### Relations d'ordre

Les chaînes de caractères sont ordonnées les unes par rapport aux autres, il est donc possible d'utiliser les opérateurs `<`, `>`, `<=` et `>=` entre deux chaînes.

La comparaison est faite en fonction de l'ordre lexicographique, une extension de l'ordre alphabétique.

```python
>>> 'abc' < 'def'
True
>>> 'abc' > 'def'
False
```

##### Appartenance

L'opérateur `in` permet de tester si une chaîne contient un caractère ou une sous-chaîne (ou vu autrement, si cette sous-chaîne appartient à la chaîne).
L'opération renvoie un booléen.

```python
>>> 'h' in 'hello'
True
>>> 'lo' in 'hello'
True
>>> 'la' in 'hello'
False
```

#### Principales méthodes

Les méthode `lstrip`, `rstrip` et `strip` permettent respectivement de renvoyer une nouvelle chaîne en supprimant les espaces au début, à la fin ou des deux côtés.

```python
>>> '  foo bar  '.lstrip()
'foo bar  '
>>> '  foo bar  '.rstrip()
'  foo bar'
>>> '  foo bar  '.strip()
'foo bar'
```

Elles acceptent un argument optionnel pour supprimer une chaîne en particulier plutôt que des espaces.

```python
>>> '...hello...'.strip('.')
'hello'
```

Les méthodes `upper`, `lower`, `capitalize` et `title` permettent d'obtenir une nouvelle chaîne en changeant la casse des caractères.

```python
>>> 'HeLlO wOrLd!'.upper()
'HELLO WORLD!'
>>> 'HeLlO wOrLd!'.lower()
'hello world!'
>>> 'HeLlO wOrLd!'.capitalize()
'Hello world!'
>>> 'HeLlO wOrLd!'.title()
'Hello World!'
```

`index` et `find` servent à trouver la première position d'un caractère (ou d'une sous-chaîne dans une chaîne.

`index` produit une erreur si le caractère n'est pas trouvé, `find` renvoie `-1`.

```python
>>> 'hello world'.index('o')
4
>>> 'hello world'.find('h')
0
>>> 'hello world'.index('world')
6
>>> 'hello world'.find('world')
6
>>> 'hello'.index('w')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found
>>> 'hello'.find('w')
-1
```

Il est possible de compter le nombre d'occurrences d'un caractère (ou d'une sous-chaîne) avec la méthode `count`.

```python
>>> 'hello world'.count('o')
2
```

On peut tester spécifiquement si une chaîne commence ou termine par une autre avec les méthodes `startswith` et `endswith`.
Ces méthodes renvoient un booléen.

```python
>>> 'hello world'.startswith('hello')
True
>>> 'hello world'.endswith('hello')
False
>>> 'hello world'.startswith('world')
False
>>> 'hello world'.endswith('world')
True
```

Différents tests sont possibles sur les chaînes de caractères pour savoir si elles sont composées de caractères alphanumériques (`isalnum`), alphabétiques (`isalpha`), numériques (`isdigit`) et d'autres encore.

```python
>>> 'salut123'.isalnum()
True
>>> 'salut 123'.isalnum()
False
>>> 'salut'.isalpha()
True
>>> 'salut123'.isalpha()
False
>>> '123'.isdigit()
True
```

#### Méthodes avancées

* Méthodes plus avancée : `str.replace`, `str.split`, `str.join`

La méthode `replace` permet de renvoyer une copie de la chaîne en remplaçant un caratère (ou une sous-chaîne) par un autre.

```python
>>> 'hello world'.replace('o', 'a')
'hella warld'
>>> 'hello world'.replace('ll', 'xx')
'hexxo world'
>>> 'hello world'.replace('ll', '')
'heo world'
```

On peut découper une chaîne de caractères vers une liste de chaînes à partir d'un séparateur avec la méthode `split`.
Par défaut, le séparateur est l'espace.

```python
>>> 'hello world'.split()
['hello', 'world']
>>> 'abc:def:ghi'.split(':')
['abc', 'def', 'ghi']
```

Enfin, il est possible d'unir les chaînes de caractère d'une liste autour d'un séparateur en utilisant la méthode `join` sur ce séparateur.

```python
>>> ':'.join(['abc', 'def', 'ghi'])
'abc:def:ghi'
```
