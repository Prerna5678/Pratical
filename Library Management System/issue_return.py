from db import get_connection
from datetime import date

def issue_book(staff_id):
    con = get_connection()
    cur = con.cursor()

    book_id = int(input("Book ID: "))
    user_id = int(input("User ID: "))

    cur.execute("SELECT quantity FROM books WHERE book_id=%s", (book_id,))
    result = cur.fetchone()

    if result and result[0] > 0:
        cur.execute("""
            INSERT INTO issue_records
            (book_id, user_id, staff_id, issue_date, status)
            VALUES (%s, %s, %s, %s, 'Issued')
        """, (book_id, user_id, staff_id, date.today()))

        cur.execute(
            "UPDATE books SET quantity = quantity - 1 WHERE book_id=%s",
            (book_id,)
        )

        con.commit()
        print("Book issued successfully")
    else:
        print("Book not available")

    con.close()

def return_book():
    con = get_connection()
    cur = con.cursor()

    issue_id = int(input("Issue ID: "))

    cur.execute(
        "SELECT book_id FROM issue_records WHERE issue_id=%s AND status='Issued'",
        (issue_id,)
    )
    record = cur.fetchone()

    if record:
        cur.execute("""
            UPDATE issue_records
            SET return_date=%s, status='Returned'
            WHERE issue_id=%s
        """, (date.today(), issue_id))

        cur.execute(
            "UPDATE books SET quantity = quantity + 1 WHERE book_id=%s",
            (record[0],)
        )

        con.commit()
        print("Book returned successfully")
    else:
        print("Invalid Issue ID")

    con.close()
