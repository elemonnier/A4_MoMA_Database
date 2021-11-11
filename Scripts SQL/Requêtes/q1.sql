SELECT c.Title
FROM Artist a, Creates b, Artwork c
WHERE a.ConstituentID = b.ConstituentID 
AND b.ObjectID = c.ObjectID
AND a.BeginDate > 1945;
