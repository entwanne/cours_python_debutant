### Fichier __main__.py

Il existe un autre fichier « magique » au sein des paquets, le fichier `__main__.py`
Mais avant d'y revenir, je dois vous parler de l'option `-m` de l'interpréteur Python.

C'est une option qui permet de demander à Python d'exécuter un module à partir de son nom.
Cela permet de ne pas avoir à connaître le chemin complet vers le fichier du module pour le lancer.
Et certains modules Python s'en servent pour mettre à disposition des petits programmes.

Par exemple le module `turtle` (un module de dessin présenté [en annexe]()) propose une démo si on l'exécute via `python -m turtle` :

![Démonstration de turtle.](img/demo_turtle.png)
Figure: `python -m turtle`

Cela fonctionne aussi avec nos propres modules.

```python
def hello():
    print('Hello World!')

if __name__ == '__main__':
    hello()
```
Code: `hello.py`

```shell
% python -m hello
Hello World!
```

[[i]]
| Pour rappel, le bloc conditionnel `if __name__ == '__main__'` permet de placer du code qui sera exécuté uniquement quand le module est lancé directement (`python hello.py` ou `python -m hello`) mais pas quand le module est importé.

Dans le cadre de notre paquet, `python -m operations` cherchera à exécuter son fichier `__main__.py`.
Nous pouvons alors y créer un tel fichier pour nous aussi faire une démonstration de notre paquet.

```python
from .addition import addition
from .soustraction import soustraction

if __name__ == '__main__':
    print('Addition: 3+5 =', addition(3, 5))
    print('Soustraction: 8-3 =', soustraction(8, 3))
```
Code: `operations/__main__.py`

```shell
% python -m operations
Addition: 3+5 = 8
Soustraction: 8-3 = 5
```
