# E - Commerce
Customer = []
#Product = {1:{"name":"Jeans","price": 799}, 2:{"name":"Shirt", "price":500},3: {"name":"T-Shirt", "price":3500}, 4:{"name":"Jacket","price": 7999}}
cart = []
Product = [{"name":"Jeans","price": 799}, {"name":"Shirt", "price":500}, {"name":"T-Shirt", "price":3500}, {"name":"Jacket","price": 7999}]
shopping_list=[]
print("+" * 70)

while True:
    print("\nYou are welcome in Customer")
    print("+" * 70)
    print("\n 1.Login \n 2.Registration \n 0.Exit")
    choice = int(input("\nEnter your choice: "))
    print("+" * 70)

    if choice == 1:
        # Login form for Customer
        username = input("Enter your name: ")
        email = input("Enter your email: ")
        Cust_login = {'username': username, 'email': email}
        flag = False

        for Cust in Customer:
            if Cust_login == Cust:
                print(Cust)
                print("You login successfully", Cust_login)
                flag = True
                while True:
                    print("\n 1.Jeans \n 2.Shirt \n 3.T-Shirt \n 4.Jacket \n 5.Checkout \n 6.View Cart \n 0.Exit")
                    prod_choice = int(input("\nEnter your choice: "))
                    name=0
                    price=0
                    total_amt=0
                    # Jeans
                    if prod_choice==1:
                         # Qty user side input
                        qty = int(input(f"Enter quantity for {name}:"))

                        # Calculation method of product * qty
                        subtotal = Product[0]["price"]* qty
                        total_amt += subtotal
                        
                        print(name," x ",qty ,"= Rs.",subtotal,"\n")
                        print("Total Amount: Rs.",total_amt)
                        print("Thank you for shopping!")
                        
                        print("+"*70)
                    # Shirt
                    elif prod_choice==2:
                        # Qty user side input
                        qty = int(input(f"Enter quantity for {name}:"))
                                                # Calculation method of product * qty
                        subtotal = price * qty
                        total_amt += subtotal
                    # T-Shirt
                    elif prod_choice==3:
                        # Qty user side input
                        qty = int(input(f"Enter quantity for {name}:"))
                        # Calculation method of product * qty
                        subtotal = price * qty
                        total_amt += subtotal
                    # Jacket
                    elif prod_choice==4:
                        # Qty user side input
                        qty = int(input(f"Enter quantity for {name}:"))
                        # Calculation method of product * qty
                        subtotal = price * qty
                        total_amt += subtotal            
                    # Checkout
                    elif prod_choice==5:
                        choice=int(input("you want to continue shopping()"))
                        choice1=int(input("Payment Option"))
                        if choice==yes:
                            print("Continue to shopping")
                        else("Thank for shopping")
                        print("+"*70)
                    # Cart
                    elif prod_choice==6:
                        # Calculation method of product * qty
                        subtotal = Product[0]["price"]* qty
                        total_amt += subtotal
                        
                        print(name," x ",qty ,"= Rs.",subtotal,"\n")
                        print("Total Amount: Rs.",total_amt)
                        print("Thank you for shopping!")
                        print("+"*70)
                    # Exit
                    elif choice==0:
                        print("Exit")
                        break
                        print("+"*70)
                    else:
                        print("Enter proper Number")
                        print("+"*70)

        else:
            print("Please try again. Invalid credentials.", Cust_login)
            print(Customer)
            print("+" * 70)
        # Show Product menu after successful login
    elif choice == 2:
        # Registration Form
        print("\nRegistration Form")
        print("+" * 70)
        reg_username = input("Enter your name: ")
        reg_email = input("Enter your email: ")
        print(Customer)
        new_user = {'username': reg_username, 'email': reg_email}

        if new_user in Customer:
            print("User already registered.")
        else:
            Customer.append(new_user)
            print("Your registration was successful.")
        print(Customer)
        print("+" * 70)

        if new_user not in Customer:

            Customer.append(new_user)
        else:
            print("user already registered")

    elif choice == 0:
        print("Exit")
        print("+" * 70)
        break

    else:
        print("Invalid choice. Please try again.")
        print("+" * 70)
