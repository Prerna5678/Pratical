# E-Commerece 
Show_Prod=[]
Customer=[]

# Choice of customer
print("*"*70)
print("\n 1.Login \n 2.Registration \n 0.Exit")
a=int(input("\n Enter your choice"))
print("*"*70)

b=[]
print("*"*70)

while True:
     if a==1:
        print("\n Welcome in E_Commerce")
        print("_"*70)
        if a==1:
            # Login form 
            username=input("Enter your name")
            password=input("Enter your password")
            Teach_login={'username':username,'password':password}
            flag=False
            for Cust in Customer:
                print(Cust)
                if Cust_login==teach:
                    print("You login Sucessfully",Cust_login)
                    flag=True
                else:
                    print("Please try again",Cust_login)
                    flag=Flase
            print(Customer)
            add_quest=[]
            print("*"*70)
            
            # Customer option
            while flag==True:
                print("\n 1.Jeans \n 2.Shirt \n 3.Pant \n 4.Jacket \n 5.Checkout \n 6.Cart \n 0.Exit ")
                a=int(input("Enter the choice"))
