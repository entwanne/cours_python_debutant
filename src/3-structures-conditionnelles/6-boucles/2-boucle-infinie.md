### Vers l'infini et au-delà

Notre boucle `while` s'arrête quand le prédicat devient faux.
Mais que se passe-t-il alors si celui-ci est toujours vrai ?  
Notre boucle se retrouve alors à tourner indéfiniment…

```pycon
>>> while True:
...     print("Vers l'infini et au-delà !")
... 
Vers l'infini et au-delà !
Vers l'infini et au-delà !
Vers l'infini et au-delà !
Vers l'infini et au-delà !
Vers l'infini et au-delà !
Vers l'infini et au-delà !
Vers l'infini et au-delà !
[...]
```

[[i]]
| Quand votre programme rencontre une boucle infinie, utilisez la combinaison de touches ||Ctrl+C|| pour l'interrompre.

Bien sûr, nous avons ici écrit volontairement une boucle infinie, mais celles-ci sont plus insidieuses et peuvent parfois se cacher là où on ne les attend pas.
Prenons par exemple le programme suivant qui a pour but de calculer la factorielle[^factorielle] d'un nombre.

[^factorielle]: La factorielle est la fonction mathématique calculant le produit des nombres entiers de 1 à n. Ainsi la factorielle de 5 est $1 \times 2 \times 3 \times 4 \times 5$ soit 120.

```python
n = int(input('Entrez un nombre : '))

i = n
fact = 1
while i != 0:
    fact *= i
    i -= 1

print('La factorielle de', n, 'vaut', fact)
```
Code: factorielle.py

Ce code fonctionne très bien pour des entiers naturels :

```
% python factorielle.py
Entrez un nombre : 5
La factorielle de 5 vaut 120
% python factorielle.py
Entrez un nombre : 1
La factorielle de 1 vaut 1
```

Mais dans le cas où l'on entre un nombre négatif, le programme se met à boucler indéfiniment et l'on doit le couper avec un ||Ctrl+C||.

```
% python factorielle.py
Entrez un nombre : -1
^CTraceback (most recent call last):
  File "factorielle.py", line 6, in <module>
    fact *= i
KeyboardInterrupt
```

En effet, pour un nombre négatif la condition `n != 0` sera toujours vrai puisque le nombre est décrémenté à chaque tour de boucle (il restera négatif et ne sera jamais nul).
Dans l'idéal il faudrait donc traiter les nombres négatifs comme une erreur et afficher un avertissement dans ces cas-là pour prévenir toute boucle infinie.

Le souci est qu'à l'exécution il n'est théoriquement pas possible de savoir si une boucle va s'arrêter ou non, c'est un problème indécidable ([problème de l'arrêt](https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_l%27arr%C3%AAt)) : dans le cas précédent on ne sait pas quelle valeur sera donnée à notre programme puisqu'elle dépend d'une saisie de l'utilisateur.  
Ainsi, il faut être prudent et faire très attention aux conditions utilisées pour les `while` et bien s'assurer que celles-ci finissent toujours par devenir fausses.

Mais nous découvrirons par la suite qu'il y a des usages légitimes de boucles infinies, et des moyens de contrôler le déroulement de la boucle.
