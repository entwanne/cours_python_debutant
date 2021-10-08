### Module datetime

Le module `datetime` fournit une interface haut-niveau pour gérer les temps et les dates, construit autour du module `time`, avec le type `datetime`.

Un objet `datetime` représente une date précise (avec année, mois, jour, heure, minutes, secondes et microsecondes), avec ou sans fuseau horaire.  
Une date avec fuseau horaire représente donc un instant précis, on dit qu'elle est avisée.
Une date sans fuseau est dite naïve car son interprétation dépend du fuseau horaire courant.

```python
>>> datetime.datetime(2000, 4, 12, 8, 30, 55)
datetime.datetime(2000, 4, 12, 8, 30, 55)
```

La méthode `now` du type `datetime` permet de récupérer l'objet associé à l'instant courant (exprimé dans le fuseau local).
Par défaut, elle renvoie une date naïve.

```python
>>> dt = datetime.datetime.now()
>>> dt
datetime.datetime(2021, 10, 1, 16, 19, 43, 840744)
```

Il est possible de préciser un fuseau horaire en argument pour obtenir une date avisée selon ce fuseau, par exemple en utilisant `datetime.timezone.utc`.

```python
>>> dt = datetime.datetime.now(datetime.timezone.utc)
>>> dt_utc
datetime.datetime(2021, 10, 1, 14, 19, 43, 840744, tzinfo=datetime.timezone.utc)
```

On voit que le fuseau horaire est stocké dans l'attribut `tzinfo` de l'objet `datetime`.

[[i]]
| Le format `datetime` ne permet que de représenter un ensemble limité de dates : seules les années 1 à 9999 sont autorisées.

#### Conversions

Les `datetime` peuvent être convertis vers d'autres types de dates à l'aide de méthodes spécifiques :

* `datetime.fromtimestamp` permet de construire un objet `datetime` depuis un _timestamp_. Un fuseau optionnel peut être donné en argument.

  ```python
  >>> datetime.datetime.fromtimestamp(1633093972)
  datetime.datetime(2021, 10, 1, 15, 12, 52)
  >>> datetime.datetime.fromtimestamp(1633093972, datetime.timezone.utc)
  datetime.datetime(2021, 10, 1, 13, 12, 52, tzinfo=datetime.timezone.utc)
  ```

* La méthode `timestamp` permet l'opération inverse (que l'objet `datetime` soit naïf ou avisé).

  ```python
  >>> dt.timestamp()
  1633097983.840744
  >>> dt_utc.timestamp()
  1633097983.840744
  ```

* On peut aussi convertir des `datetime` vers des `struct_time` à l'aide de la méthode `timetuple`.

  ```python
  >>> dt.timetuple()
  time.struct_time(tm_year=2021, tm_mon=10, tm_mday=1, tm_hour=16, tm_min=19, tm_sec=43, tm_wday=4, tm_yday=274, tm_isdst=-1)
  >>> dt_utc.timetuple()
  time.struct_time(tm_year=2021, tm_mon=10, tm_mday=1, tm_hour=14, tm_min=19, tm_sec=43, tm_wday=4, tm_yday=274, tm_isdst=-1)
  ```

Les conversions sont aussi possibles vers et depuis des chaînes de caractères, notamment en format ISO avec les méthodes `isoformat` et `fromisoformat`.

```python
>>> dt.isoformat()
'2021-10-01T16:19:43.840744'
>>> dt_utc.isoformat()
'2021-10-01T14:19:43.840744+00:00'
>>> datetime.datetime.fromisoformat('2021-10-01T16:19:43.840744')
datetime.datetime(2021, 10, 1, 16, 19, 43, 840744)
>>> datetime.datetime.fromisoformat('2021-10-01T14:19:43.840744+00:00')
datetime.datetime(2021, 10, 1, 14, 19, 43, 840744, tzinfo=datetime.timezone.utc)
```

Mais d'autres conversions en chaînes sont possibles, avec `strftime` par exemple.
Cette méthode accepte une chaîne pour représenter le format de sortie, où différents codes de formatage sont disponibles comme :

- `%a` et `%A` pour le nom du jour de la semaine (forme abrégée ou forme longue)
- `%d` pour le numéro de jour dans le mois
- `%b` et `%B` pour le nom du mois (forme abrégée ou forme longue)
- `%m` pour le numéro du mois
- `%y` et `%Y` pour l'année (sur 2 ou 4 chiffres)
- `%H`, `%M` et `%S` respectivement pour les heures, minutes et secondes
- `%z` et `%Z` pour le fuseau horaire (en tant que décalage ou par son nom)

```python
>>> dt.strftime('Le %A %d %B %Y à %Hh%M')
'Le vendredi 01 octobre 2021 à 16h19'
>>> dt_utc.strftime('Le %A %d %B %Y à %Hh%M (%Z)')
'Le vendredi 01 octobre 2021 à 14h19 (UTC)'
```

[[a]]
| Il se peut que vous obteniez des noms anglais pour les jours et mois, cela est dû à la _locale_ définie pour les conversions.
| Vous pouvez définir une _locale_ française à l'aide des lignes suivantes :
|
| ```python
| import locale
| locale.setlocale(locale.LC_ALL, 'fr_FR')
| ```
|
| (`fr_BE` pour la Belgique et `fr_CA` pour le Canada sont aussi disponibles)

On notera que ces options de formatage sont aussi disponibles au sein des _fstrings_ pour représenter des objets `datetime`.

```python
>>> f'{dt:%d/%m/%Y %H:%M}'
'01/10/2021 16:19'
>>> f'{dt_utc:%d/%m/%Y %H:%M%z}'
'01/10/2021 14:19+0000'
```

L'opération inverse est elle aussi possible (mais plus compliquée) avec la méthode `strptime` : on spécifie le chaîne représentant la date et le format attendu en arguments, la méthode nous renvoie alors l'objet `datetime` correspondant.

```python
>>> datetime.datetime.strptime('01/10/2021 14:19+0000', '%d/%m/%Y %H:%M%z')
datetime.datetime(2021, 10, 1, 14, 19, tzinfo=datetime.timezone.utc)
```

#### Durées

Il est possible de soustraire des objets `datetime` pour obtenir une durée, qui représente le nombre de jours et secondes qui séparent les deux dates.

```python
>>> dt - datetime.datetime(2000, 4, 12, 8, 30, 55)
datetime.timedelta(days=7842, seconds=28128, microseconds=840744)
```

Ces durées se matérialisent par le type `timedelta`. Elles peuvent s'additionner et se soustraire entre-elles.
Il est aussi possible de les multiplier par des nombres.

```python
>>> datetime.timedelta(days=1) + datetime.timedelta(days=1)
datetime.timedelta(days=2)
>>> datetime.timedelta(days=1) - datetime.timedelta(days=1)
datetime.timedelta(0)
>>> datetime.timedelta(days=1) * 10
datetime.timedelta(days=10)
```

Et bien sûr, on peut additionner une durée à un `datetime` (naïf ou avisé) pour obtenir un nouveau `datetime`.

```python
>>> dt + datetime.timedelta(days=1)
datetime.datetime(2021, 10, 2, 16, 19, 43, 840744)
>>> dt_utc + datetime.timedelta(days=1)
datetime.datetime(2021, 10, 2, 14, 19, 43, 840744, tzinfo=datetime.timezone.utc)
```

#### Fuseaux horaires

On l'a vu : les objets `datetime` peuvent contenir ou non des informations de fuseau horaire, selon l'usage que l'on veut en faire, et les deux types sont généralement gérés par les différentes fonctions.  
Il est cependant à noter qu'on ne peux pas mélanger dates naïves et avisées au sein des mêmes opérations.

```python
>>> dt_utc - dt
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't subtract offset-naive and offset-aware datetimes
```

Le module `datetime` ne fournit par défaut que le fuseau horaire UTC (_Temps Universel Coordonné_) avec `datetime.timezone.utc`.

Mais le type `timezone` permet de construire des fuseaux à décalage fixe par rapport à UTC, en prenant un `timedelta` en argument.

```python
>>> tz = datetime.timezone(datetime.timedelta(seconds=3600))
>>> datetime.datetime.now(tz)
datetime.datetime(2021, 10, 1, 15, 19, 43, 840744, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600)))
```

On notera aussi que la méthode `astimezone` permet de convertir une date vers un autre fuseau horaire.
Les dates naïves sont considérées comme appartenant au fuseau local.

```python
>>> dt.astimezone(tz)
datetime.datetime(2021, 10, 1, 15, 19, 43, 840744, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600)))
>>> dt.astimezone(datetime.timezone.utc)
datetime.datetime(2021, 10, 1, 14, 19, 43, 840744, tzinfo=datetime.timezone.utc)
>>> dt_utc.astimezone(tz)
datetime.datetime(2021, 10, 1, 15, 19, 43, 840744, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600)))
```

[[i]]
| `astimezone` opère une conversion sur la date pour correspondre au fuseau horaire choisi.
| Pour simplement ajouter un fuseau horaire à une date sans faire de conversion, vous pouvez utiliser la méthode `replace` avec l'argument nommé `tzinfo`.
|
| ```python
| >>> dt.replace(tzinfo=datetime.timezone.utc)
| datetime.datetime(2021, 10, 1, 16, 19, 43, 840744, tzinfo=datetime.timezone.utc)
| ```

Depuis Python 3.9, le module `zoneinfo` apporte une collection de fuseaux horaires pour traiter les fuseaux courants.

```python
>>> from zoneinfo import ZoneInfo
>>> tz = ZoneInfo('Europe/Paris')
>>> dt.astimezone(tz)
datetime.datetime(2021, 10, 1, 16, 19, 43, 840744, tzinfo=zoneinfo.ZoneInfo(key='Europe/Paris'))
```

Pour plus d'informations sur ces modules, vous pouvez consulter les documentations de [`datetime`](https://docs.python.org/fr/3/library/datetime.html) et [`zoneinfo`](https://docs.python.org/fr/3/library/zoneinfo.html).
