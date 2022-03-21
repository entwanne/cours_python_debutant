### mypy

_mypy_ est un outil d'analyse statique, qui permet de s'assurer du bon comportement d'un programme.

Sans exécuter le code, _mypy_ va _simplement_ l'analyser pour regarder si les opérations qui sont faites sur les données sont cohérentes (via les annotations de types) et ainsi éviter un certain nombre de bugs (par exemple des `ValueError` à l'exécution car un cas aurait été oublié).

Les annotations de types permettent de resteindre l'ensemble de définition des fonctions (via les types de valeurs autorisées) et ainsi mettre en évidence les cas qui ne s'y conforment pas : par exemple si une fonction attend un argument `int` et qu'on l'appelle avec une valeur issue d'une autre fonction qui peut renvoyer un `int` ou `None`, cela soulève un problème car le cas de `None` n'est pas correctement géré.

On installe _mypy_ avec la commande `pip install mypy`, puis on l'exécute en lui fournissant les fichiers à tester : `mypy fichier.py`.
Il s'occupera alors d'analyser le code et de reporter les erreurs qu'il y trouvera.

La correction des erreurs renvoyées est à votre discrétion, vous pouvez choisir de les ignorer si vous savez qu'elles n'ont pas de chance de produire de bug à l'exécution, mais il est alors préférable d'annoter le programme en conséquence pour éviter qu'elles soient relevées.
