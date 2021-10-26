### Instructions et expressions

Dans le cours j'ai plusieurs fois utilisé le terme d'« expression ».
Une expression est un élément de syntaxe Python qui possède une valeur quand il est évalué.  
`'foo'`, `3 * 5 + 2` ou encore `max(range(10))` sont des expressions.

Si je dis ça maintenant, c'est parce qu'il n'y a pas uniquement des expressions en Python.
Plus généralement, on trouve des instructions.
L'instruction c'est la définition au sens large d'un élément de syntaxe, pour résumer on pourrait dire que c'est une ligne de code.

Ainsi, les expressions sont des instructions, mais toutes les instructions ne sont pas des expressions.
Une expression c'est ce qu'on peut utiliser partout où une valeur est attendue : en argument à une fonction, dans une assignation de variable, dans une condition, etc.

```pycon
>>> len('foo')
3
>>> x = 3 * 5 + 2
>>> if max(range(10)):
...     print('ok')
... 
ok
```

Dit autrement, une expression c'est ce que l'on peut mettre entre parenthèses.

```pycon
>>> ('foo')
'foo'
>>> (3 * 5 + 2)
17
>>> (max(range(10)))
9
```

Et par exemple une assignation de variable n'est pas une expression, elle ne possède aucune valeur, pas même `None`.
Si l'on cherche à placer une assignation entre parenthèses on obtient une erreur de syntaxe.

```pycon
>>> (foo = 'bar')
  File "<stdin>", line 1
    (foo = 'bar')
         ^
SyntaxError: invalid syntax
```

De la même manière, les conditions ne sont pas des expressions, il s'agit de blocs de code.

```pycon
>>> (if True: print('ok'))
  File "<stdin>", line 1
    (if True: print('ok'))
     ^
SyntaxError: invalid syntax
```

Pourtant il serait pratique de pouvoir utiliser directement une condition dans un argument de fonction ou une assignation…
