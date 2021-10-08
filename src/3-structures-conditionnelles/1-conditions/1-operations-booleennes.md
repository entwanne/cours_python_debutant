### Test d'égalité

Nous avons vu différents opérateurs arithmétiques mais il est maintenant temps de nous intéresser à une nouvelle catégorie : les opérateurs de comparaison.
À commencer par l'opérateur d'égalité, noté `==`.

Cet opérateur appliqué à deux valeurs renvoie un état vrai (`True`) ou faux (`False`) indiquant si les valeurs sont égales ou non.

```python
>>> 1 == 1
True
>>> 1 == 2
False
>>> 2 == 2
True
```

Le test d'égalité fonctionne pour tous les types de données et quelles que soient les expressions.

```python
>>> 3 + 5 == 2 * 4
True
>>> word = 'abc'
>>> word == 'ab' + 'c'
True
>>> word == 'ab' + 'cd'
False
```

[[a]]
| Attention cependant aux comparaisons avec des flottants.
| Si vous vous souvenez, on avait vu que les nombres flottants pouvaient comporter des erreurs d'arrondis.  
| Il peut ainsi arriver qu'une égalité entre flottants que l'on pense vraie ne le soit en fait pas, en raison de ces arrondis.
|
| ```python
| >>> 0.1 + 0.2 == 0.3
| False
| >>> 0.1 + 0.2 == 0.30000000000000004
| True
| ```
|
| De manière générale, évitez donc les tests d'égalité entre nombres flottants, nous verrons dans un prochain chapitre ce que l'on peut faire à la place.

Il est aussi possible de comparer des valeurs de types différents, mais le résultat sera souvent faux car des valeurs de types différents sont généralement considérées comme différentes (exception faite pour les nombres entiers et flottants).

```python
>>> word == 2
False
>>> '2' == 2
False
>>> 2.0 == 2
True
```

Ainsi l'objectif est maintenant d'exécuter une action uniquement si un test d'égalité (une condition) est vérifié, c'est là qu'interviennent les blocs conditionnels !
