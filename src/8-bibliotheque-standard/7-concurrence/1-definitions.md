### Définitions

Mais avant celà il faut comprendre un peu le fonctionnement du processeur de notre ordinateur.
Pour simplifier, celui-ci se divise en plusieurs cœurs (souvent 4 ou 8) qui représentent chacun une unité de calcul.

Une unité de calcul ne peut exécuter qu'une opération à la fois, mais un processeur disposant de plusieurs cœurs peut ainsi en exécuter plusieurs en les répartissant sur différents cœurs.  
Un processeur à 4 cœurs pourra ainsi exécuter 4 opérations à la fois par exemple.

On parle de **parallélisme** quand plusieurs tâches sont exécutées en même temps sur différents cœurs du processeur.

![Exécution parallèle.](img/concurrence_parallelisme.png)

Mais plusieurs tâches peuvent aussi s'exécuter « simultanément » sur un même cœur : celui-ci ne sera jamais en mesure d'exécuter plus d'une opération en même temps mais il peut traiter les tâches séquentiellement en exécutant leurs opérations à tour de rôle.
On parle dans ce cas de **concurrence**.

![Exécution concurrente.](img/concurrence_concurrence.png)

[[i]]
| La **concurrence** désigne aussi le fait de partager et d'accéder à des ressources communes (un même fichier, une même liste) depuis plusieurs tâches, et la nécessité de gérer convenablement les accès simultanés (concurrents) à ces ressources.

Enfin deux tâches peuvent coexister dans un programme mais n'être traitées qu'à tour de rôle quand le programme le décide (par exemple suspendre une tâche le temps qu'un résultat arrive, la reprendre ensuite pour finaliser le traitement).
On parle dans ce dernier cas de programmation **asynchrone**.

![Exécution asynchrone.](img/concurrence_asynchrone.png)

La différence entre concurrence et asynchrone étant que dans le premier cas c'est le système/processeur qui s'occupe du cadencement des tâches et que dans le second c'est le programme (et donc par extension la personne qui le développe) qui le décide.
