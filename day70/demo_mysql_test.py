import mysql.connector
mydp = mysql.connector.connect(
    host="localhost",
    user="myusername",
    passwd="mypassword"
)

print(mydp)