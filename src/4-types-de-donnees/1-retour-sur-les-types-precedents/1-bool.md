### booléens

* Opérateurs `and`, `or` et `not`
* `and` et `or` ne renvoient pas nécessairement un booléen

On notera enfin en termes de conversions que les booléens eux-mêmes sont aussi implicitement convertis en nombres lorsqu'utilisés comme tels. On aura ainsi `True` converti en `1` et `False` en `0`.

```python
>>> False + 2 * True
2
```
