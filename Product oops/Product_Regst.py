import mysql.connector as con
con = con.connect(    
    host="localhost",
    user="root",
    password="root",
    database="Product"
    )
cur = con.cursor()
        
class Registration:
    def __init__(self,Username,Email,Password):
        self.Username=Username
        self.Email=Email
        self.Password=Password

    def Display(self):
        print("Welcome to Registration Form") 
        # Insert query
        query = "insert into regst(Username,Email,Password) values(%s,%s,%s);"
        print(query)
        # for execute your query in database
        a = (self.Username,self.Email,self.Password)
        cur.execute(query, a)
        con.commit()
        
Username=input("Enter the username")
Email=input("enter the email")
Password=input("enter the password")
R1=Registration(Username,Email,Password)
R1.Display()