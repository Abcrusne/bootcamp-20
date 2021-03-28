import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

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
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""


    # rows = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])
    # if not rows:
    #     return apology("Missing user")
    # cash = rows[0]["cash"]
    # total = cash
    # stocks = db.execute( "SELECT symbol, SUM(shares) AS shares FROM transactions WHERE user_id = :user_id GROUP BY symbol HAVING SUM (shares) > 0", user_id=session["user_id"])

    # for stock in stocks:
    #     quote =lookup(stock["symbol"])
    #     stock["name"] = quote["name"]
    #     stock["price"] = quote["price"]
    #     total += stock["shares"] * quote["price"]

    # return render_template("index.html", cash=cash, stocks=stocks, total=total)
    users = db.execute("SELECT cash FROM users WHERE id = :user_id", user_id=session["user_id"])
    stocks = db.execute(
        "SELECT symbol, SUM(shares) AS total_shares FROM transactions WHERE user_id = :user_id GROUP BY symbol HAVING total_shares > 0", user_id=session["user_id"])
    quotes = {}

    for stock in stocks:
        quotes[stock["symbol"]] = lookup(stock["symbol"])

    cash = users[0]["cash"]
    total = cash

    return render_template("portfolio.html", quotes=quotes, stocks=stocks, total=total, cash=cash)

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology("Missing Symbol.")
        elif not request.form.get("shares"):
            return apology ("Missing Shares.")
        elif not request.form.get("shares").isdigit():
            return apology ("Write a positive integer of shares.")
        quote = lookup(request.form.get("symbol"))
        shares = int(request.form.get("shares"))
        if not quote:
            return apology("Invalid Symbol")
        if not shares:
            return apology("Too few shares.")

        # SELECT how much cash the user currently has in users
        rows = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])
        if not rows:
            return apology("Missing user.")
        # check current cash which have user
        cash = rows[0]["cash"]
        # price of shares
        cost = quote["price"] * shares
        if cost > cash:
            return apology("You do not have enough cash.")
# record purchase
        db.execute("""INSERT INTO transactions (user_id, symbol, shares, price) VALUES(:user_id, :symbol, :shares, :price)""",
                  user_id=session["user_id"],
                  symbol=quote["symbol"],
                  shares=shares,
                  price=quote["price"])
# updatint lentele
        db.execute("UPDATE users SET cash = cash - :cost WHERE id = :id", cost=cost, id=session["user_id"])
        flash ("You have bought!")
        # display portfolio
        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""


    rows = db.execute("SELECT symbol, shares, price, transacted FROM transactions WHERE user_id=:user_id ORDER BY transacted ASC", user_id = session["user_id"])
    # for transaction in transactions:
    #     quote=lookup(request.form.get("symbol"))


    return render_template("history.html", rows=rows)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

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


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology("Missing Symbol")
        # get stock price
        quote = lookup(request.form.get("symbol"))
        if not quote:
            return apology("Invalid Symbol")

        return render_template("quoted.html", quote = quote)
    else:
        return render_template("quote.html")



@app.route("/register", methods=["GET", "POST"])
def register():

    # """Register user"""
    if request.method == "POST":
        if not request.form.get("username"):
            return apology (" Username is required")
        elif not request.form.get("password"):
            return apology (" Password is required")
        elif len(request.form.get("password")) < 2:
            return apology ("Minimal password length is 2.")
        elif request.form.get("password") !=  request.form.get("confirm"):
             return apology (" Passwords must match")
        elif not request.form.get("confirm"):
            return apology (" Confirmation is required")

            #  add username into database
        id =  db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)",
                         username = request.form.get("username"),
                         hash = generate_password_hash(request.form.get("password")))
        if not id:
            return apology(" Username already exist")

# log user in
        session["user_id"] = id

        flash ("Successfully registered!")
        return redirect ("/")
# Get
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology("Missing Symbol.")
        symbol = request.form.get("symbol").isupper()
        if not request.form.get("shares"):
            return apology ("Missing Shares.")
        elif not request.form.get("shares").isdigit():
            return apology ("Write a positive integer of shares.")
        quote = lookup(request.form.get("symbol"))
        shares = int(request.form.get("shares"))
        if shares < 1:
            return apology("Invalid shares.")

        if not quote:
            return apology("Invalid Symbol")
        if not shares:
            return apology("Too few shares.")
        # check if there is enough shares
        stock = db.execute("SELECT SUM(shares) as total FROM transactions WHERE user_id=:user_id AND symbol = :symbol GROUP BY symbol",
                          user_id=session["user_id"], symbol=request.form.get("symbol"))
        if len(stock) != 1 or stock[0]["total"] <= 0 or stock[0]["total"] < shares:
            return apology("You cannot buy less than 0 shares and sell more than you have.")

        # SELECT how much cash the user currently has in users
        rows = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])
        if not rows:
            return apology("Missing user.")
        # check current cash which have user
        cash = rows[0]["cash"]
        # price of shares
        cost = quote["price"] * shares

# record purchase
        db.execute("""INSERT INTO transactions (user_id, symbol, shares, price) VALUES(:user_id, :symbol, :shares, :price)""",
                  user_id=session["user_id"],
                  symbol=quote["symbol"],
                  shares=-shares,
                  price=quote["price"])
# updatint lentele
        db.execute("UPDATE users SET cash = cash + :value WHERE id = :id", value=shares * quote["price"], id=session["user_id"])
        flash ("You have sold!")
        # display portfolio
        return redirect("/")

    else:
        rows = db.execute("SELECT symbol FROM transactions WHERE user_id = :user_id GROUP BY symbol HAVING SUM(shares) > 0", user_id = session["user_id"])
        symbols = [row["symbol"] for row in rows]
        return render_template("sell.html", symbols = symbols)



@app.route("/change", methods=["GET", "POST"])
@login_required
def change():

    # User reached route via POST (as by submitting a form via POST)
    # let user to change his/her password
    if request.method == "POST":

        # Ensure old password was submitted
        if not request.form.get("oldpassword"):
            return apology("must provide your old password")

        # Query database for user_id
        rows = db.execute("SELECT hash FROM users WHERE id = :user_id", user_id=session["user_id"])

        # Ensure current password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("oldpassword")):
            return apology("Your old password is incorrect.")

        # Ensure new password is not empty
        if not request.form.get("newpassword"):
            return apology("Provide new password.")

        # Ensure new password is confirmed
        elif not request.form.get("newpassword_confirm"):
            return apology("Confirm new password")

        # Ensure new password and confirmed matches
        elif request.form.get("newpassword") != request.form.get("newpassword_confirm"):
            return apology("New password and confirmed must match.")

        # Update database
        hash = generate_password_hash(request.form.get("newpassword"))
        rows = db.execute("UPDATE users SET hash = :hash WHERE id = :user_id", user_id=session["user_id"], hash=hash)

        # Show flash
        flash("Password is changed!")

    else:
        return render_template("change.html")



def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
