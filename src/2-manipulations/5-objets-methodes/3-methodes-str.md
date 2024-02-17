### Méthodes des chaînes de caractères

Les chaînes de caractères possèdent d'autres méthodes utiles dont voici un bref aperçu.
Nous en découvrirons encore bien d'autres dans la suite de ce cours.

#### `strip`

La méthode `strip` vue précédemment retire les espaces aux extrémités de la chaîne, mais n'affecte pas ceux qui se trouvent au milieu.

```pycon
>>> ' hello   world '.strip()
'hello   world'
```

Il est possible d'appliquer la méthode sur une variable si celle-ci est assignée à une chaîne de caractères.
Ou sur toute autre expression s'évaluant comme une chaîne de caractères, des parenthèses pouvant alors être nécessaires pour changer la priorité de l'opération.

```pycon
>>> text = ' hello   world '
>>> text.strip()
'hello   world'
>>> input().strip()
  coucou
'coucou'
>>> (' to' * 3).strip()
'to to to'
```

Cette méthode, tout comme les autres qui suivent, renvoie une nouvelle chaîne de caractères modifiée.
Elle n'affecte jamais directement la chaîne sur laquelle elle est appliquée.

```pycon
>>> text.strip()
'hello   world'
>>> text
' hello   world '
```

#### `capitalize` et `title`

`capitalize` est une méthode qui permet de passer en majuscule le premier caractère de la chaîne (si c'est une lettre) et en minuscules tous les autres.

```pycon
>>> 'coucou'.capitalize()
'Coucou'
>>> 'COUCOU'.capitalize()
'Coucou'
```

Semblable à `capitalize`, `title` effectue ce traitement sur tous les mots de la chaîne de caractères.

```pycon
>>> 'bonjour à tous'.capitalize()
'Bonjour à tous'
>>> 'bonjour à tous'.title()
'Bonjour À Tous'
```

#### `upper` et `lower`

Il s'agit ici de passer la chaîne entière en majuscules ou en minuscules.

```pycon
>>> 'CoUcOu'.upper()
'COUCOU'
>>> 'CoUcOu'.lower()
'coucou'
```

#### `index`

La méthode `index` permet de trouver un caractère dans la chaîne et d'en renvoyer la position.
Il s'agit donc du comportement réciproque de l'opérateur `[ ]`.

```pycon
>>> text = 'abcdef'
>>> text.index('d')
3
>>> text[3]
'd'
```

À noter que si le caractère est présent plusieurs fois dans la chaîne, c'est la première position trouvée qui est renvoyée.

```pycon
>>> 'abcabc'.index('b')
1
```

Et une erreur survient si le caractère n'est pas trouvé.

```pycon
>>> 'abcdef'.index('g')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found
```
