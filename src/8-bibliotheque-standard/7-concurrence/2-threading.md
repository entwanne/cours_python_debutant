### Programmation multi-thread

* Présentation de `threading`
* concurrence
* Limites

Le premier mécanisme que nous allons voir est celui des _threads_, aussi appelés fils d'exécution[^exétron].

[^exétron]: Et plus rarement « exétrons » (pour unités d'exécution).

D'un point de vue système un programme prend la forme d'un processus : c'est une entité qui regroupe les instructions du programme, sa mémoire et un curseur pour se déplacer dans les instructions.  
Chaque processus possède en effet sa propre zone mémoire pour des raisons de sécurité, on ne voudrait pas que notre navigateur web puisse lire la mémoire de notre logiciel de messagerie par exemple.

Mais les processus peuvent aussi se diviser en fils d'exécution (_threads_), chaque fil étant un curseur différent dans les instructions du programme et l'ensemble des fils partageant une mémoire commune.
On a donc ainsi plusieurs tâches qui s'exécutent simultanément au sein d'un même processus.

En Python les fils d'exécution nous permettent de faire de la programmation concurrente.
Ils sont mis en œuvre par le module `threading` de la bibliothèque standard qui fournit l'interface pour les manipuler.

Ce module met à disposition un type `Thread` afin de créer de nouveaux fils.

[[i]]
| Au niveau du système d'exploitation les _threads_ sont un mécanisme de programmation parallèle, pouvant s'exécuter sur différents cœurs du processeur.  
| C'est l'interpréteur Python qui empêche ce parallélisme en ajoutant un verrou global (_Global Interpretor Lock_, ou _GIL_) qui fait qu'un seul fil peut s'exécuter à la fois pour préserver l'intégrité des données manipulées.
