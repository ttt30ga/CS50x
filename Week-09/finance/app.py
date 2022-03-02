import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    # Create new database table to store all transactions
    db.execute("CREATE TABLE IF NOT EXISTS transactions (user_id INT, t_type TEXT NOT NULL, symbol TEXT NOT NULL, name TEXT NOT NULL, shares NUMERIC NOT NULL, t_price NUMERIC NOT NULL, t_value NUMERIC NOT NULL, t_date NUMERIC NOT NULL)")

    # Get values
    user = db.execute("SELECT username, cash FROM users WHERE id = ?", session["user_id"])[0]
    portfolio = db.execute(
        "SELECT t_type, UPPER(symbol) AS symbol, name, SUM(CASE WHEN t_type = 'buy' THEN shares WHEN t_type = 'sell' THEN - shares ELSE 0 END) AS shares, t_price, SUM(t_value) AS value FROM transactions WHERE user_id = ? GROUP BY symbol", session["user_id"])

    balance = user["cash"]

    if not portfolio:
        return render_template("index.html", user=user)

    # For each stock calculate the numbers of shares owned, the current price of each stock, the total value of each holding
    for stocks in portfolio:
        # Current price
        price = lookup(stocks["symbol"])["price"]
        # Current value
        value = stocks["shares"] * price
        balance += value
        invested = balance - user["cash"]
        stocks.update({"price": price, "value": value})

    return render_template("index.html", user=user, portfolio=portfolio, price=price, value=value, invested=invested, balance=balance)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    if request.method == "POST":

        # Get values
        get_symbol = request.form.get("symbol")
        get_shares = request.form.get("shares")
        t_type = "buy"
        t_date = datetime.now()
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])

        # Ensure symbol was submitted
        if not get_symbol:
            return apology("must provide symbol")

        # Ensure symbol exists
        if not lookup(get_symbol) or lookup(get_symbol) == None:
            return apology("stock not found")

        # Ensure quantity was submitted and amount is positive
        if not get_shares or get_shares.isnumeric() != True:
            return apology("must provide an amount of shares")
        try:
            int(get_shares)
        except ValueError:
            return apology("must provide a positive amount")

        # Check user has enough cash
        t_price = lookup(get_symbol)["price"]
        t_value = t_price * int(get_shares)
        if cash[0]["cash"] < t_value:
            return apology("you don't have enough cash")
        else:
            # Update table with purchased stocks and Update user cash
            name = lookup(get_symbol)["name"]
            update_cash = cash[0]["cash"] - t_value
            db.execute("UPDATE users SET cash = ?", update_cash)
            db.execute("INSERT INTO transactions (user_id, t_type, symbol, name, shares, t_price, t_value, t_date) VALUES(?, ?, ?, ?, ?, ?, ?, ?)",
                       session["user_id"], t_type, get_symbol, name, get_shares, t_price, t_value, t_date)

        # Redirect user to index page
        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    # Get values
    transactions = db.execute(
        "SELECT t_type, UPPER(symbol) AS symbol, name, shares, t_price, t_value, t_date FROM transactions WHERE user_id = ?", session["user_id"])

    if not transactions:
        return apology("you have no transactions history")

    return render_template("history.html", transactions=transactions)


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
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

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

        # Get values
        get_symbol = request.form.get("symbol")
        stock = lookup(get_symbol)

        # Ensure symbol was submitted
        if not get_symbol:
            return apology("must provide symbol")

        # Ensure symbol exists
        elif not stock:
            return apology("stock not found")

        # Display stocks
        else:
            return render_template("quoted.html", stock=stock)

    else:
        return render_template("quote.html", stock=None)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Get values
        get_username = request.form.get("username")
        get_password = request.form.get("password")
        get_confirm_password = request.form.get("confirmation")
        cash_default = 10000.00
        hashed_password = generate_password_hash(get_password)

        # Ensure username was submitted
        if not get_username:
            return apology("must provide username")

        # Ensure password was submitted
        elif not get_password:
            return apology("must provide password")

        # Ensure confirm password was submitted
        elif not get_confirm_password:
            return apology("must confirm password")

        # Ensure password and confirm password match
        elif get_password != get_confirm_password:
            return apology("passwords must match")

        # Query database for existing username
        rows = db.execute("SELECT * FROM users WHERE username = ?", get_username)

        # Ensure username exists and password is correct
        if len(rows) > 0:
            return apology("User already registered")

        # Insert in database
        user = db.execute("INSERT INTO users (username, hash, cash) VALUES(?, ?, ?)", get_username, hashed_password, cash_default)

        # Remember which user has logged in
        session["user_id"] = user

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    portfolio = db.execute("SELECT symbol FROM transactions WHERE user_id = ? GROUP BY symbol", session["user_id"])

    if request.method == "POST":

        # Get values
        get_symbol = request.form.get("symbol")
        get_shares = request.form.get("shares")
        name = lookup(get_symbol)["name"]
        t_price = lookup(get_symbol)["price"]
        t_type = "sell"
        t_date = datetime.now()
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        transactions = db.execute(
            "SELECT symbol, shares FROM transactions WHERE user_id = ? AND symbol = ?", session["user_id"], get_symbol)

        # Ensure symbol was submitted
        if not get_symbol:
            return apology("must provide symbol")

        # Ensure shares amount is positive
        elif not get_shares or int(get_shares) <= 0:
            return apology("must provide a positive amount")

        # Ensure user has enough stocks
        shares_owned = transactions[0]["shares"]

        if int(get_shares) > shares_owned:
            return apology("you don't have enough stocks")
        else:
            # Update user cash, balance and transactions
            t_value = t_price * int(get_shares)
            update_cash = cash[0]["cash"] + t_value
            db.execute("UPDATE users SET cash = ?", update_cash)
            db.execute("INSERT INTO transactions (user_id, t_type, symbol, name, shares, t_price, t_value, t_date) VALUES(?, ?, ?, ?, ?, ?, ?, ?)",
                       session["user_id"], t_type, get_symbol, name, get_shares, t_price, t_value, t_date)

        # Redirect user to index page
        return redirect("/")

    else:
        return render_template("sell.html", portfolio=portfolio)
