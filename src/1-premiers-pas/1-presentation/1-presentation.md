### Qui es-tu, Python ?

![Logo de Python](img/logo_python.png)

Comme je le disais en introduction, Python est ce que l'on appelle un langage de programmation.  
L'ordinateur ne parlant pas notre langue, il est nécessaire d'adopter la sienne pour parler avec lui.
Mais celle-ci est très rudimentaire, c'est le langage machine compris par le processeur.

Avec le temps, d'autres langages sont apparus autour pour pouvoir communiquer avec l'ordinateur plus simplement que par des instructions processeurs, les langages de programmation.  
Je ne pourrais pas vous en faire de liste exhaustive tellement ils sont nombreux, même Wikipédia [a du mal à le faire](https://fr.wikipedia.org/wiki/Liste_de_langages_de_programmation).

Python est un langage dit de haut-niveau, c'est-à-dire qu'il s'éloigne du langage machine en ajoutant des concepts et des outils le rendant plus facile à lire et à écrire, plus proche du langage humain (de l'anglais en l'occurrence).

Python est aussi un langage portable : en dehors de certains cas exceptionnels, un programme Python peut être exécuté de la même manière sur un ordinateur Windows, Mac OS ou GNU/Linux, ainsi que sur des OS mobiles comme Android ou iOS.

Voici un exemple de code écrit en Python :

```python
def hello(name=None):
    if name is None:
        print('Hello World!')
    else:
        print('Hello', name)

hello('Clem')
hello()
```
Code: Un programme tout simple pour dire bonjour en Python

Comme on peut l'apercevoir dans l'exemple, Python est un langage qui se base sur l'indentation.
Il s'agit des espaces que l'on voit en début de lignes et qui permettent de délimiter les portions logiques du code.  
L'indentation, souvent recommandée dans les autres langages pour aérer le code et le rendre plus agréable à lire, est une nécessité en Python.

![Illustration piles incluses](img/batteries_included.jpg)
Figure: « Piles incluses » -- _Crédits: [Frank Stajano](https://commons.wikimedia.org/wiki/File:Python_batteries_included.jpg)_

Python est parfois qualifié de « piles incluses », par rapport au fait qu'il est fourni de base avec beaucoup de fonctionnalités (création de fenêtres, gestion native de différents formats de fichiers, etc.).  
Mais en plus de ça il dispose d'une large communauté de développeurs et développeuses, contribuant à élargir l'écosystème Python en développant un grand nombre de nouveaux outils pour répondre à des tâches particulières, que vous pourrez réutiliser à votre tour dans vos logiciels.  
Cette forte communauté fournit aussi à Python une documentation très complète, qui est de plus traduite en français.

De même, vous trouverez facilement quelqu'un dans la communauté Python pour vous aider dans votre développement, en vous orientant vers des forums de discussion tels que celui de Zeste de Savoir.

On dit aussi de Python qu'il est un langage orienté objet.  
Cela signifie que les valeurs que l'on y manipule sont des objets : ils ont des propriétés et des actions qui leur sont propres, ils interagissent les uns avec les autres.

C'est une technologie libre d'utilisation et gratuite.
Vous pouvez utiliser Python dans vos programmes comme vous le voulez, distribuer ou vendre ces programmes.
Cela signifie aussi que vous pouvez vous-même contribuer au code de Python.

Python se démarque par sa lisibilité, mais cela représente un coût en performances car il faut dans tous les cas que le code soit converti en langage machine.  
Cela ne devrait pour autant pas trop vous limiter dans ce que vous pourrez faire avec lui, comme je le montre dans la section qui suit.

De plus c'est un langage extensible, il vous sera donc toujours possible de réaliser du code dans un autre langage dont vous tireriez d'autres avantages puis de le brancher à du code Python.
