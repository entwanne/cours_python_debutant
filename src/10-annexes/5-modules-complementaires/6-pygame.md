### Pygame

_Pygame_ est aussi une bibliothèque dédiée à écrire des interfaces graphiques, mais pas des programes fenêtrés.
Elle est plutôt dédiée aux interfaces « imagées », comme des jeux vidéo.

![Capture d'écran](img/pygame_example.png)
Figure: _Flappython_, un jeu-vidéo fictif que l'on pourrait réaliser avec _Pygame_.

Elle s'installe par la commande `pip install pygame` dans l'environnement courant.

Elle met ensuite à disposition différents éléments graphiques pour créer des fenêtres et dessiner à l'écran.

```python
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
running = True

screen.fill((255, 255, 255))
pygame.draw.rect(screen, (0, 0, 255), (200, 200, 400, 200))

while running:
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
```

Pour apprendre à utiliser _Pygame_, je vous renvoie à [ce tutoriel](https://zestedesavoir.com/tutoriels/846/pygame-pour-les-zesteurs/) de @SuperFola sur Zeste de Savoir et [à la documentation](https://www.pygame.org/docs/) de la bibliothèque.

Une fois encore, _Pygame_ n'est pas seule dans son domaine, vous trouverez ainsi [_pyglet_](http://pyglet.org/) (abstraction autour d'_OpenGL_, plus bas-niveau), [_Arcade_](https://api.arcade.academy/) (construite autour de _pyglet_) ou [_PySFML_](https://github.com/intjelic/python-sfml) (qui ne semble plus maintenue).
