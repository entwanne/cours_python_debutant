### Format XML

Le XML (pour *eXtensible Markup Language*) est un format assez ancien toujours couramment utilisé (SVG, XHTML, docx, ODT).

C'est un langage dit de balisage, formé de différentes balises imbriquées.
Il se présente comme suit.

```xml
<monster id="001">
  <name>Pythachu</name>
  <type>foudre</type>
  <attaques>
    <attaque>tonnerre</attaque>
    <attaque>charge</attaque>
  </attaques>
  <base_pv>50</base_pv>
</monster>
```
Code: pythachu.xml

On le voit donc, une balise XML s'ouvre par un `<balise>` et se ferme avec un `</balise>`, on peut placer à l'intérieur d'autres balises (qui forment donc la hiérarchie du document) ou du texte.

Il est aussi possible de spécifier des attributs aux balises lors de leur ouverture, comme des métadonnées, avec la syntaxe `<balise attribut="valeur">`.

Un document XML ne comprend que le texte et pas d'autres types de valeurs, il vous faudra donc opérer les conversions manuellement lors du traitement du document.

#### Module `xml`

L'analyse d'un document XML n'est pas aussi simple que celle d'un JSON.
Il n'y a pas un unique module pour le faire, et pas de fonction `load` / `dump`, juste des fonctions pour opérer sur le document et aller extraire des informations à un endroit précis.

Il existe plusieurs modules Python dédiés à l'analyse des documents XML, tous regroupés dans le [module `xml`](https://docs.python.org/fr/3/library/xml.html).
Nous ne nous intéresserons ici qu'au [module `xml.etree`](https://docs.python.org/fr/3/library/xml.etree.elementtree.html).

Pour commencer, on va importer le module `xml.etree.ElementTree` qu'il est courant de simplement appeler `ET`.

```python
import xml.etree.ElementTree as ET
```

##### Lire un fichier XML

Ensuite, on va ouvrir un document XML à l'aide de la fonction `parse` de ce module.
La fonction accepte un chemin de fichier en argument, ou directement un objet-fichier.

```pycon
>>> tree = ET.parse('pythachu.xml')
>>> tree
<xml.etree.ElementTree.ElementTree object at 0x7f6ff11b5f70>
```

[[i]]
| Il est coutume d'appeler `tree` (_arbre_) un document XML, par rapport à sa structure arborescente.

Une fois ce document chargé, on peut en récupérer l'élément principal (le nœud racine) à l'aide de la méthode `getroot`.

```pycon
>>> root = tree.getroot()
>>> root
<Element 'monster' at 0x7f6ff0faaef0>
```

`root` est un objet de type `Element`. Il possède entre autres un attribut `tag` qui référence le nom de la balise, et un attribut `attrib` qui contient le dictionnaire d'attributs de la balise.

```pycon
>>> root.tag
'monster'
>>> root.attrib
{'id': '001'}
```

Notez qu'il existe aussi la fonction `fromstring` pour charger un élément à partir d'une chaîne de caractères.

```pycon
>>> ET.fromstring('<foo>bar</foo>')
<Element 'foo' at 0x7f6ff10e1900>
```

Cette fonction lève une erreur `ParseError` si la chaîne ne représente pas un document XML valide (il en est de même avec la fonction `parse`).

```pycon
>>> ET.fromstring('<foo>bar</foo')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3.9/xml/etree/ElementTree.py", line 1348, in XML
    return parser.close()
xml.etree.ElementTree.ParseError: unclosed token: line 1, column 8
```

Les éléments XML sont des objets Python itérables.
Itérer dessus revient à parcourir les balises filles.

```pycon
>>> for elem in root:
...     print(elem)
... 
<Element 'name' at 0x7f6ff0faaf40>
<Element 'type' at 0x7f6ff0faaf90>
<Element 'attaques' at 0x7f6ff0fad040>
<Element 'base_pv' at 0x7f6ff0fad130>
```

Les éléments possèdent aussi une méthode `find` pour directement trouver une balise fille en fonction de son nom.

```pycon
>>> root.find('name')
<Element 'name' at 0x7f6ff0faaf40>
>>> root.find('attaques')
<Element 'attaques' at 0x7f6ff0fad040>
```

Quand il existe plusieurs éléments du même nom, la méthode `findall` permet de tous les trouver, elle renvoie une liste d'éléments.

```pycon
>>> root.find('attaques').findall('attaque')
[<Element 'attaque' at 0x7f6ff0fad090>, <Element 'attaque' at 0x7f6ff0fad0e0>]
```

Et l'on peut accéder au contenu textuel des éléments à l'aide de leur attribut `text`.

```pycon
>>> root.find('name').text
'Pythachu'
>>> root.find('base_pv').text
'50'
>>> for attack in root.find('attaques').findall('attaque'):
...     print(attack.text)
... 
tonnerre
charge
```

##### Construire un fichier XML

Il est aussi possible de construire un document XML de toute pièce à l'aide d'`etree`.

On peut pour cela commencer par créer un élément racine en instanciant un objet `Element`, en fournissant le nom de la balise comme argument.

```pycon
>>> root = ET.Element('foo')
>>> root
<Element 'foo' at 0x7f2496c4c8b0>
```

On peut ensuite facilement ajouter des éléments à un élément parent avec la fonction `SubElement`.

```pycon
>>> ET.SubElement(root, 'bar')
<Element 'bar' at 0x7f2496c4c8b0>
>>> ET.SubElement(root, 'baz')
<Element 'baz' at 0x7f2496c44f40>
```

Et l'on peut parfaitement ajouter des sous-éléments à un sous-élément, etc.

```pycon
>>> sub = ET.SubElement(root, 'list')
>>> ET.SubElement(sub, 'item')
<Element 'item' at 0x7f2496c619a0>
>>> ET.SubElement(sub, 'item')
<Element 'item' at 0x7f2496b2af90>
```

On peut aussi manipuler directement le dictionnaire d'attributs des éléments pour en ajouter ou en modifier.

```pycon
>>> root.attrib['name'] = 'Doc'
>>> root.attrib
{'name': 'Doc'}
```

De même que l'on peut redéfinir l'attribut `text` pour ajouter du texte à une balise.

```python
root.find('bar').text = 'bonjour'
```

Enfin, le module `ET` possède une fonction `dump` pour transformer en chaîne de caractères l'élément que l'on vient de créer.

```pycon
>>> ET.dump(root)
<foo name="Doc"><bar>bonjour</bar><baz /><list><item /><item /></list></foo>
```

[[i]]
| Notez que les balises telles que `<baz />` sont des balises auto-fermantes.  
| `<baz/>` est équivalent à `<baz></baz>`, c'est simplement une balise qui ne contient ni enfants ni texte.

Il est aussi possible de créer un document (`ElementTree`) et d'appeler sa méthode `write` pour écrire le document dans un fichier.

```pycon
>>> ET.ElementTree(root).write('doc.xml')
```

```xml
<foo name="Doc"><bar>bonjour</bar><baz /><list><item /><item /></list></foo>
```
Code: doc.xml

---------------------

Il y a beaucoup à dire sur le format XML et tout ne pourra pas être décrit ici.
Sachez que c'est un format assez complet, qui comporte des mécanismes de validation (schémas XML), d'espaces de noms (_namespaces_), un sous-langage de requêtage (`XPath`) et tout un écosystème avec des outils de transformation comme XSLT.  
Tous ces termes peuvent vous amener à des ressources complémentaires sur le format XML.

Il est aussi à noter que plusieurs types de parseurs existent pour analyser des documents XML.
L'approche de construction d'un document tel que le fait `etree` n'est pas la seule.  
Il existe par exemple l'approche SAX qui consiste à ne pas construire le document mais à le parcourir et à appeler des fonctions définies par l'utilisateur pour chaque ouverture/fermeture de balise, ce qui permet de ne pas occuper de place en mémoire.

Enfin, sachez qu'il existe en Python une bibliothèque externe, [`lxml`](https://lxml.de/), qui simplifie l'usage des documents XML.

#### Avantages et inconvénients

Son ancienneté et les technologies autour (XMLSchema, XSLT, XPath) sont les forces de ce format plutôt décrié pour sa verbosité et sa relative illisibilité.  
Un autre avantage se situe au niveau des diverses technologies de _parsing_, notamment le SAX plutôt adapté aux gros documents et à la réception de données au fil de l'eau.

Mais le gros point noir d'un point de vue Python est clairement relatif à ces technologies, il est difficile de savoir par où commencer et de manipuler un document XML, là où JSON est très simple d'utilisation.
