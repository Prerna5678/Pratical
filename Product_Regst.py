import mysql.connector as con

c = con.connect(    
    host="localhost",
    user="root",
    password="username@2811",
    database="Product"
    )

cur = c.cursor()
Username=input("Enter the username")
Email=input("enter the email")
Password=input("enter the password")

# Select query
query = "select * from Regst where Username=%s and Email=%s and Password=%s;"
print(query)

# for execute your query in database
a = (Username,Email, Password)
cur.execute(query, a)
c.commit()