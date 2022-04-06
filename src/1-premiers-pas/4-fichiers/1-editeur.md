### Éditer un fichier Python

Pour ouvrir un fichier avec IDLE, il suffit de cliquer sur le menu _File_ > _New File_ (ou utiliser le raccourci ||Ctrl+N||).
Il est aussi possible d'ouvrir un fichier existant avec _Open File_ (||Ctrl+O||).
Cela ouvrira une nouvelle fenêtre à côté de l'interpréteur interactif.

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

Nous commençons simple pour le moment avec deux calculs faciles comme nous le faisions dans le chapitre précédent.
Nos fichiers de code s'étofferont avec le temps pour devenir des programmes plus complets, mais `calc.py` est déjà un programme Python à part entière, qui ne permet que de calculer le résultat de simples opérations.

--------------------

C'est à peu près le même fonctionnement si vous utilisez Geany comme éditeur de texte, vous trouvez le même genre d'options pour ouvrir un nouveau fichier, ouvrir un fichier existant et enregistrer le fichier courant, dans le menu _Fichier_.

#### En-têtes de fichier

Dans certains cas d'usage, si par la suite vous rencontrez des problèmes avec des caractères accentués par exemple, il peut être utile de définir des en-têtes à notre fichier Python.

Ce sont des données associées au fichier qui permettront à Python et au système d'exploitation d'interpréter correctement son contenu.

Je vous indique alors [cette section en annexe](https://zestedesavoir.com/tutoriels/2514/un-zeste-de-python/10-annexes/2-notes-diverses/#1-1-entetes) qui vous en dira plus.
