Customer = []
cart = []
Product = [{"name":"Jeans","price": 799}, 
           {"name":"Shirt", "price":500}, 
           {"name":"T-Shirt", "price":3500}, 
           {"name":"Jacket","price": 7999}]
shopping_list=[]

print("+" * 70)

while True:
    print("\nYou are Welcome")
    print("+" * 70)
    print("\n 1.Login \n 2.Registration \n 0.Exit")
    choice = int(input("\nEnter your choice: "))
    print("+" * 70)

    if choice == 1:
        # Login form for Customer
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        Cust_login = {'email': email, 'password': password}
        flag = False

        for Cust in Customer:
            if Cust_login == Cust:
                print(f"Welcome to shopping, {email}!")
                flag = True
                while True:
                    print("\n 1.Jeans \n 2.Shirt \n 3.T-Shirt \n 4.Jacket \n 5.View Cart \n 6.Checkout \n 0.Exit")
                    prod_choice = int(input("\nEnter your choice: "))
                    total_amt = 0  # reset total_amt for each operation

                    # Add Jeans to Cart
                    if prod_choice == 1:
                        product = Product[0]  
                        qty = int(input(f"Enter quantity for {product['name']}: "))
                        
                        # Add product to cart
                        cart.append({'name': product['name'], 'price': product['price'], 'qty': qty})
                        print(f"{product['name']} x {qty} added to your cart.")
                        print("+" * 70)

                    # Add Shirt to Cart
                    elif prod_choice == 2:
                        product = Product[1]  
                        qty = int(input(f"Enter quantity for {product['name']}: "))
                        
                        # Add product to cart
                        cart.append({'name': product['name'], 'price': product['price'], 'qty': qty})
                        print(f"{product['name']} x {qty} added to your cart.")
                        print("+" * 70)

                    # Add T-Shirt to Cart
                    elif prod_choice == 3:
                        product = Product[2]  
                        qty = int(input(f"Enter quantity for {product['name']}: "))
                        
                        # Add product to cart
                        cart.append({'name': product['name'], 'price': product['price'], 'qty': qty})
                        print(f"{product['name']} x {qty} added to your cart.")
                        print("+" * 70)

                    # Add Jacket to Cart
                    elif prod_choice == 4:
                        product = Product[3]  
                        qty = int(input(f"Enter quantity for {product['name']}: "))

                        # Add product to cart
                        cart.append({'name': product['name'], 'price': product['price'], 'qty': qty})
                        print(f"{product['name']} x {qty} added to your cart.")
                        print("+" * 70)

                    # View Cart
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

                    # Checkout
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
                                cart.clear()  # Clear the cart after checkout
                            else:
                                print("Continue shopping!")
                        print("+" * 70)

                    # Exit
                    elif prod_choice == 0:
                        print("Exit")
                        print("+"*70)
                        break
                    else:
                        print("Enter proper Number")
                        print("+"*70)
                break  # Break out of the inner while loop after successful login

        if not flag:
            print("Invalid credentials. Please try again.")
            print("+" * 70)

    elif choice == 2:
        # Registration Form
        print("\nRegistration Form")
        print("+" * 70)
        reg_password = input("Enter your password: ")
        reg_email = input("Enter your email: ")
        new_user = {'email': reg_email, 'password': reg_password}

        if new_user in Customer:
            print("User already registered.")
        else:
            Customer.append(new_user)
            print("Registration successful. Please Login now!")
        print("+" * 70)

    elif choice == 0:
        print("Exiting...")
        print("+" * 70)
        break

    else:
        print("Invalid choice. Please try again.")
        print("+" * 70)