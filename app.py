import os
from flask import Flask, render_template, redirect, request, session
import sqlite3 as sq
from werkzeug.security import check_password_hash, generate_password_hash
import database as db


# Preparation ------------------------------------------------------------
app = Flask(__name__)
app.secret_key = os.urandom(24)

db = sq.connect("data/students_database.db")

######################################## HOME PAGE ########################################################
@app.route("/")
def homepage():
    return render_template("index.html")

######################################## LOGIN ########################################################
@app.route("/login", methods=["GET", "POST"])
def login():
    # forget any user ID 
    session.clear()

    if request.method == "POST":
        
        # check for user error
        if not request.form.get("student_id"):
            return render_template("login.html", error="Student ID is required!")

        elif not request.form.get("password"):
            return render_template("login.html", error="Password is missing!")
        
        # Query database for username 

        # Ensure username exists and password is correct

        # Remember which user has logged in

        # Redirect user to home page

        # User reached route via GET (as by clicking a link or via redirect)
        return redirect("/")

    else:
        return render_template("login.html")
    
######################################## REGISTER ########################################################
@app.route("/register", methods=["GET","POST"])
def register():
    session.clear

    if request.method == "POST":
        username = request.form.get("student_id")
        password = request.form.get("password")
        password_confirm = request.form.get("password_confirm")

        if not username:
            render_template("register.html", error="Must input Student ID")
        if not password:
            render_template("register.html", error="Must input Password")
        if password_confirm != password:
            render_template("register.html", error="Password does not match")

        hashed_password = generate_password_hash(password)

        # insert new password and id into database

        
######################################## RUN FLASK ########################################################
if __name__ == "__main__":
    app.run(debug=True)