### Un peu de dessin

Et si nous nous intéressions à des algorithmes un peu plus visuels ?
Dans cette section je vous propose de dessiner diverses formes géométriques, à l'aide de caractères affichés dans le terminal.

#### Affichons un rectangle

Un premier exercice simple consiste à afficher un rectangle dans le terminal.
À partir d'une largeur et d'une hauteur données (par exemple via des `input()`), on peut afficher les différents caractères pour dessiner les bords de notre rectangle.

On pourrait par exemple utiliser le caractère `+` pour les coins, `-` pour les lignes horizontales et `|` pour les lignes verticales.

Voici ce que donnerait un rectangle de dimensions 10×5 :

```
+--------+
|        |
|        |
|        |
+--------+
```
Code: Rectangle 10×5

[[i]]
| Comme vous le voyez, les coins sont compris dans les dimensions du rectangle.  
| Pensez alors aux cas « dégénérés » tels que des rectangles de dimensions 5×1, 5×2, 1×5, 1×1, 0×0, etc.

Et voici une solution possible pour cet exercice :

[[s]]
| ```python
| width = int(input('Entrez la largeur : '))
| height = int(input('Entrez la hauteur : '))
| 
| for y in range(height):
|     line = ''
| 
|     if y == 0 or y == height - 1:
|         if width > 0:
|             line += '+'
|         line += '-' * (width - 2)
|         if width > 1:
|             line += '+'
|     else:
|         if width > 0:
|             line += '|'
|         line += ' ' * (width - 2)
|         if width > 1:
|             line += '|'
| 
|     print(line)
| ```

#### Passons au triangle

Augmentons un peu la difficulté et cherchons maintenant à afficher un triangle.
Il s'agit d'un triangle équilatéral défini par sa hauteur. Voici par exemple un triangle de hauteur 10 :

```
         *
        * *
       *   *
      *     *
     *       *
    *         *
   *           *
  *             *
 *               *
*******************
```
Code: Triangle de hauteur 10

[[i]]
| Chaque ligne du triangle fait ainsi toujours deux caractères de plus que la précédente : `*` donne suite à `* *` puis `*   *`, etc.

Et comme vous le voyez, les lignes devront être centrées pour avoir un joli résultat.

[[i]]
| Pour connaître la marge à appliquer à gauche de chaque ligne, pensez à calculer en amont la taille de la dernière ligne.

Sans plus attendre, la solution :

[[s]]
| ```python
| height = int(input('Entrez la hauteur : '))
| 
| max_len = 2 * height - 1
| 
| width = 1
| 
| for y in range(height):
|     padding = (max_len - width) // 2
|     line = ' ' * padding
| 
|     if width > 2 and y != height - 1:
|         line += '*' + ' ' * (width - 2) + '*'
|     else:
|         line += '*' * width
| 
|     print(line)
|     width += 2
| ```

#### Mon beau sapin, roi des forêts

Encore un cran de difficulté supplémentaire, mais le code du précédent triangle va nous être bien utile.
On voudrait maintenant faire dessiner un sapin à notre programme.

Un sapin serait composé de triangle et trapèzes empilés, ainsi qu'un rectangle pour le tronc.
Il serait là encore défini par une hauteur, désignant le nombre de sections du sapin ainsi que la taille de son tronc.

Vous trouverez ci-dessous des exemples de sapins de différentes tailles.

```
   *
  ***
 *****
*******
   |
```
Code: Sapin de taille 1

```
          *
         ***
        *****
       *******
        *****
       *******
      *********
     ***********
    *************
     ***********
    *************
   ***************
  *****************
 *******************
*********************
         |||
         |||
         |||
```
Code: Sapin de taille 3

```
              *
             ***
            *****
           *******
            *****
           *******
          *********
         ***********
        *************
         ***********
        *************
       ***************
      *****************
     *******************
    *********************
      *****************
     *******************
    *********************
   ***********************
  *************************
 ***************************
*****************************
            |||||
            |||||
            |||||
            |||||
```
Code: Sapin de taille 4

[[i]]
| Triangles et trapèzes se dessinent à peu près de la même manière.

[[a]]
| Attention aux tailles paires pour les dimensions du tronc.

Je ne vous propose pas de solution pour cet exercice, mais sachez que vous pouvez le retrouver sur la plateforme HackInScience : [Le sapin](https://www.hackinscience.org/exercises/sapin).

[[i]]
| [HackInScience](https://www.hackinscience.org/) est un site d'exercices algorithmiques à réaliser avec Python où vous trouverez beaucoup d'exercices de ce genre.
| Vous pouvez y exécuter directement vos codes et valider vos solutions.  
| Un exercice validé permet d'accéder aux solutions partagées par les autres membres du site.
