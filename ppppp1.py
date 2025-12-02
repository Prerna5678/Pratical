# Shopping System

Customer = []
cart = []
Product = [
    {"name": "Jeans", "price": 799},
    {"name": "Shirt", "price": 500},
    {"name": "T-Shirt", "price": 3500},
    {"name": "Jacket", "price": 7999}
]

print("+" * 70)

while True:
    print("\nYou are Welcome")
    print("+" * 70)
    print("\n1. Login \n2. Registration \n0. Exit")
    choice = int(input("\nEnter your choice: "))
    print("+" * 70)

    # -------------------- LOGIN --------------------
    if choice == 1:
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        Cust_login = {'email': email, 'password': password}
        flag = False

        for Cust in Customer:
            if Cust_login == Cust:
                flag = True
                print(f"\nWelcome to shopping, {email}!")
                print("+" * 70)

                # Shopping Menu
                while True:
                    print("\n1. Jeans \n2. Shirt \n3. T-Shirt \n4. Jacket \n5. View Cart \n6. Checkout \n0. Logout")
                    prod_choice = int(input("\nEnter your choice: "))

                    # ----- Add Products -----
                    if prod_choice in [1, 2, 3, 4]:
                        product = Product[prod_choice - 1]
                        qty = int(input(f"Enter quantity for {product['name']}: "))
                        cart.append({'name': product['name'], 'price': product['price'], 'qty': qty})
                        print(f"{product['name']} x {qty} added to your cart.")
                        print("+" * 70)

                    # ----- View Cart -----
                    elif prod_choice == 5:
                        if not cart:
                            print("\nYour cart is empty.")
                        else:
                            print("\nYour Cart:")
                            print("-" * 50)
                            total_amt = 0
                            for item in cart:
                                subtotal = item["price"] * item["qty"]
                                total_amt += subtotal
                                print(f"{item['name']} x {item['qty']} = Rs. {subtotal}")
                            print(f"Total Amount: Rs. {total_amt}")
                            print("+" * 70)

                    # ----- Checkout -----
                    elif prod_choice == 6:
                        if not cart:
                            print("Your cart is empty.")
                        else:
                            print("\nCheckout Summary:")
                            total_amt = 0
                            for item in cart:
                                subtotal = item["price"] * item["qty"]
                                total_amt += subtotal
                                print(f"{item['name']} x {item['qty']} = Rs. {subtotal}")
                            print(f"\nYour total bill is Rs. {total_amt}")
                            confirm = input("Confirm checkout? (yes/no): ")
                            if confirm.lower() == "yes":
                                print("Thank you for shopping with us!")
                                cart.clear()
                            else:
                                print("Continue shopping!")
                        print("+" * 70)

                    # ----- Logout -----
                    elif prod_choice == 0:
                        print("Logged out successfully!")
                        print("+" * 70)
                        break

                    else:
                        print("Invalid choice, please try again.")
                        print("+" * 70)

        if not flag:
            print("Invalid credentials. Please register or try again.")
            print("+" * 70)

    # -------------------- REGISTRATION --------------------
    elif choice == 2:
        print("\nRegistration Form")
        print("+" * 70)
        reg_email = input("Enter your email: ")
        reg_password = input("Enter your password: ")
        new_user = {'email': reg_email, 'password': reg_password}

        if new_user in Customer:
            print("User already registered.")
        else:
            Customer.append(new_user)
            print("Registration successful! Please login now.")
        print("+" * 70)

    # -------------------- EXIT --------------------
    elif choice == 0:
        print("Exiting... Thank you!")
        print("+" * 70)
        break

    else:
        print("Invalid choice. Please try again.")
        print("+" * 70)
