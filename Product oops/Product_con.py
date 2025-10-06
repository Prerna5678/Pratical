import mysql.connector as con

con = con.connect(    
    host="localhost",
    user="root",
    password="root",
    database="Product"
    )
cur = con.cursor()

