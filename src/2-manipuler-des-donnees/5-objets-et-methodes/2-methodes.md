### Méthodes

Les actions sur les objets sont plus généralement appelées des méthodes.

Elles sont très similaires aux fonctions, si ce n'est qu'elles appartiennent à un type et donc s'appliquent sur des objets en particulier.

Pour appeler une méthode sur une valeur, on fait suivre cette valeur d'un point puis du nom de la méthode, et enfin d'une paire de paranthèses comme pour les appels de fonction.
La méthode doit exister sur le type de la valeur pour que l'expression ait un sens.

On récupère la valeur de retour de la méthode lors de l'évaluation de l'expression.

Par exemple la méthode `strip` permet de renvoyer la chaîne en omettant les espaces au début et à la fin.

```python
>>> '   hello '.strip()
'hello'
```
