-- Task: print a description for the table first_table from hbtn_0c_0
SELECT 
    COLUMN_NAME,
    DATA_TYPE,
   IS_NULLABLE,
   COLUMN_DEFAULT
  FROM 
    INFORMATION_SCHEMA.COLUMNS
  WHERE
    TABLE_SCHEMA = 'hbtn_0c_0' AND
    TABLE_NAME = 'first_table';
