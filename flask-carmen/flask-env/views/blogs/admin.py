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
    categorys = Category.query.all()
    if request.method == "POST":
        title = request.form['title']
        category_name = request.form['category_name']
        body = request.form['body']
        # age = request.form['age']
        post = Post(
            title=title,
            category=category_name,
            body=body,
            # age=age
        )
        db.session.add(post)
        db.session.commit()
        # print(title, category_name, body)
    return render_template('admin/new_post.html', categorys=categorys)


@admin_app.route('/newcategory', methods=['get', 'post'])
def newCategory():
    # form = LoginForm()
    # if request.method == "POST" and form.validate():
    if request.method == "POST":
        # title = request.form['title']
        category_name = request.form['category_name']
        # body = request.form['body']
        # age = request.form['age']
        admin_category = Category(
            # title=title,
            category_name=category_name,
            # body=body,
            # age=age
        )
        db.session.add(admin_category)
        db.session.commit()
        print(admin_category)
    return render_template('admin/new_category.html')


@admin_app.route('/newlink', methods=['get', 'post'])
def newLink():

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
    return render_template('admin/new_link.html')


@admin_app.route('/managepost', methods=['get', 'post'])
def managePost():
    # blog_posts = Post.query.all()
    page = request.args.get('page')
    if page is not None:
        # users = User.query.paginate(1, 10)
        posts = Post.query.paginate(int(page), 10)
        # users = User.query.all()
    else:
        posts = Post.query.paginate(1, 10)

    # return render_template("user/user_list.html", users=users)
    return render_template("admin/manage_post.html", posts=posts.items,
                           pages=posts.pages,  # 总页数
                           total=posts.total,  # 总条数
                           pageList=posts.iter_pages(),  # 自动分页
                           next_num=posts.next_num,  # 下一页
                           prev_num=posts.prev_num  # 上一页
                           )
    # return render_template('admin/manage_post.html', blog_posts=blog_posts)

    # paginate分页设置
    # page = request.args.get('page')
    # users = User.query.paginate(int(page), 10)
    # # users = User.query.all()
    #
    # # return render_template("user/user_list.html", users=users)
    # return render_template("admin/manage_post.html", users=users.items,
    #                        pages=users.pages,  # 总页数
    #                        total=users.total,  # 总条数
    #                        pageList=users.iter_pages()  # 自动分页
    #                        )


@admin_app.route('/managecategory', methods=['get', 'post'])
def manageCategory():
    return render_template('admin/manage_category.html')


@admin_app.route('/managelink', methods=['get', 'post'])
def manageLink():
    # links = Link.query.all()
    page = request.args.get('page')
    if page is not None:
        # users = User.query.paginate(1, 10)
        links = Link.query.paginate(int(page), 10)
        # users = User.query.all()
    else:
        links = Link.query.paginate(1, 10)

    # return render_template("user/user_list.html", users=users)
    return render_template("admin/manage_link.html", links=links.items,
                           pages=links.pages,  # 总页数
                           total=links.total,  # 总条数
                           pageList=links.iter_pages(),  # 自动分页
                           next_num=links.next_num,  # 下一页
                           prev_num=links.prev_num  # 上一页
                           )
    # return render_template('admin/manage_link.html', links=links)


@admin_app.route("/editpost/<int:post_id>", methods=['get', 'post'])
def editPost(post_id):
    post = Post.query.get(post_id)
    categorys = Category.query.all()
    if request.method == "POST":
        post.title = request.form['title']
        post.category = request.form['category_name']
        post.body = request.form['body']
        # db.session.add(user)
        db.session.commit()
        return redirect(url_for("admin_app.managePost"))
    return render_template("admin/edit_post.html", post=post, categorys=categorys)


@admin_app.route("/post_delete/<int:post_id>")
def deletePost(post_id):
    blog_post = Post.query.get(post_id)
    db.session.delete(blog_post)
    db.session.commit()
    return redirect(url_for("admin_app.managePost"))


@admin_app.route("/editlink/<int:link_id>", methods=['get', 'post'])
def editLink(link_id):
    link = Link.query.get(link_id)
    if request.method == "POST":
        link.link_name = request.form['link_name']
        link.link_url = request.form['link_url']
        # db.session.add(user)
        db.session.commit()
        return redirect(url_for("admin_app.manageLink"))
    return render_template("admin/edit_link.html", link=link)


@admin_app.route("/link_delete/<int:link_id>")
def deleteLink(link_id):
    blog_link = Link.query.get(link_id)
    db.session.delete(blog_link)
    db.session.commit()
    return redirect(url_for("admin_app.manageLink"))