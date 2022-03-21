### Module time

Il existe plusieurs manières de représenter le temps en informatique, selon que l'on parle d'instants ou de dates.

#### Les timestamps

La plus simple d'entre toutes, c'est le _timestamp_ qui représente un instant selon le nombre de secondes écoulées depuis une date de référence appelée _epoch_ (généralement le 1er janvier 1970 à minuit UTC, norme Unix).
On y accède via la fonction `time` du module `time` qui nous renvoie un nombre flottant (incluant donc les fractions de secondes).

```pycon
>>> import time
>>> time.time()
1633091908.9014919
>>> time.time()
1633091911.8008878
```

[[i]]
| Le _timestamp_ peut aussi être un nombre négatif pour représenter les instants antérieurs à cet _epoch_.

Si une plus grande précision est nécessaire, la fonction `time_ns` permet de récupérer le _timestamp_ sous la forme d'un nombre entier de nanosecondes écoulées.

```pycon
>>> time.time_ns()
1633093266497388151
```

Étant un nombre, le _timestamp_ est très facile à manipuler, et n'est pas soumis aux problématiques sur la gestion des fuseaux horaires. Il est donc utile pour des problématiques d'horodatage (noter à quel instant s'est produit un événement).  
Cependant, on ne peut pas le considérer comme portable car son interprétation dépend de la date utilisée comme _epoch_.
Il n'est ainsi pas recommandé de transmettre un _timestamp_ à un autre programme car celui-ci pourrait l'interpréter différemment.

De plus, le _timestamp_ est un nombre soumis à un stockage limité : auparavant sur 32 bits (aujourd'hui sur 64) il ne permettait alors de ne représenter qu'un intervalle restreint de dates.

[[q]]
| Peut-être avez-vous entendu parler du bug de l'an 2038 ? Il s'agit de la date où les _timestamps_ Unix atteindront leur capacité maximale sur 32 bits, rendant leur usage impossible après cette date.  
| Mais d'ici-là, tout le monde devrait être passé aux _timestamps_ 64 bits.

Aussi, on pourrait être tenté d'utiliser des _timestamps_ pour mesurer des durées dans un programme, en calculant la différence entre les _timestamps_.
C'est une mauvaise pratique car ceux-ci ne sont pas monotones : étant alignés sur l'horloge du système, le temps peut « revenir en arrière » si l'horloge est recalibrée.

Pour un tel cas d'usage, il faut alors plutôt faire appel à la fonction `monotonic` (ou `monotonic_ns`) qui est une horloge monotonique.
Le nombre ainsi renvoyé est aussi un nombre de secondes (ou de nanosecondes) mais la date de référence est indéterminée, ils ne sont alors utiles que pour calculer des durées.

```pycon
>>> start = time.monotonic()
>>> ... # différentes opérations
>>> time.monotonic() - start
14.564803410001332
```

#### Structure de temps

Une autre manière de représenter le temps est de stocker des données liées à une date : année, mois, jour, heure, minutes, secondes, etc.
C'est ce que fait l'objet `struct_time` du module `time`.

On peut obtenir un objet `struct_time` en appelant la fonction `localtime` par exemple.

```pycon
>>> time.localtime()
time.struct_time(tm_year=2021, tm_mon=10, tm_mday=1, tm_hour=15, tm_min=12, tm_sec=52, tm_wday=4, tm_yday=274, tm_isdst=1)
>>> date = time.localtime()
>>> date.tm_year
2021
>>> date.tm_hour
15
```

Il s'agit donc d'une représentation du temps plus exploitable, dont on peut explorer les différentes composantes.
Mais un tel objet est alors dépendant du fuseau horaire (le fuseau local pour `localtime`) et des autres conventions sur les dates.

La fonction `gmtime` permet de récupérer le `struct_time` correspondant au temps courant dans le fuseau horaire UTC.

```pycon
>>> time.gmtime()
time.struct_time(tm_year=2021, tm_mon=10, tm_mday=1, tm_hour=13, tm_min=15, tm_sec=3, tm_wday=4, tm_yday=274, tm_isdst=0)
```

#### Utilitaires du module

Le module `time` met aussi à disposition quelques utilitaires.

Ainsi, il est possible de mettre le programme en pause pendant une certaine durée (en secondes) à l'aide de la fonction `sleep`.

```pycon
>>> time.sleep(3)
```

On trouve aussi certaines fonctions pour faire des conversions entre les types précédents.
Ainsi la fonction `mktime` permet de transformer un objet `struct_time` (dans le fuseau courant) en un _timestamp_.

```pycon
>>> time.mktime(date)
1633093972.0
```

Aussi, `localtime` et `gmtime` peuvent prendre un _timestamp_ en argument et renvoyer la date associée (respectivement dans le fuseau local ou en UTC).

```pycon
>>> time.localtime(1633093972.0)
time.struct_time(tm_year=2021, tm_mon=10, tm_mday=1, tm_hour=15, tm_min=12, tm_sec=52, tm_wday=4, tm_yday=274, tm_isdst=1)
>>> time.gmtime(1633093972.0)
time.struct_time(tm_year=2021, tm_mon=10, tm_mday=1, tm_hour=13, tm_min=12, tm_sec=52, tm_wday=4, tm_yday=274, tm_isdst=0)
```

Enfin, on trouve d'autres fonctions de calcul du temps dans le module, comme `process_time` (et `process_time_ns`) qui sert à calculer le nombre de secondes de travail effectif (excluant les pauses) du programme, ainsi que `perf_counter` (et `perf_counter_ns`) spécialement dédiée aux calculs de performance du programme avec une résolution adaptée (les dates de référence de ces différentes fonctions sont indéterminées).

```pycon
>>> start = time.process_time()
>>> time.sleep(3)
>>> time.process_time() - start
0.0006125660000000088
>>> start = time.perf_counter()
>>> time.sleep(3)
>>> time.perf_counter() - start
3.0024995610001497
```

Et n'hésitez pas à jeter un œil à [la documentation du module `time`](https://docs.python.org/fr/3/library/time.html) pour aller plus loin.
