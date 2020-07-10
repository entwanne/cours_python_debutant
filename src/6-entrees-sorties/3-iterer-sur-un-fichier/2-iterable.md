### Les fichiers sont itérables

La solution avec `readlines` n'est pas satisfaisante si nous voulons traiter le fichier pas à pas, et celle avec `readline` un peu compliquée : on constate que la boucle `while` ne se prête pas à ce problème puisqu'on est obligé de répéter l'opération `line = f.readline()`.

Mais pour rappel, les listes ne sont pas les seuls objets itérables.
Outre les autres exemples que l'on a déjà vus, il est aussi possible d'itérer sur des fichiers.
Et cela correspond évidemment à une itération ligne par ligne sur le fichier.

```python
>>> with open('corbeau.txt') as f:
...     for line in f:
...         line
... 
'Maître Corbeau, sur un arbre perché,\n'
'Tenait en son bec un fromage.\n'
"Maître Renard, par l'odeur alléché,\n"
'Lui tint à peu près ce langage :\n'
'Et bonjour, Monsieur du Corbeau.\n'
'Que vous êtes joli ! que vous me semblez beau !\n'
'Sans mentir, si votre ramage\n'
'Se rapporte à votre plumage,\n'
'Vous êtes le Phénix des hôtes de ces bois.\n'
'À ces mots, le Corbeau ne se sent pas de joie ;\n'
'Et pour montrer sa belle voix,\n'
'Il ouvre un large bec, laisse tomber sa proie.\n'
"Le Renard s'en saisit, et dit : Mon bon Monsieur,\n"
'Apprenez que tout flatteur\n'
"Vit aux dépens de celui qui l'écoute.\n"
'Cette leçon vaut bien un fromage, sans doute.\n'
'Le Corbeau honteux et confus\n'
"Jura, mais un peu tard, qu'on ne l'y prendrait plus.\n"
```

On fera difficilement plus simple que cette solution.

Partant de là, il est aussi facile de traiter notre fichier comme s'il ne s'agissait que d'un ensemble de lignes, avec une fonction comme la suivante.

```python
def print_text(lines):
    i = 1 # Compteur de ligne
    for line in lines:
        line = line.rstrip('\n') # On retire le saut de ligne
        print(i, ':', line)
        i += 1

with open('corbeau.txt') as f:
    print_text(f)
```

Cette fonction s'abstrait complètement du type réel de l'objet et fonctionnerait très bien avec une liste de chaînes de caractères en argument.

```python
>>> print_text(['abc', 'def', 'ghi'])
1 : abc
2 : def
3 : ghi
```
