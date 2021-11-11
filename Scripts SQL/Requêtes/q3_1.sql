CREATE VIEW View
AS SELECT a.DisplayName, COUNT(*)
FROM Artist a, Creates b, Artwork c
Where a.ConstituentID = b.ConstituentID 
AND b.ObjectID = c.ObjectID
GROUP BY a.DisplayName;