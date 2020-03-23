### Opérations booléennes

* Notion de prédicat
    * Vérifier une entrée utilisateur (nombre correct, nombre dans un intervalle)
* Différents opérateurs de comparaison : `==`, `!=`, `<`, `>`, `<=`, `>=`
* Application aux types vus précédemment (nombres entiers et flottants, chaînes de caratères)
* Priorités par rapport aux autres opérateurs

Les valeurs `True` et `False` que nous avons vues sont les deux valeurs d'un nouveau type : les booléens.

Plusieurs opérateurs de comparaison permettent en effet d'obtenir des booléens.

Outre l'opérateur d'agalité (`==`), on retrouve de la même manière l'opérateur `!=` pour tester si deux valeurs sont différentes.

```python
>>> 1 != 1
False
>>> 1 != 'abc'
True
```

Sont aussi présents les opérateurs d'inégalités `<` et `>` pour tester les relations d'ordre :

* `a < b` teste si `a` est strictement inférieur à `b` ;
* `a > b` teste si `a` est strictement supérieur à `b`.

```python
>>> 1 < 2
True
>>> 1 > 2
False
```

Cette fois-ci l'opération n'est possible qu'entre deux valeurs sont compatibles, c'est-à-dire ordonnable l'une par rapport à l'autre.
Mais c'est par exemple le cas des entiers et des flottants.

```python
>>> 5 < 5.1
True
```

Enfin ces deux opérateurs possèdent des variantes `<=` et `>=` correspondant aux opérations « inférieur ou égal » et « supérieur ou égal ».

```python
>>> 1 < 1
False
>>> 1 <= 1
True
```
