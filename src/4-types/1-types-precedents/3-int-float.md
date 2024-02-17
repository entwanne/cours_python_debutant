### Nombres

Nous avons rencontré deux types pour représenter les nombres : les entiers et les flottants (nombres à virgule).
Les premiers ne représentent que des nombres entiers, avec une précision infinie (il n'y a pas de limite), les seconds représentent des nombres réels mais avec une précision limitée.

#### Conversions

On peut facilement convertir des valeurs en `int` ou `float` en faisant appel à ces types comme à des fonctions.

```pycon
>>> int('42')
42
>>> float('4.5')
4.5
>>> int(4.5)
4
>>> int(float('4.5'))
4
```

Toute valeur n'est pas convertible en nombre, des erreurs peuvent donc survenir si l'argument est invalide.

```pycon
>>> int('4.5') # 4.5 n'est pas un nombre entier valide
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '4.5'
```

#### Opérations

Beaucoup d'opérations sont applicables sur les nombres, et les deux types sont compatibles entre eux.
On retrouve d'abord les opérations arithmétiques : addition (`+`), soustraction (`-`), multiplication (`*`), division (`/`), division euclidienne (`//`), modulo (`%`) et puissance (`**`).

```pycon
>>> 1 + 5
6
>>> 4.3 - 2
2.3
>>> 1.5 * 4
6.0
>>> 7 / 5
1.4
>>> 7 // 5
1
>>> 7 % 5
2
>>> 2 ** 3
8
```

On a aussi tous les opérateurs de comparaison, qui renvoient des valeurs booléennes : l'égalité (`==`), la différence (`!=`), l'infériorité (`<`, `<=`) et la supériorité (`>`, `>=`).

```pycon
>>> 3 == 3.0
True
>>> 1 != 2
True
>>> 3 < 4.0
True
>>> 4 > 4.0
False
>>> 4 >= 4.0
True
```

Et d'autres opérateurs ne sont accessibles que via des fonctions : la valeur absolue (`abs`), l'arrondi (`round`), le minimum (`min`), le maximum (`max`) et la division euclidienne avec reste (`divmod`).

```pycon
>>> abs(-1.2)
1.2
>>> round(1/3, 4)
0.3333
>>> min(1.5, -6, 3.7)
-6
>>> max(1.5, -6, 3.7)
3.7
>>> divmod(7, 5)
(1, 2)
```

#### Représentations des entiers

On sait que l'on peut convertir un nombre en chaîne de caractères en appelant `str`, qui utilise la représentation décimale (en base 10), mais d'autres représentations sont possibles pour les entiers.
`bin` permet d'avoir la représentation binaire (base 2), `oct` pour l'octale (base 8) et `hex` pour l'hexadécimale (base 16).

```pycon
>>> bin(42)
'0b101010'
>>> oct(42)
'0o52'
>>> hex(42)
'0x2a'
```

Ces représentations sont d'ailleurs parfaitement valides pour être entrées en tant que nombre dans l'interpréteur, qui les analysera donc selon leur préfixe (`0b`, `0o` ou `0x`).

```pycon
>>> 0b101010
42
>>> 0o52
42
>>> 0x2a
42
```

Puisqu'on en est à parler des bases, tout nombre peut ainsi être considéré comme une succession de bits (tel que la représentation renvoyée par `bin`).
Un bit étant soit 0 soit 1, on peut même parler de tableau de booléens.

Différents opérateurs -- à rapprocher des opérateurs booléens -- tirent parti de cette particularité pour offrir des opérations bit-à-bit sur les nombres.

Ainsi, l'opérateur ET (`&`) calcule le nombre résultat de l'application d'un ET binaire (`and`) entre chaque bit de deux nombres.

```pycon
>>> bin(0b101010 & 0b111000)
'0b101000'
```

$$
\begin{array}{rcccccc}
    & \color{blue}1 & \color{blue}0 & \color{blue}1 & \color{blue}0 & \color{blue}1 & \color{blue}0 \\
 \& & \color{red}1 & \color{red}1 & \color{red}1 & \color{red}0 & \color{red}0 & \color{red}0  \\
    \hline
  = & 1 & \color{blue}0 & 1 & 0 & \color{red}0 & 0
\end{array}
$$

J'utilise ici des représentations binaires pour que le calcul soit plus lisible, mais l'opérateur s'applique simplement sur des entiers et renvoie un entier.

```pycon
>>> 42 & 56
40
```

De la même manière, on a les opérateurs OU-inclusif (`|`) et OU-exclusif/XOR (`^`).

```pycon
>>> bin(0b101010 | 0b111000)
'0b111010'
```

$$
\begin{array}{rcccccc}
       & \color{blue}1 & \color{blue}0 & \color{blue}1 & \color{blue}0 & \color{blue}1 & \color{blue}0 \\
 \vert & \color{red}1 & \color{red}1 & \color{red}1 & \color{red}0 & \color{red}0 & \color{red}0  \\
       \hline
     = & 1 & \color{red}1 & 1 & 0 & \color{blue}1 & 0
\end{array}
$$

```pycon
>>> bin(0b101010 ^ 0b111000)
'0b10010'
```

$$
\begin{array}{rcccccc}
        & \color{blue}1 & \color{blue}0 & \color{blue}1 & \color{blue}0 & \color{blue}1 & \color{blue}0 \\
 \hat{} & \color{red}1 & \color{red}1 & \color{red}1 & \color{red}0 & \color{red}0 & \color{red}0  \\
        \hline
      = & \color{violet}0 & \color{red}1 & \color{violet}0 & 0 & \color{blue}1 & 0
\end{array}
$$

[[i]]
| Notez que le premier zéro n'apparaît pas dans le résultat renvoyé par Python pour le XOR, mais `0b10010` et `0b010010` sont bien deux représentations du même nombre (18).

D'autres opérations bit-à-bit sont encore possibles (`~`, `<<`, `>>`), vous pourrez en apprendre plus sur [cette page dédiée aux opérateurs](https://zestedesavoir.com/tutoriels/2514/un-zeste-de-python/10-annexes/1-glossaire/#3-3-operateurs).

#### Précision des flottants

Les nombres flottants en Python ont une précision limitée, c'est-à-dire qu'ils auront du mal à représenter des nombres trop grands ou avec trop de chiffres après la virgule.

```pycon
>>> 0.10000000000000001
0.1
```

On voit ici que le dernier 1 s'est perdu.
C'est dû au fait que ces nombres sont stockés sur une zone mémoire de taille fixe, et que des arrondis sont nécessaires dans certains cas.  
On peut le voir aussi sur d'autres opérations qui produisent normalement des nombres infinis.

```pycon
>>> 1/3
0.3333333333333333
>>> 7/6
1.1666666666666667
```

Par ailleurs, les nombres y sont stockés en base 2, et certains nombres qui nous paraissent finis (`0.1`) ne le sont pas en binaire (il faut une infinité de chiffres derrière la virgule pour représenter `0.1` en base 2).
C'est pourquoi des arrondis sont effectués sur ces nombres.
Ils ne sont pas toujours visibles, mais ils peuvent apparaître à certains moments et être source de bugs.

```pycon
>>> 0.1 + 0.1 + 0.1
0.30000000000000004
```

En raison de ces arrondis il est plutôt déconseillé de comparer deux flottants avec `==`, puisque cela pourrait amener à un résultat incohérent.
Nous verrons dans la suite du cours comment résoudre ce problème.

```pycon
>>> 0.1 + 0.1 + 0.1 == 0.3
False
```

#### Notation des flottants

`123.456` est la notation habituelle des nombres flottants, mais une autre est possible : la notation scientifique.
Il s'agit de représenter un nombre avec un exposant d'une puissance de 10. Cela aide à écrire les nombres très grands ou très petits.

Par exemple, `3.2e5` est égal à `3.2 * 10**5` soit `320000.0`, et `4e-3` à `4.0 * 10**-3` donc `0.004`

```pycon
>>> 3.2e5
320000.0
>>> 4e-3
0.004
```

Pour certains nombres, trop grands/petits pour être représentés correctement avec la notation habituelle, Python basculera automatiquement en notation scientifique.

```pycon
>>> 9.6 ** 100
1.6870319358849588e+98
>>> 2 / 10000000000
2e-10
```

Enfin, il est aussi possible avec les flottants de représenter les infinis (positif et négatif), mais ils ne sont pas directement accessibles.
On peut accéder à l'infini positif à l'aide de l'expression `float('inf')`.

```pycon
>>> inf = float('inf')
>>> inf
inf
>>> inf + 2
inf
>>> inf * inf
inf
>>> 1 / inf
0.0
```

L'infini sera toujours supérieur à n'importe quel autre nombre.

```pycon
>>> inf > 10**100
True
```

De façon similaire, on retrouve l'infini négatif avec `float('-inf')`.

#### Nombres complexes

[[i]]
| Vous pouvez passer cette section si vous n'êtes pas familiers des nombres complexes, ce n'est pas important pour la suite.

Python embarque aussi nativement les nombres complexes qui sont accessibles via le suffixe `j` pour représenter la partie imaginaire.
Les complexes sont un sur-ensemble des flottants, et les mêmes opérations sont donc applicables sur eux.

```pycon
>>> 1+2j + 4+5j
(5+7j)
>>> 0.5j + 3.2+9.3j
(3.2+9.8j)
>>> (1+2j) * (4+5j)
(-6+13j)
>>> 1j*1j
(-1+0j)
>>> (1+2j) ** 2
(-3+4j)
```

Par ailleurs, on trouve sur ces nombres des attributs `real` et `imag` pour accéder aux parties réelle et imaginaire, et une méthode `conjugate` pour calculer le conjugué.

```pycon
>>> c = 1+2j
>>> c.real
1.0
>>> c.imag
2.0
>>> c.conjugate()
(1-2j)
```

Bien sûr, les nombres complexes ne sont par ordonnables entre eux.

```pycon
>>> 1+2j < 2+1j
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'complex' and 'complex'
```

Enfin, la fonction `abs` (valeur absolue) permet aussi de calculer le module d'un nombre complexe.

```pycon
>>> abs(3+4j)
5.0
```
