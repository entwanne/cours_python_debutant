### Éditer un fichier Python

Pour ouvrir un fichier avec IDLE, il suffit de cliquer sur le menu _File_ > _New File_ (ou utiliser le raccourci ||Ctrl+N||).
Il est aussi possible d'ouvrir un fichier existant avec _Open File_ (||Ctrl+O||).
Cele ouvrira une nouvelle fenêtre à côté de l'interpréteur interactif.

Vous vous retrouvez alors face à une fenêtre blanche, où il est possible d'entrer du texte, ou plutôt du code Python.
On peut par exemple écrire le contenu suivant :

```python
8 + 5
3 * 7
```
Code: calc.py

Là, vous pouvez rédiger votre code Python puis enregistrer le fichier avec l'option _Save_ du menu (||Ctrl+S||).
Pensez à nommer votre fichier avec une extension `.py`.
Dans mon cas j'ai choisi `calc.py` comme nom de fichier.

Nous commençons simple pour le moment avec un simple calcul comme nous le faisions dans le chapitre précédent.
Nos fichiers de code s'étofferont avec le temps pour devenir des programmes plus complets, mais `calc.py` est déjà un programme Python à part entière, qui ne permet que de calculer le résultat de simples calculs.

--------------------

C'est à peu près le même fonctionnement si vous utilisez Geany comme éditeur de texte, vous trouvez le même genre d'options pour ouvrir un nouveau fichier, ouvrir un fichier existant et enregistrer le fichier courant, dans le menu _Fichier_.

#### En-têtes de fichier

Cependant il est aussi possible d'ajouter des lignes d'en-tête à notre fichier.
Il s'agit d'instructions spéciales que l'on place au tout début du fichier, avant les premières lignes de code.

[[i]]
| Ces en-têtes sont facultatives et concernent des cas particuliers qui sont décrits dans les paragraphes qui suivent.
| Elles pourront simplement vous être utiles si par la suite vous vous trouvez dans l'un des cas concernés.
|
| Aussi, pour simplifier les exemples donnés dans la suite du cours, je n'y ferai jamais figurer ces en-têtes.

##### Shebang

La première dont je veux vous parler est ce qu'on appelle le _shebang_.
C'est une instruction qui permet à certains systèmes (Linux notamment) de reconnaître un fichier exécutable comme un programme Python (ou plus précisément de savoir avec quoi lancer cet exécutable).  
Celle-ci n'est utile que pour le ou les fichiers principaux d'un projet Python, ceux qui seront amenés à être exécutés directement.

Le _shebang_ est une ligne qui prend la forme suivante, vous verrez parfois `python3` à la place de `python`.

```python
!#/usr/bin/env python
```

##### Encodage

La seconde est la déclaration de l'encodage du fichier, qui permet à Python de savoir comment le décoder.
En effet notre ordinateur est rudimentaire et ne sait pas ce qu'est du texte, de son point de vue il ne manipule que des nombres.

Un encodage c'est une règle qui lui décrit comment convertir chaque caractère utilisé dans le fichier (notamment les caractères spéciaux et les lettres accentuées) en nombres.  
Aujourd'hui l'encodage le plus courant est UTF-8, et c'est celui que je vous recommande d'utiliser pour vos fichiers.
Il est utilisé par défaut par Python, ainsi que dans IDLE et Geany.

Mais certains systèmes d'exploitation (Windows pour ne pas le citer) pourraient ne pas l'utiliser par défaut, et si c'est le cas de votre éditeur de texte, alors il faudra préciser à Python quel encodage utiliser pour lire le fichier.  
Cela se fait à l'aide d'une ligne telle que :

```python
# coding: xxx
```

Ou `xxx` serait remplacé par l'encodage utilisé dans le fichier (`utf-8`, `latin-1`, `windows_1252`, etc.).
