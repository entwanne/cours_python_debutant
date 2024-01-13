### Numpy

_Numpy_ est une bibliothèque dédiée au calcul numérique, offrant de bonnes performances pour ces opérations.
Elle est très utilisée dans le domaine scientifique (_data science_).

Elle s'installe facilement avec _Pip_ : `pip install numpy` .

Ensuite c'est une bibliothèque qui permet notamment de manipuler des tableaux de données (de même type), et d'effectuer des opérations en lots sur les valeurs de ces tableaux.

```pycon
>>> import numpy as np
>>> array = np.array([[1, 2, 3], [4, 5, 6]])
>>> array.size  # nombre de valeurs
6
>>> array.ndim  # nombre de dimensions
2
>>> array.shape  # taille des dimensions
(2, 3)
>>> array.dtype  # type des valeurs
dtype('int64')
>>> array
array([[1, 2, 3],
       [4, 5, 6]])
>>> array + 1
array([[2, 3, 4],
       [5, 6, 7]])
>>> array * 3
array([[ 3,  6,  9],
       [12, 15, 18]])
>>> array + np.arange(10, 16).reshape(2, 3)
array([[11, 13, 15],
       [17, 19, 21]])
```

Pour aller plus loin, rendez-vous [sur la documentation de la bibliothèque _Numpy_](https://numpy.org/doc/stable/).

Intéressez-vous aussi aux bibliothèques [_SciPy_](https://www.scipy.org/scipylib/index.html) (calculs numériques, calculs formels) et [_pandas_](https://pandas.pydata.org/) (analyse de données) construites autour de _Numpy_ qui s'utilisent conjointement avec elle.  
La [_matplotlib_](https://matplotlib.org/), une bibliothèque de visualisation et de dessin de graphiques en Python est aussi couramment utilisée avec _Numpy_, [un cours](https://zestedesavoir.com/tutoriels/469/introduction-aux-graphiques-en-python-avec-matplotlib-pyplot/) est même disponible sur Zeste de Savoir à son sujet.
