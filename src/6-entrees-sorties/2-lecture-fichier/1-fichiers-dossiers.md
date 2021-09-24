### Fichiers et dossiers sur l'ordinateur

Pour rappel, un ordinateur organise ses données en fichiers.
Il existe des fichiers de tous types : des images, des fichiers de code, des musiques, etc.
Un fichier représente un document bien précis sur l'ordinateur.

Chaque fichier se situe dans un dossier (ou répertoire). On peut voir les dossiers comme des classeurs où seraient rangés les fichiers.  
Ces dossiers forment une structure hiérarchique sur l'ordinateur : un dossier peut contenir d'autres dossiers, comme des intercalaires dans un classeur, ou des classeurs sur une étagère.  
Un fichier appartient alors à un dossier, qui lui-même appartient à un dossier parent, etc. jusqu'à atteindre la racine du système de fichiers.

Pour retrouver un fichier, il est alors courant d'utiliser son chemin. Il s'agit de la hiérarchie de dossiers à parcourir puis du nom du fichier en question. Ce chemin est unique.
C'est ce chemin que nous utiliserons dans nos programmes pour accéder aux fichiers.

Sous Windows, un chemin sera généralement de la forme `C:\chemin\vers\mon\fichier.txt` où `C:\` représente la racine du système de fichiers.  
Sous Linux on verra plutôt `/chemin/vers/mon/fichier.txt` (où `/` est la racine).

On dit que ce chemin est le chemin absolu vers le fichier, car il débute par la racine du système, qui permet donc de le retrouver depuis n'importe où.

Mais il est aussi possible de préciser le chemin d'un fichier à partir d'un autre répertoire, on parle alors de chemin relatif.  
Par exemple, depuis le répertoire `C:\chemin\vers` (ou `/chemin/vers`), le chemin relatif de notre fichier est `mon\fichier.txt` (ou `mon/fichier.txt`).
Il s'agit du chemin restant à parcourir pour trouver le fichier.

En programmation, nous exécuterons toujours notre code depuis un répertoire particulier, que l'on appellera répertoire courant (généralement le dossier dans lequel sont stockés les fichiers de code).
Nous pourrons ainsi référencer nos fichiers par leur chemin absolu, ou par leur chemin relatif par rapport à ce répertoire.

[[i]]
| Il est aussi possible dans un chemin relatif d'accéder à un fichier d'un répertoire parent, à l'aide de la syntaxe `..`.  
| Par exemple depuis le répertoire `C:\chemin\vers\toto` (`/chemin/vers/toto`), on peut accéder à notre fichier `fichier.txt` via le chemin relatif `..\mon\fichier.txt` (`../mon/fichier.txt`).
