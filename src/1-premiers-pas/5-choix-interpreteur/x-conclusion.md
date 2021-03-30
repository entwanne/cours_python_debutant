### Conclusion

Les deux modes ont leurs avantages et leurs inconvénients, il convient donc de tirer partie des deux.
De plus ils ne sont pas exclusifs, il est ainsi possible de lancer l'interpréteur avec l'option `-i` sur un fichier, pour obtenir un interpréteur interactif à la suite de l'exécution d'un fichier.
Ce qui est bien pratique pour vérifier un résultat dans un programme en cours de développement.

L'option `-c` de l'interpréteur est aussi utile pour lancer l'interpréteur et exécuter une simple ligne.

```sh
$ python -c 'print(1+5)'
6
```

Dans ce tutoriel, j'utiliserais toujours les signes `>>>` pour présenter les codes exécutés dans l'interpréteur interactif, et donc suivis du résultat affiché.
Les autres codes seront considérés comme écrits dans des fichiers.
