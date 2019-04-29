SELECT ships.name,classes.country,classes.numguns,ships.launched
FROM ships JOIN classes ON ships.class=classes.class;

SELECT ships.name,classes.country,classes.numguns,ships.launched
FROM classes LEFT JOIN ships ON ships.class=classes.class;

SELECT outcomes.ship
FROM outcomes JOIN battles ON outcomes.battle=battles.name
WHERE battles.date LIKE '%1942%';

SELECT classes.country,ships.name
FROM (ships LEFT JOIN outcomes ON ships.name=outcomes.ship) JOIN classes ON ships.class = classes.class
WHERE outcomes.battle IS NULL
ORDER BY classes.country;
