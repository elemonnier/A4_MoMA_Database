import csv
import re

# Création d'un fichier temporaire permettant de récupérer les données du fichier Artworks.csv, grâce aux méthodes présentes dans la librairie csv.
with open('Artworks.csv', 'r+', encoding='utf-8') as artworks:
    with open('tempArtwork.txt', 'a+', encoding='utf-8') as temp:
        reader = csv.reader(artworks)  # La fonction reader va récupérer les données du fichier csv en ignorant les virgules dans les guillemets
        writer = csv.writer(temp, delimiter="|", quotechar='\'', quoting=csv.QUOTE_NONNUMERIC)  # initialisation de la variable writer, avec des délimiteurs '|' car ce caractère n'est pas présent dans le fichier csv (pour pouvoir faire un split plus tard sans avoir de problème)
        writer.writerows(list(reader))  # écriture dans le fichier tempArtwork

# Création d'un fichier temporaire permettant de récupérer les données du fichier Artists.csv
with open('Artists.csv', 'r+', encoding='utf-8') as artists:
    with open('tempArtist.txt', 'a+', encoding='utf-8') as temp:
        reader = csv.reader(artists)
        writer = csv.writer(temp, delimiter="|", quotechar='\'', quoting=csv.QUOTE_NONNUMERIC)
        writer.writerows(list(reader))

# Création du fichier SQL permettant de remplir la table Artwork
with open('tempArtwork.txt', 'r+', encoding='utf-8') as temp:
    with open('fillArtwork.sql', 'a+', encoding='utf-8') as result:
        temp = temp.readlines()  # Lecture du fichier temporaire créé auparavant
        r = list()
        for index in range(0, len(temp)):  # Séparation du fichier afin de récupérer les données dans un tableau
            r.append(temp[index].split('|'))
        # Ecriture dans le fichier de sortie
        for x in range(2, len(r)):
            if x % 2 == 0:  # Les données du fichier tempArtwork sont toutes espacées
                result.write('INSERT INTO Artwork (Title,Date,Medium,Dimensions,CreditLine,AccessionNumber,Classification,Department,DateAcquired,ObjectID,URL) VALUES')
                result.write('(' + r[x][0] + ',' + r[x][8] + ',' + r[x][9] + ',' + r[x][10] + ',' + r[x][11] + ',' + r[x][12] + ',' + r[x][13] + ',' + r[x][14] + ',' + r[x][15] + ',' + r[x][17] + ',' + r[x][18] + ');\n')

# Création du fichier SQL permettant de remplir la table Artist
with open('tempArtist.txt', 'r+', encoding='utf-8') as temp:
    with open('fillArtist.sql', 'a+', encoding='utf-8') as result:
        temp = temp.readlines()
        r = list()
        for index in range(0, len(temp)):
            r.append(temp[index].split('|'))
        for x in range(2, len(r)):
            if x % 2 == 0:  # Les données du fichier tempArtist sont toutes espacées
                result.write('INSERT INTO Artist (ConstituentID, DisplayName, ArtistBio, Nationality, Gender, BeginDate, EndDate) VALUES')
                result.write('(' + r[x][0] + ',' + r[x][1] + ',' + r[x][2] + ',' + r[x][3] + ',' + r[x][4] + ',' + r[x][5] + ',' + r[x][6] + ');\n')

# Création du fichier SQL permettant de remplir la table Creates
# NB : ce code ne fonctionne pas pour la première et dernière ligne, une modification à la main est nécessaire pour obtenir une table sql adéquate
with open('tempArtwork.txt', 'r+', encoding='utf-8') as temp:
    with open('tempCreates.txt', 'a+', encoding='utf-8') as result:
        temp = temp.readlines()
        r = list()
        for index in range(0, len(temp)):
            r.append(temp[index].split('|'))
        result.write('INSERT INTO Creates (ObjectID, ConstituentID) VALUES\n')
        for x in range(2, len(r)):
            if x == 2:
                result.write(r[x][17] + ',' + r[x][2] + '),')
            else:
                if x % 2 == 0:
                    result.write('(' + r[x][17] + ',' + r[x][2] + '),')

# Suite du remplissage fillCreates : séparation des différents ConstituentID de la table Artwork (une oeuvre peut avoir plusieurs artistes)
with open('tempCreates.txt', 'r+', encoding='utf-8') as begin:
    with open('fillCreates.sql', 'a+', encoding='utf-8') as end:
        begin = begin.readlines()
        r = list()
        s = list()
        t = list()
        for index in range(0, len(begin)):  # Séparation du fichier afin de récupérer les données dans un tableau
            newbegin = re.sub(r", ", r",", begin[index])
            r.append(newbegin.split('\'),(\''))
        for index in range(0, len(r[1])):
            s.append(r[1][index].split(','))
        for index in range(0, len(s)):
            for index2 in range(1, len(s[index])):
                end.write('INSERT INTO Creates (ObjectID, ConstituentID) VALUES')
                end.write('(\'' + s[index][0] + ',')
                if index2 != 1:
                    end.write('\'')
                if index != len(s):
                    s[index][index2] = s[index][index2]
                    end.write(s[index][index2] + '\');\n')
                else:
                    end.write(s[index][index2] + ');\n')

# Création du fichier SQL permettant de remplir la table Belongs To, ArtisticCurrent et Museum: pas de donnée csv
