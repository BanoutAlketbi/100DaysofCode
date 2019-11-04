import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    port=8889,
    user='root',
    password ='root',
    database='mydatabase'
)
mycursor = mydb.cursor()
sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")