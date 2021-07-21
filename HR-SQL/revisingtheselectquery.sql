-- https://www.hackerrank.com/challenges/revising-the-select-query/problem

-- Query all columns for all American cities in the CITY table with populations larger than 100000. The CountryCode for America is USA.

-- remember to use '' around string for 'USA' as countrycode

SELECT ID, NAME, COUNTRYCODE, DISTRICT, POPULATION
FROM CITY
WHERE POPULATION > 100000
AND COUNTRYCODE = 'USA';

-- Query the NAME field for all American cities ... (just that column)

SELECT NAME
FROM CITY
WHERE POPULATION > 120000
AND COUNTRYCODE = 'USA';
