### Format JSON

Un premier format de données assez courant en informatique est le JSON (pour _JavaScript Object Notation_) qui comme son nom l'indique provient du Javascript.
Il s'est ainsi répandu dans le monde du web pour devenir un format de prédilection pour les échanges entre applications.

C'est un format textuel, c'est-à-dire qu'il est lisible à l'œil sous forme de texte (contrairement à un format binaire), bien que parfois difficile à écrire à la main.

Voici à quoi ressemble un document JSON :

```json
{
  "id": "001",
  "name": "Pythachu",
  "type": "foudre",
  "attaques": ["tonnerre", "charge"],
  "base_pv": 50
}
```
Code: pythachu.json

On le voit, c'est un format qui ressemble beaucoup au Python.
Il est cependant plus restreint.

Un document JSON ne peut comporter des valeurs que de 7 types :

* `null`, équivalent au `None` de Python.
* `boolean`, un booléen donc, `true` ou `false`.
* `int`, un nombre entier (`42`).
* `float,` un nombre flottant (`1.5`, `1e10`).
* `str`, une chaîne de caractère, toujours entre double-guillemets (`"hello world"`).
* `array`, un tableau de valeurs, équivalent à une liste Python (`[8, "foo"]`).
* `object`, l'équivalent plus restreint d'un dictionnaire Python : seules les chaînes de caractères peuvent être utilisées en clés, les types des valeurs sont libres (`{"key": [3, 5]}`).

#### Module `json`

Ce format est exploitable en Python avec le module `json` de la bibliothèque standard.
Le module fournit principalement 4 fonctions : `load`, `loads`, `dump` et `dumps`.
Retenez ces noms de fonctions, ils sont courants en Python et communs à beaucoup de modules de sérialisation.

##### Lecture

`load` est une fonction qui prend en argument un fichier (un objet-fichier ouvert en lecture au préalable) et traite son contenu afin de le renvoyer sous la forme d'un objet Python.
Par exemple, avec le document `pythachu.json` présenté plus haut, nous aurions ceci.

```python
>>> import json
>>> with open('pythachu.json') as f:
...     json.load(f)
... 
{'id': '001', 'name': 'Pythachu', 'type': 'foudre', 'attaques': ['tonnerre', 'charge'], 'base_pv': 50}
```

La fonction nous a renvoyé la représentation en Python de notre objet.

`loads` est similaire à `load` mais reçoit en argument une chaîne de caractères plutôt qu'un fichier (_loads_ pour _load string_). Elle traite donc le contenu directement depuis la chaîne.

```python
>>> json.loads('{"name": "Pythard", "base_pv": null}')
{'name': 'Pythard', 'base_pv': None}
```

Ces fonctions lèveront une exception si l'entrée n'est pas dans un format correct.

```python
>>> json.loads('{42: "foo"}')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  [...]
json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
```

##### Écriture

`dump` et `dumps` sont les fonctions de sérialisation, elles permettent de passer d'un objet Python à sa représentation JSON.

`dumps` reçoit en argument un objet Python et renvoie sa sérialisation sous forme d'une chaîne de caractères.

```python
>>> json.dumps([1, 2, 3, 'foo'])
'[1, 2, 3, "foo"]'
```

`dump` reçoit un objet Python et un fichier (ouvert en écriture), la sérialisation de l'objet sera écrite dans le fichier donné.

```python
with open('output.json', 'w') as f:
    json.dump({'key': 'value'}, f)
```

```json
{"key": "value"}
```
Code: output.json

Ces deux fonctions prennent aussi un argument nommé `indent` qui permet de préciser l'indentation du document de sortie.
Avec `json.dump({'key': 'value'}, f, indent=2)`, nous aurions obtenu le résultat suivant.

```json
{
  "key": "value"
}
```
Code: output.json

L'objet passé en argument se doit d'être composé de types convertibles en JSON, une exception sera levée dans le cas contraire.

```python
>>> json.dumps(1+5j)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  [...]
TypeError: Object of type complex is not JSON serializable
```

#### Avantages et inconvénients

Les avantages de ce format sont qu'il est très répandu et assez lisible, il est donc adapté pour une communication basique entre programmes (notamment des API web) ou pour sauvegarder des données simples (dans les types supportés par le format).

C'est en revanche un format avec une syntaxe assez stricte, qui ne conviendrait pas à une écriture humaine, évitez-le donc pour un fichier de configuration.
Il est assez verbeux et ne se prête pas forcément à des échanges « intenses » entre programmes.
De plus il ne permet pas de représenter tous les objets Python, ce qui peut-être limitant dans certains cas.
