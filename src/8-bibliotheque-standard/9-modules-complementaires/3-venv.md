### Environnements virtuels

En utilisant _Pip_ comme nous venons de le faire, les paquets sont installés au niveau du système ou de l'utilisateur.
C'est accommodant parce que le paquet est alors disponible partout et utilisable par tous les projets, mais cela peut parfois poser problème.

En effet, une seule version d'un paquet peut être disponible à la fois, ce qui fait que tous les projets doivent partager cette même version.
Impossible alors pour un projet de bénéficier des évolutions récentes d'un module complémentaire si un autre projet dépend d'une version plus ancienne.

Pour résoudre ce problème, on va chercher à cloisonner nos applications, afin qu'elles gardent leurs dépendances (les modules complémentaires qu'elles doivent installer) auprès d'elles plutôt que de les installer sur tout le système.
Et cela se fait à l'aide des environnements virtuels.

Un environnement virtuel n'est ni plus ni moins qu'un répertoire cloisonné de bibliothèques Python.
On peut donc avoir autant d'environnements virtuels que l'on veut sur le système, qui contiendront chacun leurs bibliothèques dans les versions qu'ils veulent.  
Mais bien sûr, dans un même environnement, une bibliothèque ne pourra être installée qu'en un seul exemplaire (donc une seule version).

Pour créer un nouvel environnement, on utilise la commande _shell_ `python -m venv` suivie d'un nom, souvent `env` ou `venv`.
Ce nom correspond au nom du répertoire qui sera créé pour l'environnement, depuis le répertoire courant donc.  
On fera en sorte d'utiliser le répertoire du projet comme répertoire courant.

```sh
% python -m venv env
```

Cette commande a donc créé un dossier `env` dans le répertoire courant.
Pour l'instant cet environnement est juste créé, mais pour l'utiliser nous devons l'activer.

Cela se fait à l'aide de la commande `source XXX/bin/activate` sous Linux/Mac ou `XXX\\Scripts\\Activate.ps1` sous Windows.
Avec `XXX` remplacé par le nom du répertoire de l'environnement, `env` dans notre cas.

```sh
% source env/bin/activate
(env) % 
```

On voit que le _prompt_ de notre _shell_ est maintenant préfixé d'un `(env)` pour signifier que nous sommes à l'intérieur de l'environnement.

Toutes les commandes que nous exécuterons maintenant (notamment les `pip install`) le seront à l'intérieur de cet environnement et n'affecteront pas le reste du système.

[[i]]
| Il est nécessaire d'activer l'environnement virtuel chaque fois que vous ouvrez un nouveau terminal pour pouvoir l'utiliser.

Une fois votre travail terminé, si vous souhaitez sortir de l'environnement virtuel, vous pouvez utiliser la commande `deactivate`.

```sh
(env) % deactivate
%
```

Vous pouvez consulter [la page de documentation du module `venv`](https://docs.python.org/fr/3/library/venv.html) pour de plus amples informations à son sujet.
