### Arguments variadiques

* `*args`, `**kwargs`

Vous pensiez avoir tout vu sur les arguments ? Que nenni !
Certaines fonctions que nous utilisons couramment exploitent encore des fonctionnalités inconnues.

Si je vous demandais par exemple de recoder la fonction `print`, comment procéderiez-vous ?
Pour rappel, la fonction permet de recevoir un nombre variable d'arguments.

```python
>>> print()

>>> print(1)
1
>>> print(1, 2, 3)
1 2 3
```

On pourrait essayer de placer plusieurs paramètres optionnels à la suite mais on ne couvrirait jamais tous les cas : si l'on créait une fonction avec 10 paramètres optionnels il ne serait pas possible de l'appeler avec 11 arguments.

Il doit donc y avoir autre chose, une manière de gérer un nombre variable d'arguments : les arguments variadiques !

* _unpacking_

Ce chapitre lui-même ne vous présente pas toutes les possibilités des arguments et paramètres en Python, aussi je vous invite à consulter les liens suivants :

*