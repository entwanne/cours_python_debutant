### Conversions de types

Comme indiqué, `input` renvoie toujours une chaîne de caractères.
Comment faire alors pour demander à l'utilisateur un nombre afin de l'utiliser dans un calcul ?

Chaque type peut en fait être vu comme une fonction permettant de convertir une valeur vers ce type.
Ainsi `int` permet de convertir en nombre entier, `float` en nombre flottant et `str` en chaîne de caractères.

```python
>>> int(4.2)
4
>>> float(4)
4.0
>>> str(4)
'4'
>>> int('10')
10
```

On voit dans ce dernier exemple que `'10'` et `10` sont des valeurs de types différents, la première est une chaîne de caractères et la seconde un nombre.

Pour traiter une entrée de l'utilisateur comme un nombre, il convient donc de convertir en `int` le retour d'`input`.

```python
>>> n = int(input('Choisis un nombre : '))
Choisis un nombre : 5
>>> print('Le double de', n, 'vaut', n * 2)
Le double de 5 vaut 10
```
