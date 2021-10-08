### Autres formats

Nous avons fait un tour des modules disponibles dans la bibliothèque standard de Python, mais ce ne sont pas les seuls formats existant.
Pour les autres, il faudra en revanche s'appuyer sur des modules tiers, nous verrons par la suite comment en installer.

Voici donc quelques autres formats que vous pourriez croiser et qui se prêtent à diverses utilisations.

##### toml

Le format _toml_ est un format simple adapté à des fichiers de configuration.
Il permet de représenter des couples clé/valeur typés regroupés en sections.

```toml
[window]
width = 800
height = 600

[game]
save = "game.dat"
```
Code: config.toml

* Page de la bibliothèque `toml` en Python : <https://github.com/uiri/toml>

##### yaml

_YAML_ est un format de données riches, semblable à _JSON_ mais plus axé sur la lisibilité.
Il permet de décrire de manière claire des données complexes.

```yaml
id: 001
name: Pythachu
type: foudre
attaques:
  - tonnerre
  - charge
base_pv: 50
```
Code: pythachu.yaml

* Page de la bibliothèque `PyYAML` en Python : <https://pyyaml.org/wiki/PyYAML>

##### msgpack

_msgpack_ est lui aussi un format de données assez semblable à JSON, à l'exception près que c'est un format binaire.
Il permet donc de manière compacte de représenter nombres, chaînes de caractères, listes et dictionnaires.

C'est un format interopérable qui possède des bibliothèques pour à peu près tous les langages.

* Page du projet `msgpack` : <https://msgpack.org/>

##### Protobuf

*Protobuf* est un format plus complexe destiné à établir des protocoles de communication entre programmes.
Les programmes doivent donc utiliser un protocole commun qui définit les types des données transmises dans un message.

Cela permet d'omettre les informations de typage dans la sérialisation, et d'avoir une assurance de la validité des données transmises.

* Page du projet `protobuf` : <https://developers.google.com/protocol-buffers>
