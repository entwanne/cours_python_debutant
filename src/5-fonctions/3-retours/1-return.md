### Renvoyer une valeur avec return

Pour l'instant nos fonctions s'occupent d'afficher des valeurs mais ne renvoient rien (ou plutôt renvoient `None`).

```python
def addition(a, b):
    print(a + b)
```

C'est-à-dire que `addition(1, 2)` est une expression qui s'évalue à `None`, malgré le texte affiché par la fonction.

```python
>>> x = addition(1, 2)
3
>>> print(x)
None
```

On ne peut donc rien faire de ce résultat qui a été affiché par la fonction.
Afin d'extraire le résultat, il va nous falloir le renvoyer depuis notre fonction, ce qui se fait avec le mot-clé `return`.

`return` est suivi d'une expression vers laquelle sera évalué l'appel de la fonction.

```python
def addition(a, b):
    return a + b
```

On remarque que maintenant, l'appel à la fonction n'affiche plus rien (il n'y a plus de `print`).

```python
>>> x = addition(1, 2)
```

En revanche, on récupère bien le résultat calculé dans la variable `x`.

```python
>>> print(x)
3
```

`x = addition(1, 2)` est grossièrement équivalent à `x = 1 + 2`, l'expression `addition(1, 2)` valant `1 + 2`.

Étant une expression à part entière, il est possible de l'utiliser comme valeur dans d'autres expressions :

```python
>>> addition(addition(1, 1), addition(addition(1, 1), 1))
5
```
