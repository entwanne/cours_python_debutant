### Problématique

On sait demander à Python de résoudre des problèmes simples sur des chaînes de caractères comme :

* récupère-moi les N premiers caractères de la chaîne (`my_string[:N]`) ;
* teste si telle chaîne commence par tel préfixe (`my_string.startswith(prefix)`) ;
* découpe-moi cette chaine en morceaux selon les espaces (`my_string.split(' ')`) ;
* etc.

Mais comment pourrions-nous procéder pour des problèmes plus complexes comme « est-ce que ma chaîne de caractères représente un nombre » ?[^flottants]

[^flottants]: Nous ne nous intéresserons ici qu'aux notations simples pour des nombres décimaux comme `42`, `+12.5` ou encore `-18000`, exit les nombres complexes ou les notations sans partie entière telles que `.3` ou à base d'exposants comme `1e10`.

Une solution évidente serait de tenter une conversion `float(my_string)` et voir si elle réussit ou elle échoue.[^faux_positifs]

[^faux_positifs]: Ce qui ne remplit pas à 100% la demande puisque reconnaît les formes `.3`, `1e10` et même `inf` qui ne nous intéressent pas ici.

Mais intéressons-nous ici à une autre solution qui consisterait à analyser notre chaîne caractère par caractère afin d'identifier si oui ou non elle correspond à un nombre.
La chaîne pourrait commencer par un `+` ou un `-`, suivraient une série de chiffres potentiellement suivis d'un `.` et d'une nouvelle série de chiffres.

```python
def is_number(my_string):
    # On traite notre chaîne comme un itérateur pour simplifier les traitements
    it = iter(my_string)
    first_char = next(it, '')

    # On ignore le préfixe + ou -
    if first_char in ('+', '-'):
        first_char = next(it, '')

    # On vérifie que la chaîne commence par un chiffre
    if not first_char.isdigit():
        return False

    for char in it:
        if char == '.':
            # Si on tombe sur un point, on sort de la boucle pour traiter la partie décimale
            # On vérifie cependant que la partie décimale commence par un chiffre
            next_char = next(it, '')
            if not next_char.isdigit():
                return False
            break
        elif not char.isdigit():
            # Si le caractère n'est pas un chiffre, la chaîne ne peut pas représenter un nombre
            return False

    # On recommence pour la partie décimale (optionnelle)
    for char in it:
        if not char.isdigit():
            return False

    # On est arrivé jusqu'au bout, la chaîne représente un nombre
    return True
```

```pycon
>>> is_number('123')
True
>>> is_number('123.45')
True
>>> is_number('-123.45')
True
>>> is_number('+12000')
True
>>> is_number('abc')
False
>>> is_number('12c4')
False
>>> is_number('.5')
False
>>> is_number('10.')
False
>>> is_number('.')
False
>>> is_number('')
False
```

Cette solution est un peu fastidieuse mais nous verrons par la suite qu'il y a plus simple grâce aux _regex_.
