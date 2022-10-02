### Une histoire d'automates

Ce processus que nous venons de réaliser avance pas à pas dans notre chaîne de caractères, identifiant à chaque étape s'il peut continuer ou s'il doit s'arrêter.
On peut le représenter comme un ensemble d'états (les caracèteres ou motifs attendus dans la chaîne) reliés par des transitions/liens selon quand il est possible de passer d'un état à l'autre.

Voici ainsi une représentation schématique de notre fonction `is_number`, on l'appelle un automate fini.

![Automate](img/automate.png)
Figure: Automate `is_number` -- image générée par [regexper](https://regexper.com/)

Cette représentation nous montre que pour qu'une chaîne soit reconnue comme valide, il faut pouvoir trouver un chemin reliant l'état `Start of line` à l'état `End of line` en parcourant les caractères de la chaîne.
Chaque état traversé consomme un caractère et un état peut être traversé plusieurs fois si les transitions le permettent, formant ainsi une boucle.

Un automate fini est un modèle de calcul qui parcourt des données séquentiellement (notre chaîne caractère par caractère) afin d'identifier des motifs, le tout sans utiliser de mémoire.

L'ensemble des motifs (ou mots) qui peuvent être identifiés par un automate forme ce qu'on appelle un langage.
Dans notre exemple le langage est formé des représentations de nombres de la forme `123` et `4.56` pouvant être préfixés d'un `+` ou d'un `-`.  
Il est d'usage de représenter un automate sous la forme d'un graphe montrant les relations entre les états comme précédemment.

Un état correspond à l'avancée dans la chaîne de caractères, en consommant les caractères qui correspondent au motif.  
On part de l'état initial (à gauche) et on avance vers la droite tant qu'une transition correspond au caractère lu dans notre chaîne (plusieurs chemins sont possibles).
Si l'on atteint l'état final (à droite) alors c'est que le motif est reconnu dans la chaîne.

![Animation automate](img/automate_gif.gif)
Figure: Animation de l'automate pour tester la chaine `-123.45`

Il existe plusieurs types d'automates, les automates finis étant les plus simples d'entre eux.
On dit d'un langage formé de mots reconnaissables par un automate fini qu'il est rationnel, d'où le terme d'expression rationnelle.

Le graphe ci-dessus illustre donc une expression rationnelle pour reconnaître les chaînes représentant des nombres. Mais nous allons tout de suite voir une manière plus formelle de la décrire.
