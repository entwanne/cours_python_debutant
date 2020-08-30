### Traiter l'exception

* Blocs `try`/`except`
* Attraper la bonne exception (le plus finement possible)

Pour gérer les exceptions on va utiliser un nouveau type de bloc, ou plutôt un couple de blocs.
Il s'agit de `try` et `except`, l'un ne va pas sans l'autre.

Dans le bloc `try`, on place le code qui peut potentiellement échouer

```python
try:
    result = 1 / 0
except:
    print('Division par zéro')
```

* Mécanisme de la remontée d'erreur
* Placer judicieusement les except
