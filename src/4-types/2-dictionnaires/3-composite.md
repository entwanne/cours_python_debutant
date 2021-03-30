### Données composites

Une autre cas d'utilisation des dictionnaires est celui d'agréger dans un même objet plusieurs valeurs liées les unes aux autres, plutôt que dans des variables différentes.
Pensez par exemple à la représentation des monstres dans notre TP : on a un nom d'un côté, un nombre de PV de l'autre et aussi une liste d'attaques.

À la place, on pourrait utiliser un dictionnaire par monstre, en y faisant figurer toutes ses données.

```python
{
    'nom': 'Pythachu',
    'PV': 50,
    'attaques': ['tonnerre', 'charge'],
}
```

Car en effet, tous les types de données sont acceptés en tant que valeurs, et toutes les valeurs n'ont pas besoin d'être du même type.

Mais on peut faire encore mieux.
En usant de listes et de dictionnaires, on construit donc facilement des structures arborescentes pour représenter toutes nos données.

```python
monstres = {
    'Pythachu': {
        'type': 'foudre',
        'description': 'Petit rat surchargé.',
        'attaques': ['tonnerre', 'charge'],
    },
    'Pythard': {
        'type': 'aquatique',
        'description': "Tétard qui a cru qu'il était tôt.",
        'attaques': ['jet-de-flotte', 'charge'],
    },
    'Ponytha': {
        'type': 'flamme',
        'description': 'Cheval enflammé.',
        'attaques': ['brûlure', 'charge'],
    },
}

attaques = {
    'charge': {'degats': 20},
    'tonnerre': {'degats': 50},
    'jet-de-flotte': {'degats': 40},
    'brûlure': {'degats': 40},
}

joueurs = [
    {
        'monstre': 'Pythachu',
        'PV': 100,
    },
    {
        'monstre': 'Ponytha',
        'PV': 120,
    },
]
```

Ainsi, on représente dans des variables différentes la structure de nos données.
Pour avoir d'un côté la définition des monstres et des attaques, et de l'autre les monstres en jeu.

```python
>>> print('Joueur 1 :', joueurs[0]['monstre'])
Joueur 1 : Pythachu
>>> print('Attaques :', monstres[joueurs[0]['monstre']]['attaques'])
Attaques : ['tonnerre', 'charge']
>>> print('Dégâts de tonnerre :', attaques['tonnerre']['degats'])
Dégâts de tonnerre : 50
```
