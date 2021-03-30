### Plusieurs return dans une fonction

Une fonction n'est pas limitée à un seul `return` et il est ainsi possible d'en avoir plusieurs pour contrôler le flux d'exécution.

L'exécution de la fonction s'arrêtera au premier `return` rencontré, renvoyant la valeur associée à l'expression de ce `return`.

On pourrait par exemple imaginer une fonction `division(a, b)` renvoyant la division de `a` par `b` et gérant le cas de la division par zéro en renvoyant zéro.

```python
def division(a, b):
    if b == 0:
        return 0
    return a / b
```

Dans les cas où `b` vaut zéro, on rentrera donc dans le bloc de la première condition et le `return` sera exécuté.
On se retrouve donc à sortir de la fonction sans exécuter la suite, c'est pourquoi aucune exception n'est ensuite levée.

```python
>>> division(1, 2)
0.5
>>> division(2, 0)
0
```

Si aucun `return` n'est rencontré lors de l'exécution de la fonction, c'est la valeur `None` qui sera automatiquement renvoyée.

```python
def secret_addition(a, b):
    if a + b == 42:
        return 42
```

```python
>>> secret_addition(12, 30)
42
>>> secret_addition(12, 33)
>>> print(secret_addition(12, 33))
None
```

Pour rappel, la valeur `None` n'est par défaut pas affichée par l'interpréteur interactif, d'où l'appel à `print`.
