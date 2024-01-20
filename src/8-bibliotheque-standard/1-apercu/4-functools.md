### Functools

Préccédemment dans [la section dédiée aux décorateurs](https://zestedesavoir.com/tutoriels/2514/un-zeste-de-python/7-perfectionnement/4-fonctions/#4-4-decorateurs) du chapitre de rappel sur les fonctions j'abordais le module `functools` pour les décorateurs `cache` et `lru_cache` qu'il comportait.  
Il est maintenant temps de revenir sur ce module pour voir ce qu'il peut nous apporter d'autre.

#### `lru_cache` / `cache`

Ces deux fonctions peuvent donc s'utiliser comme décorateurs pour appliquer facilement un cache sur une fonction.
Elles interceptent pour cela les arguments envoyés à la fonction afin de savoir si un appel similaire a déjà été réalisé (et conservé dans le cache) et de renvoyer directement son résultat si c'est le cas.  
Dans l'autre cas de faire l'appel habituel à la fonction et d'en stocker le retour.

`lru_cache` dispose d'un mécanisme le LRU (_Least Recently Used_ soit _Utilisés le Plus Récemment_) avec une taille limitée pour ne garder en cache que les résultats les plus récents (128 résultats par défaut).  
`cache` met en place un cache infini (il faut alors faire attention à l'empreinte mémoire qu'il peut avoir au fil du temps), équivalent à `lru_cache` appelée avec une taille `None`.

```python
import functools
import json

@functools.lru_cache(3)
def product(a, b):
    print('Calcul de', a, '*', b)
    return a * b

@functools.cache
def get_settings():
    # La fonction ne prend pas d'arguments donc on sait que le cache ne grossira pas
    # La mise en cache permet de ne charger le fichier qu'une seule fois
    with open('settings.json') as f:
        return json.load(f)
```

```json
{
    "env": "dev",
    "version": "1.1"
}
```
Code: settings.json

```pycon
>>> product(3, 5)
Calcul de 3 * 5
15
>>> product(3, 5)
15
>>> product(1, 2)
Calcul de 1 * 2
2
>>> product(-1, -1)
Calcul de -1 * -1
1
>>> product(1, 0)
Calcul de 1 * 0
0
>>> product(3, 5)
Calcul de 3 * 5
15
>>> get_settings()
{'env': 'dev', 'version': '1.1'}
```

Mais attention, le cache nécessite de stocker les arguments de l'appel et utilise pour cela un dictionnaire.
Les clés d'un dictionnaire devant être _hashables_, cela signifie qu'on est limités sur les types d'objets utilisés en arguments, sont ainsi exclus les listes et les dictionnaires.

```pycon
>>> product([0], 3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

On notera que les fonctions décorées d'un cache disposent d'une méthode `cache_clear` pour effacer tous les résultats enregistrés.

```pycon
>>> product(3, 5)
15
>>> product.cache_clear()
>>> product(3, 5)
Calcul de 3 * 5
15
```

Ainsi qu'une méthode `cache_info` pour obtenir des informations sur le cache (nombre d'entrées maximum, nombre d'entrées courantes, nombre de fois où un résultat a été trouvé ou non).

```pycon
>>> get_settings.cache_info()
CacheInfo(hits=0, misses=1, maxsize=None, currsize=1)
>>> get_settings()
{'env': 'dev', 'version': '1.1'}
>>> get_settings.cache_info()
CacheInfo(hits=1, misses=1, maxsize=None, currsize=1)
```

#### `partial`

`partial` permet l'application partielle d'une fonction, c'est-à-dire de stocker des arguments pour un appel futur.
Elle renvoie alors un nouvel objet qui s'utilise comme une fonction, et peut être appelé à son tour (avec des arguments — qui s'ajouteront à ceux stockés — ou non).

```pycon
>>> debug = functools.partial(print, 'DEBUG:')
>>> debug('test')
DEBUG: test
>>> debug('foo')
DEBUG: foo
>>> debug()
DEBUG:
```

#### `reduce`

Vous vous souvenez des fonctions _builtin_ `map` et `filter` que [nous avons vues plus tôt](https://zestedesavoir.com/tutoriels/2514/un-zeste-de-python/7-perfectionnement/3-boucles/#fonctions-map-et-filter) ?
Ce duo s'utilise pour transformer et filtrer les éléments d'un itérable, à la manière des listes en intension.

```pycon
>>> numbers = map(int, '9248135')
>>> numbers = filter(lambda x: x > 2, numbers)
>>> list(numbers)
[9, 4, 8, 3, 5]
```

Mais il s'agissait auparavant d'un trio puisque s'ajoutait aussi (en Python 2) la fonction `reduce`, elle est aujourd'hui déplacée dans le module `functools`.

C'est une fonction qui permet d'appliquer une opération sur les éléments successifs d'un itérable, opération qui prend en arguments le précédent résultat et l'élement courant.  
`functools.reduce(op, seq)` est ainsi équivalent à `op(op(op(seq[0], seq[1]), seq[2]), seq[3])...`.

On comprend alors son nom de `reduce` puisqu'elle permet de réduire un ensemble de valeurs en une seule.

Utilisée avec l'opération `operator.add` elle peut par exemple calculer la somme des valeurs de l'itérable. Ou leur produit avec `operator.mul`.

```pycon
>>> import operator
>>> functools.reduce(operator.add, [1, 2, 3, 4])
10
>>> functools.reduce(operator.mul, [1, 2, 3, 4])
24
```

Elle ressemble à la fonction `accumulate` d'`itertools` vue dans la section précédente, sauf qu'elle ne renvoie ici que le dernier résultat et non les résultats intermédiaires.
