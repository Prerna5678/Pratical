import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="username@2811",  # replace with your MySQL password
    database="Product"
)
cursor = conn.cursor()

# ------------------ USER SYSTEM ------------------ #
def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        print("Registration successful ✅")
    except mysql.connector.IntegrityError:
        print("⚠ Username already exists, try another.")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    cursor.execute("SELECT id FROM users WHERE username=%s AND password=%s", (username, password))
    user = cursor.fetchone()

    if user:
        print("Login successful ✅")
        return user[0]   # return user_id
    else:
        print("❌ Invalid username or password")
        return None

# ------------------ CART SYSTEM ------------------ #
def add_item(user_id, name, price):
    cursor.execute("INSERT INTO cart (user_id, name, price) VALUES (%s, %s, %s)", (user_id, name, price))
    conn.commit()
    print("Item added to cart.")

def display_cart(user_id):
    cursor.execute("SELECT id, name, price FROM cart WHERE user_id=%s", (user_id,))
    items = cursor.fetchall()

    if not items:
        print("Your cart is empty.")
    else:
        total = 0
        print("\nYour Cart:")
        for row in items:
            print(f"{row[0]}. {row[1]}: Rs.{row[2]}")
            total += row[2]
        print(f"Total: Rs.{total}")

def remove_item(user_id, item_id):
    cursor.execute("DELETE FROM cart WHERE id=%s AND user_id=%s", (item_id, user_id))
    conn.commit()
    print("Item removed from cart.")

# ------------------ MAIN PROGRAM ------------------ #
def main():
    print("Welcome to Shopping Cart App 🛒")

    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            user_id = login()
            if user_id:
                shopping_menu(user_id)
        elif choice == "3":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice.")

def shopping_menu(user_id):
    while True:
        print("\nShopping Menu")
        print("1. Add item")
        print("2. View cart")
        print("3. Remove item")
        print("4. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter item name: ")
            price = int(input("Enter item price: "))
            add_item(user_id, name, price)

        elif choice == "2":
            display_cart(user_id)

        elif choice == "3":
            display_cart(user_id)
            item_id = int(input("Enter item ID to remove: "))
            remove_item(user_id, item_id)

        elif choice == "4":
            print("Logged out ✅")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

cursor.close()
conn.close()
