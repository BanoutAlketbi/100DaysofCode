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
val = [
    ("Peter", "Street 21"),
    ("Amy", "Apple st 43"),
    ("Hannah", "Mountain 21"),
    ("Better", "Green st 24")
]
    

mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
