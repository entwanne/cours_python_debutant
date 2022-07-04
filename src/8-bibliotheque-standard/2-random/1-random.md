### Le module random

La bibliothèque standard de Python comprend un module `random` dédié aux opérations aléatoires.

Nous sommes sur un ordinateur et l'aléatoire n'est pas réellement possible[^impossible] mais il existe une astuce.
Cette astuce ce sont les générateurs pseudo-aléatoires.

[^impossible]: À moins d'utiliser un périphérique dédié.

Ces générateurs sont des outils produisant des suites de nombres qui semblent aléatoirement tirés.
Pour cela ils s'appuient sur des paramètres extérieurs tels que le temps ou le statut des périphériques afin d'initialiser leur état, puis sur des opérations mathématiques pour générer un nombre en fonction des précédents.  
En pratique ça fonctionne bien, mais attention : deux générateurs qui seraient initialisés avec la même valeur produiraient exactement les mêmes nombres.

Certains langages vous demandent d'initialiser le générateur pseudo-aléatoire avant de commencer à faire des tirages, mais Python le fait pour nous lors de l'import du module `random`, et est donc directement utilisable.

```pycon
>>> import random
```

Le module propose de nombreuses fonctions, mais nous n'allons nous intéresser qu'à certaines d'entre elles.

#### Nombres aléatoires

Premièrement, le plus simple, les fonctions pour tirer un nombre entier aléatoire, tel un lancer de dé.
Il y en a deux, `randrange` et `randint`.

La première reçoit entre 1 et 3 arguments, comme la fonction `range`, formant donc un intervalle avec une valeur de début (0 si omise), de fin et un pas (1 si omis).
Elle renvoie un nombre aléatoire compris dans cet intervalle (pour rappel, la valeur de fin est exclue de l'intervalle).

Voici par exemple des tirages de nombres entre 1 et 6 (inclus).

```pycon
>>> random.randrange(1, 7)
5
>>> random.randrange(1, 7)
4
>>> random.randrange(1, 7)
2
```

Ce qui est d'ailleurs strictement équivalent à :

```pycon
>>> random.randrange(6) + 1
3
>>> random.randrange(6) + 1
2
```

(bien sûr, vous n'obtiendrez pas nécessairement les mêmes résultats que les exemples)

Si l'on ne souhaitait tirer que des valeurs de dé impaires, on pourrait ajouter un pas à notre appel.

```pycon
>>> random.randrange(1, 7, 2)
5
>>> random.randrange(1, 7, 2)
1
>>> random.randrange(1, 7, 2)
3
```

La fonction `randint` est un peu similaire si ce n'est qu'elle prend deux arguments (ni plus ni moins) et qu'elle retourne un nombre de cet intervalle, bornes incluses.
Ainsi, notre tirage de dé se ferait comme suit.

```pycon
>>> random.randint(1, 6)
6
>>> random.randint(1, 6)
4
```

#### Opérations aléatoires

Mais tirer un nombre aléatoire ce n'est pas tout, et le module propose d'autres opérations aléatoires intéressantes.

Par exemple, la fonction `choice` permet de sélectionner aléatoirement un élément dans une liste.

```pycon
>>> actions = ['manger', 'dormir', 'aller au ciné']
>>> random.choice(actions)
'manger'
>>> random.choice(actions)
'aller au ciné'
```

Je parle de liste, mais tout objet se comportant comme une liste[^list_like] est aussi accepté, les `range` par exemple.
Ainsi, `random.choice(range(1, 7))` est équivalent à `random.randrange(1, 7)`.

[^list_like]: C'est-à-dire ayant une taille et permettant d'accéder à n'importe quel élément à partir de son index.

```pycon
>>> random.choice(range(1, 7))
3
```

Si vous souhaitez tirer plusieurs valeurs sans remise, `choice` ne sera pas adaptée, vous risqueriez de tirer plusieurs fois la même.

```pycon
>>> random.choice(actions)
'manger'
>>> random.choice(actions)
'manger'
```

Dans ce cas orientez-vous vers `sample`, qui prend en argument le nombre de valeurs à tirer en plus de la liste.

```pycon
>>> random.sample(actions, 2)
['dormir', 'manger']
```

Enfin, la fonction `shuffle` permet de simplement trier aléatoire la liste (elle modifie la liste reçue en paramètre).

```pycon
>>> random.shuffle(actions)
>>> actions
['aller au ciné', 'manger', 'dormir']
>>> random.shuffle(actions)
>>> actions
['dormir', 'aller au ciné', 'manger']
```

C'est utile pour mélanger un paquet de cartes ou d'autres opérations du genre, et avoir ensuite un tirage sans remise.

```pycon
>>> cards = ['as de pique', '3 de trèfle', '7 de carreau', 'dame de cœur']
>>> random.shuffle(cards)
>>> cards.pop()
'3 de trèfle'
>>> cards.pop()
'7 de carreau'
```
