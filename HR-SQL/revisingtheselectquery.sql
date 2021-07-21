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

-- Query all attributes of every Japanese city in the CITY

SELECT ID, NAME, COUNTRYCODE, DISTRICT, POPULATION
FROM CITY
WHERE COUNTRYCODE = 'JPN';

-- Query the names of all the Japanese cities in the CITY table.

SELECT NAME
FROM CITY
WHERE COUNTRYCODE = 'JPN';

-- Query a list of CITY and STATE from the STATION table.

SELECT CITY, STATE
FROM STATION;

-- Query a list of CITY names from STATION for cities that have an even ID number.
-- https://www.w3schools.com/mysql/func_mysql_mod.asp
-- MOD(X,N) gives the remainder of X/N
-- Note that it's not mod(id/2), it's seperated by a comma
-- https://www.w3schools.com/sql/sql_distinct.asp
-- SELECT DISTINCT is used to get individual values

SELECT DISTINCT(CITY)
FROM STATION
WHERE (ID%2) = 0;



-- Query the Name of any student in STUDENTS who scored higher than
-- Marks. Order your output by the last three characters of each name.
-- If two or more students both have names ending in the same last
-- three characters (i.e.: Bobby, Robby, etc.),
-- secondary sort them by ascending ID.
-- Note - https://www.w3schools.com/sql/func_sqlserver_char.asp
-- char


SELECT NAME
FROM STUDENTS
WHERE MARKS > 75
--
ORDER BY NAME ASC;

-- Write a query that prints a list of employee names (i.e.: the name attribute) from the Employee table in alphabetical order.
-- note you can use operation ORDER BY, ASC, DESC
-- where ASC, DESC are ascending or descending

SELECT NAME
FROM EMPLOYEE
ORDER BY NAME ASC;


-- Write a query that prints a list of employee names (i.e.: the name attribute) for employees in Employee having a salary greater than  per month who have been employees for less than  months. Sort your result by ascending employee_id.

SELECT NAME
FROM EMPLOYEE
WHERE SALARY > 2000
AND MONTHS < 10;
