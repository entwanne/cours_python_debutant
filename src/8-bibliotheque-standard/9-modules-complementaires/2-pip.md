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
  Downloading Pillow-8.3.2-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.0 MB)
     |████████████████████████████████| 3.0 MB 2.9 MB/s 
Installing collected packages: Pillow
Successfully installed Pillow-8.3.2
```

Le paquet sera alors installé par défaut pour l'utilisateur courant (ou pour tout le système si la commande est exécutée avec les droits d'administration).

[[a]]
| Attention aux paquets frauduleux.
| Il peut arriver que certains paquets imitent le nom de paquets connus pour diffuser du code malicieux.
| Assurez-vous donc de toujours utiliser le nom clairement défini sur le site officiel.

Il est aussi possible de spécifier une version précise du paquet à l'aide de la syntaxe `paquet==version`, par exemple `pip install Pillow==8.3.2`.
On peut aussi préciser plusieurs paquets à la suite à installer.

À l'inverse, on peut supprimer un paquet installé à l'aide de la commande `uninstall`.
La désisntallation demandera une confirmation (`y`) pour supprimer le paquet.

```sh
% pip uninstall Pillow
Found existing installation: Pillow 8.3.2
Uninstalling Pillow-8.3.2:
  Would remove:
    ...
Proceed (Y/n)? y
  Successfully uninstalled Pillow-8.3.2
```

Il est aussi possible de lister les paquets installés avec `pip list`.

Par défaut, `pip` fait appel à l'index _PyPI_ (_Python Package Index_) pour trouver les paquets à installer, c'est le dépôt officiel des paquets Python, qui peut être consulté à cette URL : <https://pypi.org/>.

Il est possible sur le site de faire des recherches sur l'index ou d'explorer les projets pour retrouver des paquets.
Chaque paquet vient avec une page de description et un ensemble de métadonnées.
Voici par exemple [la page du paquet `Pillow`](https://pypi.org/project/Pillow/).

--------------------

Pour plus d'informations au sujet de _Pip_, vous pouvez vous reporter au [guide officiel](https://docs.python.org/fr/3/installing/index.html).
