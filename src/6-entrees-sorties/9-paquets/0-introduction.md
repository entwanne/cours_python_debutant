## Les paquets

Les paquets (ou _packages_) forment une entité hiérarchique au-dessus des modules : un paquet est un module qui contient d'autre modules, un peu comme un dossier contient des fichiers.  
D'ailleurs, les paquets prennent généralement la forme de dossiers sur le système de fichiers.

On en a déjà rencontré pendant ce cours : souvenez-vous du module `xml.etree.ElementTree` : il s'agissait en fait d'un module `ElementTree` dans un paquet `xml.etree`.
On comprend par la même occasion qu'`etree` est lui-même imbriqué dans un paquet `xml`, car les paquets sont hiérarchiques.
