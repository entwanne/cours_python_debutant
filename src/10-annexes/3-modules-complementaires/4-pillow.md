### Pillow

_Pillow_ est un paquet Python dédié à l'imagerie, c'est une bibliothèque qui permet de lire et créer des images.

Le paquet _Pip_ s'appelle _Pillow_ (`pip install Pillow`), mais c'est ensuite un module `PIL` qu'il faut importer depuis le code.
_PIL_ était l'ancien nom du paquet (en Python 2), _Python Image Libary_.

```python
from PIL import Image, ImageDraw

img = Image.new('RGB', (400, 300), color='red')  # crée une nouvelle image
draw = ImageDraw.Draw(img)
draw.rectangle(((100, 100), (300, 200)), fill='blue')
img.show()  # affiche l'image dans une fenêtre
img.save('output.png')  # enregistre l'image
```

Des informations complémentaires sur _Pillow_ peuvent être trouvée dans [la documentation de la bibliothèque](https://pillow.readthedocs.io/en/stable/).
