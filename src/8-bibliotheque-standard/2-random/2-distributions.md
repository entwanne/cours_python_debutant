### Distributions

#### Lois de distribution

Voilà pour ce qui est des tirages dit discrets (on a un ensemble de valeurs connues et on veut tirer une valeur dans celles-ci) mais il est aussi possible de tirer des nombres dans des intervalles continus.

Par exemple, très simple, la fonction `random` va renvoyer un nombre flottant entre 0 et 1 (1 étant exclu de l'intervalle).

```pycon
>>> random.random()
0.9294919627802888
>>> random.random()
0.47588843177000617
```

Le tirage de ce nombre est uniforme, grossièrement cela veut dire qu'on a autant de chances de tirer un nombre n'importe où dans l'intervalle.

Une fonction est spécifiquement dédiée au tirage uniforme entre deux nombres flottants, il s'agit de la fonction `uniform`.

```pycon
>>> random.uniform(0, 10)
1.4017486291855232
>>> random.uniform(0, 10)
5.926447309804371
```

Suivant les arrondis, la borne supérieure peut être inclue ou non dans l'intervalle, mais cela a peu d'importance : il est pratiquement impossible de tomber sur ce nombre précis, puisqu'il y en a une infinité[^infini].

[^infini]: Pas exactement puisque la représentation d'un flottant est finie, mais vous comprenez l'idée.

On a l'habitude de présenter une distribution par sa densité de probabilité, la fonction qui montre quelles zones de l'intervalle ont plus de chances d'être sollicitées.  
Dans le cas d'une distribution uniforme, cette densité est constante.

![Densité de probabilité d'une distribution uniforme.](img/random_uniform.png)

D'autres distributions sont possibles pour les tirages de nombres flottants.

Il y a par exemple la distribution triangulaire accessible via la fonction `triangular`, qui prend en argument les deux bornes de l'intervalle.  
On parle de distribution triangulaire car sa densité représente un triangle entre les deux bornes.

![Densité de probabilité d'une distribution triangulaire.](img/random_triangular.png)

Ainsi, les valeurs autour du sommet du triangle auront plus de probabilité d'être tirées que celles aux extrémités.

```pycon
>>> random.triangular(0, 10)
4.0479535343895865
```

Un troisième argument optionnel, le mode, permet de spécifier la valeur du sommet du triangle (par défaut il s'agit du milieu de l'intervalle, 5 dans notre exemple).

```pycon
>>> random.triangular(0, 10, 2)
2.4400405218007473
```

On trouve aussi la distribution normale, qui représente la distribution naturelle autour d'une moyenne avec un certain écart type.
La moyenne et l'écart type sont les deux arguments de la fonction `normalvariate`.

```pycon
>>> random.normalvariate(5, 1)
4.655500829738334
>>> random.normalvariate(5, 1)
5.808402224132684
```

Sa densité de probabilité prend la forme d'une cloche centrée autour de la moyenne. Plus on s'éloigne de la moyenne, moins les valeurs ont de chance d'être tirées.

![Densité de probabilité d'une distribution normale.](img/random_normal.png)

#### Pondération

Un autre point important à propos des tirages aléatoires concerne la pondération.
En effet, les tirages discrets que nous avons effectués jusqu'ici étaient tous uniformes : chaque valeur avait autant de chance que les autres de tomber.

Avec `random.randint(1, 6)`, chaque valeur a une probabilité de $\frac{1}{6}$ d'être tirée.
On peut d'ailleurs le vérifier en simulant un très grand nombre de tirages et en calculant le nombre d'occurrences de chaque valeur pour en déterminer la fréquence.  
Si le tirage est bien uniforme, chaque valeur est censée être équitablement présente.

```pycon
>>> from collections import Counter
>>> occurrences = Counter()
>>> N = 10000
>>> for _ in range(N):
...     val = random.randint(1, 6)
...     occurrences[val] += 1
...
>>> for val, occ in sorted(occurrences.items()): # sorted pour afficher selon l'ordre des clés
...     print(f'{val}: {occ / N}')
...
1: 0.1649
2: 0.1638
3: 0.1687
4: 0.1695
5: 0.1654
6: 0.1677
```

On voit que chaque fréquence est proche de 0,1666.

![Distribution uniforme des valeurs.](img/random_uniform_weights.png)

Mais parfois on souhaiterait pouvoir pondérer notre tirage, affecter un poids différent à chaque valeur.
Une manière de faire serait d'utiliser un `choice` et d'y mettre plusieurs fois les valeurs selon l'importance que l'on souhaite leur donner.

```python
choices = [1, 2, 3, 4, 4, 5, 5, 6, 6, 6]
```

Ici, 6 a une probabilité de 0,3 ($\frac{3}{10}$) d'être tiré, 4 et 5 en ont une de 0,2 et les autres sont de 0,1.

```pycon
>>> occurrences = Counter()
>>> for _ in range(N):
...     val = random.choice(choices)
...     occurrences[val] += 1
...
>>> for val, occ in sorted(occurrences.items()):
...     print(f'{val}: {occ / N}')
...
1: 0.0982
2: 0.1021
3: 0.0968
4: 0.1982
5: 0.1985
6: 0.3062
```

Mais j'ai choisi un exemple facile, il est généralement assez compliqué de déterminer combien de valeurs on souhaite metre en fonction de la probabilité que l'on veut leur donner, et cela peut amener à des listes de valeurs assez grandes.

Heureusement, Python a pensé à nous et propose une fonction qui prend directement en compte la pondération, il s'agit de la fonction `random.choices`.

Par défaut la fonction est sembable à `choice`, attribuant le même poids à chaque valeur, sauf qu'elle renvoie la valeur tirée sous forme d'une liste.

```pycon
>>> random.choices(range(1, 7))
[6]
```

C'est parce qu'il est possible de lui demander de tirer plusieurs valeurs (avec remise) en utilisant le paramètre `k`.

```pycon
>>> random.choices(range(1, 7), k=3)
[1, 1, 6]
```

Mais l'intérêt de cette fonction se situe dans son deuxième argument qui est une liste de poids, correspondant donc aux valeurs données en premier argument.
Notre tirage de tout à l'heure pourrait se réécrire de la façon suivante :

```pycon
>>> weights = [0.1, 0.1, 0.1, 0.2, 0.2, 0.3]
>>> random.choices(range(1, 7), weights)
[5]
```

![Pondération des valeurs.](img/random_weights.png)

Encore une fois, on peut le vérifier en calculant les fréquences d'apparition.

```pycon
>>> occurrences = Counter()
>>> for _ in range(N):
...     val = random.choices(range(1, 7), weights)[0] # Attention, choices renvoie une liste
...     occurrences[val] += 1
... 
>>> for val, occ in sorted(occurrences.items()):
...     print(f'{val}: {occ / N}')
... 
1: 0.0995
2: 0.1008
3: 0.1008
4: 0.2018
5: 0.2
6: 0.2971
```

J'ai utilisé ici des fréquences comme poids, mais il est possible d'utiliser n'importe quels nombres, Python calculera la fréquence en fonction de la somme des poids.

```pycon
>>> weights = [1, 1, 1, 2, 2, 3]
>>> random.choices(range(1, 7), weights)
[2]
```

Enfin, il est aussi possible d'utiliser des poids cumulés pour le tirage.
Dans ce cas, la fonction prend un paramètre `cum_weights` définissant ces poids.

Les poids cumulés peuvent être vus comme une réglette graduée entre 0 et 1, chaque valeur se voyant attribuer une graduation.
Un nombre est tiré entre 0 et 1, et c'est la valeur située juste à droite de cette graduation qui sera sélectionné.

Notre tirage précédent peut alors s'écrire comme suit.

```pycon
>>> cum_weights = [0.1, 0.2, 0.3, 0.5, 0.7, 1]
>>> random.choices(range(1, 7), cum_weights=cum_weights)
[5]
```

Je vous laisse calculer la fréquence des tirages pour le vérifier.

![Poids cumulés.](img/random_cum_weights.png)
