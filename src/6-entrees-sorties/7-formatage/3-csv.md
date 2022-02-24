### Format CSV

Le format CSV (*Comma-Separated Values*) est un format textuel utilisé pour représenter des données tabulaires, comme un tableur.
Chaque ligne du fichier correspondra à une ligne du tableau, et les lignes sont divisées en colonnes selon un séparateur (généralement `,` ou `;`).

Voici un exemple de document CSV :

```csv
nom,type,degats
charge,normal,20
tonnerre,foudre,50
jet-de-flotte,aquatique,40
brûlure,flamme,40
```
Code: attaques.csv

Une première ligne (l'en-tête) identifie les noms des colonnes, elle est facultative, mais il faudra en tenir compte lors de l'analyse du fichier.

Comme en XML, toutes les données du document sont considérées comme du texte, les nombres devront donc être convertis manuellement.

#### Module `csv`

Le module `csv` de la bibliothèque standard offre ce qu'il faut pour traiter un document CSV.

##### Lecture

Le module fournit une fonction `reader` qui permet de lire un document CSV depuis un fichier.  
Elle reçoit donc le fichier en argument[^reader_argument] et renvoie un itérable contenant les lignes du CSV, ces lignes prenant la forme de listes de valeurs.

[^reader_argument]: En réalité tout itérable sur des lignes (chaînes de caractères) est accepté en entrée, un fichier correspond à cette définition.

```pycon
>>> import csv
>>> with open('attaques.csv') as f:
...     reader = csv.reader(f)
...     for row in reader:
...         print(row)
...
['nom', 'type', 'degats']
['charge', 'normal', '20']
['tonnerre', 'foudre', '50']
['jet-de-flotte', 'aquatique', '40']
['brûlure', 'flamme', '40']
```

Comme on le voit notre en-tête est considérée comme une ligne à part entière.
Il serait néanmoins possible de l'isoler en utilisant par exemple la fonction `next` de Python (je reviendrai plus tard sur cette fonction).

```pycon
>>> with open('attaques.csv') as f:
...     reader = csv.reader(f)
...     header = next(reader)
...     print('en-tête:', header)
...     for row in reader:
...         print(row)
...
en-tête: ['nom', 'type', 'degats']
['charge', 'normal', '20']
['tonnerre', 'foudre', '50']
['jet-de-flotte', 'aquatique', '40']
['brûlure', 'flamme', '40']
```

Mais encore mieux, le module offre aussi l'utilitaire `DictReader`.
Celui-ci s'utilise de la même manière que `reader`, mais il consomme directement l'en-tête et produit les lignes sous forme de dictionnaires plutôt que de listes (utilisant les valeurs de l'en-tête comme clés).

```pycon
>>> with open('attaques.csv') as f:
...     reader = csv.DictReader(f)
...     for row in reader:
...         print(row)
... 
{'nom': 'charge', 'type': 'normal', 'degats': '20'}
{'nom': 'tonnerre', 'type': 'foudre', 'degats': '50'}
{'nom': 'jet-de-flotte', 'type': 'aquatique', 'degats': '40'}
{'nom': 'brûlure', 'type': 'flamme', 'degats': '40'}
```

##### Écriture

On trouve de manière similaire une fonction `writer` recevant un fichier (ouvert en écriture) pour y écrire des données tabulaires au format CSV.
Cette fonction renvoie un objet possédant une méthode `writerow` qui sera appelée pour l'écriture de chaque ligne.

```pycon
>>> with open('monstres.csv', 'w') as f:
...     writer = csv.writer(f)
...     writer.writerow(['nom', 'type', 'pv']) # en-tête
...     writer.writerow(['pythachu', 'foudre', '100'])
...     writer.writerow(['ponytha', 'flamme', '150'])
... 
13
21
20
```

Chaque appel renvoie le nombre d'octets écrits dans le fichier.

Le code précédent produit donc le fichier suivant.

```csv
nom,type,pv
pythachu,foudre,100
ponytha,flamme,150
```
Code: monstres.csv

On notera que l'objet possède aussi une méthode `writerows` pour écrire plusieurs lignes en une fois (en prenant en argument une liste de lignes).

De même, le module propose aussi `DictWriter` pour écrire des lignes depuis un dictionnaire.  
Le `DictWriter` doit être appelé avec en arguments le fichier de sortie mais aussi la ligne d'en-tête, qui servira à extraire les bonnes valeurs des dictionnaires.
La ligne d'en-tête en elle-même sera écrite en appelant la méthode `writeheader` de l'objet.

Ainsi, notre code précédent est équivalent à :

```python
with open('monstres.csv', 'w') as f:
    writer = csv.DictWriter(f, ['nom', 'type', 'pv'])
    writer.writeheader()
    writer.writerow({'nom': 'pythachu', 'type': 'foudre', 'pv': '100'})
    writer.writerow({'nom': 'ponytha', 'type': 'flamme', 'pv': '150'})
```

##### Dialectes

Une particularité du CSV est de supporter plusieurs dialectes, car différents outils apportent au format leurs propres spécifications.
`,` n'est pas toujours le séparateur de colonnes par exemple.
Le dialecte définit aussi quels caractères d'échappement utiliser dans différents contextes.

Ainsi, toutes les fonctions que nous avons vu acceptent un argument nommé `dialect` qui permet de choisir le dialecte à utiliser (il s'agit d'`'excel'` par défaut), ou directement des arguments correspondant aux options à définir (`delimiter`, `quotechar`, `escapechar`, etc.).

#### Avantages et inconvénients

Le format CSV a l'intérêt d'être interopérable, malgré ses multiples dialectes qui peuvent rendre son utilisation confuse.
Il est néanmoins assez lisible et facile d'utilisation.

C'est par contre un format assez limité qui ne permet que de représenter des données tabulaires simples (peu adapté pour formater des données arborescentes) et qui ne permet pas de typer ses valeurs.
