### Tableau des opérateurs

#### Opérateurs simples (expressions)

En plus des mots-clés précédents, on trouve aussi les opérateurs suivants.
Ces opérateurs sont constitués de caractères spéciaux et ne sont donc pas des noms.

+----------+----------+----------+----------+----------+
|   `+`    |   `%`    |   `&`    |   `!=`   |   `:=`   |
+----------+----------+----------+----------+----------+
|   `-`    |   `**`   |   `|`    |   `<`    |   `<<`   |
+----------+----------+----------+----------+----------+
|   `*`    | `x(...)` |   `^`    |   `>`    |   `>>`   |
+----------+----------+----------+----------+----------+
|   `/`    | `x.attr` |   `~`    |   `<=`   |   `@`    |
+----------+----------+----------+----------+----------+
|   `//`   | `x[...]` |   `==`   |   `>=`   |   `,`    |
+----------+----------+----------+----------+----------+

* `+`: Addition / concaténation, ou opérateur unaire positif.
  ```python
  >>> 3 + 5
  8
  >>> 'abc' + 'def'
  'abcdef'
  >>> +42
  42
  ```
* `-`: Soustraction / différence ou opérateur unaire négatif.
  ```python
  >>> 3 - 5
  -2
  >>> -42
  -42
  ```
  ```python
  >>> {1, 2, 3} - {2, 3, 4}
  {1}
  ```
* `*`: Multiplication, concaténation multiplicative, ou opérateur _splat_.
  ```python
  >>> 3 * 5
  15
  >>> 'cou' * 2
  'coucou'
  >>> [3] * 4
  [3, 3, 3, 3]
  ```
  ```python
  func(*[1, 2, 3])
  ```
* `/`: Division ou séparateur de chemins.
  ```python
  >>> 3 / 5
  0.6
  ```
  ```python
  >>> Path('a') / Path('b')
  PosixPath('a/b')
  ```
* `//`: Division entière (euclidienne).
  ```python
  >>> 10 // 3
  3
  ```
* `%`: Modulo (reste de division) ou formatage de chaîne.
  ```python
  >>> 10 % 3
  1
  ```
  ```python
  >>> 'salut %s' % 'toto'
  'salut toto'
  ```
* `**`: Exponentiation (puissance) ou _double-splat_
  ```python
  >>> 5 ** 3
  125
  ```
  ```python
  func(**{'arg': 42})
  ```
* `x(...)`: Appel de fonction (ou _callable_), instanciation de type.
  ```python
  >>> round(3.5)
  4
  >>> list()
  []
  ```
* `x.attr`: Accès à un attribut.
  ```python
  >>> Path('a/b').name
  'b'
  ```
* `x[...]`: Accès à un élément. Permet aussi le _slicing_.
  ```python
  >>> squares[3]
  9
  >>> squares[4:8]
  [16, 25, 36, 49]
  ```
* `&`: Conjonction (_ET_) bit-à-bit ou intersection d'ensembles.
  ```python
  >>> bin(0b101 & 0b110)
  '0b100'
  ```
  ```python
  >>> {1, 2, 3} & {2, 3, 4}
  {2, 3}
  ```
* `|`: Disjonction (_OU_) bit-à-bit ou union d'ensembles.
  ```python
  >>> bin(0b101 | 0b110)
  '0b111'
  ```
  ```python
  >>> {1, 2, 3} | {2, 3, 4}
  {1, 2, 3, 4}
  ```
* `^`: _XOR_ bit-à-bit ou différence symétrique d'ensembles.
  ```python
  >>> bin(0b101 ^ 0b110)
  '0b11'
  ```
  ```python
  >>> {1, 2, 3} ^ {2, 3, 4}
  {1, 4}
  ```
* `~`: Négation (_NON_) bit-à-bit, opérateur unaire.
  ```python
  >>> bin(~0b101)
  '-0b110'
  ```
* `==`: Test d'égalité.
  ```python
  >>> 5 == 4 + 1
  True
  ```
* `!=`: Test de différence.
  ```python
  >>> 5 != 4 + 1
  False
  ```
* `<`: Test d'infériorité stricte.
  ```python
  >>> 3 < 5
  True
  ```
* `>`: Test de supériorité stricte.
  ```python
  >>> 3 > 5
  False
  ```
* `<=`: Test d'infériorité.
  ```python
  >>> 3 <= 5
  True
  >>> 3 <= 3
  True
  ```
* `>=`: Test de supériorité.
  ```python
  >>> 3 >= 5
  False
  >>> 3 >= 3
  True
  ```
* `:=`: Expression d'assignation[^python_38].
  ```python
  >>> if x:= 5:
  ...     print(x+1)
  ...
  6
  ```
* `<<`: Décalage de bits à gauche.
  ```python
  >>> bin(0b101 << 2)
  '0b10100'
  ```
* `>>`: Décalage de bits à droite.
  ```python
  >>> bin(0b10101 >> 2)
  '0b101'
  ```
* `@`: Multiplication matricielle[^python_35][^non_aborde].
* `,`: La virgule est un peu à part, c'est un séparateur (arguments, listes, etc.) mais aussi l'opérateur qui permet de créer des tuples.
  ```python
  >>> 1,
  (1,)
  >>> 3, 4, 5
  (3, 4, 5)
  ```

[^python_35]: Introduit en [Python 3.5](https://zestedesavoir.com/articles/175/sortie-de-python-3-5/).
[^python_38]: Introduit en [Python 3.8](https://docs.python.org/fr/3/whatsnew/3.8.html).
[^non_aborde]: Non abordé dans ce cours.

#### Opérateurs d'assignation

+-------+-------+-------+-------+-------+
|  `=`  | `*=`  | `%=`  | `|=`  | `>>=` |
+-------+-------+-------+-------+-------+
| `+=`  | `/=`  | `**=` | `^=`  | `@=`  |
+-------+-------+-------+-------+-------+
| `-=`  | `//=` | `&=`  | `<<=` |       |
+-------+-------+-------+-------+-------+

Les opérations d'assignation suivent toutes le même principe, `var = expression`.

```python
>>> x = 42
>>> x
42
```

L'opérateur utilisé applique simplement l'opération cible (`+` pour `+=` etc.) entre la variable initiale et l'expression.

```python
>>> x += 2  # x = x + 2
>>> x
44
>>> x //= 3  # x = x // 3
>>> x
14
```

[[a]]
| Attention, certaines assignations peuvent s'opérer en-place sur l'objet.
| `a += b` n'est donc pas strictement équivalent à `a = a + b`.
|
| ```python
| >>> values = [1, 2]
| >>> copy = values
| >>> values += [3]
| >>> copy
| [1, 2, 3]
| ```

Les opérations d'assignation permettent aussi d'assigner les éléments des conteneurs.

```python
values[0] = 42
dic[key] = value
```
