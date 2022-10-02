### Une histoire d'automates

La solution que nous venons de réaliser s'apparente à un automate fini, un modèle de calcul qui parcourt des données séquentiellement (notre chaîne caractère par caractère) afin d'identifier des motifs, le tout sans utiliser de mémoire.

L'ensemble des motifs (ou mots) qui peuvent être identifiés par un automate forme ce qu'on appelle un langage.
Dans notre exemple le langage est formé des représentations de nombres de la forme `123` et `4.56` pouvant être préfixés d'un `+` ou d'un `-`.

Il est d'usage de représenter un automate sous la forme d'un graphe montrant les relations entre les états.

![Automate](img/automate.png)
Figure: Automate `is_number` -- image générée par [regexper](https://regexper.com/)

Un état correspond à l'avancée dans la chaîne de caractères, en consommant les caractères qui correspondent au motif.  
On part de l'état initial (à gauche) et on avance vers la droite tant qu'un chemin correspond au caractère lu dans notre chaîne (plusieurs chemins sont possibles).
Si l'on atteint l'état final (à droite) alors c'est que le motif est reconnu dans la chaîne.

![Animation automate](img/automate_gif.gif)
Figure: Animation de l'automate pour tester la chaine `-123.45`

Il existe plusieurs types d'automates, les automates finis étant les plus simples d'entre eux.
On dit d'un langage formé de mots reconnaissables par un automate fini qu'il est rationnel, d'où le terme d'expression rationnelle.

Le graphe ci-dessus représente donc une expression rationnelle pour reconnaître les chaînes représentant des nombres. Mais nous allons tout de suite voir une manière plus formelle de la décrire.
