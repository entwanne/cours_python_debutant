### Gestion des nombres

On a vite fait de passer sur les nombres car on peut croire que l'on en a fait le tour une fois que l'on a vu les types `int`, `float` et `complex` car ils semblent en effet couvrir toutes les catégories de nombres que l'on connaît.  
Si c'est vrai pour ce qui est des nombres entiers, les types dédiés aux réels et aux complexes sont des approximations.

#### Nombres décimaux

En effet, nous avons vu que les `float` étaient stockés par l'ordinateur sous forme binaire et étaient donc souvent des approximations des nombres décimaux que nous connaissons, ce qui pouvait mener à des erreurs d'arrondis.

```python
>>> 0.1 + 0.1 + 0.1
0.30000000000000004
```

Un autre type existe néanmoins pour représenter de façon précise un nombre décimal, il s'agit du type `Decimal` du module `decimal`.

```python
>>> from decimal import Decimal
>>> Decimal('0.1')
Decimal('0.1')
>>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1')
Decimal('0.3')
```

Un `Decimal` s'instancie avec une chaîne de caractère représentant notre nombre décimal et se comporte ensuite comme n'importe quel nombre : toutes les opérations usuelles peuvent s'y appliquer.

```python
>>> Decimal('1.5') * Decimal('3.7')
Decimal('5.55')
>>> Decimal('-4.2') - Decimal('1.1')
Decimal('-5.3')
```

Les décimaux sont aussi compatibles avec les entiers, une opération entre des nombres des deux renverra toujours un décimal.

```python
>>> Decimal('0.1') + 3
Decimal('3.1')
>>> Decimal('0.1') * 4
Decimal('0.4')
>>> Decimal('0.1') ** 2
Decimal('0.01')
```

[[q]]
| Vous vous demandez pourquoi on instancie un `Decimal` avec une chaîne de caractères plutôt qu'un `float` ?
|
| Il est en fait possible de créer un décimal à partir d'un flottant, mais ce flottant comprenant dès le départ une erreur d'arrondi, celle-ci se répercutera sur le décimal.
|
| ```python
| >>> Decimal(0.1)
| Decimal('0.1000000000000000055511151231257827021181583404541015625')
| ```

On notera par ailleurs qu'il est possible de créer un décimal à partir d'un nombre entier, ce dernier ne comportant pas d'approximation.

```python
>>> Decimal(1) / Decimal(10)
Decimal('0.1')
```

À tout moment, il est possible de converir un décimal en entier ou flottant à l'aide d'un appel à `int` ou `float`.

```python
>>> int(Decimal('1.4') * Decimal('1.5'))
2
>>> float(Decimal('1.4') * Decimal('1.5'))
2.1
```

Les nombres décimaux sont pratiques pour manipuler des valeurs qui ne doivent pas subir d'arrondis involontaires, comme des valeurs monétaires, mais sont performants à manipuler que les flottants qui sont directement gérés par le processeur.

Enfin, les décimaux sont tout de même soumis à une précision limitée qui ne leur permet alors pas de représenter tous les nombres décimaux possibles.  
Avec une précision par défaut de 28 décimales, on remarque ainsi qu'il y a une perte de précision quand il y a un trop gros écart entre le chiffre le plus à gauche et celui le plus à droite, qui se ressent lors des opérations suivantes.

```python
>>> Decimal('1.000000000000000000000000001') * 2
Decimal('2.000000000000000000000000002')
>>> Decimal('1.0000000000000000000000000001') * 2
Decimal('2.000000000000000000000000000')
```

La précision des décimaux peut cependant être connue et réglée à l'aide des fonctions `getcontext` et `setcontext` tel que décrit dans [la documentation du module]().

```python
>>> from decimal import getcontext
>>> ctx = getcontext()
>>> ctx.prec = 30
>>> Decimal('1.0000000000000000000000000001') * 2
Decimal('2.0000000000000000000000000002')
>>> ctx.prec = 1
>>> Decimal('1.01') + Decimal('1.01')
Decimal('2')
```

#### Nombres rationnels

Mais quelle que soit la précision choisie, celle-ci sera toujours finie (pour des raisons de performances), et on ne pourra donc pas représenter un nombre avec une infinité ou un trop grand nombre de décimales.  
On ne peut pas représenter de façon exacte le nombre `1/3` avec un `Decimal`.

En revanche, il existe un autre type pour représenter les nombres rationnels : le type `Fraction` du module `fractions`.

[[i]]
| Pour rappel, un nombre rationnel est un nombre qui peut s'écrire comme le quotient (la fraction) entre deux nombres entiers, tels que `1/3`, `15/10` (1.5) ou encore `8/2` (4).

Un objet `Fraction` s'instancie avec le numérateur et le dénominateur de la fraction et s'utilise ensuite comme n'importe quel nombre.

```python
>>> from fractions import Fraction
>>> Fraction(1, 3) + Fraction(1, 3)
Fraction(2, 3)
>>> Fraction(1, 3) * Fraction(3, 1)
Fraction(1, 1)
```

Les fractions sont elles aussi compatibles avec les entiers, et convertibles en `int` ou `float`.

```python
>>> Fraction(1, 3) * 4
Fraction(4, 3)
>>> int(Fraction(4, 3))
1
>>> float(Fraction(4, 3))
1.3333333333333333
```

Ce type offre donc une précision infinie pour les nombres rationnels, mais avec un certain coût en performances.
Ne l'utilisez donc que si vous avez besoin d'une précision exacte sur vos nombres, comme pour un solveur d'équations.

#### Hiérarchie des nombres

Les types de nombres sont généralement compatibles entre eux : il est possible d'exécuter une opération entre un entier et un flottant, comme entre un rationnel et un complexe.
Mais qu'attendre du résultat d'une telle opération ?

On le sait, une opération entre un entier et un flottant renvoie un flottant, car c'est lui qui est le plus à même de stocker le résultat.
En effet, `2 * 3.4` ne pourra pas être représenté dans un entier.

Il existe en fait une hiéarchie entre les types numériques qui définit quel type doit être renvoyé lors d'une telle opération.
Il s'agira toujours du type le plus haut dans la hiérarchie.

Cette hiérarchie reprend les notions d'ensembles de nombres en mathématiques : il y a les nombres complexes tout en haut, puis les réels, les rationnels, les relatifs et enfin les entiers naturels.  
En Python, les complexes sont représentés par le type `complex`, les réels par `float`, les rationnels par `fractions.Fraction`, et les entiers relatifs et naturels par `int`.

Cela explique qu'une opération entre une fraction et un complexe renverra toujours un complexe.

```python
>>> Fraction(1, 3) + 2j
(0.3333333333333333+2j)
```

Mais ce ne sont pas les seuls types de nombres que vous pourriez être amenés à manipuler, et certaines bibliothèques pourraient venir avec leurs propres types.  
Pour autant, ces types se conformeraient à la hiérarchie présentée au-dessus car ils y feraient référence en utilisant les types abstraits (`Number`, `Complex`, `Real`, `Rational`, `Integral`) définis dans le module `numbers`.

Les types abstraits ainsi définis permettent de savoir à quelle classe appartient à un nombre, à l'aide d'appels à `isinstance`.

```python
>>> import numbers
>>> isinstance(4, numbers.Integral) # Les int sont des entiers
True
>>> isinstance(4, numbers.Real) # Mais ce sont aussi des réels
True
>>> isinstance(4, numbers.Number) # Ou tout simplement des nombres au sens large
True
>>> isinstance(4.2, numbers.Real) # Les flottants sont des réels
True
>>> isinstance(4.2, numbers.Rational) # Mais ne sont pas des rationnels
False
>>> isinstance(Fraction(1, 3), numbers.Rational) # Contrairement aux fractions
True
```

Les décimaux sont un cas un peu à part car ils ne s'inscrivent pas dans la hiérarchie, ils se situent quelque part entre les entiers et les rationnels. Aussi, les décimaux ne sont pas considérés comme des instances de `numbers.Real` ou `numbers.Rational`.

```python
>>> isinstance(Decimal('0.1'), numbers.Number)
True
>>> isinstance(Decimal('0.1'), numbers.Real)
False
>>> isinstance(Decimal('0.1'), numbers.Rational)
False
```

Cela implique que les décimaux ne sont pas compatibles avec les autres types de la hiérarchie, et ne le sont en fait qu'avec les entiers.

#### Biblitohèques mathématiques

On a vu qu'il existait en Python le module `math` qui regroupe l'essentiel des fonctions mathématiques sur les nombres réels.
On le sait moins, mais il existe aussi un module `cmath` pour des fonctions équivalentes dans le domaine des complexes.

```python
>>> import math
>>> math.sqrt(2) # Racine carrée de 2
1.4142135623730951
>>> math.sqrt(-1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: math domain error
>>> import cmath
>>> cmath.sqrt(2)
(1.4142135623730951+0j)
>>> cmath.sqrt(-1)
1j
```

Le module étend donc le domaine de définition de certaines fonctions de `math` pour permettre de les appliquer à des nombres complexes. C'est le cas des fonctions trigonométriques ou exponentielles par exemple.

```python
>>> cmath.cos(1+2j)
(2.0327230070196656-3.0518977991518j)
>>> cmath.exp(1j * cmath.pi)
(-1+1.2246467991473532e-16j)
```

Mais à propos de nombres, on trouve aussi le module `statistics` qui comme son nom l'indique fournit des outils de statistiques.
On trouvera ainsi des fonctions pour calculer la moyen (`mean`), la médiane (`median`), la variance (`variance`) ou encore l'écart type (`stdev`) d'une série de données.

```python
>>> data = [1, 2, 2, 3, 4, 5, 5, 6, 7]
>>> statistics.mean(data)
3.888888888888889
>>> statistics.median(data)
4
>>> statistics.variance(data)
4.111111111111111
>>> statistics.stdev(data)
2.0275875100994063
```

Pour plus d'informations sur les outils fournis par ce module, je vous invite à vous reporter sur [sa documentation]().
