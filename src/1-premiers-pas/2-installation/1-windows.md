### Installation sous Windows

#### Depuis le Microsft Store

Le plus simple si vous utilisez Windows 10 ou plus est de vous orienter vers le _Microsoft Store_, le gestionnaire de paquets officiel sous Windows.

Vous pourrez y trouver la dernière version du paquet « Python », publié par la _Python Software Foundation_.
Ce paquet se chargera d'installer les programmes Python et IDLE (je reviendrai sur lui par la suite) qui seront tous deux présents dans le menu « Démarrer ».

[[a]]
| Le paquet Python publié par la _PSF_ est entièrement gratuit.
| Si vous êtes invité à payer c'est que vous avez sélectionné un paquet frauduleux ne provenant pas de la PSF.

[[i]]
| Le _Microsoft Store_ impose certaines restrictions sur les paquets qui y sont publiés.
| Ainsi, Python installé de cette manière ne vous permettra pas de réaliser des programmes utilisant les emplacements partagés ou le registre.
|
| Ces fonctionnalités ne sont pas abordées dans ce tutoriel et donc ne devraient pas poser problème, mais reportez-vous à l'installateur officiel si vous avez un tel besoin.

#### Avec l'installateur officiel

Pour l'installation classique sous Windows, il vous suffit de vous rendre sur le site officiel de Python dans la section « Downloads > Windows  » : <https://www.python.org/downloads/windows/>.

![Page des téléchargements.](img/download_windows.png)

Là, vous pouvez sélectionner le lien « Download Windows installer (64-bit) » de la version stable (_Stable Release_) la plus récente[^versions].
Téléchargez le fichier `.exe` pointé et exécutez-le.

[^versions]: Ces informations sont données pour le cas général. Dans d'autres cas précis (version ancienne de Windows, système 32 bits), référez-vous aux recommandations données par la page de téléchargement.

[[a]]
| Téléchargez toujours l'inistallateur depuis le site officiel de Python plutôt qu'une autre source, afin d'éviter tout programme frauduleux.

![Installation de Python](img/win_installer.png)

Cochez alors les cases « Install launcher for all users » (installer pour tous les utilisateurs) et « Add Python to PATH » (ajouter Python aux chemins système) pour simplifier les utilisations futures.
Cliquez ensuite sur « Install now » (installer maintenant) afin de procéder à l'installation de Python sur votre système.

#### Avec un environnement de développement

Pour des utilisations spécifiques (telles que la programmation scientifique), il peut être utile de préférer l'installation d'un environnement de développement dédié.
Je vous redirige pour cela vers le tutoriel [Installer un environnement de développement python avec conda](https://zestedesavoir.com/tutoriels/1448/installer-un-environnement-de-developpement-python-avec-conda/) de @Gabbro.
