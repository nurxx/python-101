SELECT moviestar.name 
FROM moviestar JOIN starsin ON moviestar.name=starsin.starname
WHERE moviestar.gender LIKE 'M' AND starsin.movietitle LIKE 'Terms of Endearment';

SELECT starsin.starname
FROM movie JOIN starsin ON movie.title=starsin.movietitle 
WHERE movie.year LIKE '1995' and movie.studioname LIKE 'MGM'; 

ALTER TABLE studio 
ADD COLUMN PRESIDENT VARCHAR(30)

UPDATE studio 
SET president='John Doe' WHERE name='Disney'

UPDATE studio 
SET president='Mary Doe' WHERE name='MGM' 

 UPDATE studio 
SET president='Lilly Bush' WHERE name='Fox' 

UPDATE studio 
SET president='Lilly Bush' WHERE name='Paramount'

UPDATE studio 
SET president='Daniel Hulk' WHERE name LIKE '%USA%' 

 UPDATE studio 
SET president='John Doe' WHERE name='Warner Bros' 

 SELECT m1.title 
FROM movie AS m1
WHERE m1.length > (SELECT m2.length 
                    FROM movie AS m2
                    WHERE m2.title LIKE 'Gone With the Wind' ); 
				
SELECT m1.name
FROM movieexec AS m1
WHERE m1.networth > (SELECT m2.networth 
                      FROM movieexec AS m2
                      WHERE m2.name LIKE 'Merv Griffin');