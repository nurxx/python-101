SELECT address
FROM studio
WHERE name LIKE 'MGM';

SELECT birthdate
FROM moviestar
WHERE name LIKE 'Kim Basinger';

SELECT name 
FROM movieexec 
WHERE networth > 10000000; 

SELECT name
FROM moviestar 
WHERE gender LIKE 'M' OR address LIKE 'Prefect Rd.';

INSERT INTO MOVIESTAR
	VALUES('Zahari Baharov','Riot Rd.','M','1989-03-11'); 


DELETE FROM STUDIO
WHERE address LIKE '%5%'
					
UPDATE movie 
SET studioname='Fox' 
WHERE title LIKE '%Star%'; 

