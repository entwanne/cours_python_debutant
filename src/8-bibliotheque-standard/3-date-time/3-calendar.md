### Module calendar

Le module `calendar` est un module qui sert principalement à afficher de simples calendriers dans le terminal.

```pycon
>>> import calendar
>>> calendar.prmonth(2021, 10)
    octobre 2021
lu ma me je ve sa di
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31
```

Le module contient ainsi des fonctions `month` et `calendar`.
La première prend une année et un mois en arguments et renvoie la représentation de ce mois.
La seconde prend une année et renvoie la représentation de tous les mois de cette année.  
Les tailles des lignes et des colonnes sont configurables à l'aide des différents paramètres de ces fonctions.

Les fonctions `prmonth` et `prcal` sont des raccourcis pour directement afficher ces représentations sur le terminal.

Le module apporte aussi différents attributs pour connaître les noms de jours et de mois :

* `day_name` est le tableau des noms de jours de la semaine
* `day_abbr` est celui des noms de jours abrégés
* `month_name` est le tableau des noms de mois
* `month_abbr` est celui des noms de mois abrégés

```pycon
>>> calendar.day_name[0]
'lundi'
>>> calendar.day_abbr[1]
'mar.'
>>> calendar.month_name[3]
'mars'
>>> calendar.month_abbr[7]
'juil.'
```

--------------------

Enfin, on trouve aussi dans ce module une fonction `timegm` qui permet de convertir un objet `struct_time` en _timestamp_.

```pycon
>>> calendar.timegm(time.gmtime())
1633102464
```

D'autres fonctions sont encore disponibles dans le module, je vous laisse les découvrir [sur la page de documentation](https://docs.python.org/fr/3/library/calendar.html).
