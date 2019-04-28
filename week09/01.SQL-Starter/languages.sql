CREATE TABLE Languages(
id INTEGER NOT NULL PRIMARY KEY,
language VARCHAR(20),
answer VARCHAR(32),
answered BOOLEAN,
guide TEXT);


INSERT INTO Languages
VALUES (1,'Python','Google', 0,'A folder named Python was created. Go there and fight with program.py!'),
       (2,'Go','200 OK', 0,'A folder named Go was created. Go there and try to make Google Go run.'),
	   (3,'Java','Object Oriented Programming', 0,'A folder named Java was created. Can you handle the class?'),
	   (4,'Haskell','Lambda', 0,'Something pure has landed. Go to Haskell folder and see it!'),
	   (5,'C#','NDI=', 0,'Do you see sharp? Go to the C# folder and check out.'),
	   (6,'Ruby','https://www.ruby-lang.org/bg/', 0, 'Ruby, ruby, rubyyy, aaahaaaahaa! (music). Go to Ruby folder!'),
	   (7,'C++','Header files', 0,'Here be dragons! It''s C++ time. Go to the C++ folder.'),
	   (8,'JavaScript','Douglas Crockford', 0, 'NodeJS time. Go to JavaScript folder and Node your way!');
	   
ALTER TABLE Languages
ADD COLUMN rating INTEGER 

UPDATE Languages
SET rating=1
WHERE id=1 OR id=5

UPDATE Languages
SET rating=8
WHERE id=7 OR id=4 OR id=3

UPDATE Languages
SET rating=9
WHERE id=2 OR id=6 OR id=8

UPDATE Languages
SET answered=1
WHERE language LIKE 'Python' OR language LIKE 'Go';

SELECT language
FROM Languages
WHERE answer LIKE '200 OK' or answer LIKE 'Lambda';