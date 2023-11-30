-- Task: print a description for the table first_table from hbtn_0c_0
SELECT 
    *    
  FROM 
    INFORMATION_SCHEMA.COLUMNS
  WHERE
    TABLE_SCHEMA = 'hbtn_0c_0' AND
    TABLE_NAME = 'first_table';
