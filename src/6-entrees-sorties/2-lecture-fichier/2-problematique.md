### Problématique : sauvegarder l'état de notre jeu

Avec notre jeu, nous sommes pour l'instant obligé de faire toute la partie en une fois.
Bon, il est assez simpliste et ne consiste que dans un combat.

Mais imaginons que nous le développions pour avoir un système de tournoi, ou développer un RPG autour, alors il serait pratique de pouvoir mettre le jeu en pause.
Pour cela, il va falloir d'une manière ou d'une autre enregistrer l'état actuel du jeu afin de le reprendre plus tard.

Et la manière la plus simple de procéder, c'est d'utiliser un fichier : l'état du jeu sera sauvegardé dans le fichier à la fermeture, et rechargé depuis le même fichier au lancement.
Nous allons donc dans un premier temps voir comment nous pouvons gérer nos fichier, et dans un second nous nous intéresserons au format des données.
