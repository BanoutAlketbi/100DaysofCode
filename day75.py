import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    port=8889,
    user='root',
    password ='root',
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE MyEmployee")
mydb = mysql.connector.connect(
    host='localhost',
    port=8889,
    user='root',
    password ='root',
    database='MyEmployee'
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE Employee (id INT AUTO_INCREMENT PRIMARY KEY, FirstName VARCHAR(255), LastName VARCHAR(255), Age VARCHAR(255), Gender VARCHAR(255), Salary VARCHAR(255))")
mycursor.mydb.cursor()

import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    port=8889,
    user='root',
    password ='root',
    database='MyEmployee'
)
mycursor = mydb.cursor()
sql = "INSERT INTO Employee (FirstName, LastName, Age, Gender, Salary) VALUES (%s, %s, %s, %s, %s)"
val = [
    ('Ahmed', 'Ali', 30, 'Male', 10000),
    ('Khalid', 'Muhammed', 34, 'Male', 7000),
    ('Norah', 'Saleh', 29, 'Female', 7000)
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "records inserted.")
print("show all records")
sql = "SELECT * FROM Employee"
mycursor.execute(sql)

myresult = mycursor.fetchall()
for Employee in myresult:
    print(Employee)
print("First Name, Gender and Salary")
sql = "SELECT FirstName, Gender, Salary FROM Employee"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for Employee in myresult:
    print(Employee)
print("records sorted by first name")
sql = "SELECT * FROM Employee ORDER BY FirstName DESC"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for Employee in myresult:
    print(Employee)
print("records afer deleting")
sql = "DELETE FROM Employee WHERE age = 34"
mycursor.execute(sql)
mydb.commit()
print(Employee)