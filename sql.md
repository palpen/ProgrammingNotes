# Notes on SQL commands

# Basic SQL Queries

* Count number of rows that satisfy condition
    - `SELECT COUNT(*) FROM table_name WHERE field_name > 0`


## SQLite

### Open a .db file in terminal
`sqlite3 chat.db`

### View tables in database
`.tables`

### View column names of a given table
`PRAGMA table_info(table_name);`

### How to exit session
`exit;`