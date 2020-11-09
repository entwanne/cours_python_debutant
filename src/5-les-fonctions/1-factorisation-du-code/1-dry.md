### Don't Repeat Yourself

L'idée première, c'est d'éviter de se répéter, de dupliquer du code.
En effet, il y a plusieurs portions du code de notre TP qui pourraient être mises en commun et qui nous ferait gagner en clarté.

Un code dupliqué, c'est un code plus diffile à maintenir.
Déjà, il est plus long à lire et il faut garder plus d'éléméents de contexte en tête pour le comprendre.
Mais ça alourdit aussi les étapes de réécriture / correction.

Quand un code est présent à un seul endroit, il n'y a que cet endroit à réécrire pour l'adapter.
Quand il est dupliqué à dix emplacements différents, il devient plus difficile d'aller tous les corriger.
Et une erreur peut facilement s'y glisser, si l'on oublie l'un de ces emplacements.

En factorisant le code, on isole les portions logiques que l'on peut ainsi plus facilement retrouver.
On divise ainsi un programme en plusieurs petites portions de code qu'il est aisé de relire indépendamment les unes des autres.
On verra aussi par la suite qu'un code divisé en fonctions est plus facile à tester.
