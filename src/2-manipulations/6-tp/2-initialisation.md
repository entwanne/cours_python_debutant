### Initialisation du jeu

Tout d'abord, avant de faire un premier tour de combat, il faut procéder à l'initialisation du jeu.
En effet, il nous faut connaître les monstres en jeu et leur nombre initial de points de vie.

Pour cela on utilisera la fonction `input` afin de demander aux deux joueurs les différentes informations.
Nous les conserverons dans des variables et les afficherons en début de partie à l'aide de la fonction `print`.

```
Entrez le nom du 1er joueur : pythachu
Et son nombre de PV : 50
Entrez le nom du 2ème joueur : pythard
Et son nombre de PV : 40

+++++++++++++++++++++++++++++++++++++++++++++
+ Pythachu (50 PV) affronte Pythard (40 PV) +
+++++++++++++++++++++++++++++++++++++++++++++
```

Vous le voyez, j'ai ajouté un cadre autour du message à afficher.
On peut faire ça facilement à l'aide des opérateurs `+` et `*` que nous avons vus pour les chaînes de caractères.  
La fonction `len` vous sera utile aussi pour que la largeur du cadre s'adapte à la taille du texte.

On peut voir que j'ai passé en majuscule la première lettre des noms, saurez-vous retrouver la méthode qui permet ça ?
Aussi, il nous faudra penser à convertir les PV saisis pour les traiter en tant que nombres.

#### Solution

Cette première étape devrait se faire assez facilement, et je vous laisse revoir les chapitres précédents en cas de doutes.

Voici tout de même la solution que je propose à ce début d'exercice, à comparer avec la vôtre.
Je la mets en balise ||secret||, suivie de quelques explications.

[[s]]
| ```python
| name1 = input('Entrez le nom du 1er joueur : ').capitalize()
| pv1 = int(input('Et son nombre de PV : '))
| 
| name2 = input('Entrez le nom du 2ème joueur : ').capitalize()
| pv2 = int(input('Et son nombre de PV : '))
|
| print()
|
| message = name1 + ' (' + str(pv1) + ' PV) affronte ' + name2 + ' (' + str(pv2) + ' PV)'
| print('+' * (len(message)+4))
| print('+', message, '+')
| print('+' * (len(message)+4))
| ```
|
| * La méthode `capitalize`, appliquée directement sur le retour d'`input` nous permet de transformer un `'pytachu'` entré en `'Pythachu'`.
| * Les points de vie sont convertis en nombres à l'aide d'appels à `int`.
| * `print` peut s'utiliser sans arguments pour juste afficher une ligne vide et séparer les informations les unes des autres.
| * Pour l'affichage du cadre, on commence par forger une variable `message` qui contient le message à afficher. Ça se fait aisément à l'aide de concaténations (`+`) entre nos différents bouts de texte.
| * À partir de la taille du message, on peut alors afficher les lignes haute et basse du cadre. Mais attention : avec les marges, elles comprennent 4 caractères de plus que le message.
| * Enfin, pour l'affichage du message à proprement parler, on peut juste utiliser les différents arguments de `print`, sans concaténation.

Nous pouvons maintenant passer à la suite du TP.
