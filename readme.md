Welcome to the MoMA New York Artworks Database! - By Etienne Lemonnier and Victor Royer
You will find important information on the artworks, the artists ...

In the "Report" folder, please find the project report.
In the "Python Script" folder, please find the algorithms that created the SQL scripts.
In the "SQL Scripts" folder are the scripts for creating, populating and operating the tables.

------------ Python:

To run Python scripts, use an IDE like PyCharm, and compile the "csvtosql.py" file, being careful that the "Artworks.csv" and "Artists.csv" files are indeed present in the current directory. Do not use the original "Artworks.csv" file found on GitHub, it is not strictly homogeneous. For information, the "Artworks.csv" file found in the "Script Python" directory has gone through a pre-processing phase, thanks to to the following commands (to be entered in normal VIM mode):
:%s/^M\n//g
:%s/(\n\n/(/g
:%s/^M //g
:%s/>\n/>/g
:%s/''//g
:%s/'//g
:%s/|//g

The algorithm launched will create three .txt files, ignore them, they are only temporary files that were used to create the final SQL files.
The three .sql files created will appear in the directory.
Warning: the fillCreates.sql file must go through a post-processing phase under VIM to be operational (to be entered in normal VIM mode):
:%s/''/'/g 
:153787d 
:%s/)');/);/g

The three files will then be operational!

-------------- SQL:

To fill the database under Debian / Postgresql (to be entered in order):
cp /mnt/[path]/LEMONNIER_ROYER_projet_bdd/Scripts\ SQL/* .
cp /mnt/[path]/LEMONNIER_ROYER_projet_bdd/Scripts\ SQL/Requêtes/* .
sudo service postgresql restart
sudo -u postgres psql
\i createTables.sql (as soon as you access Postgresql)
\i fillArtist.sql
\i fillArtwork.sql (at least 3 minutes of insertion to be expected)
\i fillCreates.sql (errors expected because some data is missing in the input files: ignore them)

Then you can manipulate the tables as you wish with SQL commands.
Also, you can enter \i q1 ... q5 for specific searches (see file names in the "Requêtes" folder).

Note: The "ArtisticCurrent" and "Museum" tables are empty due to missing data in the input files.


Have a good data journey!
