import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    port=8889,
    user='root',
    password ='root',
    database='mydatabase'
)
mycursor = mydb.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Road 21")

mycursor.execute(sql, val)
mydb.commit()
print("1 record inserted, ID:", mycursor.lastrowid)
