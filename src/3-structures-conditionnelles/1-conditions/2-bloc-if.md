### Bloc conditionnel

Une condition en Python correspond à un bloc `if`, traduction anglaise du mot « si ».
Un bloc est un élément de syntaxe que nous n'avons pas encore vu jusqu'ici : il s'agit de plusieurs lignes de code réunies au sein d'une même entité logique.

Un bloc conditionnel est introduit à l'aide du mot-clé `if` suivi d'une expression et d'un signe `:`.  
Le contenu du bloc est constituté des lignes qui suivent, qui doivent être indentées par rapport à l'ouverture du bloc, c'est-à-dire décalées vers la droite avec des espaces pour les démarquer.
On utilise conventionnellement 4 espaces.  
Le contenu du bloc ne sera exécuté que si l'expression du `if` est évaluée à « vrai » (`True`).

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
Code: Exécution du programme

Comme on le voit, un bloc prend fin dès la première ligne qui n'est pas indentée.

[[a]]
| Pour cet exemple comme pour ceux qui suivront, je vous conseille d'utiliser un fichier Python plutôt que l'interpréteur interactif qui gère assez mal les problématiques d'indentation.
| J'y reviens juste après.

Lorsque la condition est fausse, le contenu du bloc `if` n'est jamais exécuté et on passe directement à la suite du programme.

```python
if 1 == 2:
    print("Cette ligne n'est jamais exécutée")

print('Cette ligne est en dehors du bloc')
```

Qui donne à l'exécution :

```
Cette ligne est en dehors du bloc
```
Code: Exécution du programme

Mais les exemples qui précèdent ont peu d'intérêt car les conditions sont fixées et ont donc toujours la même valeur.
Il pourrait être intéressant par exemple d'intéragir avec l'utilisateur à l'aide d'un `input`.

```python
nbr = int(input('Devinez le nombre secret : '))

if nbr == 42:
    print('Bravo, vous avez trouvez le nombre mystère !')

print('Relancez le programme pour une nouvelle partie')
```

On peut alors exécuter le programme plusieurs fois pour tester nos réponses, et avoir une exécution différente selon ce que l'on saisit.

```
Devinez le nombre secret : 10
Relancez le programme pour une nouvelle partie
```
Code: Première exécution

```
Devinez le nombre secret : 42
Bravo, vous avez trouvez le nombre mystère !
Relancez le programme pour une nouvelle partie
```
Code: Seconde exécution

#### Interpréteur interactif

L'interpréteur interactif peut parfois poser problème quand on utilise des blocs.
Il demande en effet de laisser une ligne vide après chaque bloc (ce qui n'est pas nécessaire autrement), sans quoi vous obtiendrez une erreur de syntaxe.

```pycon
>>> if 2 == 2:
...     print('Gagné')
... print('Fin')
  File "<stdin>", line 3
    print('Fin')
    ^
SyntaxError: invalid syntax
```

On remarque cela aux caractères utilisés par le prompt : quand nous sommes en dehors de tout bloc, les caractères `>>>` sont utilisés.
Mais une fois dans un bloc, ce prompt se transforme en `...`, signifiant que l'interpréteur attend d'autres lignes à ajouter au bloc.  
Tout ce qui est tapé derrière un `...` est donc considéré par l'interpréteur interactif comme appartenant toujours au même bloc, ce qui provoque une erreur de syntaxe lorsque l'indentation est absente.

Une ligne vide permet de demander à l'interpréteur de sortir du bloc, qui serait alors exécuté immédiatement avant de passer à la suite.

```pycon
>>> if 2 == 2:
...     print('Gagné')
...
Gagné
>>> print('Fin')
Fin
```

Dans un fichier, la première syntaxe est parfaitement valide, puisque ce sont les tabulations uniquement qui délimitent les blocs.

```python
if 2 == 2:
    print('Gagné')
print('Fin')
```

De la même manière, il est impossible d'avoir une ligne vide au milieu d'un bloc conditionnel dans l'interpréteur interactif, alors que cette syntaxe est valide en Python.

```python
if 2 == 2:
    print('Gagné')

    print('Tu es trop fort')
```

[[i]]
| Ces limitations peuvent être très gênantes et c'est pourquoi l'interpréteur interactif est déconseillé pour des codes complexes.
| Il reste toutefois très utile pour tester rapidement un petit bout de code.

#### Blocs sur une ligne

Il faut relever une exception au fait que le contenu d'un bloc conditionnel soit toujours indenté.

Si un bloc se compose d'une seule ligne, il est possible de faire suivre cette ligne directement après le `:` du `if`, sans retour à la ligne ni indentation.

```python
if nbr == 42: print('Bravo, vous avez trouvez le nombre !')
```

Cette forme est à déconseiller car elle fait perdre en lisibilité, mais elle reste néanmoins utile pour des cas particuliers comme une vérification rapide avec `python -c`.

```shell
% python -c "if 2 * 21 == 42: print('Bravo')"
Bravo
```
