### Annotations de types

Tout comme il est possible de typer les paramètres de fonction à l'aide d'annotations, de telles annotations sont disponibles aussi pour typer nos variables.
Là encore les annotations n'ont qu'un rôle purement indicatif (pour de la documentation) ou peuvent être analysées par des outils externes comme `mypy`.

Pour annoter une variable avec un type, on place simplement un signe `:` suivi du type avant le signe `=` de l'assignation.

```python
>>> foo: str = 'bar'
```

Il est aussi possible d'annoter une variable sans la définir, en faisant juste suivre un nom de variable d'une annotation, sans assignation.

```python
>>> number: int
```

[[a]]
| Attention, dans ce cas la variable est annotée mais n'a pas de valeur.
| `number` reste une variable indéfinie.

```python
>>> number
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'number' is not defined
```

On peut alors la définir plus tard, sans avoir besoin de repréciser l'annotation de type qui sera conservée pour la variable.

```python
>>> number = 42
>>> number
42
```
