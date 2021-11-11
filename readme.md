Bienvenue dans la base de données des oeuvres du MoMA de New York ! - Par Etienne Lemonnier et Victor Royer
Vous y trouverez les informations importantes sur les oeuvres, les artistes...

Dans le dossier "Rapport", veuillez trouver le rapport du projet.
Dans le dossier "Script Python", veuillez trouver l'algorithme ayant permis de créer les scripts SQL.
Dans le dossier "Scripts SQL" se trouvent les scripts de création, population et exploitation des tables.

--------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------- Python --------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------------------------

Pour lancer scripts Python, utiliser un IDE comme PyCharm, et compiler le fichier "csvtosql.py", en faisant attention que
les fichiers "Artworks.csv" et "Artists.csv" soient bien présents dans le répertoire courant.
Ne pas utiliser le fichier "Artworks.csv" originel trouvé sur GitHub, celui-ci n'est pas rigoureusement homogène.
Pour information, le fichier "Artworks.csv" présent dans le répertoire "Script Python" est passé par une phase de pré-processing, grâce
aux les commandes suivantes (à saisir dans le mode normal de VIM) :
:%s/^M\n//g
:%s/(\n\n/(/g
:%s/^M //g
:%s/>\n/>/g
:%s/''//g
:%s/'//g
:%s/|//g

L'algorithme lancé va créer trois fichiers .txt, les ignorer, ce ne sont que des fichiers temporaires ayant permis de créer les fichiers SQL finaux.
Les trois fichiers .sql créés apparaîtront dans le répertoire.
Attention : le fichier fillCreates.sql devra passer par une phase de post-processing sous VIM pour être opérationnel (à saisir dans le mode normal de VIM) :
:%s/''/'/g 
:153787d 
:%s/)');/);/g

Les trois fichiers seront alors opérationnels !

--------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------- SQL --------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------------------------

Pour remplir la base de données sous Debian / Postgresql  (à saisir dans l'ordre) :
cp /mnt/[votre chemin]/LEMONNIER_ROYER_projet_bdd/Scripts\ SQL/* .
cp /mnt/[votre chemin]/LEMONNIER_ROYER_projet_bdd/Scripts\ SQL/Requêtes/* .
sudo service postgresql restart
sudo -u postgres psql
\i createTables.sql (dès l'accès à Postgresql)
\i fillArtist.sql
\i fillArtwork.sql (au moins 3 minutes d'insertion à prévoir)
\i fillCreates.sql (erreurs attendues car certaines données sont manquantes dans les fichiers d'entrée : les ignorer)

Puis vous pouvez manipuler les tables comme vous le souhaitez avec les commandes SQL.
Egalement, vous pouvez saisir \i q1 ... q5 pour des recherches spécifiques (voir nom des fichiers dans le dossier "Requêtes").

Note : Les tables "ArtisticCurrent" et "Museum" sont vides à cause de données manquantes dans les fichiers d'entrée.


Bon parcours de données ! 