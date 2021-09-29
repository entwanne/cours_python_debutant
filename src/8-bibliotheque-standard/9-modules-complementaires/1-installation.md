### Installation

Il existe plusieurs manières d'installer des modules complémentaires en Python.

D'abord, ils peuvent être installés au niveau du système d'exploitation, notamment si celui-ci met à disposition un gestionnaire de paquets.
Sous Ubuntu on trouve ainsi un paquet `python3-numpy` dans `apt` pour installer la bilbiothèque Python `numpy` par exemple.  
Sous Windows, on trouvera parfois des fichiers `.exe` permettant d'installer des modules particuliers.

Ces installations se font au niveau du système, les bibliothèques deviennent alors disponibles depuis n'importe où sur l'ordinateur.

On trouve aussi des suites logicielles, telles que Anaconda (voir [ce tutoriel sur Zeste de Savoir](https://zestedesavoir.com/tutoriels/1448/installer-un-environnement-de-developpement-python-avec-conda/)), qui viennent directement avec un ensemble de paquets tiers pour un usage particulier (ici des bibliothèques dédiées au calcul scientifique) et ainsi en simplifier l'installation.

Mais ces solutions sont assez dépendantes du système utilisé, et il devient difficile de simplement dire « mon code a besoin du module _potjevleesch_ pour fonctionner » si son installation est différente sur chaque machine.

Heureusement, Python fournit un outil pour simplifier et unifier tout cela : `pip` !
