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

* `else` pour savoir comment s'est terminée une boucle (peu utilisé)

* `continue` et `else` aussi applicables aux boucles `for`
