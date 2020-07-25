# Notes on SQL commands

# Basic SQL Queries (for SQL Server)

```sql
--- Get all unique values of column
SELECT DISTINCT column
FROM table

--- Get unique values of column and the count for each
SELECT column, COUNT(column)
FROM table
GROUP BY column

-- Get count of distinct values in column
SELECT COUNT(DISTINCT column)
FROM table

-- Count number of rows that satisfy conditions (e.g. column>0, column=10)
SELECT COUNT(*)
FROM table
WHERE condition1
AND condition2

-- List all columns for the table in DBNAME..TABLENAME
USE DBNAME
SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME='TABLENAME'
ORDER BY COLUMN_NAME
```

## SQLite

### Open a .db file in terminal
`sqlite3 chat.db`

### View tables in database
`.tables`

### View column names of a given table
`PRAGMA table_info(table_name);`

### How to exit session
`exit;`
