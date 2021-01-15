### Introspection

* Principe de l'introspection
* Examiner une valeur (objet, fonction, module) avec `repr`, `type`, `help`, `dir`, `vars`

Avant d'en venir proprement au débogage de notre programme, faisons un tour des outils qui sont à notre disposition pour examiner notre programme.
Il s'agit de fonctions proposées par Python pour inspecter différentes valeurs du programme.  
On parle d'outils d'introspection car ils permettent au programme de s'examiner lui-même.

La première information, toute bête, c'est la valeur en elle-même, ou plutôt sa représentation.
C'est ce que l'on obtient quand on tape juste le nom de la variable dans l'interpréteur interactif par exemple.

```python
>>> value = 'toto'
>>> value
'toto'
```

Cette représentation est fournie par la fonction `repr`, qui renvoie donc une chaîne de caractères représentant la valeur.
Elle peut tout à fait être appelée depuis un programme pour afficher (avec `print`) l'état d'une variable.

```python
print(repr(value))
```

On connaît par exemple déjà la fonction `type` qui renvoie le type d'une valeur.
C'est tout bête mais c'est déjà un

* Suivre et comprendre les exceptions
* Débogage à l'aide de `print`
* Débogage à l'aide de tests (assertions)
