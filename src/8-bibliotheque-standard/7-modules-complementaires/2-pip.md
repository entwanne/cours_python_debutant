### Pip, le gestionnaire de paquets Python

_Pip_ est un gestionnaire de paquets spécialement dédié à l'installation de modules complémentaires pour Python.
Il est normalement inclus dans toute installation récente de Python.
Vous pouvez vous en assurer en essayant d'exécuter la commande `python -m pip` (ou `python3 -m pip`, voire `py -m pip` sur Windows) depuis un terminal (pas depuis une console Python).

[[i]]
| Si toutefois ce n'était pas le cas, regardez si un paquet `python-pip` ou `python3-pip` existe dans le gestionnaire de paquets de votre système que vous pourriez installer.  
| Sinon, vous pouvez exécuter la commande `python3 -m ensurepip --default-pip` (`py -m ensurepip --default-pip` sous Windows) pour demander à Python d'installer le nécessaire.

Pip peut donc être invoqué via la commande _shell_ `python -m pip` (`py -m pip` sous Windows), ou par le simple raccourci `pip`.

L'outil comprend plusieurs commandes, notamment la commande `install` pour installer un paquet, suivie du nom du paquet à installer.
Ce nom sera généralement inscrit sur les sites officiels des bibliothèques que vous souhaitez installer.

```sh
% pip install Pillow
Collecting Pillow
  Downloading Pillow-9.0.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (4.3 MB)
     |████████████████████████████████| 4.3 MB 1.7 MB/s 
Installing collected packages: Pillow
Successfully installed Pillow-9.0.1
```

Le paquet sera alors installé par défaut pour l'utilisateur courant (ou pour tout le système si la commande est exécutée avec les droits d'administration).

[[a]]
| Attention aux paquets frauduleux.
| Il peut arriver que certains paquets imitent le nom de paquets connus pour diffuser du code malicieux.
| Assurez-vous donc de toujours utiliser le nom clairement défini sur le site officiel.

Il est aussi possible de spécifier une version précise du paquet à l'aide de la syntaxe `paquet==version`, par exemple `pip install Pillow==9.0.1`.
C'est la méthode conseillée dans votre répertoire de travail pour être sûr de la version utilisée.  
On peut même préciser plusieurs noms de paquets à installer derrière `pip install`.

`pip install` accepte aussi une option `-r` suivie d'un nom de fichier, ce fichier devant contenir les dépendances à installer dans une syntaxe comprise par `pip install` :

```text
Pillow==9.0.1
pyglet
```
Code: `requirements.txt`

```sh
% pip install -r requirements.txt
Collecting Pillow
  Using cached Pillow-9.0.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (4.3 MB)
Collecting pyglet==1.5.22
  Downloading pyglet-1.5.22-py3-none-any.whl (1.1 MB)
     |████████████████████████████████| 1.1 MB 2.8 MB/s 
Installing collected packages: pyglet, Pillow
Successfully installed Pillow-9.0.1 pyglet-1.5.22
```

À l'inverse, on peut supprimer un paquet installé à l'aide de la commande `uninstall`.
La désisntallation demandera une confirmation (`y`) pour supprimer le paquet.

```sh
% pip uninstall Pillow
Found existing installation: Pillow 9.0.1
Uninstalling Pillow-9.0.1:
  Would remove:
    ...
Proceed (Y/n)? y
  Successfully uninstalled Pillow-9.0.1
```

Il est aussi possible de lister les paquets installés avec `pip list`.

```sh
% pip list
Package    Version
---------- -------
Pillow     9.0.1
pip        21.2.4
pyglet     1.5.22
setuptools 58.1.0
```

`pip freeze` permet quant à lui d'extraire la liste des paquets installés dans une syntaxe comprise par `pip install`.

```sh
% pip freeze
Pillow==9.0.1
pyglet==1.5.22
```

[[i]]
| Il est ainsi courant d'utiliser la liste renvoyée par `pip freeze` pour former un fichier `requirements.txt` qui pourra ensuite permettre de réinstaller à l'identique ces mêmes dépendances dans un autre environnement à l'aide d'un `pip install -r requirements.txt`.  
| Cela permet d'avoir un environnement reproductible d'une machine à l'autre.

Par défaut, `pip` fait appel à l'index _PyPI_ (_Python Package Index_) pour trouver les paquets à installer, c'est le dépôt officiel des paquets Python, qui peut être consulté à cette URL : <https://pypi.org/>.

Il est possible sur le site de faire des recherches sur l'index ou d'explorer les projets pour retrouver des paquets.
Chaque paquet vient avec une page de description et un ensemble de métadonnées.
Voici par exemple [la page du paquet `Pillow`](https://pypi.org/project/Pillow/).

--------------------

Pour plus d'informations au sujet de _Pip_, vous pouvez vous reporter au [guide officiel](https://docs.python.org/fr/3/installing/index.html).
