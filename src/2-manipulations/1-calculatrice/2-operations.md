### Autres opérateurs

L'opérateur de division (`/`) entre deux nombres calcule une division décimale et renvoie un nombre flottant, mais ce n'est pas la seule opération de division possible.  
En effet, Python permet aussi de réaliser une division euclidienne (ou division entière) avec les opérateurs `//` et `%`, calculant respectivement le quotient et le reste de la division.

Souvenez-vous : cela correspond à la division posée que l'on apprenait à l'école où à partir du dividende et du diviseur, par multiplications et soustractions successives, on trouvait ce quotient et ce reste (indivisible).

![Division euclidienne](img/division.png)

```pycon
>>> 13 // 5
2
>>> 13 % 5
3
```

On peut vérifier notre résutlat en multipliant le quotient par le diviseur et en lui ajoutant le reste.

```pycon
>>> 2 * 5 + 3
13
```

Ces opérations renvoient des nombres entiers quand elles sont appliquées à des nombres entiers.

Une autre opération mathématique courante est l'exponentiation, autrement dit la mise en puissance.
Cette opération se note `**`, avec le nombre à gauche et la puissance à droite.

```pycon
>>> 5 ** 2 # 5 à la puissance 2 soit 5 au carré
25
>>> 1.5 ** 3 # 1.5 au cube
3.375
```

Et pour les connaisseurs il est aussi possible d'utiliser des puissances flottantes, comme `0.5` pour calculer une racine carrée.

```pycon
>>> 2 ** 0.5
1.4142135623730951
```

#### Priorités des opérateurs

Comme nous l'avons vu, les opérateurs ont chacun leur priorité, et celle-ci peut être changée à l'aide de parenthèses.  
Ainsi, l'exponentiation est prioritaire sur la multiplication et la division, elles-mêmes prioritaires sur l'addition et la soustraction.

+--------------------------------+
| -> Priorité des opérateurs <-  |
+----------+---------------------+
| Priorité |      Opérateur      |
+==========+=====================+
|        1 | `(...)`             |
+----------+---------------------+
|        2 | `**`                |
+----------+---------------------+
|        3 | `*`, `/`, `//`, `%` |
+----------+---------------------+
|        4 | `+`, `-`            |
+----------+---------------------+

Et chaque opérateur a aussi ses propres règles d'associativité.
Ce sont des règles qui indiquent si, pour des opérations de même priorité, elles doivent s'exécuter de gauche à droite ou de droite à gauche.

Si elles importent peu pour l'addition et la multiplication (`(1+2)+3` et `1+(2+3)` ont la même valeur, de même pour `(2*3)*4` et `2*(3*4)`), elles le sont pour les autres opérations.

Les opérations de priorités 3 et 4 (addition, soustraction, mutliplication, divisions) sont toutes associatives à gauche, c'est-à-dire que les opérations de gauche sont exécutées en priorité, de façon à ce que `1 - 2 + 3` soit égal à `(1-2) + 3`.

```pycon
>>> 1 - 2 + 3
2
>>> (1 - 2) + 3
2
>>> 1 - (2 + 3)
-4
>>>
>>> 1 / 2 / 3
0.16666666666666666
>>> (1 / 2) / 3
0.16666666666666666
>>> 1 / (2 / 3)
1.5
>>>
>>> 1 / 2 * 3
1.5
>>> (1 / 2) * 3
1.5
>>> 1 / (2 * 3)
0.16666666666666666
```

À l'inverse, l'opération d'exponentiation (`**`) st associative à droite, donc les opérations sont exécutées de drotie à gauche.

```pycon
>>> 2 ** 3 ** 4
2417851639229258349412352
>>> 2 ** (3 ** 4)
2417851639229258349412352
>>> (2 ** 3) ** 4
4096
```
