### Autres manières d'itérer

On sait itérer sur les clés et récupérer la valeur associée à chaque clé, mais est-ce qu'il n'y a pas plus simple ?
En effet, imaginons que nous ne soyons intéressé que par les valeurs du dictionnaires, pourquoi s'encombrer avec les clés ?

Les dictionnaires possèdent pour cela une méthode `values` renvoyant l'ensemble des valeurs du dictionnaire, sans les clés.

```python
>>> phonebook.values()
dict_values(['0633432380', '0663621029', '0714381809'])
```

La méthode renvoie un objet d'un type un peu spécial, `dict_values`.
Il s'agit en fait d'une « vue », une sorte de liste qui n'existerait pas en tant que telle en mémoire (il n'y a pas de tableau d'éléments) mais qui saurait où aller chercher ses éléments.  
Il n'y a donc pas de duplication, la vue référence juste les valeurs du dictionnaire.

Et cet objet un peu spécial est bien sûr itérable :

```python
>>> for phone in phonebook.values():
...     print('Numéro de téléphone :', phone)
... 
Numéro de téléphone : 0633432380
Numéro de téléphone : 0663621029
Numéro de téléphone : 0714381809
```

De façon symétrique on trouve aussi une méthode `keys` pour renvoyer une vue sur les clés.

```python
>>> phonebook.keys()
dict_keys(['Alice', 'Bob', 'Alex'])
```

Itérer sur cette vue revient donc à itérer directement sur le dictionnaire, mais comme on dit « explicit is better than implicit »[^PEP20].

[^PEP20]: Il s'agit d'un « vers » extrait de la [PEP20](), un « poème » qui décrit la philosophie de Python.

```python
>>> for name in phonebook.keys():
...     print(name)
... 
Alice
Bob
Alex
```

Enfin, les dictionnaires disposent d'une troisième vue très utile, la vue `items`.
Cette vue renvoie les couples clé/valeur du dictionnaire.

```python
>>> phonebook.items()
dict_items([('Alice', '0633432380'), ('Bob', '0663621029'), ('Alex', '0714381809')])
```

Étant donné qu'il s'agit de couples, on peut itérer sur cette vue en précisant deux variables dans notre `for` : une pour recevoir la clé et une pour la valeur.

```python
>>> for name, phone in phonebook.items():
...     print(name, ':', phone)
... 
Alice : 0633432380
Bob : 0663621029
Alex : 0714381809
```
