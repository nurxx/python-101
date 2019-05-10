SELECT AVG(speed) AS AvgSpeed
FROM pc;

SELECT AVG(laptop.screen) AS AvgScreen
FROM laptop JOIN product ON laptop.model=product.model
GROUP BY product.maker;

SELECT AVG(speed) as AvgSpeed
FROM laptop
WHERE price>1000;

SELECT AVG(price) AS AvgPrice
FROM pc
GROUP BY hd;

SELECT AVG(price) AS AvgPrice
FROM pc
WHERE speed>500;

SELECT AVG(price) AS AvgPrice
FROM pc JOIN product ON pc.model=product.model
WHERE product.maker LIKE 'A';

SELECT AVG(price)
FROM ( SELECT laptop.price
       FROM laptop JOIN product ON laptop.model=product.model
       WHERE product.maker LIKE 'B'
	UNION
	SELECT price
        FROM pc JOIN product ON pc.model=product.model
        WHERE product.maker LIKE 'B')

SELECT maker
FROM product
WHERE type LIKE 'PC'
GROUP BY model
HAVING COUNT(DISTINCT model)>=3;

SELECT product.maker
FROM pc JOIN product ON pc.model=product.model
WHERE pc.price = (SELECT MAX(price)
                    FROM pc);

SELECT AVG(hd) as AvgHD
FROM pc JOIN product ON pc.model=product.model
WHERE product.maker IN (SELECT maker
                         FROM product
                         WHERE type LIKE 'PC' OR 'Printer');
