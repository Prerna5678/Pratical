import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="username@2811",      
    database="Library"
)

connection.close()
