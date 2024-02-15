### Un monde rempli de bugs

Dans un monde idéal, on écrirait le code d'un programme du premier coup et celui-ci fonctionnerait sans aucun bug.
Malheureusement ce monde n'est pas le nôtre, ici les bugs sont légion.

Regardez le code suivant, qui se veut être un équivalent à la fonction `sum` de Python.

```python
def my_sum(numbers):
    result = numbers[0]
    size = len(numbers) - 1
    for i in range(1, size):
        result += numbers[i]
```

En regardant le code rapidement on se dit que ça doit répondre au problème.
Et pourtant plusieurs bugs se sont glissés dans le code de la fonction qui font qu'elle ne pourra pas renvoyer le bon résultat.

Pour vérifier ça on va tester notre fonction, c'est-à-dire l'appeler avec différents arguments et vérifier son comportement et sa valeur de retour.

On pourrait tester une fois pour toutes les cas qui nous passent par la tête, considérer la fonction comme bonne si elle valide tout et ne plus y toucher, mais c'est une technique qui risquerait de laisser passer beaucoup de bugs.
En effet, un code est amené à évoluer. Et si nous touchons au code de notre fonction (ou d'une autre fonction qu'elle appellerait), il faudrait nous assurer que son comportement est toujours le bon, qu'il n'y a pas eu de régressions.

Pour cela, on préfère avoir une suite de tests que l'on réappliquera à chaque nouvelle modification, afin de vérifier que nous n'avons rien cassé (que le comportement est toujours celui attendu).
Il faudra donc écrire les scénarios de tests les plus précis et complets possibles pour qu'ils couvrent bien tout ce que doit réaliser la fonction.

Des bugs peuvent se glisser à toutes les phases du développement, et il est donc préférable de ne pas attendre la fin du développement d'une fonctionnalité pour la tester.
Tester tôt permet en effet d'éliminer plus tôt les bugs rencontrés, et de ne pas les enfouir sous d'autres couches qui les rendront plus difficilement détectables.

Certains modèles vont encore plus loin et préconisent l'écriture des tests avant même de réaliser les fonctionnalités cibles (on parle de _test-driven development_).
Cela permet d'être clair sur le comportement attendu et d'avancer itérativement en écrivant les tests puis les fonctionnalités, jusqu'à ce que notre fonction remplisse tous les cas de tests attendus.

Nous allons maintenant voir comment écrire simplement nos scénarios de tests en Python.
