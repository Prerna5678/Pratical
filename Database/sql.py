import mysql.connector as con

con = con.connect(
    host="localhost", user="root", password="root", database="python_login"
)

cur = con.cursor()

# login i=email and password
x = input("enter your email :")
y = input("enter your password :")

# sql query for retive user data from database
#query = "select * from user where email='"+x+"' and pass='"+y+"';"
#print(query)    
query = "select * from user where email=%s and pass=%s ;"

# for execute your query in database
#cur.execute(query)
cur.execute(query,(x,y))

r = cur.fetchone()    
print(r)
if r==None:
    print("id and password dose not match")
else:
    print("welcome..!")
    