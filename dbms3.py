import mysql.connector as con

try:
    print("🔌 Connecting to database...")

    # Try to connect
    c = con.connect(
        host="localhost",
        user="root",
        password="username@2811",
        database="pract1_db"
    )

    print("✅ Connected to pract1_db.")  # If this prints, connection is OK

    cur = c.cursor()
    print("📌 Cursor created.")

    x = input("Enter the email: ")
    y = input("Enter the password: ")

    que = "INSERT INTO practical1 (email, password) VALUES (%s, %s);"
    a = (x, y)

    print(f"📤 Inserting data: {a}")
    cur.execute(que, a)

    c.commit()
    print("💾 Commit successful. Data inserted.")

except con.Error as err:
    print("❌ MySQL Error:", err)

except Exception as e:
    print("❌ General Error:", e)

finally:
    if 'cur' in locals() and cur:
        cur.close()
        print("🔚 Cursor closed.")
    if 'c' in locals() and c:
        c.close()
        print("🔚 Connection closed.")
