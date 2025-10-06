from Product_Regst import *
import mysql.connector as con

c = con.connect(    
    host="localhost",
    user="root",
    password="username@2811",
    database="Product"
    )

cur = c.cursor()

Email=input("enter the email")
Password=input("enter the password")

# Select Query
query = "select * from Login where Email=%s and Password=%s;"
print(query)

# for execute your query in database
a = (Email, Password)
cur.execute(query, a)
c.commit()