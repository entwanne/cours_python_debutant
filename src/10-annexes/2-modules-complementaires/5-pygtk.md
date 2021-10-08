### PyGObject (PyGTK)

_PyGObject_ (anciennement _PyGTK_) est une bibliothèque qui permet de créer des programmes fenêtrés, des interfaces graphiques riches (_GUI_) formées de zones de texte, de menus ou encore de boutons.  
Elle repose sur _Gtk_, un module logiciel écrit en C pour réaliser de telles interfaces, notamment utilisé par Gimp, Firefox ou encore Gnome.

![Caputre d'écran](img/pygobject_example.png)
Figure: Capture d'écran de _Quod Libet_, un lecteur de musique écrit en Python utilisant _PyGtk_.

La procédure d'installation de _PyGObject_ varie selon les systèmes, je vous laisse donc consulter [cette page](https://pygobject.readthedocs.io/en/latest/getting_started.html) pour trouver celle qui vous convient.

Ensuite je vous invite à lire [ce tutoriel](https://zestedesavoir.com/tutoriels/870/des-interfaces-graphiques-en-python-et-gtk/) de @Wizix sur Zeste de Savoir pour apprendre comment prendre en main cette bibliothèque.
Vous pouvez aussi vous reporter au [tutoriel officiel](https://python-gtk-3-tutorial.readthedocs.io/en/latest/) (en anglais).  
Voici néanmoins un code permettant de réaliser une petite interface.

```python
import gi
# Vérification de la version de Gtk
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

# Création d'une fenêtre
window = Gtk.Window(title='Hello World')
box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
window.add(box)

# Ajout d'éléments graphiques

label = Gtk.Label(label='Salut')
box.pack_start(label, True, True, 0)

button = Gtk.Button(label='Clique !')
box.pack_start(button, True, True, 0)

# Connexion des événements et affichage

window.show_all()
window.connect('destroy', Gtk.main_quit)
button.connect('clicked', Gtk.main_quit)

Gtk.main()
```

Consultez aussi [le site officiel](https://pygobject.readthedocs.io/) pour aller plus loin avec _PyGtk_.

[[i]]
| Bon à savoir : la bibliothèque standard de Python embarque le module [`tkinter`](https://docs.python.org/fr/3/library/tkinter.html) pour créer des programme fenêtrés, mais qui n'est pas forcément le module le plus abordable pour cela.  
| Sur certains systèmes (Debian/Ubuntu par exemple) il n'est pas présent par défaut et il faut installer le paquet _APT_ `python3-tk`.
|
| Voir [Programmation avec tkinter](https://zestedesavoir.com/tutoriels/1729/programmation-avec-tkinter/) de @Dan737 pour en apprendre plus sur _tkinter_.

_PyGtk_ et _tkinter_ ne sont pas les seules bibliothèques pour écrire des programmes _GUI_, on trouve par exemple [_PyQt_](https://riverbankcomputing.com/software/pyqt/intro) ou [_wxPython_](https://www.wxpython.org/).
