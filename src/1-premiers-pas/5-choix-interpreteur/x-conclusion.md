### Conclusion

Les deux modes ont leurs avantages et leurs inconvénients, il convient donc de tirer partie des deux.  
De plus ils ne sont pas exclusifs, il est ainsi possible de lancer l'interpréteur avec l'option `-i` sur un fichier, pour obtenir un interpréteur interactif à la suite de l'exécution d'un fichier.
Ce qui est bien pratique pour vérifier un résultat dans un programme en cours de développement.

Par exemple si on reprend le fichier suivant :

```python
print(8 + 5)
print(3 * 7)
```
Code: calc.py

On peut l'exécuter avec l'option `-i` et continuer à utiliser l'interpréteur à la suite du fichier.

```sh
% python -i calc.py
13
21
>>> 1 / 2
0.5
```

Son utilité n'apparaît peut-être pas flagrante pour le moment, mais ça nous sera utile quand nous aurons des fichiers plus complets et que nous voudrons y tester une valeur en particulier.

--------------------

L'option `-c` de l'interpréteur est aussi utile pour lancer l'interpréteur et exécuter une simple ligne.

```sh
$ python -c 'print(1+5)'
6
```

Dans ce tutoriel, j'utiliserai toujours les signes `>>>` pour présenter les codes exécutés dans l'interpréteur interactif, et donc suivis du résultat affiché.
Les autres codes seront considérés comme écrits dans des fichiers.
