### Les tuples

Les tuples (parfois traduits en n-uplets) sont des équivalents non modifiables aux listes.
C'est-à-dire des séquences d'un nombre fixe d'éléments : après la définition, on ne peut ni ajouter, ni supprimer, ni remplacer d'élément.

Un tuple est généralement défini par une paire de parenthèses contenant les éléments séparés par des virgules.
Comme une liste, un tuple peut contenir des éléments de types différents.

```python
>>> (1, 2, 3)
(1, 2, 3)
>>> ('a', 'b', 'c')
('a', 'b', 'c')
>>> (42, '!')
(42, '!')
```

On notera tout de même que les parenthèses sont facultatives, c'est la virgule qui définit réellement un tuple.
Comme pour les opérations arithmétiques, les parenthèses servent en fait à gérer les priorités et mettre en valeur le tuple.

```python
>>> 1, 2, 3
(1, 2, 3)
>>> 1, 2, 3 * 3
(1, 2, 9)
>>> (1, 2, 3) * 3
(1, 2, 3, 1, 2, 3, 1, 2, 3)
```

Il faut bien penser à cette virgule lorsque l'on cherche à définir un tuple contenant un unique élément.
En effet, `(1)` étant une notation équivalente à `1`, il est nécessaire d'en ajouter une pour expliciter le tuple.

```python
>>> (1)
1
>>> (1,)
(1,)
>>> 1,
(1,)
```

Par ailleurs, il est possible de définir un tuple vide à l'aide d'une simple paire de parenthèses (il n'y a dans ce cas pas de confusion avec d'autres utilisations possibles des parenthèses).

```python
>>> ()
()
```

J'utiliserai principalement le terme de tuple, mais il faut savoir qu'on rencontre parfois d'autres noms suivant la taille du tuple.
On parle ainsi parfois de couple pour des tuples de 2 éléments, des triplets pour 3, etc.

Par exemple il est courant de dire que la méthode `items` des dictionnaires renvoie des couples clé/valeur.

```python
>>> phonebook = {'Alice': '0633432380', 'Bob': '0663621029', 'Alex': '0714381809'}
>>> for couple in phonebook.items():
...     print(couple)
... 
('Alice', '0633432380')
('Bob', '0663621029')
('Alex', '0714381809')
```
