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


-- Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.

-- select outer function
-- select ( X - Y ) as total_count
-- this will give us a total-count, difference between X and Y
select
  (
      -- SELECT all with COUNT(*) <-- measure of all values
    SELECT
      COUNT(*)
    from
      STATION
  ) - (
      -- SELECT individuals with COUNT(DISTINCT COL)
    SELECT
      COUNT(DISTINCT CITY)
    from
      STATION
  ) as total_count



-- Query the two cities in STATION with the shortest and longest CITY names,
-- as well as their respective lengths (i.e.: number of characters in the name).
-- If there is more than one smallest or largest city, choose the one that comes
-- first when ordered alphabetically.

-- sql server len https://www.w3schools.com/sql/func_sqlserver_len.asp
-- sql server orderby https://www.w3schools.com/sql/sql_orderby.asp

-- note! SQL function accepted for LEN() was LENGTH()
-- it's ASC / DESC not ASC/DSC

SELECT CITY, LENGTH(CITY)
FROM STATION
ORDER BY LENGTH(CITY), CITY ASC LIMIT 1;
SELECT CITY, LENGTH(CITY)
FROM STATION
ORDER BY LENGTH(CITY) DESC LIMIT 1;




-- Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates.
-- The LIKE operator is used in a WHERE clause to search for a specified pattern in a column.
-- https://www.w3schools.com/sql/sql_like.asp

SELECT DISTINCT CITY
FROM STATION
WHERE CITY NOT LIKE '[a,e,i,o,u]%' AND CITY NOT LIKE '%[a,e,i,o,u]'


-- Query the Name of any student in STUDENTS who scored higher than 75 Marks.
-- Order your output by the last three characters of each name.
-- If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), secondary sort them by ascending ID.

-- Note - you can get the right three characters:
-- https://www.w3schools.com/sql/trysqlserver.asp?filename=trysql_func_sqlserver_right

-- Note - ORDER BY works with multiple columns
-- https://www.w3schools.com/sql/sql_orderby.asp

SELECT NAME
FROM STUDENTS
WHERE MARKS > 75
-- get last three characters in name using RIGHT(COL,NUMCHAR)
-- ORDER BY works with multiple columns, use name first, then ID
ORDER BY RIGHT(NAME, 3), ID ASC;

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
