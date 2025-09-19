import mysql.connector as con

# c = con.connect(host="localhost", user="root", password="root", database="p_db")
c = con.connect(    
    host="localhost",
    user="root",
    password="username@2811",
    database="pract1_db"
    )
cur = c.cursor()
print(c)

x = input("enter your email : ")
y = input("enter your pass : ")

que = "insert into practical1(email,password) values(%s,%s);"

v = (x, y)

cur.execute(que, v)

c.commit()
