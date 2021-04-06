from flask import request, redirect, url_for
from flask import render_template
from libs import db
from flask import Blueprint
from models import User


auth_app = Blueprint("auth_app", __name__)


@auth_app.route('/blog-register', methods=['get', 'post'])
def blog_register():
    # form = LoginForm()
    # if request.method == "POST" and form.validate():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        # sex = request.form['sex']
        # age = request.form['age']
        user = User(
            username=username,
            password=password,
            # sex=sex,
            # age=age
        )
        db.session.add(user)
        db.session.commit()
        print(username, password)
    return render_template('auth/auth_login.html')