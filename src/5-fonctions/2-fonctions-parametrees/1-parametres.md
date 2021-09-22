### Paramètres de fonction

On sait définir et appeler une fonction, mais on obtient toujours la même chose à chaque appel.
Il serait bien de pouvoir faire varier le comportement d'une fonction suivant les valeurs de certaines expressions, et c'est là qu'interviennent les paramètres.

Le paramètre est une variable définie dans la fonction qui recevra une valeur lors de chaque appel. Cette valeur pourra être de tout type, suivant ce qui est fourni en argument.  
Les noms des paramètres sont inscrits lors de la définition de la fonction, entre les parenthèses qui suivent son nom.

```python
def table_multiplication(n):
    for i in range(1, 11):
        print(n, '×', i, '=', n*i)
```

Encore une fois, les paramètres sont des variables et donc suivent les mêmes règles de nomenclature.
S'il y a plusieurs paramètres, ils doivent être séparés par des virgules.

```python
def hello(firstname, lastname):
    print('Hello', firstname, lastname, '!')
```

Lors de l'appel de la fonction, on utilisera les arguments pour donner leurs valeurs aux paramètres.
On précise ainsi les valeurs dans les parenthèses qui suivent le nom de la fonction.

```python
>>> table_multiplication(3)
3 × 1 = 3
3 × 2 = 6
3 × 3 = 9
3 × 4 = 12
3 × 5 = 15
3 × 6 = 18
3 × 7 = 21
3 × 8 = 24
3 × 9 = 27
3 × 10 = 30
>>> table_multiplication(5)
5 × 1 = 5
5 × 2 = 10
5 × 3 = 15
5 × 4 = 20
5 × 5 = 25
5 × 6 = 30
5 × 7 = 35
5 × 8 = 40
5 × 9 = 45
5 × 10 = 50
```

Le comportement est le même pour les fonctions à plusieurs paramètres, les valeurs leurs sont attribuées dans l'ordre des arguments : le premier paramètre prend la valeur du premier argument, etc.  
Chaque argument correspond ainsi à un paramètre (et inversement).

```python
>>> hello('Père', 'Noël')
Hello Père Noël !
>>> hello('Blanche', 'Neige')
Hello Blanche Neige !
```

Une erreur survient s'il n'y a pas assez d'arguments pour compléter tous les paramètres.

```python
>>> hello()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: hello() missing 2 required positional arguments: 'firstname' and 'lastname'
>>> hello('Asterix')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: hello() missing 1 required positional argument: 'lastname'
```

Au contraire, une autre erreur est levée s'il y a trop d'arguments par rapport au nombre de paramètres.

```python
>>> hello('Homer', 'Jay', 'Simpson')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: hello() takes 2 positional arguments but 3 were given
```

Derrière ces exemples simples, il est bien sûr possible d'avoir de vrais comportements qui dépendent des valeurs de nos paramètres.

```python
def print_div(a, b):
    if b == 0:
        print('Division impossible')
    else:
        print(a / b)
```

```python
>>> print_div(5, 2)
2.5
>>> print_div(1, 0)
Division impossible
```
