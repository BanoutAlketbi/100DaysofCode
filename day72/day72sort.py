import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    port=8889,
    user='root',
    password ='root',
    database='mydatabase'
)
mycursor = mydb.cursor()
sql = "SELECT * FROM customers ORDER BY name"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
    