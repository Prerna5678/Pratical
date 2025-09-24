import mysql.connector as con

c = con.connect(    
    host="localhost",
    user="root",
    password="username@2811",
    database="pract1_db"
    )

cur = c.cursor()

x=input("enter the email")
y=input("enter the password")

query = "select * from user where email=%s and password=%s ;"
print(query)

# for execute your query in database
r = cur.execute(query)
print(r)