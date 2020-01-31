### Exécution

* Exécution de l'interpréteur sur le fichier
* Avoir un interpréteur persistant (ne se ferme pas à la fin du programme)

On exécute donc le fichier à l'aide de l'interpréteur… et rien ne se passe.
Enfin plus précisément on ne voit rien.

Le code a bien été exécuté mais il n'a affiché aucun résultat, donc rien de visible.
Dans l'interpréteur interactif, la valeur calculée de chaque ligne était affichée dans le terminal, parce que c'est plus facile à suivre.
Mais dans le cas d'un fichier, ça polluerait inutilement la console, on ne veut pas afficher le résultat de chaque calcul.

On aimerait tout de même pouvoir en afficher certains, et il existe pour cela la commande `print`.
Elle permet, suivie d'une paire de parenthèses comprenant une valeur, d'afficher cette valeur sur le terminal.

```python
print(42)
print(8 + 5)
```

Il faut bien différencier l'affichage de l'évaluation.
L'évaluation c'est le processus par lequel Python calcule le résultat d'une expression, sans nécessairement l'afficher.

Dans notre fichier, nous pouvons aussi placer des commentaires pour expliquer ce qui est fait.
Les commentaires ne sont pas interprétés par Python, ils se destinent aux développeurs qui liront le fichier, et permettent de renseigner des informations ou documenter.

Un commentaire est simplement une ligne commençant par un `#` et suivie de n'importe quel texte.
On peut aussi placer un commentaire derrière une ligne de code, toujours en le faisant précéder d'un `#`.

```python
# Calcul du prix au kilo de pommes

# Nous avons acheté 500g de pommes pour 1€
print(1 / 0.5) # Prix total (€) / Poids des pommes (Kg)
```
