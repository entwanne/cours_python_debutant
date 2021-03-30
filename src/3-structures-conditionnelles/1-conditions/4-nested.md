### Structures multiples

#### Enchaînement

Les exemples présents dans les sections qui précèdent montraient des structures conditionnelles seules : chacune est introduite par un `if`, peut comporter plusieurs clauses `elif` et peut être terminée par un `else`.

Mais dans un programme il est généralement nécessaire de tester différentes conditions et donc d'avoir plusieurs structures conditionnelles, c'est-à-dire plusieurs `if`.

Dans un fichier, on placera donc les blocs conditionnels les uns à la suite des autres, et Python comprendra qu'il s'agit d'une nouvelle structure chaque fois qu'il verra un `if`.

```python
user = input("Entrez le nom d'utilisateur: ")
password = intput("Entrez le mot de passe: ")

if user == 'admin':
    print("Le compte administrateur est désactivé")

if password == '1234':
    print("Mot de passe trop faible")
elif password == '4321':
    print("C'est pas mieux")
```

Dans le code précédent, les deux structures conditionnelles sont indépendantes l'une de l'autre.
Le deuxième `if / elif` est exécuté quelle que soit l'issue du premier `if`.

Et comme on le voit, le `elif` se rapporte toujours au `if` qui le précède directement, il en est de même pour `else`.

Cette syntaxe est parfaitement valide en Python mais peut parfois poser problème dans l'interpréteur interactif.
En effet, ce dernier n'interprète pas les sauts de ligne de la même manière, et nécessite ainsi toujours une ligne vide pour marquer la fin d'une structure conditionnelle.

On le remarque aux caractères utilisés par le prompt.
Il s'agit par défaut de `>>>` qui indique que nous sommes en dehors de tout bloc.
Une fois dans un bloc, ce prompt se transforme en `...` signifiant que l'interpréteur attend d'autres lignes à ajouter au bloc.  
Une ligne vide permet alors de demander à l'interpréteur de sortir du bloc.

De la même façon, il sera impossible d'avoir une ligne vide au milieu d'un bloc conditionnel dans l'interpréteur interactif.
Ces limitations peuvent être très gênants et c'est pourquoi le *REPL* est déconseillé pour des codes complexes.
Il reste toutefois très utile pour tester rapidement un petit bout de code.

#### Imbrication

Une autre manière de combiner plusieurs blocs conditionnels consiste à les imbriquer / emboîter.
Il est effectivement courant au sein d'un bloc `if` de vouloir tester une nouvelle condition pour effectuer un traitement particulier.

Pour rappel, Python délimite les blocs de code par leur indentation, c'est-à-dire les 4 espaces laissées en début de ligne.
Quand il n'y a qu'un seul bloc, on ne constate qu'un niveau d'indentation.

Mais pour imbriquer une nouvelle condition sous une autre, il va nous falloir passer au niveau d'indentation suivant en ajoutant encore 4 espaces.
Ainsi, Python compte le nombre d'espaces présentes en début de ligne pour déterminer dans quel bloc il se trouve.

```python
quit = input('Voulez vous quitter le programme (oui/non) ? ')

if quit == 'oui':
    confirm = input('Vous êtes sûr (oui/non) ?')
    if confirm == 'oui':
        print('Fermeture en cours...')
    else:
        print('Décidez-vous !')
else:
    print('Ok, on continue.')
```

Je vous invite à recopier le code qui précède dans un fichier et à l'exécuter en testant les 3 combinaisons possibles.
On constate bien que la condition sur `confirm` n'est exécutée que lorsque `quit` vaut « oui », et que les `else` sont indentés au même niveau que les `if` auxquels ils se rapportent.
