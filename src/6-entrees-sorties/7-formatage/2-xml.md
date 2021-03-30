### Format XML

Le XML (pour *eXtensible??? Markup Language*) est un format assez ancien toujours couramment utilisé (SVG, XHTML).

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

* Lecture du XML
    * Récupération du nœud racine
    * Accès aux attributs
    * Itération sur les enfants
    * Accès au texte
    * Parcours récursif
    * Erreurs de parsing
* Construction/écriture d'un XML
    * Création de balises, attributs
    * Ajout d'enfants, de texte
    * Dump

* Différents types de parseurs (SAX)
* Ressources complémentaires sur le XML
    * XML, namespaces, schémas de validation, XSLT, XPath
* Module `lxml`

#### Avantages et inconvénients

Son ancienneté et les technologies autour (XMLSchema, XSLT, XPath) sont les forces de ce format plutôt décrié pour sa verbosité et sa relative illisibilité.  
Un autre avantage se situe au niveau des diverses technologies de _parsing_, notamment le SAX plutôt adapté aux gros documents et à la réception de données au fil de l'eau.

Mais le gros point noir d'un point de vue Python est clairement relatif à ces technologies, il est difficile de savoir par où commencer et de manipuler un document XML, là où JSON est très simple d'utilisation.
