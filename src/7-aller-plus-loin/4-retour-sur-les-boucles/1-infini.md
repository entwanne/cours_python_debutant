### Vers l'infini et au-delà

* Boucles infinies
* Théorème de l'arrêt (turing-complete, non prouvable)
* => Faire attention aux conditions (et préférer les `for` plus facilement prédictibles)

* Sortir d'une boucle : `break`

Nous avons vu les boucles `for` pour itérer sur des données, puis les boucles `while` pour boucler sur une condition.
Dans tous nos cas, nous considérions que nos boucles étaient finies, qu'elles se termineraient forcément après un certain nombre de tours.
Mais ce n'est pas toujours le cas, et volontairement ou non on peut tomber dans des cas de boucle infinie.

```python
while True:
    print("Vers l'infini et au-delà !")
```

[[i]]
| Utilisez la combinaison de touches ||Ctrl+C|| pour couper le programme.

Volontairement, ça peut être pour laisser tourner un programme en tâche de fond -- un serveur par exemple -- qui tournerait continuellement pour traiter des requêtes.
Et dans ce cas des dispositifs seront mis en place pour terminer proprement le programme quand on le souhaite.

Involontairement c'est plus problématique, et ça peut arriver avec une boucle `while` dont la condition serait toujours vraie.
Le cas précédent est flagrant mais ça ne l'est pas toujours autant.

```python
```

Le soucis c'est qu'à l'exécution il n'est théoriquement pas possible de savoir si une boucle va s'arrêter ou non, c'est un problème indécidable (théorème de l'arrêt).
Ainsi, il faut être prudent et faire très attentions aux conditions utilisées pour les `while`, ou utiliser autant que possible des boucles `for`, plus facilement prédictibles.