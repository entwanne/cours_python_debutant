### Chaînes de bytes

Pour la suite nous allons quitter les formats textuels et nous intéresser aux formats dits « binaires », qui ne sont donc pas lisibles comme du texte.
Et pour cela, nous avons besoin de découvrir un autre type de Python, le type `bytes`.

Ce type représente une chaîne d'octets, les octets étant l'unité de stockage des informations sur un ordinateur, soit des nombres de 8 bites (de 0 à 255 inclus).
Un objet _bytes_ peut donc être vue comme un tableau de nombres, chaque nombre étant la valeur d'un octet.

On peut d'ailleurs définir un objet _bytes_ à partir d'un tel tableau.

```python
>>> bytes([1, 2, 3])
b'\x01\x02\x03'
```

La représentation de notre objet peut sembler perturbante, mais il s'agit bien de notre tableau.

```python
>>> data = bytes([1, 2, 3])
>>> data[0]
1
```

Comme les chaînes de caractères, les chaînes d'octets sont immutables.

```python
>>> data[0] = 10
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'bytes' object does not support item assignment
```

Les deux types sont d'ailleurs assez semblables, ils étaient même confondus en Python 2, les deux identifient des chaînes.  
Les caractères ne sont qu'une abstraction pour interpréter des octets comme du texte, et une chaîne de caractères est ainsi une chaîne d'octets munie d'une règle définissant comment interpréter les octets en caractères.
Cette règle est appelée un encodage, mais j'y reviendrai ensuite.

Cette similitude entre les deux s'appuie entre autres sur la table ASCII qui établit une correspondance entre certains caractères (notamment les caractères alphanumériques latins « de base » -- sans accents -- et les chiffres) et des octets, elle sert encore aujourd'hui de base à de nombreux encodages.

* Insérer la table ASCII

C'est pourquoi, lors de l'affichage, Python essaie généralement de représenter un objet _bytes_ comme du texte, en s'appuyant sur la table ASCII.

```python
>>> bytes([65, 66, 67])
b'ABC'
```

65, 66 et 67 sont les valeurs ASCII des caractères `A`, `B` et `C`.

On le voit ainsi, une chaîne d'octets peut simplement se définir comme une chaîne de caractères préfixée d'un `b`.

```python
>>> b'foobar'
b'foobar'
```

Cela ne change rien au fait que la chaîne ainsi créée est toujours considérée comme un tableau de nombres.

```python
>>> b'foobar'[0]
102
```

Bien sûr, seulement les caractères de la table ASCII sont utilisables pour construire une chaîne d'octet, impossible d'y utiliser des caractères spéciaux qui n'ont aucune correspondance.

```python
>>> b'été'
  File "<stdin>", line 1
SyntaxError: bytes can only contain ASCII literal characters.
```

Et comme on l'a vu plus haut, on peut utiliser la notation `\xNN` pour insérer des octets particuliers, `NN` étant la valeur de l'octet en hexadécimal.

```python
>>> data = b'\x01\x2A\x61'
>>> data[1]
42
>>> hex(data[1])
'0x2a'
>>> hex(data[2])
'0x61'
```

Les octets pouvant être interprétés comme des caractères sont affichés comme tel par Python pour faciliter la lisibilité.

```python
>>> data
b'\x01*a'
```

Qui dit similitude avec les chaînes de caractères dit aussi opérations similaires.
Ainsi il est possible de concaténer des chaînes d'octets et d'y appliquer pratiquement les mêmes méthodes.

```python
>>> b'abc' + b'def'
b'abcdef'
>>> b'foo'.replace(b'o', b'e')
b'fee'
>>> b'a;b;c'.split(b';')
[b'a', b'b', b'c']
```

Mais les deux types ne sont pas compatibles entre-eux.

```python
>>> b'abc' + 'def'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't concat str to bytes
```

#### Encodages

Il est en revanche possible de convertir l'un vers l'autre.
Les chaînes de caractères possèdent une méthode `encode` renvoyant une chaîne d'octets.

```python
>>> 'foobar'.encode()
b'foobar'
```

À l'inverse, les chaînes d'octets ont une méthode `decode` pour les convertir en chaînes de caractères.

```python
>>> b'foobar'.decode()
'foobar'
```

Je n'utilise ici que des caractères de la table ASCII, mais cela fonctionne aussi avec des caractères « spéciaux ».

```python
>>> 'été'.encode()
b'\xc3\xa9t\xc3\xa9'
>>> b'\xc3\xa9t\xc3\xa9'.decode()
'été'
```

Comment cela fonctionne ? Avec la notion d'encodage dont je parlais plus haut.
Un encodage c'est une table qui fait la correspondance entre des caractères et des octets, associant un ou plusieurs octets à un caractère.
La table ASCII est un encodage (mais avec un ensemble limité de caractères).

En Python, on utilise plus couramment des encodages unicode -- qui peuvent représenter tous les caractères existant -- et plus particulièrement UTF-8.
C'est cet encodage UTF-8 qui a été utilisé par défaut lors des opérations précédentes.
En effet, les méthodes `encode` et `decode` peuvent prendre un argument optionnel pour spécifier l'encodage vers lequel encode / depuis lequel décoder.

```python
>>> 'été'.encode('utf-8')
b'\xc3\xa9t\xc3\xa9'
```

On notera que la taille varie entre chaînes de caractères et chaînes d'octets, l'appel à `len` nous renverra 3 dans le premier cas et 5 dans le second. C'est bien parce que l'on compte soit les caractères soit les octets.

```python
>>> len('été')
3
>>> len('été'.encode('utf-8'))
5
```

D'autres encodages existent et ils ont chacun leurs particularités.
Par exemple l'UTF-32 est un encodage unicode qui représente chaque caractère sur 4 octets.

```python
>>> 'été'.encode('utf-32')
b'\xff\xfe\x00\x00\xe9\x00\x00\x00t\x00\x00\x00\xe9\x00\x00\x00'
>>> 'abc'.encode('utf-32')
b'\xff\xfe\x00\x00a\x00\x00\x00b\x00\x00\x00c\x00\x00\x00'
```

Ou encore l'encodage latin-1 (ou iso-8859-1) un langage encore parfois utilisé sur certains systèmes en Europe (Windows notamment).

```python
>>> 'été'.encode('latin-1')
b'\xe9t\xe9'
```

Mais latin-1 n'est pas un encodage unicode et ne pourra donc pas représenter tous les caractères.

```python
>>> '♫'.encode('utf-8')
b'\xe2\x99\xab'
>>> '♫'.encode('latin-1')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeEncodeError: 'latin-1' codec can't encode character '\u266b' in position 0: ordinal not in range(256)
```

Une chaîne ayant été encodée avec un certain encodage doit toujours être décodé avec ce même encodage, cela donnerait sinon lieu à des erreurs ou des incohérences.

```python
>>> 'été'.encode('utf-8').decode('latin-1')
'Ã©tÃ©'
>>> 'été'.encode('latin-1').decode('utf-8')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9 in position 0: invalid continuation byte
```

Les encodages interviennent quand vous traitez des données extérieures au programme, et notamment des fichiers.
Ainsi, la fonction `open` dispose d'un paramètre `encoding` pour préciser l'encodage du fichier à ouvrir.

```python
with open('output.txt', 'w', encoding='latin-1') as f:
    f.write('été')
```

Gardez donc en tête qu'un fichier texte (ou même n'importe quel texte) est toujours lié à un encodage, et que celui-ci n'est pas toujours UTF-8.
Souvent l'encodage sera renseigné comme métadonnée avec le fichier, comme c'est le cas en HTTP avec l'en-tête `Content-Type` qui précise l'encodage des données.

#### Mode binaire

Mais tous les fichiers ne représentent pas du texte, même sous des encodages particuliers, les images par exemple.
Ainsi, on voudrait parfois pouvoir traiter un fichier comme des données brutes, comme des octets.

Cela est possible à l'aide du mode binaire, il s'agit d'un caractère `b` ajouté au mode d'ouverture du fichier.
Ce mode aura pour effet que toutes les opérations sur le fichier traiteront des chaînes d'octets et non des chaînes de caractères.

```python
>>> with open('output.txt', 'rb') as f:
...     f.read()
... 
b'\xe9t\xe9'
```

Il en est de même en écriture, où les méthodes attendront des chaînes d'octets.

```python
>>> with open('output.txt', 'wb') as f:
...     f.write(b'\x01\x02\x03')
... 
3
```

Ce mode nous sera utile pour maintenant aborder un autre format de sérialisation des données, un format binaire.
