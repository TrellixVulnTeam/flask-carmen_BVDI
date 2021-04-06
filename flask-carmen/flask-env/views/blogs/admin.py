from flask import request, redirect, url_for
from flask import render_template
from libs import db
from flask import Blueprint
from models import User, Post, Category, Link

admin_app = Blueprint("admin_app", __name__)


@admin_app.route('/newpost', methods=['get', 'post'])
def newPost():
    # form = LoginForm()
    # if request.method == "POST" and form.validate():
    if request.method == "POST":
        title = request.form['title']
        category = request.form['category']
        body = request.form['body']
        # age = request.form['age']
        post = Post(
            title=title,
            category=category,
            body=body,
            # age=age
        )
        db.session.add(post)
        db.session.commit()
        print(title, category, body)
    return render_template('admin/new_post.html')


@admin_app.route('/newcategory', methods=['get', 'post'])
def newCategory():
    # form = LoginForm()
    # if request.method == "POST" and form.validate():
    if request.method == "POST":
        # title = request.form['title']
        category = request.form['category']
        # body = request.form['body']
        # age = request.form['age']
        admin_category = Category(
            # title=title,
            category=category,
            # body=body,
            # age=age
        )
        db.session.add(admin_category)
        db.session.commit()
        print(admin_category)
    return render_template('admin/new_category.html')


@admin_app.route('/newlink', methods=['get', 'post'])
def newLink():
    # form = LoginForm()
    # if request.method == "POST" and form.validate():
    # links = Link.query.all()
    if request.method == "POST":
        link_name = request.form['link_name']
        link_url = request.form['link_url']
        admin_link = Link(
            link_name=link_name,
            link_url=link_url,
        )
        db.session.add(admin_link)
        db.session.commit()
        print(admin_link)
    # else:

        # return redirect(url_for("admin_app.blogList"), links=links)
    return render_template('admin/new_link.html')


@admin_app.route("/bloglist", methods=['get', 'post'])
def blogList():
    links = Link.query.all()

    return redirect("admin/blog.html", links=links)