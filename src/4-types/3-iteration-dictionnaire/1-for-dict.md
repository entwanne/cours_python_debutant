### Dictionnaire et boucle for

Mais itérer sur un dictionnaire, qu'est-ce que ça veut dire ?

En fait un dictionnaire peut être vu comme un ensemble de clés.
Itérer sur un dictionnaire revient donc à itérer sur ces clés.

```python
>>> phonebook = {'Alice': '0633432380', 'Bob': '0663621029', 'Alex': '0714381809'}
>>> for name in phonebook:
...     print(name)
...
Alice
Bob
Alex
```

Et à partir d'une clé, il est facilement possible d'accéder à la valeur associée, grâce à l'opérateur `[]`.

```python
>>> for name in phonebook:
...     print(name, ':', phonebook[name])
...
Alice : 0633432380
Bob : 0663621029
Alex : 0714381809
```

[[i]]
| Si vous utilisez une version de Python antérieure à 3.6, il se peut que vous obteniez un ordre différent dans les itérations.
| En effet, l'ordre des éléments dans un dictionnaire était auparavant aléatoire.

Le fait qu'un dictionnaire soit itérable le rend donc convertible en liste (en appelant `list`) ce qui aura pour effet de renvoyer la liste des clés.

```python
>>> list(phonebook)
['Alice', 'Bob', 'Alex']
```
