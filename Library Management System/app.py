from flask import Flask, render_template, request, redirect, url_for, session
import pymysql
from datetime import date

app = Flask(__name__)
app.secret_key = "library_secret_key"

# ---------- DATABASE CONNECTION ----------
def get_db_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="username@2811",   # change if needed
        database="Library",
        cursorclass=pymysql.cursors.DictCursor
    )

# ---------- LOGIN & SIGNUP ----------
@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    message = ""
    signup_message = ""

    if request.method == "POST":
        action = request.form.get("action")

        conn = get_db_connection()
        cur = conn.cursor()

        # ---------- SIGN UP (STUDENT ONLY) ----------
        if action == "signup":
            name = request.form["name"]
            department = request.form["department"]
            username = request.form["username"]
            password = request.form["password"]

            try:
                cur.execute(
                    "INSERT INTO users (name, department, username, password, user_type) "
                    "VALUES (%s, %s, %s, %s, 'Student')",
                    (name, department, username, password)
                )
                conn.commit()
                signup_message = "Signup successful! Please sign in."
            except:
                signup_message = "Username already exists!"

            conn.close()
            return render_template("login.html", signup_message=signup_message)

        # ---------- LOGIN ----------
        if action == "login":
            username = request.form["username"]
            password = request.form["password"]

            # Admin
            cur.execute(
                "SELECT * FROM admin WHERE username=%s AND password=%s",
                (username, password)
            )
            admin = cur.fetchone()

            # Staff
            cur.execute(
                "SELECT * FROM staff WHERE username=%s AND password=%s",
                (username, password)
            )
            staff = cur.fetchone()

            # User
            cur.execute(
                "SELECT * FROM users WHERE username=%s AND password=%s",
                (username, password)
            )
            user = cur.fetchone()

            conn.close()

            if admin:
                session["role"] = "admin"
                session["name"] = admin["name"]
                return redirect(url_for("dashboard"))

            elif staff:
                session["role"] = "staff"
                session["name"] = staff["name"]
                return redirect(url_for("dashboard"))

            elif user:
                session["role"] = "user"
                session["user_id"] = user["user_id"]
                session["name"] = user["name"]
                return redirect(url_for("dashboard"))

            else:
                message = "Invalid username or password"

    return render_template("login.html", message=message, signup_message=signup_message)

# ---------- DASHBOARD ----------
@app.route("/dashboard")
def dashboard():
    if "role" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html", role=session["role"], name=session["name"])

# ---------- ADD BOOK (ADMIN / STAFF) ----------
@app.route("/add-book", methods=["GET", "POST"])
def add_book():
    if session.get("role") not in ["admin", "staff"]:
        return redirect(url_for("dashboard"))

    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        price = request.form["price"]
        quantity = request.form["quantity"]
        image = request.form["image"]

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO books (title, author, price, images, quantity) "
            "VALUES (%s, %s, %s, %s, %s)",
            (title, author, price, image, quantity)
        )
        conn.commit()
        conn.close()

        return redirect(url_for("view_books"))

    return render_template("add_book.html")

# ---------- VIEW BOOKS ----------
@app.route("/view-books")
def view_books():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    books = cur.fetchall()
    conn.close()
    return render_template("view_books.html", books=books)

# ---------- ISSUE BOOK ----------
@app.route("/issue-book", methods=["GET", "POST"])
def issue_book():
    if session.get("role") not in ["admin", "staff", "user"]:
        return redirect(url_for("login"))

    conn = get_db_connection()
    cur = conn.cursor()

    if request.method == "POST":
        book_id = request.form["book_id"]
        user_id = session.get("user_id", 1)   # admin/staff demo
        staff_id = 1                           # demo staff id

        cur.execute(
            "INSERT INTO issue_records "
            "(book_id, user_id, staff_id, issue_date, return_date, status) "
            "VALUES (%s, %s, %s, %s, %s, 'Issued')",
            (book_id, user_id, staff_id, date.today(), date.today())
        )
        conn.commit()

    cur.execute("SELECT * FROM books WHERE quantity > 0")
    books = cur.fetchall()
    conn.close()

    return render_template("issue_book.html", books=books)

# ---------- RETURN BOOK ----------
@app.route("/return-book", methods=["GET", "POST"])
def return_book():
    if session.get("role") not in ["admin", "staff", "user"]:
        return redirect(url_for("login"))

    conn = get_db_connection()
    cur = conn.cursor()

    if request.method == "POST":
        issue_id = request.form["issue_id"]
        cur.execute(
            "UPDATE issue_records SET status='Returned' WHERE issue_id=%s",
            (issue_id,)
        )
        conn.commit()

    cur.execute("SELECT * FROM issue_records WHERE status='Issued'")
    records = cur.fetchall()
    conn.close()

    return render_template("return_book.html", records=records)

# ---------- LOGOUT ----------
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

# ---------- MAIN ----------
if __name__ == "__main__":
    app.run(debug=True)
