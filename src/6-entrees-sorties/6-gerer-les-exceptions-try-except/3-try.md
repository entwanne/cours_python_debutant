### Traiter l'exception

* Blocs `try`/`except`
* Attraper la bonne exception (le plus finement possible)

Pour gérer les exceptions on va utiliser un nouveau type de bloc, ou plutôt un couple de blocs, introduits par les mots-clés `try` et `except` (littéralement « essaie » et « à l'exception de »).

Ces deux mots-clés vont de paire pour intercepter les erreurs.  
Dans le bloc `try` on place le code qui peut échouer, et le bloc `except` sera exécuté si et seulement si une exception survient.
Il aura pour effet d'attraper cette exception et donc éviter que le programme ne plante.

```python
>>> try:
...     result = 1 / 0
... except:
...     print('Division par zéro')
...
Division par zéro
```

* Mécanisme de la remontée d'erreur
* Placer judicieusement les except
