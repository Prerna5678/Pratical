from Product_Regst import *
from Product_Login import *

import mysql.connector as con
con = con.connect(    
    host="localhost",
    user="root",
    password="root",
    database="Product"
    )
cur = con.cursor()

class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    
    def Customer(self):
        while True:
            print("Welcome")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Enter choice: ")
            if choice==1:
                Registration.Product_Regst()
            elif choice==2:
                Login.Product_Login()
            elif choice==3:
                # Exit
                break
            else:
                print("Invalid choice")

    def Display(self):   
        while True:
            print("Welcome to Shopping Menu")
            print("1. View item")
            print("2. Add cart")
            print("3. Remove item")
            print("4. Logout")

            choice = input("Enter choice: ")
            
            if choice==1:
                # View item 
                query="select * from Product_db;"
                print(query)
            elif choice==2:
                # Add Cart
                query = "insert into Product_db(Qty) values (%s);"
                print(query)
            elif choice==3:
                # Remove Cart
                query=""
                print(query)
            elif choice==4:
                # Logout
                break
            else:
                print("Invalid choice")

            # for execute your query in database
            cur.execute(query)
            con.commit()

class cart:
    def Add_cart(self):
        # insert query
        print("This is cart")  

P1=Product()
P1.Customer()
P1.Display()
