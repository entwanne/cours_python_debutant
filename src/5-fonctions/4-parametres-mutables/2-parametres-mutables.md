### Paramètres mutables

Ça peut donc être perturbant au premier abord, puisque la modification d'un paramètre altère la valeur passée en argument.

```python
def append_zero(values):
    values.append(0)
    return values
```

```pycon
>>> l = [1, 2, 3]
>>> append_zero(l)
[1, 2, 3, 0]
>>> l
[1, 2, 3, 0]
```

Ce n'est pas le cas avec une redéfinition qui crée une nouvelle instance (et donc oublie la référence précédente).

```python
def append_zero(values):
    values = values + [0]
    return values
```

```pycon
>>> l = [1, 2, 3]
>>> append_zero(l)
[1, 2, 3, 0]
>>> l
[1, 2, 3]
```

Attention cependant à l'opérateur `+=` des listes qui opère une modification sur la liste existante plutôt qu'une réaffectation sur une nouvelle liste.

```python
def append_zero(values):
    values += [0]
    return values
```

```pycon
>>> l = [1, 2, 3]
>>> append_zero(l)
[1, 2, 3, 0]
>>> l
[1, 2, 3, 0]
```

#### Effets de bord

Modifier ainsi les valeurs passées en paramètres provoque ce que l'on appelle des effets de bord, c'est-à-dire que l'exécution de la fonction affecte un état extérieur, elle n'est pas reproductible dans les mêmes conditions.  
On dit aussi qu'elle n'est pas « pure » (contrairement à une fonction purement mathématique qui ne ferait que calculer un nouveau résultat à partir des paramètres).

Parfois, ces effets de bord sont désirables, mais ils ne le sont pas toujours.
Dans les cas où on veut les éviter, on privilégiera alors des types immutables (tuples par exemple) ou l'on créera des copies des objets reçus en paramètres.

```python
def append_zero(values):
    values = list(values) # on crée une copie
    values.append(0)
    return values
```
