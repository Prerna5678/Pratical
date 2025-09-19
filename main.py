import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="username@2811",
    database="pract1_db"
    
)

mycursor=db.mycursor()
#mycursor.execute("CREATE DATABASE textdatabase")