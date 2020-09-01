### Distributions

Voilà pour ce qui est des tirages dit discrets (on a un ensemble de valeurs connues et on veut tirer une valeur dans celles-ci) mais il est aussi possible de tirer des nombres dans des intervalles continus.

Par exemple, très simple, la fonction `random` va renvoyer un nombre flottant entre 0 et 1 (1 étant exclu de l'intervalle).

```python
>>> random.random()
0.9294919627802888
>>> random.random()
0.47588843177000617
```

Le tirage de ce nombre est uniforme, grossièrement cela veut dire qu'on a autant de chances de tirer un nombre n'importe où dans l'intervalle.

Une fonction est spécifiquement dédiée au tirage uniforme entre deux nombres flottants, il s'agit de la fonction `uniform`.

```python
>>> random.uniform(1, 10)
1.4017486291855232
>>> random.uniform(1, 10)
5.926447309804371
```

Suivant les arrondis, la borne supérieure peut être inclue ou non dans l'intervalle, mais cela a peu d'importance : il est pratiquement impossible de tomber sur ce nombre précis, puisqu'il y en a une infinité[^infini].

[^infini]: Pas exactement puisque la représentation d'un flottant est finie, mais vous comprenez l'idée.

D'autres distributions sont possibles pour les tirages de nombres flottants.

* Note sur les distributions

```python
>>> random.triangular(1, 10)
4.0479535343895865
```

* `normalvariate`
* `gauss`

Un autre point important à propos des tirages aléatoires concerne la pondération.

* Pondération
* `choices`
* Poids, poids cumulés
