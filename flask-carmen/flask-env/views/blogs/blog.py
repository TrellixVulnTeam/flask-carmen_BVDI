from flask import request, redirect, url_for
from flask import render_template
from libs import db
from flask import Blueprint
from models import Link, Post

blog_app = Blueprint("blog_app", __name__)


@blog_app.route('/bloglist', methods=['get', 'post'])
def blogList():
    # blog_posts = Post.query.order_by(Post.timestamp.desc()).all()
    links = Link.query.all()
    # page = request.args.get('page', 1, type(int))  # 从查询字符串获取当前页数
    # per_page = 10
    # pagination = Post.query.order_by(Post.timestamp.desc()).paginate(page, per_page)  # 分页对象
    # posts = pagination.items  # 当前页数的记录对象
    # return render_template('blog/blog.html', links=links, pagination=pagination, posts=posts)
    # else:
    # paginate分页设置
    # print(request.values.get("page"))
    page = request.args.get('page')
    if page is not None:
        # users = User.query.paginate(1, 10)
        posts = Post.query.paginate(int(page), 10)
        print(posts.next_num, posts.prev_num)
        # users = User.query.all()
    else:
        posts = Post.query.paginate(1, 10)

    # return render_template("user/user_list.html", users=users)
    return render_template("blog/blog.html", links=links, posts=posts.items,
                           pages=posts.pages,  # 总页数
                           total=posts.total,  # 总条数
                           pageList=posts.iter_pages(),  # 自动分页
                           next_num=posts.next_num,  # 下一页
                           prev_num=posts.prev_num  # 上一页
                           )
