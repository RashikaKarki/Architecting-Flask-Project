from flask import Blueprint, render_template, redirect, url_for, request, make_response, Response, jsonify
from util import validate_user, db_write
from localStoragePy import localStoragePy

localStorage = localStoragePy('flask_arch','json')

authentication = Blueprint("authentication", __name__,     template_folder='template', static_folder='static')

@authentication.route("/register", methods=["GET", "POST"])
def register_user():
    if request.method == 'POST':
        user_email = request.form["email"]
        user_password = request.form["password"]
        if user_password:
            if db_write([user_email, user_password], "auth"):
                # Registration Successful
                return redirect(url_for('authentication.login_user'))
            else:
                # Registration Failed
                return render_template('register.html', msg = "Registration Failed. Try Again!")
        else:
            # Registration Failed
            return render_template('register.html', msg = "Registration Failed. Try Again!")
    return render_template('register.html')

@authentication.route("/login", methods=["GET","POST"])
def login_user():
    if request.method == 'POST':
        user_email = request.form["email"]
        user_password = request.form["password"]
        user_token = validate_user(user_email, user_password)
        localStorage.setItem("token", user_token)
        if user_token:
            return redirect(url_for('user_post.view'))
        else:
            # Registration Failed
            return render_template('login.html', msg = "Incorrect Credentials!")
    return render_template('login.html')