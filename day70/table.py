import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    port=8889,
    user='root',
    password ='root',
    database='mydatabase'
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers(name VARCHAR(255), address VARCHAR(255))")
