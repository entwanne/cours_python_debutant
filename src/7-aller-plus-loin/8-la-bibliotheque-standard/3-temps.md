### Gestion du temps

Différents modules de la bibliothèque standard permettent de gérer les dates et le temps, des données qui ne sont pas toujours faciles à manipuler en raison de différentes conventions (durée des mois, années bissextiles, fuseaux horaires, heure d'été, secondes intercalaires, etc.).

Il existe plusieurs manières de représenter le temps en informatique,

* timestamp: nombre de secondes écoulées depuis le 1er janvier 1970 minuit UTC (_epoch_)
    * timestamp négatif pour les dates antérieures
    * stockage limité sur certains systèmes (32 bits / 64 bits) -> bug de l'an 2038
    * Nombre flottant en Python (millisecondes)
    * facile à manipuler (différence entre timestamps), pas de question de timezone
    * pratique pour des données d'horodatage
* struct_time: stockage des données liées à une date (année, mois, jour, heure, fuseau)
    * représente une date d'une manière plus exploitable
    * dépend du fuseau horaire et autres conventions sur les dates
    * permet des opérations sur les dates (avancer d'un jour, etc.)

* Module time: gestion basique du temps
    * time.sleep() pour attendre
    * Calcul du temps avec time.time(), time.process_time(), time.perf_counter()
        * + équivalents _ns()
    * date courante avec gmtime / localtime
    * conversions timestamp <-> strut_time (mktime / gmtime)

* Module datetime: gestion haut-niveau des dates
    * Construit par-dessus time
    * Ne gère qu'un ensemble restreint de dates (depuis l'an 1 jusqu'à l'an 9999)
    * Conversions vers/depuis des chaînes de caractères
        * chaînes de formatage
    * timedelta, opérations sur les dates
    * Notions de dates naïves (sans tz) et avisées (avec tz)
        * today / now / utcnow
    * Conversions avec les autres types de dates
    * tzinfo/timezone + timezones avec zoneinfo

* Module calendar ? (présentation brève)
