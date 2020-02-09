# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

## import sqlite 3 package
import sqlite3
import pymysql

## CONNECT TO DATABASE
connection = sqlite3.connect("classrooms.db")
#connection.close()

## CREATE A TABLE

#cursor allows you to invoke methods that execute SQLite statements 
cursor = connection.cursor()

# define query for creating table
create_table = """
                CREATE TABLE classrooms (
                student_id INTEGER PRIMARY KEY,
                name VARCHAR(20),
                gender CHAR(1),
                physics_grade INTEGER,
                chemistry_grade INTEGER,
                math_grade
                ); """
                
#execute query
cursor.execute(create_table)                        

#commit changes
connection.commit()

#close connection
connection.close()

## INSERT DATA

# sample data as a list of tuples
classroom_data = [(1, "Pookie Jones", "F", 89, 70, 92),
                  (2, "Ronnie Ray", "M", 98, 93, 67),
                  (3, "Pokey Jo", "M", 86, 88, 88),
                  (4, "Peaches nCream", "F", 99, 89, 87),
                  (5, "Sonny Jones", "M", 78, 76, 98)]

# open connection
connection = sqlite3.connect("classrooms.db")

# open cursor
cursor = connection.cursor()

# insert records
for student in classroom_data:
    insert_statement = """INSERT INTO classrooms
                        (student_id, name, gender, physics_grade, chemistry_grade, math_grade)
                        VALUES
                        ({0}, "{1}", "{2}", {3}, {4}, {5});""".format(student[0], student[1], student[2],
                                                                student[3], student[4], student[5])
    #execute insert query
    cursor.execute(insert_statement)

# commit the changes
connection.commit()

#close the connection
connection.close()

## Extract Data

connection = sqlite3.connect("classrooms.db")
cursor = connection.cursor()

query = "SELECT * FROM classrooms"
cursor.execute(query)
result = cursor.fetchall()

#print result of query
for row in result:
    print(row)
    
connection.close()

#stopped at 5:23