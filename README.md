# SQL Shorts v1.1.0

### I made this program to help make sqlite3 less conplicated to use, there developer has a few term's and conditions. 

## How to download SQL Shorts.

### Just download the zip git repository or clone it on your system:
```bash
$git clone "paste clone link here without qoutes"
```
---

# How to use sqlite3 term

## 1. first import the package
```python
from database.sqlite import *
```

## 2. Create Table
```python
# db = DATABASE('Name_DataBase.db')
db = DATABASE('company.db')

# db.sql_create_table('Table_Name',"(column_1 DataType, column_2 DataType,...)")
db.sql_create_table('customer',"(firstName text,lastName text)")
```

## 3. Insert data
```python
# sql_insert_data( Name_of_Table, (John, Smith) ) 
# Remeber to put your data inside a tuple
db.sql_insert_data('customer',('John','Doe'))
```

## 4. Update data
```python
#sql_update_data('Table_Name',"column_1 = value_1, column_2 = value_2,...",RowId)
db.sql_udate_data('customer',"firstName = 'James', lastName = 'Smith'",1)
```

## 5. Delete data
```python
#sql_detele_data('Table_Name',RowId)
db.sql_delete_data('customer',1)
```

## 6. Delete Table
```python
# db.sql_drop_table('Table_Name')
db.sql_drop_table('customer')
```

## 7. View data all from table
```python
# db.sql_view_all('Table_Name')
db.sql_view_all('customer')
```

## 8. View filtered data from table
```python
# db.sql_view_specific('Table_Name','column_1,column_2,...')
db.sql_view_specific('customer','fname, email')
```

## 7. Search data from table

> you will still type sqlite3 syntax for search for LIKE characters
```python
#this will bring all the first names that start with Jo
firstName LIKE 'Jo%'
```

```python
#Using AND/OR
firstName LIKE 'Jo%' OR lastName LIKE 'Smi%'

firstName LIKE 'Jo%' AND lastName LIKE 'Smi%'
```

```python
# This is how you could write your syntax in there method
db.sql_search_table('customer',"rowid = 2 AND fname = 'Bob'")
```