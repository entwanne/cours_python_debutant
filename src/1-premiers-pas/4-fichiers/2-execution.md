### Exécution du fichier

Maintenant que nous avons écrit notre premier programme nous pouvons donc passer à la prochaine étape : l'exécuter !  
Dans IDLE, cela se fait à l'aide du menu _Run_ > _Run Module_ (ou de la touche ||F5||).
De même dans Geany avec la commande _Execute_ (||F5||).

On exécute donc le fichier à l'aide de l'interpréteur… et rien ne se passe.
Enfin plus précisément on ne voit rien de particulier.

![Exécution du fichier dans IDLE.](img/idle_exec_file.png)

Le code a bien été exécuté mais il n'a affiché aucun résultat, donc rien de visible.
Dans l'interpréteur interactif, la valeur calculée de chaque ligne était affichée dans le terminal, parce que c'est plus facile à suivre.
Mais dans le cas d'un fichier, ça polluerait inutilement la console, on ne veut pas afficher le résultat de chaque calcul intermédiaire.

On aimerait tout de même pouvoir en afficher certains, et il existe pour cela la commande `print`.
Elle permet, suivie d'une paire de parenthèses comprenant une valeur, d'afficher cette valeur sur le terminal.

```python
print(8 + 5)
print(3 * 7)
```
Code: calc.py

Il faut bien différencier l'affichage de l'évaluation.
L'évaluation c'est le processus par lequel Python calcule le résultat d'une opération, sans nécessairement l'afficher.

##### Commentaires

Dans notre fichier, nous pouvons aussi placer des commentaires pour expliquer ce qui est fait.
Les commentaires ne sont pas interprétés par Python, ils se destinent aux développeurs qui liront le fichier, et permettent de renseigner des informations ou documenter.

Un commentaire est simplement une ligne commençant par un `#` et suivie de n'importe quel texte.
On peut aussi placer un commentaire derrière une ligne de code, toujours en le faisant précéder d'un `#`.

```python
# Calcul du prix au kilo de pommes

# Nous avons acheté 500g de pommes pour 1€
print(1 / 0.5) # Prix total (€) / Poids des pommes (Kg)
```
Code: pommes.py

#### Exécution depuis le terminal

Voilà pour l'exécution depuis l'éditeur de texte, mais si vous êtes un adepte de la console vous voudrez peut-être aussi lancer votre programme depuis le terminal.

Pour cela, il suffit de lancer un terminal dans le répertoire où se trouve votre fichier de code (ou de se rendre dans le bon répertoire avec la commande `cd`) puis de lancer `python calc.py` (ou `python3` suivant la version par défaut).

```sh
% python calc.py
13
21
```

[[a]]
| Attention sous Windows, pensez à utiliser un terminal persistant pour éviter que celui-ci ne se ferme à la fin du programme ou lorsqu'une erreur est rencontrée.
|
| Évitez donc d'exécuter vos fichiers en double-cliquant dessus et préférez ouvrir un Powershell dans lequel vous appellerez Python comme ci-dessus.

Sous Linux vous pouvez aussi rendre votre programme exécutable en lui donnant les droits d'exécution (`chmod +x calc.py`) et en plaçant le _shebang_ `#!/usr/bin/env python` (ou `python3`) en en-tête du fichier.

```sh
% ./calc.py
13
21
```
