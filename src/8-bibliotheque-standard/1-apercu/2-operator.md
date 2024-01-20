### Opérateurs

Les opérateurs font en quelque sorte partie des _built-ins_ même si on y pense moins.
Après tout, il s'agit aussi de fonctions natives de Python.

Mais les opérateurs sont des symboles et on ne peut pas les manipuler en tant que tels.
En revanche, le module `operator` fournit pour chaque opérateur de Python un équivalent sous forme de fonction.  
On y trouve ainsi des fonctions `add`, `sub`, `pow` ou encore `eq`.

```pycon
>>> import operator
>>> operator.add(3, 5)
8
>>> operator.sub(10, 1)
9
>>> operator.pow(2, 3)
8
>>> operator.eq('a', 'a')
True
>>> operator.eq('a', 'b')
False
```

Quelques subtilités à noter :

* Il y a deux fonctions de division (`truediv` et `floordiv`) pour les deux opérateurs correspondant (respectivement `/` et `//`).

    ```pycon
    >>> operator.truediv(10, 4)
    2.5
    >>> operator.floordiv(10, 4)
    2
    ```

* `operator.concat` (concaténation) est équivalent à `operator.add`, ces deux opérations se représentant par l'opérateur `+`, mais s'attend à ce que ses arguments soient des séquences.

    ```pycon
    >>> operator.concat('foo', 'bar')
    'foobar'
    >>> operator.add('foo', 'bar')
    'foobar'
    >>> operator.concat(3, 5)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'int' object can't be concatenated
    ```

* Les opérateurs `&` et `|` deviennent `and_` et `or_`, suffixés d'un `_` pour ne pas générer de conflit avec les mots-clés `and` et `or`. De même que `not` devient `not_`.

    ```pycon
    >>> operator.and_(3, 1)
    1
    >>> operator.or_(3, 1)
    3
    >>> operator.not_(False)
    True
    ```

* Pour chaque fonction `xxx` d'un opérateur arithmétique on trouve une fonction `ixxx` pour l'opérateur en-place (par-exemple `iadd` pour `+=`).

    ```pycon
    >>> values = []
    >>> operator.iadd(values, [42])
    [42]
    >>> values
    [42]
    ```

* Les opérateurs `foo[key]`, `foo[key] = value` et `del foo[key]` sont appelés `getitem`, `setitem` et `delitem`.
  `getitem` renvoie la valeur demandée, `setitem` et `delitem` renvoient `None`.

    ```pycon
    >>> operator.setitem(values, 0, 21)
    >>> operator.getitem(values, 0)
    21
    >>> operator.delitem(values, 0)
    >>> values
    []
    ```

* On trouve une fonction spéciale `itemgetter` qui permet de générer un opérateur renvoyant la valeur associée à une clé dans un conteneur.

    ```pycon
    >>> get_3rd = operator.itemgetter(3)
    >>> get_3rd('abcdef')
    'd'
    >>> get_3rd([3, 4, 5, 6])
    6
    >>> get_3rd(range(10))
    3
    >>> get_foo = operator.itemgetter('foo')
    >>> get_foo({'foo': -12})
    -12
    ```
