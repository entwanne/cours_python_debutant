### Fonctions natives

Je ne reviendrai pas sur l'ensemble des fonctions natives (*built-ins*) car beaucoup ont déjà été présentées dans les chapitres précédents, notamment [celui rappelant les différents types](https://zestedesavoir.com/tutoriels/2514/un-zeste-de-python/4-types/1-types-precedents/) et [celui dédié aux outils sur les boucles](https://zestedesavoir.com/tutoriels/2514/un-zeste-de-python/7-perfectionnement/3-boucles/#3-3-outils).

Mais quelques autres de ces fonctions méritent qu'on en parle un peu.

##### Manipulation de caractères

Les fonctions `ord` et `chr` par exemple permettent de manipuler les caractères et leurs codes numériques.  
Jusqu'ici on n'a jamais dissocié caractères et chaînes de caractères, puisque les caractères sont simplement des chaînes de taille 1.

Mais en pratique, une chaîne de caractères s'apparente plutôt à une séquence de code numériques (des nombres entiers) où chaque code identifie un caractère particulier selon la spécification unicode.

Ainsi, la fonction `ord` permet simplement de récupérer le code associé à un caractère, et la fonction `chr` le caractère associé à un code.

```pycon
>>> ord('x')
120
>>> chr(120)
'x'
>>> ord('♫')
9835
>>> chr(9835)
'♫'
```

Ces fonctions peuvent permettre de jongler un peu avec la table unicode pour réaliser des opérations particulières en exploitant les caractéristiques de cette table.

Par exemple pour récupérer n'importe quelle carte à jouer en connaissant [la manière dont elles sont stockées](https://fr.wikipedia.org/wiki/Table_des_caract%C3%A8res_Unicode/U1F0A0) :

```pycon
>>> card_base = ord('🂠')
>>> chr(card_base + 0x20 + 0x05) # 5 de carreau
'🃅'
>>> chr(card_base + 0x10 + 0x0B) # Valet de pic
'🂻'
```

`ord` échoue naturellement si on lui passe une chaîne de plusieurs caractères, et `chr` si on lui donne un code en dehors des bornes définies par unicode.

```pycon
>>> ord('salut')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: ord() expected a character, but string of length 5 found
>>> chr(1000000000)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: chr() arg not in range(0x110000)
```

##### Formattage des valeurs

La fonction `format` permet d'obtenir la représentation formatée de n'importe quelle valeur, sous forme d'une chaîne de caractères.

Vous ne la connaissez pas mais c'est elle qui intervient dans le mécanisme des chaînes de formatage (_f-string_) pour transformer les valeurs et leur appliquer le format demandé.  
Elle prend ainsi en arguments la valeur et le format (les options de formatage) à lui appliquer.

```pycon
>>> format(42, '05X')
'0002A'
>>> format(123.4, 'e')
'1.234000e+02'
>>> format('salut', '>10')
'     salut'
```

Appelée sans format, elle opère juste la conversion en chaîne de caractères de la valeur donnée et devient ainsi équivalente à `str`.

```pycon
>>> format(25)
'25'
```

##### Évaluation dynamique

[[a]]
| La fonction qui suit peut introduire de grosses failles de sécurité dans vos programmes et doit donc être utilisée avec parcimonie : seulement sur des données qui sont sûres, jamais sur des données reçues de l'utilisateur ou d'un tiers.

Python est un langage dynamique et permet en cela d'exécuter du code à la volée au sein du programme.  
C'est l'objectif de la fonction `eval` qui prend en argument une chaîne de caractères représentant une expression Python, l'interprète et en renvoie le résultat.

```pycon
>>> eval('1 + 3')
4
>>> x = 5
>>> eval('x * 8')
40
```

Cela offre donc la possibilité d'exécuter du code dynamiquement et donc de dépasser les fonctionnalités de base du langage.
Par exemple pour créer en un coup une imbrication de 20 listes.

```pycon
>>> eval('['*20 + 'None' + ']'*20)
[[[[[[[[[[[[[[[[[[[[None]]]]]]]]]]]]]]]]]]]]
```

--------------------

Toutes ces fonctions natives peuvent être retrouvées sur [la page de documentation dédiée](https://docs.python.org/fr/3/library/functions.html).
