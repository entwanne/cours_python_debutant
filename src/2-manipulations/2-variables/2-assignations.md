### Assignations

Comme son nom l'indique, une variable n'est pas fixée dans le temps.
À tout moment, il est possible de la réassigner sur une nouvelle valeur, perdant ainsi la trace de l'ancienne.

```pycon
>>> result = 6 * 7
>>> result
42
>>> result = 9 * 4
>>> result
36
```

![Réassignation de variable.](img/variable_reassign.png)

Mais on peut aussi utiliser une même variable à gauche et à droite de la définition.

```pycon
>>> result = result + 1
```

Il ne faut donc pas voir ici le `=` comme une égalité, mais bien comme une assignation.  
La ligne précédente signifie que l'on prend la valeur actuelle de `result` (36), que l'on lui ajoute 1, et que l'on assigne ce nouveau résultat à la variable `result`.
`result` vaut donc maintenant 37.

Autre exemple avec la réassignation d'une variable x.

```pycon
>>> x = 3
>>> x = x + 2
>>> x
5
```

Les opérations du type `x = x + y` sont d'ailleurs tellement courantes que Python leur a prévu un opérateur d'affectation spécifique : `+=`.  
`x += 1` est ainsi équivalent à `x = x + 1`.
On appelle cette opération une incrémentation, car on ajoute un incrément au nombre actuel.

Et cela ne se limite pas à l'addition mais comprend aussi les autres opérateurs arithémtiques qui bénéficient tous de leur propre opérateur d'affectation : `-=`, `*=`, `/=`, `//=`, `%=` et `**=`.
L'opération de soustraction-assignation (`-=`) s'appelle une décrémentation.

```pycon
>>> x = 0
>>> x -= 8
>>> x *= -11
>>> x //= 4
>>> x **= 3
>>> x %= 10
>>> x
8
```

Une autre propriété intéressante de l'opérateur `=` est qu'il peut être chaîné afin de définir plusieurs variables en même temps.

```pycon
>>> x = y = 10
>>> x
10
>>> y
10
```
