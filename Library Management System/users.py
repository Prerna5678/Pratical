from db import get_connection
from books import add_book, view_books
from issue_return import issue_book, return_book
import sys

def staff_login():
    # Debug line to check function is called
    print("DEBUG: staff_login() called")
    sys.stdout.flush()  # Ensures the DEBUG line appears before input()

    # Take username and password from staff
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    # Connect to database
    con = get_connection()
    cur = con.cursor()

    # Check if staff exists
    cur.execute(
        "SELECT staff_id, name FROM staff WHERE username=%s AND password=%s",
        (username, password)
    )
    staff = cur.fetchone()
    con.close()

    # If staff exists, go to staff menu
    if staff:
        print(f"\nWelcome {staff[1]}")
        staff_menu(staff[0])
    else:
        print("Invalid username or password")

def staff_menu(staff_id):
    while True:
        print("""
-------- STAFF MENU --------
1. Add Book
2. View Books
3. Issue Book
4. Return Book
5. Logout
""")
        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Please enter numbers only")
            continue

        if choice == 1:
            add_book()
        elif choice == 2:
            view_books()
        elif choice == 3:
            issue_book(staff_id)
        elif choice == 4:
            return_book()
        elif choice == 5:
            print("Logging out...")
            break
        else:
            print("Invalid choice")
