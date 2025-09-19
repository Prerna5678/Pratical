import mysql.connector as con

con = con.connect(    
    host="localhost",
    user="root",
    password="username@2811",
    database="pract1_db"
    )
cur = con.cursor()

# login i=email and password
x = input("enter your email :")
y = input("enter your password :")

# sql query for retive user data from database
query = "select * from user where email='" + x + "' and pass='" + y + "';"
# query = "select * from user where email=%s and pass=%s ;"
print(query)

# for execute your query in database
r = cur.execute(query)
print(r)
