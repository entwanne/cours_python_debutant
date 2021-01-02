### Bloc with

Nous avons vu les blocs `with` plus tôt, quand nous apprenions à utiliser les fichiers.
Permettant de gérer l'acquisition/libération de ressources, ils sont en fait une autre manière de traiter les exceptions.

```python
with open('hello.txt') as f:
    print(int(f.read()))
```

Dans le code précédent, même si la ligne 2 échoue (si le fichier ne contient pas un nombre), le fichier sera correctement fermé (Python appellera `f.close()` pour nous).  
Car c'est ce que garantit le bloc `with` : assurer que le code de libération de la ressource sera toujours appelé.

En cela, il s'apperente à un `try` / `finally`, puisqu'il s'agit d'exécuter une action pour acquérir la ressource (avant le `try`) puis pour la libérer (dans le `finally`).  
Mais de façon transparente, on n'a pas à faire d'appel explicite à `f.close()` pour fermer notre fichier.

Le bloc précédent est alors équivalent à :

```python
f = open('hello.txt')
try:
    print(int(f.read())
finally:
    f.close()
```

#### Supprimer une exception

* `contextlib.suppress`
