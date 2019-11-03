import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    port=8889,
    user='root',
    password ='root'
)


mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase")