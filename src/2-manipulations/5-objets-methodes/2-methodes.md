### Méthodes

Les actions sur les objets sont plus généralement appelées des méthodes.

Elles sont très similaires aux fonctions, si ce n'est qu'elles appartiennent à un type et donc s'appliquent sur des objets en particulier (sur les objets de ce type).

Pour appeler une méthode sur une valeur, on fait suivre cette valeur d'un point puis du nom de la méthode, et enfin d'une paire de paranthèses comme pour les appels de fonction.
On récupère de la même manière la valeur de retour de la méthode lors de l'évaluation de l'expression.

Par exemple la méthode `strip` du type `str` permet de renvoyer la chaîne de caractères en retirant les espaces présents au début et à la fin.

```pycon
>>> '   hello '.strip()
'hello'
```

Pour que l'expression ait un sens, il faut bien sûr que la méthode existe pour cet objet.
On obtient une erreur dans le cas contraire.

```pycon
>>> 'hello'.toto()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'toto'
```
