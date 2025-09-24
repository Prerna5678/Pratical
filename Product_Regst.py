import mysql.connector as con

c = con.connect(    
    host="localhost",
    user="root",
    password="username@2811",
    database="Product"
    )

cur = c.cursor()
username=input("Enter the username")
Email=input("enter the email")
Password=input("enter the password")

query = "select * from Regst where username=%s and email=%s and password=%s ;"
print(query)

# for execute your query in database
r = cur.execute(query)
print(r)