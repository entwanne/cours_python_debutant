### Bloc conditionnel

Une condition s'introduit à l'aide d'un bloc `if`, traduction anglaise du mot « si ».
Un bloc est un élément de syntaxe que nous n'avons pas encore vu jusqu'ici : il s'agit de plusieurs lignes de code réunies au sein d'une même entité logique.

Un bloc conditionnel est introduit à l'aide du mot-clé `if` suivi d'une expression et d'un signe `:`.  
Le contenu du bloc est constituté des lignes qui suivent, qui doivent être indentées par rapport à l'ouverture du bloc, c'est-à-dire décalées vers la droite avec des espaces pour les démarquer.
On utilise conventionnellement 4 espaces.  
Le contenu du bloc ne sera exécuté que si l'expression du `if` est évaluée vraie.

```python
if 2 == 2:
    print('> Nous sommes dans le bloc conditionnel')
    print('> Ici encore')
print('Nous sommes en dehors du bloc')
```

Ainsi le code précédent se lit :

> * Si 2 est égal à 2, afficher « Nous sommes dans le bloc conditionnel » et « Ici encore ».
> * Dans tous les cas afficher « Nous sommes en dehors du bloc ».

Et s'exécute comme suit.

```
> Nous sommes dans le bloc conditionnel
> Ici encore
Nous sommes en dehors de tout bloc
```

(Pour cet exemple comme pour ceux qui suivront, je vous conseille d'utiliser un fichier Python plutôt que l'interpréteur interactif qui gère assez mal les problématiques d'indentation.)

Si la condition est fausse, le contenu du bloc n'est jamais exécuté.

```python
if 1 == 2:
    print("Cette ligne n'est jamais exécutée")
print('Cette ligne est en dehors du bloc')
```

```
Cette ligne est en dehors du bloc
```
Comme on le voit, un bloc prend fin dès la première ligne qui n'est pas indentée.

Mais ces exemples ont peu d'intérêt car les conditions sont fixées et ont donc toujours la même valeur.
Il pourrait être intéressant par exemple d'intéragir avec l'utilisateur à l'aide d'un `input`.

```python
nbr = int(input('Devinez le nombre secret : '))

if nbr == 42:
    print('Bravo, vous avez trouvez le nombre !')

print('Relancez le programme pour une nouvelle partie')
```

```
Devinez le nombre secret : 10
Relancez le programme pour une nouvelle partie
```

```
Devinez le nombre secret : 42
Bravo, vous avez trouvez le nombre !
Relancez le programme pour une nouvelle partie
```

#### Blocs sur une ligne

Il faut relever une exception au fait que le contenu d'un bloc conditionnel soit toujours indenté.

Si un bloc se compose d'une seule ligne, il est possible de faire suivre cette ligne directement arpès le `:` du `if`, sans retour à la ligne ni indentation.

```python
if nbr == 42: print('Bravo, vous avez trouvez le nombre !')
```

Cette forme est à déconseiller car elle fait perdre en lisibilité, mais elle reste néanmoins utile pour des cas particuliers comme une vérification rapide avec `python -c`.
