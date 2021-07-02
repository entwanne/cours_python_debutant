### Une étiquette sur une valeur

Lorsque nous entrons une expression dans l'interpréteur interactif, sa valeur est calculée puis affichée dans le terminal.
Mais après cela elle est perdue.
Pourtant il pourrait nous être utile de conserver un résultat, afin de le réutiliser par la suite dans d'autres calculs.

Par exemple, dans un jeu, on aimerait pouvoir conserver le nombre de points de vie d'un joueur, pour l'utiliser dans le calcul des dégâts ou pour le modifier.

C'est là qu'interviennent les variables, qui vont nous permettre de stocker ces résultats.
Une variable, c'est juste un nom que l'on associe à une valeur, afin d'indiquer à Python de la conserver en mémoire (de ne pas l'effacer) mais aussi de pouvoir la retrouver (grâce à son nom).

On peut voir la variable comme une simple étiquette qui sera collée sur notre valeur pour indiquer comment elle se nomme.

En Python, on assigne une variable sur une valeur à l'aide de l'opérateur `=`.
À gauche on écrit le nom de la variable, une suite de lettres sans espace.
La valeur peut être n'importe quelle expression comme vu précédemment.

```python
>>> result = round(8 / 3) + 2
```

On voit que l'interpréteur ne nous affiche rien cette fois-ci, parce que le résultat a été stocké dans `result`.
Le nom de la variable devient alors une valeur comme une autre, qui peut être utilisé dans différentes expressions.

Dans chaque expression, le nom de variable est évalué par Python et remplacé par sa valeur, permettant donc d'exécuter la suite du calcul.

```python
>>> result
5
>>> result + 1
6
>>> min(result + 2, result * 2)
7
```

Et par extension, il est donc possible de définir une variable à l'aide de la valeur d'une autre variable :

```python
>>> result2 = result - 1
>>> result2
4
```
