from db import get_connection

def add_book():
    con = get_connection()
    cur = con.cursor()

    book_id = int(input("Book ID: "))
    title = input("Title: ")
    author = input("Author: ")
    quantity = int(input("Quantity: "))

    cur.execute(
        "INSERT INTO books VALUES (%s,%s,%s,%s)",
        (book_id, title, author, quantity)
    )

    con.commit()
    con.close()
    print("Book added successfully")

def view_books():
    con = get_connection()
    cur = con.cursor()

    cur.execute("SELECT * FROM books")
    records = cur.fetchall()

    print("\nBook ID | Title | Author | Quantity")
    print("-----------------------------------")
    for row in records:
        print(row)

    con.close()
