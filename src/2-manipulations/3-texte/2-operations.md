### Opérations sur les chaînes

Une chaîne de caractères est une valeur à part entière, et comme toute valeur elle a certaines opérations qui lui sont applicables.

Pour commencer, la fonction `len` est une fonction de base de Python, qui peut être appelée avec une chaîne de caractères en argument.
La fonction renverra un nombre entier représentant la longueur de la chaîne, c'est-à-dire le nombre de caractères qu'elle contient.

```python
>>> len('Hello')
5
>>> len('Hello World!')
12
```

L'opérateur d'addition (`+`) que nous avons vu pour les nombres existe aussi pour le texte, mais il a un sens un peu différent.
On ne va en effet pas additionner deux chaînes, mais les concaténer : les mettre l'une à la suite de l'autre.

```python
>>> 'Hello' + ' World' + '!'
'Hello World!'
```

Nous retrouvons aussi l'opérateur `*` pour représenter un autre type de concaténation, la répétition d'une chaîne un certain nombre de fois.

```python
>>> 'to' * 3
'tototo'
```

Toutes les facilités vues jusqu'ici restent valables.

```python
>>> msg = 'Salut '
>>> msg += 'tom'*2 + ' et ' + 'na'*2
>>> print(msg)
Salut tomtom et nana
```

Mais nous découvrons aussi d'autres opérateurs que nous n'avions pas vus jusque là.
Les chaînes de caractères formant un tableau d'éléments, il est possible d'accéder de façon directe à chacun de ces éléments.

Cela se fait à l'aide de crochets (`[ ]`) en indiquant entre-eux la position du caractère voulu.
Il faut savoir que généralement en informatique on compte à partir de 0.
Le premier caractère d'une chaîne se trouve donc à la position 0 de la séquence, le deuxième caractère à la position 1, etc. jusqu'au n-ième caractère à la position *n-1*.

```python
>>> msg = 'Salut'
>>> msg[0]
'S'
>>> msg[0] + msg[1] + msg[2] + msg[3] + msg[4]
'Salut'
```

La valeur `'S'` renvoyée par `msg[0]` est un caractère, c'est-à-dire en Python une chaîne de taille 1.

On peut ainsi accéder à n'importe quel caractère de la chaîne à partir de son index, s'il est compris dans les bornes (de `0` à `len(msg)-1`).

```python
>>> msg[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
```

On observe qu'au-delà on obtient une erreur `IndexError`, soit un index invalide.
Il est en revanche possible d'utiliser des index négatifs pour prendre la chaîne en sens inverse : -1 correspond au dernier caractère, -2 à l'avant dernier, jusqu'à `-len(msg)` pour le premier.
Chaque caractère a ainsi deux positions possibles dans la chaîne.

```python
>>> msg[-1]
't'
>>> msg[-3]
'l'
>>> msg[-5]
'S'
```
