### Limitations

De par leur construction (automates finis) les expressions rationnelles sont normalement assez limitées en raison de l'absence de mémorisation : elles ne permettent de reconnaître que des langages rationnels.  
Il s'agit du type de langage le plus simple dans la [hiérarchie de Chomsky](https://fr.wikipedia.org/wiki/Hi%C3%A9rarchie_de_Chomsky), on ne peut pas les utiliser pour décrire des structures récursives par exemple.

Mais le moteur de _regex_ de Python permet d'aller au-delà de certaines limitations (au prix de l'efficacité et de la lisibilité) en fournissant des fonctionnalités supplémentaires :

* Le _look-ahead_ qui permet de regarder ce qui suit une expression.

    ```pycon
    >>> # trouve toutes les lettres suivies d'un "b"
    >>> re.findall(r'\w(?=b)', 'ab cd eb')
    ['a', 'e']
    >>> # ou celles qui ne sont pas suivies d'une espace
    >>> re.findall(r'\w(?! )', 'ab cd eb')
    ['a', 'c', 'e', 'b']
    ```

* Le _look-behind_ pour regarder ce qui précède.

    ```pycon
    >>> # trouve toutes les lettres précédées d'un "a"
    >>> re.findall(r'(?<=a)\w', 'ab de ac')
    ['b', 'c']
    >>> # ou celles qui ne sont pas précédées d'une espace
    >>> re.findall(r'(?<! )\w', 'ab de ac')
    ['a', 'b', 'e', 'c']
    ```

* Les _back-references_ pour référencer une expression déjà capturée.

    ```pycon
    >>> # trouve les motifs doublés
    >>> re.findall(r'(\w+)(\1)', 'toto tutu tati')
    [('to', 'to'), ('tu', 'tu')]
    >>> reconnaît N occurrences de "a" suivies d'un "b" et de N nouvelles occurences de "a"
    >>> re.fullmatch(r'(a+)b(\1)', 'aba')
    <re.Match object; span=(0, 3), match='aba'>
    >>> re.fullmatch(r'(a+)b(\1)', 'aaabaaa')
    <re.Match object; span=(0, 7), match='aaabaaa'>
    >>> re.fullmatch(r'(a+)b(\1)', 'abaaa')
    ```

Cependant, même avec ces fonctionnalités supplémentaires certaines choses restent impossibles.
Par exemple on ne peut pas écrire de motif pour reconnaître N occurreces de « a » suivies de N occurrences de « b ».  
De même qu'une expression arithmétique (`3 * (1 + 2 * 5)`), par sa nature récursive, ne peut pas être reconnue par une _regex_, même étendue.

On notera enfin que les fonctionnalités étendues présentées ici ne sont pas standards et ne seront pas reconnues par les moteurs de _regex_ « purs »[^re2], je vous recommande donc de les éviter autant que possible (ainsi que pour des questions de lisibilité et de performances) et de préférer des algorithmes plus classiques pour résoudre vos problèmes complexes.

[^re2]: Par exemple la bibliothèque [`re2`](https://pypi.org/project/google-re2/) qui propose une implémentation optimale d'un moteur d'expressions rationnelles (à l'aide d'automates finis justement) ne comprend pas ces extensions (et c'est ce qui lui permet d'être optimale).
