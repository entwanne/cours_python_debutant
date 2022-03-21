### En-têtes de fichiers

Il est possible d'ajouter des lignes d'en-tête à nos fichiers Python.
Il s'agit d'instructions spéciales que l'on place au tout début du fichier, avant les premières lignes de code.

[[i]]
| Ces en-têtes sont facultatives et concernent des cas particuliers qui sont décrits au long du cours.
| Elles pourront simplement vous être utiles si par la suite vous vous trouvez dans l'un des cas concernés.
|
| Aussi, pour simplifier les exemples donnés dans le cours, je n'y ferai jamais figurer ces en-têtes.

##### Shebang

La première dont je veux vous parler est ce qu'on appelle le _shebang_.
C'est une instruction qui permet à certains systèmes (Linux notamment) de reconnaître un fichier exécutable comme un programme Python (ou plus précisément de savoir avec quoi lancer cet exécutable).  
Celle-ci n'est utile que pour le ou les fichiers principaux d'un projet Python, ceux qui seront amenés à être exécutés directement.

Le _shebang_ est une ligne qui prend la forme suivante, vous verrez parfois `python3` à la place de `python`.

```python
#!/usr/bin/env python
```

Elle définit quel programme utiliser pour exécuter le fichier.
Ici on fait appel à la commande `env` pour localiser le programme `python` et c'est ce dernier qui exécutera notre fichier.

On trouve parfois aussi `!#/usr/bin/python` qui stipule directement le chemin du programme Python mais est moins portable d'un environnement à un autre.

Cela permet ensuite pour un fichier Python `programme.py` disposant des droits d'exécution (`chmod +x programme.py`) d'être exécuté à l'aide d'un simple `./programme.py` depuis le répertoire courant.

```sh
% ./programme.py
Hello World!
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

Où `xxx` serait remplacé par l'encodage utilisé dans le fichier (`utf-8`, `latin-1`, `windows_1252`, etc.).
