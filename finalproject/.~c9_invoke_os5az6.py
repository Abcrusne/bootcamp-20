import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import login_required, apology

# from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
# app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///information.db")

@app.route("/")
def index():

    return render_template("layout.html")

@app.route("/menu", methods=["GET", "POST"])
@login_required
def menu():
    if request.method == "POST":
        if not request.form.get("meal"):
            return ("Missing Meal.")
        elif not request.form.get("amount"):
            return ("Missing Amount.")
        elif not request.form.get("amount").isdigit():
            return ("Write a positive integer of amount.")
        amount = int(request.form.get("amount"))
        if amount < 0:
            return ("Invalid amount")
        if not amount:
            return ("Too few amount.")
        meal = request.form.get("meal")
        print(meal);
#    SELECT meal and price from menu
        rows = db.execute("SELECT meal, price FROM menu")
        for row in rows:
            meals=row["meal"]
            price=row["price"]
        # meals = [row["meal"] for row in rows]
        # price = [row["price"] for row in rows]
         # cost of order
        cost = price * amount
        print(cost)
        db.execute("""INSERT INTO history  (user_id, meal, amount, cost) VALUES(:user_id, :meal, :amount, :cost) """,
                  user_id=session["user_id"],
                  meal=meal,
                  amount=amount,
                  cost = cost)
        # return render_template("menu.html", meals=meals, price=price)
        flash ("Successfully ordered!")
        return redirect ("/")


    else:
        # rows = db.execute("SELECT cost FROM history ")
        # cost = [row["cost"] for row in rows]
        # for row in rows:
        #     meals=row["meal"]
        #     price=row["price"]
        rows = db.execute("SELECT meal, price FROM menu")
        meals = [row["meal"] for row in rows]
        price = [row["price"] for row in rows]


        return render_template("menu.html", meals=meals, price=price)


@app.route("/menu", methods=["GET", "POST"])
@login_required
def menud():
    """Get stock quote."""
    if request.method == "POST":
        if not request.form.get("meal"):
            return apology("Missing Meal")
        meal =  request.form.get("meal")
        return render_template("menud.html", meal=meal)
    else:
        return render_template("menu.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return("must provide password")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():

    # """Register user"""
    if request.method == "POST":
        if not request.form.get("username"):
            return apology(" Username is required")
        elif not request.form.get("password"):
            return apology(" Password is required")
        elif len(request.form.get("password")) < 2:
            return apology("Minimal password length is 2.")
        elif request.form.get("password") !=  request.form.get("confirm"):
             return apology("Passwords must match")
        elif not request.form.get("confirm"):
            return apology(" Confirmation is required")

            #  add username into database
        id =  db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)",
                         username = request.form.get("username"),
                         hash = generate_password_hash(request.form.get("password")))
        if not id:
            return("Username already exist")

# log user in
        session["user_id"] = id

        flash ("Successfully registered!")
        return redirect ("/")
# Get
    else:
        return render_template("register.html")