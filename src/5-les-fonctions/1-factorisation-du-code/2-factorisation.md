### Factoriser

La question va maintenant être de savoir comment identifier et réunir les portions logiques pour éviter les répétitions.

Mais souvent, on sera pas face à deux codes strictement identiques, ils seront simplement similaires.
L'idée sera alors de travailler à les rendre identiques afin de les factoriser en un unique fonction.
Pour cela, il faudra identifier les paramètres variables qui agissent sur le code et le font se différencier.
Une fois ces paramètres isolés et placés dans des variables avant la portion concernée, le code deviendra factorisable/

Prenons l'exemple suivant, qui affiche les tables de multiplication de `3` et de `5`.

```python
for i in range(1, 11):
    print(3, '×', i, '=', 3*i)

for i in range(1, 11):
    print(5, '×', i, '=', 5*i)
```

On a deux boucles très semblables qui ne sont pourtant pas identiques.
Un paramètre diffère entre les deux, le nombre par lequel on multiplie.
Si l'on isole ce nombre dans une variable, on constate que nos deux boucles deviennent identiques.

```python
n = 3
for i in range(1, 11):
    print(n, '×', i, '=', n*i)

n = 5
for i in range(1, 11):
    print(n, '×', i, '=', n*i)
```

C'est donc ça le travail de factorisation : œuvrer pour que des codes similaires mais différents puisse utiliser une fonction commune.
