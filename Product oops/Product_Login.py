import mysql.connector as con
con = con.connect(    
    host="localhost",
    user="root",
    password="root",
    database="Product"
    )
cur = con.cursor()
class Login:
    def __init__(self,Username,Email,Password):
        self.Username=Username
        self.Email=Email
        self.Password=Password

    def Display(self):
        print("Welcome to Login Form")
        # Insert Query
        query = "insert into Login (Username,Email,Password) values(%s,%s,%s);"
        print(query)

        # for execute your query in database
        a = (Username,Email, Password)
        cur.execute(query, a)
        con.commit()

Username=input("Enter the Username")
Email=input("enter the Email")
Password=input("enter the Password")
L1=Login(Username,Email,Password)
L1.Display()