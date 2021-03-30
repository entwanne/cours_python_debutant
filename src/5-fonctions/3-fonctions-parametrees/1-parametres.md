### Paramètres de fonction

On sait définir et appeler une fonction, mais on obtient toujours la même chose à chaque appel.
Il serait bien de pouvoir faire varier le comportement d'une fonction suivant les valeurs de certaines expressions, et c'est là qu'interviennent les paramètres.

Le paramètre est une variable définie dans la fonction qui recevra une valeur lors de chaque appel.
Les noms des paramètres sont inscrits lors de la définition de la fonction, entre les parenthèses qui suivent son nom.

```python
def hello(name):
    print('Hello', name)
```

Encore une fois, les paramètres sont des variables et donc suivent les mêmes règles de nomenclature.

Lors de l'appel de la fonction, on utilisera les arguments pour donner leurs valeurs aux paramètres.
On précise ainsi les valeurs dans les parenthèses qui suivent le nom de la fonction.

```python
>>> hello('John')
Hello John
>>> hello('Jude')
Hello Jude
>>> hello('World')
Hello World
```

Le comportement est le même pour les fonctions à plusieurs paramètres, les valeurs leurs sont attribuées dans l'ordre des arguments : le premier paramètre prend la valeur du premier argument, etc.  
Chaque argument correspond ainsi à un paramètre (et inversement).

```python
def a(b, c):
    print(b, c)
```

```python
>>> a(1, 2)
1 2
```

Une erreur survient s'il n'y a pas assez d'arguments pour compléter tous les paramètres.

```python
>>> a()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: a() missing 2 required positional arguments: 'b' and 'c'
>>> a(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: a() missing 1 required positional argument: 'c'
```

Au contraire, une autre erreur est levée s'il y a trop d'arguments par rapport au nombre de paramètres.

```python
>>> a(1, 2, 3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: a() takes 2 positional arguments but 3 were given
```

Derrière ces exemples simples, il est bien sûr possible d'avoir de vraies comportements qui dépendent des valeurs de nos paramètres.

```python
def print_div(a, b):
    if b == 0:
        print('Division impossible')
    else:
        print(a / b)
```
