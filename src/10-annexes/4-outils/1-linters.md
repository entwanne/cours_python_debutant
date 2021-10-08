### Linters

Un _linter_ est un programme qui permet de vérifier le style des fichiers de code, et notamment qu'ils respectent [les règles énoncées par la PEP8](https://www.python.org/dev/peps/pep-0008/).

La PEP8 est à l'origine une description du style que doivent adopter les développements au sein de Python lui-même, qui s'est popularisée et est maintenant considérée comme un standard pour tous les projets Python.  
Il ne faut cependant pas la voir comme un énoncé de règles strictes, comme dirait un célèbre pirate « c'est plus un guide qu'un véritable réglement ».

#### Flake8

_Flake8_ est donc un outil en ligne de commande permettant de vérifier la conformité avec la PEP8, relevant toutes les _infractions_ trouvées dans les fichiers de code (mauvais espacements, lignes trops longues, etc.).

On installe l'outil par la commande `pip install flake8`, puis il s'utilise via `flake8`, optionellement suivi de répertoires ou de fichiers à explorer (par défaut il explorera tout le répertoire courant).

_Flake8_ est configurable, et permet d'activer ou désactiver certaines règles de style, je vous invite pour cela à consulter [sa page de documentation](https://flake8.pycqa.org/).

#### Pylint

_Pylint_ est un outil qui va plus loin que _Flake8_.
Il ne se contente pas de relever les fautes de style, mais cherche aussi à identifier de potentiels erreurs et problèmes de conception.

L'installation `pip install pylint` fournit un utilitaire `pylint`, que l'on appelle en lui donnant les fichiers à vérifier en arguments.

Il est lui aussi hautement configurable, et je vous renvoie pour cela [à sa documentation](https://pylint.pycqa.org/).

#### Black

_Black_ est un outil relativement récent dont l'objectif est d'unifier les règles de style Python et éviter les querelles de chapelles : il est prévu pour ne pas être configurable et donc appliquer le même style partout.

Après une installation via `pip install black`, on utilise la commande `black` en lui fournissant des fichiers ou répertoires à explorer, que _Black_ se chargera de réécrire selon son style.

[La page de documentation](https://black.readthedocs.io/) du projet vous renseignera davantage sur ses fonctionnalités.

#### isort

_isort_ est un outil d'un autre genre, qui s'occupe de l'ordonnancement des lignes d'import.
On peut lui spécifier une configuration et il se chargera de réordonner de façon logique les imports : d'abord la bibliothèque standard, puis les modules tiers, puis le paquet courant, etc.

Il s'installe en tapant `pip install isort` puis est disponible par la commande `isort` qui prend optionnellement des fichiers ou répertoires en arguments (s'applique à tout le répertoire par défaut).

Pour plus d'informations, rendez-vous [sur la documentation d'_isort_](https://pycqa.github.io/isort/).
