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

* `else` pour savoir comment s'est terminée une boucle (peu utilisé)

* `continue` et `else` aussi applicables aux boucles `for`
