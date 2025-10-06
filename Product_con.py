import mysql.connector as con

con = con.connect(    
    host="localhost",
    user="root",
    password="username@2811",
    database="Product_oops"
    )
cur = con.cursor()

