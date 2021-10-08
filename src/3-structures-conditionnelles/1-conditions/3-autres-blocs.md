### Et sinon ?

Nous avons vu quoi faire quand une condition était vraie, mais ce n'est pas le seul cas qui nous intéresse.
Une condtion est en effet soit vraie soit fausse, et un traitement particulier doit pouvoir être apporté à ce deuxième cas de figure.

Python fournit pour cela le bloc `else` (« sinon ») qui se place directement après un bloc `if`.
Aucune expression n'est nécessaire derrière le mot-clé `else` (pas de condition à préciser), le signe `:` reste néanmoins obligatoire pour introduire le bloc.

Le contenu du bloc `else` sera exécuté si et seulement si la condition du `if` est fausse.

```python
secret = 42
nbr = int(input('Devinez le nombre secret : '))

if nbr == secret:
    print('Bravo, vous avez trouvez le nombre !')
else:
    print('Perdu, le nombre était', secret)

print('Relancez le programme pour une nouvelle partie')
```

Le programme précédent se lit comme suit :

> Le joueur entre un nombre.
>
> * Si le nombre est égal à 42, afficher « Bravo […] ».
> * Sinon, afficher « Perdu […] ».
>
> Dans tous les cas, afficher « Relancez le programme […] ».

Avec nos blocs conditionnels nous avons chaque fois deux issues : soit la condition du `if` est vraie et nous entrons dans son bloc, soit elle est fausse et c'est le bloc `else` qui est exécuté.
Il est en fait possible d'avoir plus d'options que cela en combinant plusieurs conditions, c'est-à-dire en testant une seconde condition quand la première est fausse.
Plutôt que d'avoir un simple « si / sinon » nous pourrions avoir « si / sinon si / sinon ».

Ce « sinon si » prend la forme du mot-clé `elif` (contraction de « else if » en anglais), qui s'utilise donc suivi d'une nouvelle expression conditionnelle.

```python
secret = 42
nbr = int(input('Devinez le nombre secret : '))

if nbr == secret:
    print('Bravo, vous avez trouvez le nombre !')
elif nbr == secret - 1:
    print('Un peu plus...')
else:
    print('Perdu, le nombre était', secret)

print('Relancez le programme pour une nouvelle partie')
```

Ainsi, dans le cas où `nbr` vaut `secret` nous afficherons « Bravo », s'il vaut `secret - 1` nous obtiendrons « Un peu plus » et nous aurons « Perdu » dans tous les autres cas.

Une structure conditionnelle peut contenir autant de blocs `elif` que nécessaire (contrairement au `else` qui ne peut être présent qu'une fois), pour tester différentes conditions à la suite.

```python
secret = 42
nbr = int(input('Devinez le nombre secret : '))

if nbr == secret:
    print('Bravo, vous avez trouvez le nombre !')
elif nbr == secret - 1:
    print('Un peu plus...')
elif nbr == secret + 1:
    print('Un peu moins...')
else:
    print('Perdu, le nombre était', secret)

print('Relancez le programme pour une nouvelle partie')
```

Il faut bien noter qu'un bloc `elif` dépend du `if` et des autres `elif` qui le précèdent, son contenu ne sera donc exécuté que si toutes les conditions précédentes se sont révélées fausses.

`if` étant le mot-clé qui introduit une structure conditionnelle, il doit être placé avant les `elif` / `else`.
De même, `else` terminant cette structure, il se place à la suite de tous les `elif`.

`elif` et `else` restent bien sûr optionnels, un bloc conditionnel peut ne contenir qu'un simple `if`.
On peut aussi imaginer un `if` suivi de `elif` mais sans `else`.

```python
secret = 'p4ssw0rd'
password = input('Entrez le mot de passe : ')

if password == '':
    print('Veuillez saisir un mot de passe valide')
elif password == secret:
    print('Authentification réussie')
```
