-> Annexe méthodologie

#### Transformer un code récursif en itératif

* Récursivité peu recommandée en Python
* Problèmes qui s'expriment mieux en récursif
* Simuler la pile d'appels en itératif

On a vu que Python n'était pas le langage le plus adapté au modèle récursif, mais certains problèmes s'expriment mieux de façon récursive.
Toutefois, il reste possible de les transposer en itératif, et c'est ce que nous allons voir ici.

Commençons avec un exemple simple et prenons le cas de la fonction factorielle : il s'agit pour un nombre entier *N* de renvoyer les produits des nombres de 1 à *N*.
Ainsi la factorielle de 5 (notée $5!$) est égale à $1 \times 2 \times 3 \times 4 \times 5$ soit 120.

Récursivement, on sait que la factorielle de *N* est égale à *N* multiplié par la factorielle de *N-1*.
Et par définition on a la factorielle de 0 qui vaut 1, ce qui forme notre condition de fin.

Notre fonction récursive est donc la suivante.

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

Vous pouvez tester, elle nous donne les bons résultats.

[[a]]
| La fonction échouera pour les nombres négatifs mais ils ne nous intéressent pas ici car sont en dehors de l'ensemble de définition.
| L'idéal serait bien sûr d'avoir une exception dédiée à ces cas.

* \+ Fonction de parcours de hiérarchie arborescente ?

<!--
Premièrement, on va chercher à transformer notre fonction pour qu'elle soit « récursive terminale ».
On dit d'une fonction récursive qu'elle est terminale si elle n'effectue plus aucune opération après l'appel récursif, c'est-à-dire que la valeur de l'appel est directement renvoyée.  
Par exemple une fonction récursive `f` est terminale si tous les appels récursifs sont de la forme `return f(...)`.

Notre fonction actuelle n'est pas récursive terminale car nous utilisons le résultat de l'appel récursif dans une opération (multiplication) avant de le renvoyer.  
Pour corriger cela, il va donc falloir déporter notre opération dans l'appel récursif : plutôt que de calculer `n * resultat` après l'appel récursif, on va demander à cet appel de multiplier lui-même son résultat par `n`, et on va pour cela lui passer en argument.
Un tel argument est généralement appelé « accumulateur » et je nommerai donc le paramètre `acc`.

L'idée est d'utiliser la valeur de ce paramètre comme la mémoire des appels récursifs précédents et d'effectuer les opérations au fur et à mesure.


```python
def factorial(n, acc):
    if n == 0:
        return 1
    return n * factorial(n - 1, acc=n)
```
-->

Premièrement, pour remplacer les appels récursifs il va nous falloir simuler notre propre pile d'appels.
En effet, il nous faut conserver un mécanisme pour stocker les valeurs dont on veut calculer le résultat.  
Cette pile prendra la forme d'une liste Python, dans laquelle nous stockerons les arguments que l'on voudrait passer à nos appels récursifs.
Logiquement elle commencera par ne contenir que la valeur actuelle, `n`.

```python
def factorial(n):
    stack = [n]
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

Ensuite on va ajouter une boucle pour itérer sur notre pile et y déplacer le code de notre fonction.
On ne peut pas utiliser de `for n in stack` ici car la taille de la pile va varier pendant l'itération, ce qui créerait des comportements incohérents.
De plus nous voulons un mécanisme de pile (dernier entré, premier sorti) plutôt que de file (premier entré, premier sorti).  
Le plus simple est alors d'utiliser un `while stack` suivi d'un `n = stack.pop()` pour sortir le dernier élément à chaque itération.

```python
def factorial(n):
    stack = [n]
    while stack:
        n = stack.pop()
        if n == 0:
            return 1
        return n * factorial(n - 1)
```

<!--
Maintenant pour la passer en itératif, on va d'abord isoler l'appel récursif sur une ligne, pour le traiter séparément.

```python
def factorial(n):
    if n == 0:
        return 1
    tmp = factorial(n - 1)
    return n * tmp
```

Ensuite on ajoute une boucle et on y déplace notre code, le plus simplement du monde avec un `while True`.
Puis on retire les `return` qui n'ont plus de sens, on les remplace par une assignation de variable (disons `ret`), variable que l'on renvoie à la fin.  
À la place du `return` de notre condition de fin on ajoute aussi un `break` pour sortir de la boucle.

```python
def factorial(n):
    while True:
        if n == 0:
            ret = 1
            break
        tmp = factorial(n - 1)
        ret = n * tmp
    return ret
```
-->
