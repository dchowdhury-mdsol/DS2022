import mysql.connector as connector
import numpy as np


mydb = connector.connect(
    host='localhost',
    user='root',
    password='Es6z-ogf3-axw2',
    database='lab_server'
)

cursor = mydb.cursor()

# cursor.execute("CREATE DATABASE lab_server")
# cursor.execute("CREATE TABLE students (id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(255), avg_grade INT)")

# cursor.execute("SELECT * FROM students")


# sql = "INSERT INTO students (first_name, avg_grade) VALUES (%s, %s)"
# val = [
#     ("Daiyan", 0),
#     ("Sudipta", 0)
# ]

# cursor.executemany(sql, val)
# print(cursor.rowcount, "was inserted.")

# cursor.execute("CREATE TABLE student_grades (student_id INT, assignment_num INT, assignment_grade INT, assignment_num_and_student_id VARCHAR(255) PRIMARY KEY)")
# cursor.execute("SELECT * FROM student_grades")

sql = "INSERT INTO student_grades (student_id, assignment_num, assignment_grade, assignment_num_and_student_id) VALUES (%s, %s, %s, %s)"
val = [
    (1, 1, 100, "11"),
    (1, 2, 90, "12"),
    (1, 3, 94, "13"),
    (1, 4, 97, "14"),
    (2, 1, 65, "21"),
    (2, 2, 70, "22"),
    (2, 3, 0, "23"),
    (2, 4, 15, "24")
] 

cursor.executemany(sql, val)
# print(cursor.rowcount, "was inserted.")

# cursor.execute()
myresults = cursor.fetchall()
for x in myresults:
    print(x)

sql1 = "SELECT AVG(assignment_grade) AS average FROM student_grades WHERE student_id = 1"
sql2 = "SELECT AVG(assignment_grade) AS average FROM student_grades WHERE student_id = 2"

cursor.execute(sql1)
rows = cursor.fetchall()
print(rows)
cursor.execute(sql2)
rows = cursor.fetchall()
print(rows)

sql3 = "UPDATE students SET avg_grade = 95.25 WHERE id = 1"
sql4 = "UPDATE students SET avg_grade = 37.50 WHERE id = 2"

cursor.execute(sql3)
row = cursor.fetchall()
for x in row:
    print(x)

cursor.execute("SELECT * from students")
row = cursor.fetchall()
for x in row:
    print(x)