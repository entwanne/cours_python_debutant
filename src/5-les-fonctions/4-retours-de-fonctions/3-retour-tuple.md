### Renvoyer plusieurs valeurs

Comme on vient de le voir, la fonction s'arrête au premier `return` rencontré.
Une fonction renvoie donc toujours une et une seule valeur, celle de l'expression située derrière ce premier `return`.

Mais il existe une astuce pour faire comme si on renvoyait plusieurs valeurs en une fois : en utilisant un tuple contenant ces valeurs.
C'est le cas de la fonction `divmod` de Python, renvoyant à la fois la division et le modulo.

```python
>>> divmod(13, 4)
(3, 1)
```

On pourrait recoder cette fonction comme cela.

```python
def divmod(a, b):
    return (a // b, a % b)
```

Les parenthèses autour des tuples étant facultatives, il est courant de les omettre pour les `return`, ce qui donne vraiment l'impression de renvoyer plusieurs valeurs.

```python
def divmod(a, b):
    return a // b, a % b
```

#### Unpacking

Mais une construction très intéressante en Python à ce propos est l'_unpacking_, qui permet de déstructurer un tuple.
Il s'agit en fait d'utiliser un tuple de variables comme membre de gauche lors d'une assignation, pour assigner les éléments du tuple de droite aux variables de gauche.

```python
>>> (a, b) = (3, 4)
>>> a
3
>>> b
4
```

Encore une fois, les parenthèses sont facultatives, on a donc un semblant d'affectation multiple.

```python
>>> a, b = 3, 4
```

Et bien sûr, cela fonctionne aussi avec les fonctions renvoyant un tuple.

```python
>>> d, m = divmod(13, 4)
>>> d
3
>>> m
1
```

Parfois, certains éléments du tuple ne nous intéressent pas lors de l'unpacking, une convention dans ces cas là est d'utiliser la variable `_` pour affecter les résultats inintéressants.

```python
def compute(x):
    return x, x*2, x*3, x*4
```

```python
>>> _, a, _, b = compute(2)
>>> a
4
>>> b
8
```

Enfin, une propriété amusante de la construction/déconstruction de tuples est qu'elle permet facilement d'échanger les valeurs de deux variables.
En effet, il suffit de construire un tuple avec les valeurs des deux variables puis de le déconstruire vers ces deux mêmes variables en les inversant.

```python
>>> a = 3
>>> b = 5
>>> a, b = b, a
>>> a
5
>>> b
3
```
