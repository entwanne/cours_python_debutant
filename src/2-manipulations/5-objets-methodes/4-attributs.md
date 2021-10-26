### Attributs

Les objets sont caractérisés par leur type et les méthodes qui lui sont applicables, mais ce n'est pas tout.
Chaque objet a une existence propre, qui le différencie des autres objets du même type, et des données annexes peuvent lui être associées.  
Ces données annexes sont autant de valeurs qui peuvent décrire l'état interne des objets. On les appelle des attributs.

Ils sont peu utilisés sur les objets que nous manipulons jusqu'ici (nombres et chaînes de caractères) car ces objets correspondent à de la donnée brute et n'ont pas besoin de valeurs annexes.  
Leur utilité peut alors ne pas sembler évidente pour le moment, mais elle le deviendra quand on manipulera des objets plus complexes, composés de différentes données.

Il n'empêche que nos objets de base possèdent tout de même quelques attributs.
Par exemple, chaque objet Python est pourvu d'un attribut `__class__` (faites bien attention aux deux _underscores_ de chaque côté) qui permet d'accéder à son type.

```pycon
>>> 'hello'.__class__
<class 'str'>
>>> 1.4.__class__
<class 'float'>
```

Vous découvrez ainsi la syntaxe pour accéder à un attribut d'un objet : on fait suivre l'objet d'un point puis du nom de l'attribut.
C'est donc similaire aux méthodes, qui fonctionnent sur le même principe.

On notera cependant une petite différence pour les nombres entiers : comme le point y a déjà une signification (précéder une potentielle partie décimale) il ne peut pas être utilisé tel quel pour accéder aux attributs.  
On ne peut ainsi pas écrire `42.__class__` qui ne serait pas compris par Python, il faut alors entourer le nombre de parenthèses pour lever toute ambigüité.

```pycon
>>> 42.__class__
  File "<stdin>", line 1
    42.__class__
       ^
SyntaxError: invalid syntax
>>> (42).__class__
<class 'int'>
```

Cette exception ne s'applique bien sûr qu'aux nombres littéraux, et pas aux variables qui référencent des nombres qui n'ont aucun problème d'ambigüité à ce niveau.

```pycon
>>> x = 42
>>> x.__class__
<class 'int'>
```

Les nombres entiers possèdent aussi deux attributs `numerator` (numérateur) et `denominator` (dénominateur) qui leur permettent d'être vus comme des fractions (et donc d'être utilisés dans un contexte où une fraction serait attendue, nous découvrirons ça plus tard).
Comme il s'agit de nombres entiers, le dénominateur sera toujours de 1.

```pycon
>>> x.numerator
42
>>> x.denominator
1
```
