from flask import request, redirect, url_for
from flask import render_template
from libs import db
from flask import Blueprint
from models import User


blog_app = Blueprint("blog_app", __name__)


@blog_app.route('/bloglist', methods=['get', 'post'])
def blogList():
    # # form = LoginForm()
    # # if request.method == "POST" and form.validate():
    # if request.method == "POST":
    #     username = request.form['username']
    #     password = request.form['password']
    #     # sex = request.form['sex']
    #     age = request.form['age']
    #     user = User(
    #         username=username,
    #         password=password,
    #         # sex=sex,
    #         age=age
    #     )
    #     db.session.add(user)
    #     db.session.commit()
    #     print(username, password)
    return render_template('blog/blog.html')
