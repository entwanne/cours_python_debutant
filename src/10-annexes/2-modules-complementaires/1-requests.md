### Requests

_Requests_ est une bibliothèque Python de référence, qui permet de réaliser des requêtes HTTP (interroger des sites web).
Elle est connue pour sa facilité d'utilisation.

On l'installe via `pip install requests`.

Par exemple on peut l'utiliser pour interroger l'API de Zeste de Savoir, ici pour obtenir la liste des tags du site.

```python
>>> import requests
>>> resp = requests.get('https://zestedesavoir.com/api/tags')
>>> resp.status_code
200
>>> resp.text
'{"count":5071,"next":"https://zestedesavoir.com/api/tags/?page=2","previous":null,"results":[{"id":1,"title":"exercice"},{"id":2,"title":"java"},{"id":3,"title":"langages oo"},{"id":4,"title":"urgent"},{"id":5,"title":"bug"},{"id":6,"title":"suggestion"},{"id":7,"title":"transmis"},{"id":8,"title":"blog"},{"id":9,"title":"régression"},{"id":10,"title":"front"}]}'
>>> resp.json()
{'count': 5071,
 'next': 'https://zestedesavoir.com/api/tags/?page=2',
 'previous': None,
 'results': [{'id': 1, 'title': 'exercice'},
             {'id': 2, 'title': 'java'},
             {'id': 3, 'title': 'langages oo'},
             {'id': 4, 'title': 'urgent'},
             {'id': 5, 'title': 'bug'},
             {'id': 6, 'title': 'suggestion'},
             {'id': 7, 'title': 'transmis'},
             {'id': 8, 'title': 'blog'},
             {'id': 9, 'title': 'régression'},
             {'id': 10, 'title': 'front'}]}
```

Pour plus d'informations au sujet de _Requests_, je vous invite à consulter [sa documentation](https://docs.python-requests.org/en/latest/).
