from flask import Flask, Blueprint, render_template, redirect, url_for, request, make_response, Response, jsonify
from util import validate_user, db_write
from localStoragePy import localStoragePy

app = Flask(__name__)

localStorage = localStoragePy('flask_arch','json')


@app.route("/register", methods=["GET", "POST"])
def register_user():
    if request.method == 'POST':
        user_email = request.form["email"]
        user_password = request.form["password"]
        if user_password:
            if db_write([user_email, user_password], "auth"):
                # Registration Successful
                return redirect(url_for('login_user'))
            else:
                # Registration Failed
                return render_template('register.html', msg = "Registration Failed. Try Again!")
        else:
            # Registration Failed
            return render_template('register.html', msg = "Registration Failed. Try Again!")
    return render_template('register.html')

@app.route("/login", methods=["GET","POST"])
def login_user():
    if request.method == 'POST':
        user_email = request.form["email"]
        user_password = request.form["password"]
        user_token = validate_user(user_email, user_password)
        localStorage.setItem("token", user_token)
        if user_token:
            return "Login Success!"
        else:
            # Registration Failed
            return render_template('login.html', msg = "Incorrect Credentials!")
    return render_template('login.html')