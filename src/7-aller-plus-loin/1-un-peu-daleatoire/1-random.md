### Le module random

La bibliothèque standard de Python comprend un module `random` dédié aux opérations aléatoires.

Nous sommes sur un ordinateur est l'aléatoire n'est pas réellement possible[^impossible] mais il existe une astuce.
Cette astuce ce sont les générateurs pseudo-aléatoires.

[^impossible]: À moins d'utiliser un périphérique dédié.

Ces générateurs sont des outils produisant des suites de nombres qui semblent aléatoirement tirés.
Pour cela ils s'appuient sur des paramètres extérieurs tels que le temps afin d'initialiser leur état, puis sur des opérations mathématiques pour générer un nombre en fonction des précédents.  
En pratique ça fonctionne bien, mais attention : deux générateurs qui seraient initialisés avec la même valeur produiraient exactement les mêmes nombres.

Certains langages vous demandent d'initialiser le générateur pseudo-aléatoire avant de commencer à faire des tirages, mais Python le fait pour nous lors de l'import du module `random`, et est donc directement utilisable.

```python
>>> import random
```

Le module propose de nombreuses fonctions mais nous n'allons nous intéresser qu'à certaines d'entre-elles.

#### Nombres aléatoires

Premièrement, le plus simple, les fonctions pour tirer un nombre entier aléatoire, tel un lancer de dé.
Il y en a deux, `randrange` et `randint`.

La première reçoit entre 1 et 3 arguments, comme la fonction `range`, formant donc un intervalle avec une valeurs de début (0 si omise), de fin et un pas (1 si omis).
Elle renvoie un nombre aléatoire compris dans cet intervalle (pour rappel, la valeur de fin est exclue de l'intervalle).

Voici par exemple des tirages de nombres entre 1 et 6 (inclus).

```python
>>> random.randrange(1, 7)
5
>>> random.randrange(1, 7)
4
>>> random.randrange(1, 7)
2
```

Ce qui est d'ailleurs strictement équivalent à :

```python
>>> random.randrange(6) + 1
3
>>> random.randrange(6) + 1
2
```

(bien sûr, vous n'obtiendrez pas nécessairement les mêmes résultats que les exemples)

Si l'on ne souhaitait tirer que des valeurs de dé impaires, on pourrait ajouter un pas à notre appel.

```python
>>> random.randrange(1, 7, 2)
5
>>> random.randrange(1, 7, 2)
1
>>> random.randrange(1, 7, 2)
3
```

La fonction `randint` est un peu similaire si ce n'est qu'elle prend deux arguments (ni plus ni moins) et qu'elle retourne un nombre de cet intervalle, bornes incluses.
Ainsi, notre tirage de dé se ferait comme suit.

```python
>>> random.randint(1, 6)
6
```

#### Opérations aléatoires

* Tirer un élément : `choice`, `sample` et `shuffle`
