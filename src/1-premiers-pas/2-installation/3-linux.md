### Installation sous GNU/Linux

Si vous utilisez Linux, il est probable que Python soit déjà installé sur votre système, car il est nécessaire à certains outils d'administration.
Mais il se peut qu'il ne soit pas installé dans la bonne version.

Pour savoir s'il est déjà installé, vous pouvez entrer la commande `python -V` ou `python3 -V` dans un terminal et vous assurer de voir apparaître un message `Python 3.x.y`

#### Ubuntu / Debian / Linux Mint

Sur la distribution Debian et ses dérivées, le gestionnaire de paquets est `apt` et le paquet dédié à Python 3 se nomme `python3`.
Il vous faudra les droits administrateur pour l'installer au niveau du système.

Si vous utilisez un gestionnaire de paquets graphique, il vous suffit de faire une recherche sur `python3` et d'installer le paquet correspondant.

Sinon cela peut aussi se faire à l'aide des commandes suivantes.

```sh
sudo apt update
sudo apt install python3
```

La première commande ne sert qu'à mettre à jour l'index des dépôts pour éviter toute surprise.

[[a]]
| Sur ces distributions, il faudra utiliser la commande `python3` plutôt que simplement `python` pour invoquer la version 3 de Python.

#### Fedora

Sur Fedora, vous pouvez installer le paquet `python` à l'aide du gestionnaire `dnf`.
Vous aurez pour cela besoin des droits administrateurs.

```sh
dnf install python
```

#### Archlinux

Sur Archlinux, `python` est présent dans les dépôts du gestionnaire de paquets `pacman`.
Vous pouvez l'installer avec la commande suivante, qui nécessite les droits administrateurs.

```sh
pacman -Sy python
```

#### Autres distributions

Pour les autres distributions Linux, vous pouvez vous référer à votre gestionnaire de paquets pour trouver un paquet `python` ou `python3`.

Dans le cas échéant, il est toujours possible de télécharger Python depuis ses sources [sur la page des téléchargements](https://www.python.org/downloads/) : sélectionnez la version voulue puis cliquez sur le lien « Download », vous pouvez alors télécharger le fichier « Gzipped source tarball » au format gzip.
Il faudra ensuite suivre la procédure pour compiler Python : <https://docs.python.org/fr/3/using/unix.html#building-python>.
