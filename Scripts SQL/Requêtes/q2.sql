SELECT a.DisplayName, COUNT(*)
FROM Artist a, Creates b, Artwork c
Where a.ConstituentID = b.ConstituentID 
AND b.ObjectID = c.ObjectID
And position('gelatin silver print' in c.Medium) != 0
AND a.DisplayName != 'Unknown photographer'
GROUP BY a.DisplayName
ORDER BY COUNT
DESC
LIMIT 10;