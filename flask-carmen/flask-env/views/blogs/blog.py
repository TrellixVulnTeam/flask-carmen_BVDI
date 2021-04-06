from flask import request, redirect, url_for
from flask import render_template
from libs import db
from flask import Blueprint
from models import Link, Post

blog_app = Blueprint("blog_app", __name__)


@blog_app.route('/bloglist', methods=['get', 'post'])
def blogList():
    blog_posts = Post.query.all()
    links = Link.query.all()
    return render_template('blog/blog.html', links=links, blog_posts=blog_posts)
