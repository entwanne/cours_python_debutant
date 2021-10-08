### Définir une fonction (bloc def)

On définit une fonction à l'aide du mot-clé `def` qui introduit un bloc.
On le fait suivre du nom de la fonction, d'une paire de parenthèses et d'un signe `:`.
Toutes les lignes indentées qui suivent appartiendront au corps de la fonction.

```python
def toto():
    print('Hello')
    print('World!')
```

Ainsi, les lignes ne sont pas directement exécutées.
Le bloc de code précédent ne fait que créer une nouvelle fonction connue sous le nom de `toto`.
Son contenu sera exécuté lors de l'appel à la fonction.

Le nom d'une fonction est similaire à celui d'une variable, et doit donc se soumettre aux mêmes règles : composé uniquement de lettres, de chiffres et d'_underscores_ (`_`), et ne pouvant pas commencer par un chiffre.
