### Déboguer avec votre IDE

Jongler entre l'éditeur de texte d'un côté et le débogueur de l'autre n'est pas toujours évident.
Certains éditeurs permettent d'intégrer directement le débogueur dans leur interface.
C'est le cas de PyCharm par exemple.

Il est ainsi possible de cliquer à gauche des lignes de code pour placer des points d'arrêt.
Ils sont illustrés par un rond rouge dans la marge.
Cliquer sur un tel rond permet de supprimer un point d'arrêt déjà posé.

![Point d'arrêt dans PyCharm.](img/pycharm_breakpoint.png)

Il faut ensuite exécuter le programme en mode _debug_ (_Run > Debug_) pour les prendre en compte.
L'exécution se déroule alors normalement nous demandant d'entrer les différentes saisies, puis le programme se met en pause et bascule sur l'interface de débogage quand le point d'arrêt est rencontré.

![Interface de débogage.](img/pycharm_debug.png)

Là nous pouvons directement avoir un aperçu des variables présentes dans la fonction, et les boutons reprennent les actions que nous avons pu voir avec Pdb : passer à l'instruction suivante, reprendre l'exécution du programme, redémarrer depuis le début, etc.

Pour plus d'informations sur le débogage avec PyCharm je vous invite à consulter [cette page d'aide](https://www.jetbrains.com/help/pycharm/part-1-debugging-python-code.html#summary) (en anglais).
