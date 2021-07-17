### Boucle for ou boucle while ?

Avec nos deux types de boucles, on pourrait se demander quand utiliser l'une et quand utiliser l'autre.

Un bloc `while` correspond à l'action de répéter. On répète un même traitement et on fait varier les paramètres.  
Il peut s'agir d'attendre une certaine entrée utilisateur ou d'affiner un calcul par exemple.
Le but est alors que la boucle `while` serve à construire/calculer une valeur que l'on réutilisera par la suite.

On peut par exemple imaginer une boucle `while` pour calculer itérativement la racine carrée de 2 selon la [méthode de Héron](https://fr.wikipedia.org/wiki/M%C3%A9thode_de_H%C3%A9ron), en s'arrêtant quand une certaine précision a été atteinte.

```python
x = 1

while abs(2 - x**2) > 0.001:
    x = (x + 2/x) / 2

print('La racinne carrée de 2 vaut environ', x)
```

Pour tout le reste, il y a la boucle `for`.

Un bloc `for` correspond à l'action d'itérer, de parcourir des éléments.  
Quand on souhaite exécuter une action pour chaque valeur d'une séquence identifiable (éléments d'une liste, caractères d'une chaîne, nombres d'un intervalle, etc.) c'est un `for` qui doit être utilisé, pour tout ce qui peut s'apparenter à de l'itération sur des valeurs.

Dans l'exemple des boucles infinies, nous n'aurions par exemple pas rencontré de problème en utilisant une boucle `for`.
Ces dernières sont en effet plus facilement prédictibles si l'on sait que l'on va itérer sur un ensemble fini d'éléments (tel qu'un intervalle de nombres).

```python
n = int(input('Entrez un nombre : '))

fact = 1
for i in range(2, n + 1):
    fact *= i

print('La factorielle de', n, 'vaut', fact)
```
