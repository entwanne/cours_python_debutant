### Des tables d'association

Comme les listes, les dictionnaires sont des conteneurs.
C'est-à-dire qu'ils contiennent d'autres valeurs auxquelles on peut accéder avec l'opérateur d'indexation `[]`.

Mais plutôt qu'associer une valeur à un index, ils vont l'associer à une clé quelconque, par exemple une chaîne de caractères.
Il s'agit donc d'un ensemble de couples clé-valeur.

Un dictionnaire se définit avec des accolades, entre lesquelles les couples sont séparés par des virgules. Un couple clé-valeur est de la forme `cle: valeur`.

Voilà à quoi pourrait ressembler le répertoire téléphonique donné en introduction :

```python
phonebook = {'Alice': '0633432380', 'Bob': '0663621029', 'Alex': '0714381809'}
```

C'est déjà plus clair à écrire, mais là où ça devient intéressant c'est pour l'accès aux éléments.
On retrouve en effet l'opérateur `[]`, mais on va pouvoir lui préciser une clé de notre dictionnaire plutôt qu'un index.

```python
>>> phonebook['Alex']
'0714381809'
```

Il suffit de connaître le nom pour accéder au numéro, pas besoin de parcourir tout le répertoire.
On comprend donc l'analogie avec le dictionnaire, qui permet d'associer des définitions à des mots, et de retrouver la définition à partir du mot.
