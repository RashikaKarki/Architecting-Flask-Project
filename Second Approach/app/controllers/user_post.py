from flask import Blueprint, render_template, redirect, url_for, request
from util import db_write, get_posts
from localStoragePy import localStoragePy

user_post = Blueprint("user_post", __name__)

localStorage = localStoragePy('flask_arch', 'json')

@user_post.route("/upload_post", methods=["GET", "POST"])
def upload():
    user_email = localStorage.getItem("token")
    if user_email ==  None:
        return redirect(url_for('authentication.login_user'))
    if request.method == 'POST':
        post = request.form["post"]
        if db_write([user_email, post], "posts"):
            return redirect(url_for('user_post.view'))
        else:
            return render_template('post/upload_post.html', msg = "Upload Failed!", user = user_email)
    return render_template('post/upload_post.html', user = user_email)

@user_post.route("/view_post", methods=["GET"])
def view():
    user_email = localStorage.getItem("token")
    print(user_email)
    if user_email ==  None:
        return redirect(url_for('authentication.login_user'))
    data = get_posts()
    return render_template('post/view_post.html', data = data, user = user_email)
