### Une étiquette sur une valeur

En effet, ce sont les variables qui vont nous permettre de stocker nos résultats de calculs.
Une variable, c'est juste un nom que l'on associe à une valeur, afin d'indiquer à Python de la conserver en mémoire (de ne pas l'effacer) mais aussi de pouvoir la retrouver (grâce à son nom).

On peut voir la variable comme une simple étiquette qui sera collée sur notre valeur pour indiquer comment elle se nomme.

En Python, on assigne une variable sur une valeur à l'aide de l'opérateur `=`.
À gauche, on écrit le nom de la variable, une suite de lettres sans espace.
La valeur peut être n'importe quelle expression comme vu précédemment.

```pycon
>>> result = round(8 / 3) + 2
```

On voit que l'interpréteur ne nous affiche rien cette fois-ci, parce que le résultat a été stocké dans `result`.
`result` est une variable qui pointe non pas vers l'expression `round(8 / 3) + 2` mais vers le résultat de cette opération, soit le nombre 5.

![Une variable est une étiquette sur une valeur.](img/variable_assign.png)

Si l'interpréteur ne nous affiche rien, c'est aussi parce que `result = round(8 / 3) + 2` n'est pas une expression.
Cette ligne définit une variable mais ne possède pas de valeur à proprement parler. On ne peut pas l'utiliser au sein d'une autre expression.
On dit simplement qu'il s'agit d'une instruction.

Le nom de la variable définie devient quant à lui une valeur comme une autre, qui peut être utilisée dans différentes opérations.  
Dans chaque expression, le nom de variable est évalué par Python et remplacé par sa valeur, permettant donc d'exécuter la suite du calcul.

```pycon
>>> result
5
>>> result + 1
6
>>> min(result + 2, result * 2)
7
```

Et par extension, il est donc possible de définir une variable à l'aide de la valeur d'une autre variable :

```pycon
>>> result2 = result - 1
>>> result2
4
```
