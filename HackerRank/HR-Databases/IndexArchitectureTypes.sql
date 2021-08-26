-- https://www.hackerrank.com/challenges/indexes-1/problem

-- how many index architecture types are there in Microsoft SQL Server?

-- There are two types of Indexes in SQL Server:
-- Clustered Index
-- Non-Clustered Index

-- https://www.sqlshack.com/what-is-the-difference-between-clustered-and-non-clustered-indexes-in-sql-server/

-- A clustered index defines the order in which data is physically stored in a table. Table data can be sorted in only way, therefore, there can be only one clustered index per table. In SQL Server, the primary key constraint automatically creates a clustered index on that particular column.

-- A non-clustered index doesn’t sort the physical data inside the table. In fact, a non-clustered index is stored at one place and table data is stored in another place. This is similar to a textbook where the book content is located in one place and the index is located in another. This allows for more than one non-clustered index per table.

-- https://www.hackerrank.com/challenges/indexes-2/problem
-- which of the following is true about row locators in MS SQL Server?
-- If the table does not have a clustered index, the row locator is the clustered index key for the row.
-- If the table has a clustered index, or the index is on an indexed view, the row locator is a pointer to the row.
-- If the table has a clustered index, or the index is on an indexed view, the row locator is the clustered index key for the row.
-- None of the above-mentioned statement is true.
