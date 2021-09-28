### Contrôle du flux

`break` permet donc de stopper la boucle.
Il n'est pas seulement disponible pour les boucles `while`, on peut aussi l'utiliser dans un `for`.

```python
>>> for i in range(10):
...     print(i)
...     if i == 5:
...         break
... 
0
1
2
3
4
5
```

Comme précédemment, la sortie de boucle est immédiate, l'effet ne serait donc pas le même si le `print` était placé après le bloc `if`.

```python
>>> for i in range(10):
...     if i == 5:
...         break
...     print(i)
... 
0
1
2
3
4
```

Il faut savoir que dans le cas de boucles imbriquées, `break` ne se rapporte qu'à la boucle juste au-dessus.
Il n'est pas possible d'influer sur les boucles extérieures.

```python
>>> for x in range(3):
...     for y in range(3):
...         if y == 2:
...             break
...         print(x, y)
... 
0 0
0 1
1 0
1 1
2 0
2 1
```

Mais `break` n'est pas le seul mot-clé de contrôle du flux d'une boucle et je vais maintenant vous parler de `continue`.

`continue` permet aussi de terminer immédiatement l'itération en cours, mais pour passer à la suivante.
Quand un `continue` est rencontré, on est directement conduit à la ligne d'introduction de la boucle et sa condition est réévaluée.

```python
while True:
    value = input('Entrez un nombre: ')
    if not value:
        break
    if not value.isdigit():
        print('Nombre invalide')
        continue
    value = int(value)
    print(f'{value} * 2 = {value * 2}')
```

C'est un mot-clé très utile quand on traite une liste de données et que l'une des valeurs est invalide, on peut alors simplement l'ignorer et passer à la suivante.

```python
values = [1, 2, 3, -1, 4, 5]

total = 0
for value in values:
    if value < 0:
        print('Invalid value', value)
        continue
    total += value
```

On a aussi le mot-clé `else` qui est assez facile à comprendre sur une boucle `while` : il intervient après la boucle si la condition a été évaluée comme fausse.

```python
pv = 50

while pv > 0:
    print(f'Pythachu a {pv} PV')
    pv -= 20
    print('Pythachu perd 20 PV')
else:
    print('Pythachu est KO')
```

Le `else` intervient donc dans tous les cas… sauf si on a quitté la boucle sans réévaluer la condition (qui ne peut donc pas être fausse), c'est-à-dire en utilisant un `break`.  
Ainsi, `else` permet de savoir comment s'est terminée une boucle, si on en est sorti normalement (auquel cas on passe dans le bloc) ou si on l'a interrompue (le bloc n'est pas exécuté).

```python
pv = 50

while pv > 0:
    print(f'Pythachu a {pv} PV')
    degats = input('Nombre de degats : ')
    if not degats.isdigit():
        break
    degats = int(degats)
    pv -= degats
    print(f'Pythachu perd {degats} PV')
else:
    print('Pythachu est KO')
```

`else` est aussi applicable à la boucle `for` en ayant le même effet, il permet de savoir si la boucle est arrivée jusqu'au bout sans être interrompue.

Ainsi, sans `break` le `else` est bien exécuté.

```python
>>> for i in range(5):
...     print(i)
... else:
...     print('end')
... 
0
1
2
3
4
end
```

Avec un `break` il ne l'est pas.

```python
>>> for i in range(5):
...     print(i)
...     if i == 3:
...         break
... else:
...     print('end')
... 
0
1
2
3

```

[[i]]
| Le mot-clé `else` est souvent mal compris -- on pourrait croire qu'on entre dans le `else` uniquement s'il n'y a pas eu d'itérations -- et donc peu recommandé pour lever toute ambiguïté.
