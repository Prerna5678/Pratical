# E - Commerce
Customer = []
Product = [("Jeans", 799), ("Shirt", 500), ("T-Shirt", 3500), ("Jacket", 7999)]
cart = []

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
                print("You login successfully", Cust_login)
                flag = True
                break

        if not flag:
            print("Please try again. Invalid credentials.", Cust_login)
            print("+" * 70)
            continue

        # Show Product menu after successful login
        while True:
            print("\n 1.Jeans \n 2.Shirt \n 3.T-Shirt \n 4.Jacket \n 5.Checkout \n 6.View Cart \n 0.Exit")
            prod_choice = int(input("\nEnter your choice: "))
        # Jeans
        if choice==1:
            Qty=int(input("Enter the qty"))
            print(Product[0])
            print("+"*70)
            # Shirt
        elif choice==2:
            Qty=int(input("Enter the qty"))
            print(Product[1])
            print("+"*70)
        # T-Shirt
        elif choice==3:
            Qty=int(input("Enter the qty"))
            print(Product[2])
            print("+"*70)
        # Jacket
        elif choice==4:
            Qty=int(input("Enter the qty"))
            print(Product[3])
            print("+"*70)
        # Checkout
        elif choice==5:
            print()
            print("+"*70)
        # Cart
        elif choice==6:
            print()
            print("+"*70)
        # Exit
        elif choice==0:
            print("Exit")
            break
            print("+"*70)
        else:
            print("Enter proper Number")
            print("+"*70)
            1
    elif choice == 2:
        # Registration Form
        print("\nRegistration Form")
        print("+" * 70)
        reg_username = input("Enter your name: ")
        reg_email = input("Enter your email: ")
        new_user = {'username': reg_username, 'email': reg_email}

        if new_user in Customer:
            print("User already registered.")
        else:
            Customer.append(new_user)
            print("Your registration was successful.")
        print(Customer)
        print("+" * 70)

    elif choice == 0:
        print("Exit")
        print("+" * 70)
        break

    else:
        print("Invalid choice. Please try again.")
        print("+" * 70)