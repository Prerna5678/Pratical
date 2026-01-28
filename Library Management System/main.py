from users import staff_login

while True:
    try:
        print("""
        LIBRARY MANAGEMENT SYSTEM
        1. Staff Login
        2. Exit
        """)

        choice = int(input("Enter choice: "))

        if choice == 1:
            staff_login()
        elif choice == 2:
            break
        else:
            print("Invalid choice")

    except ValueError:
        print("Please enter numbers only")
