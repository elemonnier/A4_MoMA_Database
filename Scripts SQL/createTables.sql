CREATE TABLE Museum(
        IDMuseum   Varchar (50) ,
        MuseumName Varchar (50)  ,
        MuseumCity Varchar (50) 
	,CONSTRAINT Museum_PK PRIMARY KEY (IDMuseum)
);

CREATE TABLE ArtisticCurrent(
        IDCurrent        Varchar (50)  ,
        CurrentName      Varchar (50)  ,
        BeginYearCurrent Varchar (50)  ,
        EndYearCurrent   Varchar (50)  ,
        DescriptionText  Varchar (50)
	,CONSTRAINT ArtisticCurrent_PK PRIMARY KEY (IDCurrent)
);

CREATE TABLE Artist(
        ConstituentID Varchar (500) ,
        DisplayName   Varchar (500) ,
        ArtistBio     Varchar (500) ,
        Nationality   Varchar (50) ,
        Gender        Varchar (50) ,
        BeginDate     Int ,
        EndDate       Int ,
        IDCurrent     Varchar (50)
	,CONSTRAINT Artist_PK PRIMARY KEY (ConstituentID)

	,CONSTRAINT Artist_ArtisticCurrent_FK FOREIGN KEY (IDCurrent) REFERENCES ArtisticCurrent(IDCurrent)
);

CREATE TABLE Artwork(
        ObjectID        Varchar (500)  ,
        Type            Varchar (5000)  ,
        Title           Varchar (5000)  ,
        Classification  Varchar (5000)  ,
        Date            Varchar (5000)  ,
        Url             Varchar (5000)  ,
        Dimensions      Varchar (5000)  ,
        Medium          Varchar (5000)  ,
        CreditLine      Varchar (5000)  ,
        AccessionNumber Varchar (5000)  ,
        Department      Varchar (5000)  ,
        DateAcquired    Varchar (5000)  ,
        IDCurrent       Varchar (5000)  ,
        IDMuseum        Varchar (5000) 
	,CONSTRAINT Artwork_PK PRIMARY KEY (ObjectID)

	,CONSTRAINT Artwork_ArtisticCurrent_FK FOREIGN KEY (IDCurrent) REFERENCES ArtisticCurrent(IDCurrent)
	,CONSTRAINT Artwork_Museum0_FK FOREIGN KEY (IDMuseum) REFERENCES Museum(IDMuseum)
);


CREATE TABLE belongs_to(
        IDCurrent     Varchar (50) ,
        ConstituentID Varchar (500) 
	,CONSTRAINT belongs_to_PK PRIMARY KEY (IDCurrent,ConstituentID)

	,CONSTRAINT belongs_to_ArtisticCurrent_FK FOREIGN KEY (IDCurrent) REFERENCES ArtisticCurrent(IDCurrent)
	,CONSTRAINT belongs_to_Artist0_FK FOREIGN KEY (ConstituentID) REFERENCES Artist(ConstituentID)
);

CREATE TABLE creates(
        ObjectID      Varchar (50) ,
        ConstituentID Varchar (500) 
	,CONSTRAINT creates_PK PRIMARY KEY (ObjectID,ConstituentID)

	,CONSTRAINT creates_Artwork_FK FOREIGN KEY (ObjectID) REFERENCES Artwork(ObjectID)
	,CONSTRAINT creates_Artist0_FK FOREIGN KEY (ConstituentID) REFERENCES Artist(ConstituentID)
);