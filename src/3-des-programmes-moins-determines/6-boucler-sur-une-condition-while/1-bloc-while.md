### Boucler sur une condition

C'est ainsi qu'entre en scène la boucle `while` (qui signifie littéralement « tant que ») et qui sert à boucler sur un prédicat.
Un bloc `while` est alors assez similaire à un `if` : on a le mot-clé `while` suivi d'une expression conditionnelle puis d'un `:`, puis les lignes indentées qui correspondent au contenu du bloc.

Ce contenu sera exécuté en boucle tant que le prédicat est vrai. Mais le prédicat est resté avant chaque nouvelle itération.
Il s'agit donc dans le contenu du bloc de faire varier les valeurs utilisées par le prédicat, afin qu'il finisse par être faux et que l'on sorte de la boucle.

```python
answer = 'o'

while answer == 'o':
    print('Vous êtes dans la boucle')
    answer = input('Souhaitez-vous rester dans la boucle (o/n) ? ')

print('Vous êtes sorti de la boucle')
```

```
Vous êtes dans la boucle
Souhaitez-vous rester dans la boucle (o/n) ? o
Vous êtes dans la boucle
Souhaitez-vous rester dans la boucle (o/n) ? o
Vous êtes dans la boucle
Souhaitez-vous rester dans la boucle (o/n) ? n
Vous êtes sorti de la boucle
```

À la première ligne de mon fichier, j'initialise une variable `answer` à `'o'`.
Sans elle, la condition de mon `while` ne serait pas valide puisque `answer` n'aurait pas encore été définie (elle ne l'est ensuite que dans le bloc du `while`).

Je lui donne comme valeur `'o'` pour que la condition du `while` soit vraie et que l'on puisse entrer dans le bloc.
Si j'initialise la variable à `'n'`, alors la condition sera fausse dès le premier test et le contenu du bloc jamais exécuté.

Pour chaque tour de boucle, l'expression conditionnelle est à nouveau évaluée. Si elle s'évalue à faux, la boucle s'arrête immédiatement.
Ainsi dans mon exemple, à la 4ème itération de la boucle, `answer` vaut maintenant `'n'` (c'est la valeur qui lui a été donnée dans la 3ème itération).
L'expression étant fausse, la boucle se termine et son contenu n'est pas exécuté pour la 4ème itération.

Mais l'expression conditionnelle n'est testée qu'au tout début de chaque itération, pas au milieu de celle-ci, ce qui fait que la boucle ne peut se terminer qu'à un moment bien précis.
Dans le code qui quit, 

```python
pv = 50

print('Pythachu a', pv, 'PV')

while pv > 0:
    print('Pythachu perd 20 PV')
    pv -= 20
    print('Il lui reste maintenant', pv, 'PV')

print('Pythachu est KO, avec', pv, 'PV')
```

```
Pythachu a 50 PV
Pythachu perd 20 PV
Il lui reste maintenant 30 PV
Pythachu perd 20 PV
Il lui reste maintenant 10 PV
Pythachu perd 20 PV
Il lui reste maintenant -10 PV
Pythachu est KO, avec -10 PV
```

On constate bien qu'au cours de la 3ème itération, le nombre de PV est inférieur à 0.
Mais l'itération continue (on affiche le message), ce n'est qu'à l'itération suivante que l'expression est recalculée et que la boucle se termine.

On remarque aussi que la valeur `pv` existe toujours après la boucle, et possède la dernière valeur qui lui a été assignée.
