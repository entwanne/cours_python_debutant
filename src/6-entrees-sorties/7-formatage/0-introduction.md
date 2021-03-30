## Formater les données

On a vu comment ouvrir des fichiers et y écrire du texte, mais toutes les données que nous manipulons ne sont pas du textes.
Bien sûr il est possible de les convertir, c'est d'ailleurs ce que fait la fonction `print` sur ce qu'elle reçoit, mais comment conserver une structure des données ?

Par exemple pour notre sauvegarde il va nous falloir enregistrer l'état du jeu, tout ce qui différencie la partie en cours d'une autre : les noms des monstres et leurs points de vie.
Il s'agit donc de données de types différents (chaînes de caractères, nombres) qu'il va nous falloir représenter, en utilisant pour cela un format de données adéquat.
Le format est une notion un peu abstraite qui explique de quelle manière les données doivent être traitées, comment elles peuvent être reconstruites à partir de leur représentation.

Tous les fichiers que l'on utilise représentent leurs données selon un certain format, et tous les formats ne permettent pas de stocker la même chose, ils ont chacun leurs particularités.
On ne représente pas une image de la même manière qu'une musique par exemple.

On appelle sérialisation l'opération qui permet de transformer en texte des données structurées, de façon à pouvoir reconstruire ces données ensuite.
À l'inverse, cette reconstruction s'appelle une désérialisation. On parle aussi de _parsing_ pour qualifier l'analyse syntaxique du texte et l'extraction des données.
