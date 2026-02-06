from flask import Flask, render_template, request, redirect, url_for, session
import pymysql
import os
from werkzeug.utils import secure_filename
from datetime import date

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.secret_key = "library_secret_key"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

#DATABASE CONNECTION
def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="username@2811",
        database="library",
        cursorclass=pymysql.cursors.DictCursor
    )

# LOGIN PAGE
@app.route("/")
@app.route("/login")
def login():
    return render_template("login.html")

# DASHBOARD
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# ADD BOOK
@app.route("/add-book", methods=["GET", "POST"])
def add_book():
    return render_template("add_book.html")

# ISSUE BOOK
@app.route("/issue-book", methods=["GET", "POST"])
def issue_book():
    return render_template("issue_book.html")

# VIEW BOOKS
@app.route("/view-books", methods=["GET", "POST"])
def issue_book():
    return render_template("view_books.html")

# LOGOUT,
@app.route("/logout")
def logout():
    return redirect(url_for("login"))


# MAIN 
if __name__ == "__main__":
    app.run(debug=True)

