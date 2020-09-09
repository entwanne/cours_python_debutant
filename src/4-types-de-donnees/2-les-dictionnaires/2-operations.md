### Opérations sur les dictionnaires

Les dictionnaires sont des objets modifiables, on retrouve donc l'opérateur d'indexation en lecture et en écriture.

```python
>>> phonebook['Alice']
'0633432380'
>>> phonebook['Bob'] = '0712800331'
>>> del phonebook['Alex']
>>> phonebook
{'Alice': '0633432380', 'Bob': '0712800331'}
```

Par contre pas de _slicing_ ici, cela n'a pas de sens sur un dictionnaire.

Une clé non trouvée dans le dictionnaire provoque une erreur.

```python
>>> phonebook['Mehdi']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Mehdi'
```

On retrouve aussi l'opérateur d'appartenance (`in`), qui fonctionne sur les clés et non sur les valeurs.

```python
>>> 'Bob' in phonebook
True
>>> '0633432380' in phonebook
False
```

Et on peut connaître la taille d'un dictionnaire en appelant la fonction `len`.

```python
>>> len(phonebook)
2
```

* égalité/différence entre dictionnaires
    * l'ordre des éléments n'importe pas dans un test d'égalité

Comme tout objet, il est possible de tester l'égalité entre deux dictionnaires avec l'opérateur `==`, et la différence avec `!=`.
Deux dictionnaires sont considérés comme égaux s'ils contiennent les mêmes éléments, avec les mêmes valeurs pour les mêmes clés.
Quel que soit l'ordre des éléments dans le dictionnaire.

```python
>>> {'a': 1} == {'a': 1}
True
>>> {'a': 0} == {'b': 0}
False
>>> {'a': 0, 'b': 1} != {'b': 1, 'a': 0}
False
>>> {'a': 0, 'b': 1} != {'b': 1, 'a': 0, 'c': 2}
True
```

#### Méthodes principales

Une première méthode intéressant est la méthode `get`.
Elle agit comme l'opérateur `[]` mais sans produire d'erreur si la clé n'est pas trouvée.

```python
>>> phonebook.get('Mehdi')
>>> print(phonebook.get('Mehdi'))
None
```

Comme on le voit, la valeur renvoyée si la clé n'est pas trouvée est `None`.
Il est possible de renvoyer une autre valeur en la précisant comme second argument à `get`.

```python
>>> phonebook.get('Mehdi', 'xxx')
'xxx'
```

Ensuite on va surtout trouver des méthodes pour modifier le dictionnaire, comme on en trouvait sur les listes.

La méthode `pop` est d'ailleurs équivalente à celle des listes, elle supprime une clé du dictionnaire et renvoie la valeur associée.

```python
>>> phonebook.pop('Alice')
'0633432380'
```

L'appel produit une erreur si la clé n'est pas trouvée, mais il est là encore possible de donner une valeur par défaut en deuxième argument.

```python
>>> phonebook.pop('Mehdi')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Mehdi'
>>> phonebook.pop('Mehdi', 'xxx')
'xxx'
```

La méthode `update` permet d'étendre le dictionnaire avec les données d'un autre dictionnaire.

```python
>>> phonebook.update({'Julie': '0619096810', 'Mehdi': '0762253973'})
>>> phonebook
{'Bob': '0712800331', 'Julie': '0619096810', 'Mehdi': '0762253973'}
```

Si une clé existe déjà dans le dictionnaire actuel, sa valeur est remplacée par la nouvelle qui est reçue.

```python
>>> phonebook.update({'Julie': '0734593960'})
>>> phonebook
{'Bob': '0712800331', 'Julie': '0734593960', 'Mehdi': '0762253973'}
```

La méthode `clear` sert à vider complètement un dictionnaire.

```python
>>> phonebook.clear()
>>> phonebook
{}
```

`{}` représente donc un dictionnaire vide.

Enfin, `setdefault` est un peu le pendant de `get` mais en écriture : elle va insérer une valeur dans le dictionnaire seulement si la clé n'est pas déjà présente.  
La méthode renvoie la valeur associée à cette clé dans le dictionnaire, donc soit celle qui vient d'être ajoutée soit celle qui était déjà présente.

```python
>>> phonebook.setdefault('Julie', '0619096810')
'0619096810'
>>> phonebook.setdefault('Julie', '0734593960')
'0619096810'
>>> phonebook
{'Julie': '0619096810'}
```

* Conversions: appel à `dict(...)`, args (mapping ou liste d'items) & kwargs