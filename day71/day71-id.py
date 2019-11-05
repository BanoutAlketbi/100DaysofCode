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
