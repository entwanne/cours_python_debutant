### Interpréteur interactif

Ainsi, comme nous l'avons vu dans le chapitre précédent, nous pouvons exécuter l'interpréteur interactif à l'aide du programme IDLE, ou de la commande `python` dans un terminal.

Vous vous retrouvez maintenant face à ce que l'on appelle une invite de commande.
Cela se reconnaît par les `>>>` en début de ligne, qu'on appelle le _prompt_.
L'interpréteur attend que vous lui demandiez quelque chose.

Mais quoi ? Pour commencer, je vous propose d'entrer un nombre, Python le comprendra.

```python
>>> 12
12
```

![Exécution dans l'interpréteur interactif.](img/idle_exec.png)

Nous avons demandé à Python d'exécuter le code `12`, il a répondu 12.
Ce qu'on ne voit pas, c'est que Python a évalué le code que nous avons entré. Il l'a analysé et en a calculé le résultat.
Puis il a affiché ce résultat pour que nous en ayons connaissance.

Ainsi, Python nous dit que `12` vaut `12`. Merci Python !

[[i]]
| Notez que lorsqu'au long de ce cours je vous présenterai un code sous la forme suivante :
|
| ```python
| >>> foo
| bar
| ```
|
| Cela signifie qu'il faut exécuter le code `foo` dans l'interpréteur Python et que celui-ni nous affiche alors `bar`.  
| J'utiliserai donc cette notation avec des chevrons pour présenter des exemples de l'interpréteur interactif.
