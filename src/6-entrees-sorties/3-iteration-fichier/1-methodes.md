### Méthodes des fichiers

Avec `read` nous savons lire le contenu complet dans une chaîne de caractères.
Mais ce n'est pas toujours le plus pratique et il est souvent préférable de pouvoir traiter un fichier par morceaux.
En plus, ça évite de devoir stocker la totalité du fichier en mémoire si ça n'est pas nécessaire (heureusement que les lecteurs vidéo ne chargent pas tout le contenu d'un film dans une chaîne de caractères).

Pour ce chapitre, j'utiliserai le fichier `corbeau.txt` avec le contenu suivant :

[[s]]
| ```
| Maître Corbeau, sur un arbre perché,
| Tenait en son bec un fromage.
| Maître Renard, par l'odeur alléché,
| Lui tint à peu près ce langage :
| Et bonjour, Monsieur du Corbeau.
| Que vous êtes joli ! que vous me semblez beau !
| Sans mentir, si votre ramage
| Se rapporte à votre plumage,
| Vous êtes le Phénix des hôtes de ces bois.
| À ces mots, le Corbeau ne se sent pas de joie ;
| Et pour montrer sa belle voix,
| Il ouvre un large bec, laisse tomber sa proie.
| Le Renard s'en saisit, et dit : Mon bon Monsieur,
| Apprenez que tout flatteur
| Vit aux dépens de celui qui l'écoute.
| Cette leçon vaut bien un fromage, sans doute.
| Le Corbeau honteux et confus
| Jura, mais un peu tard, qu'on ne l'y prendrait plus.
| ```
| Code: corbeau.txt

Une première manière de découper est d'utiliser l'argument optionnel de `read` qui permet de préciser une taille.
La longueur du texte renvoyée sera ainsi toujours inférieure ou égale à cette taille (inférieur s'il n'y a plus rien d'autre à lire par exemple), et le curseur avancé d'autant dans le fichier.

```python
>>> with open('corbeau.txt') as f:
...     f.read(100)
...     f.read(100)
...     f.read(100)
...     f.read(100)
...     f.read(100)
...     f.read(100)
...     f.read(100)
...     f.read(100)
... 
"Maître Corbeau, sur un arbre perché,\nTenait en son bec un fromage.\nMaître Renard, par l'odeur alléch"
'é,\nLui tint à peu près ce langage :\nEt bonjour, Monsieur du Corbeau.\nQue vous êtes joli ! que vous m'
'e semblez beau !\nSans mentir, si votre ramage\nSe rapporte à votre plumage,\nVous êtes le Phénix des h'
'ôtes de ces bois.\nÀ ces mots, le Corbeau ne se sent pas de joie ;\nEt pour montrer sa belle voix,\nIl '
"ouvre un large bec, laisse tomber sa proie.\nLe Renard s'en saisit, et dit : Mon bon Monsieur,\nAppren"
"ez que tout flatteur\nVit aux dépens de celui qui l'écoute.\nCette leçon vaut bien un fromage, sans do"
"ute.\nLe Corbeau honteux et confus\nJura, mais un peu tard, qu'on ne l'y prendrait plus.\n"
```

Il serait possible, à l'aide d'une boucle, de parcourir le fichier en entier.

```python
with open('corbeau.txt') as f:
    chunk = f.read(100)
    while chunk:
        print(chunk)
        chunk = f.read(100)
```

C'est très bien quand on souhaite découper en morceaux de taille fixe (ou tronçons, _chunks_), mais ça se prête assez mal à un fichier texte.
Une lecture ligne par ligne nous serait plus utile.

Et c'est le but de la méthode `readline`.
Celle-ci s'occupe de repérer où sont les retours à la ligne et ainsi de ne renvoyer qu'une ligne à la fois, en gardant ce qui suit pour un prochain appel.

```python
>>> with open('corbeau.txt') as f:
...     line = f.readline()
...     while line:
...         line
...         line = f.readline()
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

On constate tout de même que le retour à la ligne est considéré comme faisant partie de la ligne.

On trouve aussi la méthode `readlines` pour lire toutes les lignes d'un coup et les renvoyer dans un tableau.
Mais on retombe sur le problème initial : cela demande à stocker le fichier en mémoire dans sa totalité.

```python
>>> with open('corbeau.txt') as f:
...     f.readlines()
... 
['Maître Corbeau, sur un arbre perché,\n',
 'Tenait en son bec un fromage.\n',
 "Maître Renard, par l'odeur alléché,\n",
 'Lui tint à peu près ce langage :\n',
 'Et bonjour, Monsieur du Corbeau.\n',
 'Que vous êtes joli ! que vous me semblez beau !\n',
 'Sans mentir, si votre ramage\n',
 'Se rapporte à votre plumage,\n',
 'Vous êtes le Phénix des hôtes de ces bois.\n',
 'À ces mots, le Corbeau ne se sent pas de joie ;\n',
 'Et pour montrer sa belle voix,\n',
 'Il ouvre un large bec, laisse tomber sa proie.\n',
 "Le Renard s'en saisit, et dit : Mon bon Monsieur,\n",
 'Apprenez que tout flatteur\n',
 "Vit aux dépens de celui qui l'écoute.\n",
 'Cette leçon vaut bien un fromage, sans doute.\n',
 'Le Corbeau honteux et confus\n',
 "Jura, mais un peu tard, qu'on ne l'y prendrait plus.\n"]
```
