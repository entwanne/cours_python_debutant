### Égalité

Nous avons vu différents opérateurs arithmétiques mais il est maintenant temps de nous intéresser à une nouvelle catégorie : les opérateurs de comparaison.
À commencer par l'opérateur d'égalité, `==`.

Cet opérateur appliqué à deux valeurs renvoie un état vrai (`True`) ou faux (`False`) indiquant si les valeurs sont égales ou non.

```python
>>> 1 == 1
True
>>> 1 == 2
False
```

Le test d'égalité fonctionne pour tous les types de données et quelles que soient les expressions.

```python
>>> word = 'abc'
>>> word == 'ab' + 'c'
True
>>> word == 'ab' + 'cd'
False
```

Il est aussi possible de comparer des valeurs de types différents.

```python
>>> word == 2
False
```

Ainsi l'objectif est maintenant d'exécuter une action uniquement si un test (une condition) est vérifié, c'est là qu'interviennent les blocs conditionnels.
