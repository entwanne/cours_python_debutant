### Méthodes des chaînes de caractères

* `capitalize`, `upper`, `lower`, `index`
Les chaînes de caractères possèdent d'autres méthodes utiles dont voici un bref aperçu.

#### `strip`

La méthode `strip` vue précédemment retire les espaces aux extrêmités de la chaîne, mais n'affecte pas ceux qui se trouvent au milieu.

```python
>>> ' hello   world '.strip()
'hello   world'
```

#### `capitalize` et `title`

`capitalize` est une méthode qui permet de passer en majuscule le premier caractère de la chaîne (si c'est une lettre) et en minuscules tous les autres.

```python
>>> 'coucou'.capitalize()
'Coucou'
>>> 'COUCOU'.capitalize()
'Coucou'
```

Semblable à `capitalize`, `title` effectue ce traitement sur tous les mots de la chaîne de caractères.

```python
>>> 'bonjour à tous'.capitalize()
'Bonjour à tous'
>>> 'bonjour à tous'.title()
'Bonjour À Tous'
```

#### `upper` et `lower`

Il s'agit ici de passer la chaîne entière en majuscules ou en minuscules.

```python
>>> 'CoUcOu'.upper()
'COUCOU'
>>> 'CoUcOu'.lower()
'coucou'
```

#### `index`

La méthode `index` permet de trouver un caractère dans la chaîne et d'en renvoyer la position.
Il s'agit donc du comportement réciproque de l'opérateur `[ ]`.

```python
>>> text = 'abcdef'
>>> text.index('d')
3
>>> text[3]
'd'
```

À noter que si l'opérateur est présent plusieurs fois, c'est la première position trouvée qui est renvoyée.

```python
>>> 'abcabc'.index('b')
1
```

Et une erreur survient si le caractère n'est pas trouvé.

```python
>>> 'abcdef'.index('g')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found
```
