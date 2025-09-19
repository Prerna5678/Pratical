import mysql.connector as con

c = con.connect(    
    host="localhost",
    user="root",
    password="username@2811",
    database="pract1_db"
    )
#c.cursor()
cur = c.cursor()

x = input("Enter the email:")
y = input("Enter the password:")

que = "insert into practical1(email,password) values(%s,%s);"

a = (x, y)
cur.execute(que, a)
c.commit()
