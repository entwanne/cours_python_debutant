### Appel de fonction

On appelle notre fonction comme toute autre fonction (sans arguments pour le moment), en faisant suivre son nom d'une paire de parenthèses.

```pycon
>>> toto()
Hello
World!
```

Le code contenu dans le bloc de notre fonction est alors exécuté, c'est pourquoi nous voyons s'afficher les messages passés à `print`.

Tout le code de la fonction sera à nouveau exécuté à chaque nouvel appel, chaque appel étant indépendant des autres.

```pycon
>>> toto()
Hello
World!
>>> toto()
Hello
World!
```

Ce sont les parenthèses qui demandent à Python d'appeler la fonction et d'en exécuter le contenu.
Sans elles, l'interpréteur ne ferait qu'évaluer l'expression `toto` pour nous indiquer qu'elle correspond à une fonction.

```pycon
>>> toto
<function toto at 0x7fea64fcf1f0>
```

[[i]]
| Ne vous souciez pas de cette valeur `0x7fea64fcf1f0` qui apparaît derrière et qui différera sûrement chez vous, il ne s'agit que de l'emplacement en mémoire de la fonction.
