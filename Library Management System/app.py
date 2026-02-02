from flask import Flask, render_template, request, redirect, url_for, session
import pymysql
import os
from werkzeug.utils import secure_filename
from datetime import date

# ================= CONFIG =================
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.secret_key = "library_secret_key"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# ================= DATABASE CONNECTION =================
def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="username@2811",
        database="library",
        cursorclass=pymysql.cursors.DictCursor
    )

# ================= LOGIN =================
@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        role = request.form.get("role")

        conn = get_connection()
        cur = conn.cursor()
        if role == "Admin":
            cur.execute("SELECT * FROM admin WHERE username=%s AND password=%s", (username, password))
            user = cur.fetchone()
        elif role == "Staff":
            cur.execute("SELECT * FROM staff WHERE username=%s AND password=%s", (username, password))
            user = cur.fetchone()
        elif role == "User":
            cur.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
            user = cur.fetchone()
        else:
            user = None

        conn.close()

        if user:
            session["username"] = username
            session["role"] = role
            return redirect(url_for("dashboard"))
        else:
            message = "Invalid credentials"

    return render_template("login.html", message=message)

# ================= SIGNUP =================
@app.route("/signup", methods=["GET", "POST"])
def signup():
    message = ""
    if request.method == "POST":
        fullname = request.form.get("fullname")
        username = request.form.get("username")
        password = request.form.get("password")
        role = request.form.get("role")

        conn = get_connection()
        cur = conn.cursor()
        try:
            if role == "User":
                cur.execute(
                    "INSERT INTO users (name, username, password, user_type, department) VALUES (%s,%s,%s,%s,%s)",
                    (fullname, username, password, "Student", "General")
                )
            else:
                cur.execute(
                    "INSERT INTO staff (name, username, password, role) VALUES (%s,%s,%s,%s)",
                    (fullname, username, password, role)
                )
            conn.commit()
            message = "Sign up successful! You can now login."
        except pymysql.err.IntegrityError:
            message = "Username already exists!"
        finally:
            conn.close()

    return render_template("login.html", signup_message=message)

# ================= LOGOUT =================
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

# ================= DASHBOARD =================
@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        return redirect(url_for("login"))

    conn = get_connection()
    cur = conn.cursor()

    # Fetch books
    cur.execute("SELECT * FROM books")
    books = cur.fetchall()

    # Fetch issued books
    cur.execute("""
        SELECT issue_records.issue_id, books.book_id, books.title, users.name AS user_name
        FROM issue_records
        JOIN books ON issue_records.book_id = books.book_id
        JOIN users ON issue_records.user_id = users.user_id
    """)
    issued_books = cur.fetchall()

    # Counts
    cur.execute("SELECT COUNT(*) AS total FROM books")
    total_books = cur.fetchone()["total"]

    cur.execute("SELECT COUNT(*) AS issued FROM issue_records WHERE status='Issued'")
    issued_count = cur.fetchone()["issued"]

    available_books = total_books - issued_count

    conn.close()

    return render_template("dashboard.html",
                           books=books,
                           issued_books=issued_books,
                           total_books=total_books,
                           issued_books_count=issued_count,
                           available_books=available_books)

# ================= ADD BOOK =================
@app.route("/add-book", methods=["GET", "POST"])
def add_book():
    if "username" not in session:
        return redirect(url_for("login"))

    message = ""
    if request.method == "POST":
        title = request.form.get("title")
        author = request.form.get("author")
        price = request.form.get("price")
        quantity = request.form.get("quantity")

        image_file = request.files.get("image")
        if image_file:
            filename = secure_filename(image_file.filename)
            path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            image_file.save(path)
        else:
            filename = ""

        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO books (title, author, price, images, quantity) VALUES (%s,%s,%s,%s,%s)",
                    (title, author, price, filename, quantity))
        conn.commit()
        conn.close()
        message = "Book added successfully!"

    return render_template("add_book.html", message=message)

# ================= ISSUE BOOK =================
@app.route("/issue-book", methods=["GET", "POST"])
def issue_book():
    if "username" not in session:
        return redirect(url_for("login"))

    message = ""
    conn = get_connection()
    cur = conn.cursor()

    # Fetch books and users
    cur.execute("SELECT * FROM books WHERE quantity>0")
    books = cur.fetchall()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()

    if request.method == "POST":
        book_id = request.form.get("book_id")
        user_id = request.form.get("user_id")
        staff_id = 1  # For simplicity, assign logged-in staff as 1
        today = date.today()
        cur.execute(
            "INSERT INTO issue_records (book_id,user_id,staff_id,issue_date,return_date,status) VALUES (%s,%s,%s,%s,%s,%s)",
            (book_id, user_id, staff_id, today, today, "Issued")
        )
        cur.execute("UPDATE books SET quantity=quantity-1 WHERE book_id=%s", (book_id,))
        conn.commit()
        message = "Book issued successfully!"

    conn.close()
    return render_template("issue_book.html", books=books, users=users, message=message)


# ================= MAIN =================
if __name__ == "__main__":
    app.run(debug=True)
