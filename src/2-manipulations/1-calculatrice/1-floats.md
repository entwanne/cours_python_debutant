### Des nombres à virgule

Nous nous sommes intéressés aux principaux opérateurs arithmétiques à l'exception de l'un d'entre-eux : l'opérateur de division (`/`).
Il est un peu différent des autres parce que la division entre deux nombres entiers n'est pas nécessairement un nombre entier.

En effet, que vaut « 5 divisé par 2 » (`5 / 2`) ? Aucun des nombres que l'on sait représenter n'est égal à ce résultat.
Il nous faut aller au-delà des nombres entiers pour découvrir le monde des nombres à virgule, ou nombres flottants.
Les nombres flottants se composent d'une partie entière et d'une partie fractionnaire séparées par un point (notation anglaise).
Ainsi le résultat de notre précédent calcul se note `2.5`.

```pycon
>>> 5 / 2
2.5
```

Chaque valeur en Python est associée à un type, c'est-à-dire qu'elle appartient à une certaine catégorie.
Cette catégorie régit les opérations qui sont applicables sur ses valeurs.
Les nombres entiers (`int`) et les flottants (`float`) sont deux types différents, deux catégories distinctes.

```pycon
>>> 8 / 2
4.0
```

Ainsi ici Python nous renvoie la valeur `4.0`, qui n'est pas la même chose que `4`.
Les deux valeurs sont égales et représentent le même nombre, mais elles ne sont pas du même type en Python.

Les opérations que nous avons vues sur les nombres entiers s'appliquent aussi aux flottants, la différence étant que le résultat sera toujours un nombre flottant.

```pycon
>>> 1.1 + 3.4
4.5
>>> 4.5 * 2.7
12.15
>>> 12.15 - 0.1
12.05
>>> 12.05 / 0.5
24.1
```

Et ces deux types de nombres sont compatibles entre-eux, il est par exemple possible d'additionner un entier et un flottant.
Là aussi le résultat sera un flottant, pour éviter toute perte d'information de la partie fractionnaire.

```pycon
>>> 5 + 0.8
5.8
>>> 0.3 * 10
3.0
```

Une chose à laquelle il faut faire attention avec les nombres à virgule se situe sur les arrondis.
Par exemple, il n'est pas possible de représenter la division de 8 par 3 par un nombre à virgule précis, et c'est donc le nombre le plus proche qui nous sera renvoyé par cette opération.

```pycon
>>> 8 / 3
2.6666666666666665
```

Mais ça ne s'arrête pas là. Contrairement à nous qui avons l'habitude du système décimal, l'ordinateur stocke les nombres sous forme binaire.  
Ainsi, tous les nombres décimaux que nous utilisons ne sont pas représentables par un flottant, et Python devra effectuer un arrondi.

C'est le cas de `0.1` qui est en fait égal à `0.100000000000000005...`
À l'usage, il est ainsi courant de rencontrer des cas où ces erreurs d'arrondis deviennent visibles, comme dans les exemples suivants.

```pycon
>>> 0.1 + 0.1 + 0.1
0.30000000000000004
>>> 1.5 * 1.6
2.4000000000000004
```
