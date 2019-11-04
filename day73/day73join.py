import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    port=8889,
    user='root',
    password ='root',
    database='mydatabase'
)
mycursor = mydb.cursor()
sql = "SELECT \
    info.name AS name, \
    FROM info \
    INNER JOIN work ON info.name = work.id"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in my result:
    print(x)

sql = "SELECT \
    info.name AS name, \
    FROM info \
    LEFT JOIN work ON info.name = work.id"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in my result:
    print(x)