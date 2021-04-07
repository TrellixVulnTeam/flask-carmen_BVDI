from flask import Flask, request, redirect, url_for, abort, jsonify, make_response
from flask import render_template, flash
from jinja2 import escape
from flask_migrate import Migrate
from flask_mail import Mail
from libs import db
from models import Message, Post
import click
from views.blogs.admin import admin_app
from views.blogs.auth import auth_app
from views.blogs.blog import blog_app
from views.messages.messages import message_app
from views.users.users import user_app

app = Flask(__name__)
app.register_blueprint(user_app, url_prefix="/user")
app.register_blueprint(message_app, url_prefix="/message")
app.register_blueprint(blog_app, url_prefix="/blog")
app.register_blueprint(auth_app, url_prefix="/auth")
app.register_blueprint(admin_app, url_prefix="/admin")


# app是一个符合wsgi接口协议的python程序对象
# 服务器可以将用户的访问请求数据发送给这个app
# app = Flask(__name__)
app.secret_key = 'secret string'
# 配置数据库
# 变更后是否追踪，这里默认为True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# cms.db为数据库名字
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///cms.db"
# 实例化数据库名称为db
db.init_app(app)

migrate = Migrate(app, db)
mail = Mail(app)


@app.route('/', methods=('GET',))
def index():
    return render_template("index/index.html")


@app.route('/zen', methods=('GET',))
def zen():
    return render_template("index/zen.html")


@app.route('/schedule', methods=('GET',))
def schedule():
    # print("hello")
    return render_template("index/schedule.html")


@app.route('/sun', methods=('GET',))
def sun():
    # print("hello")
    return render_template("index/sun.html")


@app.route('/crystal', methods=('GET',))
def crystal():
    # print("hello")
    return render_template("index/crystal.html")


@app.route('/form')
def form():
    return render_template('index/form.html')


@app.route('/hello', methods=('GET',))
def hello():
    name = request.args.get('name')
    if name is None:
        name = request.cookies.get('name', 'Human')
    return '<h1>Hello, %s! <script>alert("nihao!!")</script></h1>' % escape(name)


@app.route('/getyear', methods=('GET',))
def getyear():
    # print("hello")
    # name = request.args.get('name', 'Flask')
    # return '<h1>Hello, %s!</h1>' % (2021-year)# 根据int转换器得出计算年限
    # return '', 302, {'Location':'http://www.lixf6.com:5000'}# 重定向到制定网址
    # return redirect('http://www.lixf6.com:5000')# 重定向到制定网址
    return redirect(url_for('hello'))  # 重定向到hello视图函数


@app.route('/404')
def not_found():
    abort(404)


@app.route('/foo')
def foo():
    return jsonify(name='Li Xuefu', gender="muzi")


@app.route('/set/<name>')
def set_cookie(name):
    response = make_response(redirect(url_for('hello')))
    response.set_cookie('name', name)
    return response


@app.route('/flash')
def just_flash():
    flash('I am flash')
    return redirect(url_for('index'))


@app.cli.command()
@click.option('--count', default=10, help='create messages, default is 10')
def forge_say_hello(count):
    """创造留言板用户数据"""
    from faker import Faker
    fake = Faker()  # 用来创造虚拟数据的faker实例
    click.echo("Working...")
    for i in range(count):
        message = Message(
            author=fake.name(),
            author_text=fake.sentence(),
            timestamp=fake.date_time_this_year()
        )
        db.session.add(message)
    db.session.commit()
    click.echo("Created %s fake messages" % count)


@app.cli.command()
@click.option('--count', default=10, help='create posts, default is 10')
def forge_new_post(count):
    """创造Post数据"""
    from faker import Faker
    import random
    fake = Faker()  # 用来创造虚拟数据的faker实例
    click.echo("Working...")
    lst = ["Pride", "Envy", "Wrath", "Sloth", "Greed", "Gluttony", "Lust"]
    for i in range(count):
        post = Post(
            title=fake.name(),
            body=fake.sentence(),
            category=random.choice(lst),
            timestamp=fake.date_time_this_year()
        )
        db.session.add(post)
    db.session.commit()
    click.echo("Created %s fake posts" % count)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
