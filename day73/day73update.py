import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    port=8889,
    user='root',
    password ='root',
    database='mydatabase'
)
mycursor = mydb.cursor()
sql ="UPDATE customers SET address = 'Apple St 21' WHERE address = 'Apple st 43'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")