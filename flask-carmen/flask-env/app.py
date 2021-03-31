from flask import Flask, request, redirect, url_for, abort, jsonify, make_response
from flask import render_template, flash
from jinja2 import escape
from flask_migrate import Migrate
from flask_mail import Mail
from libs import db
import click

# app是一个符合wsgi接口协议的python程序对象
# 服务器可以将用户的访问请求数据发送给这个app
from models import User

app = Flask(__name__)
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


# @app.cli.command()
# def initdb():
#     db.create_all()
#     click.echo("Initialized database.")


@app.route('/', methods=('GET',))
def index():
    return render_template("index/index.html")


@app.route('/zen', methods=('GET',))
def zen():
    return render_template("index/zen.html")


# @app.route('/index', methods=('GET',))
# def index():
#     return render_template("index/index.html")


@app.route('/home', methods=('GET',))
def home():
    lists = [
        {"title": "头条新闻", "intro": "XXXXXXXXX"},
        {"title": "头条新闻", "intro": "XXXXXXXXX"},
        {"title": "头条新闻", "intro": "XXXXXXXXX"},
    ]
    # 左边的newsLists代表传入模板变量名称，lists则是要出入的对象
    return render_template("index/home.html", newsLists=lists)


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


@app.route('/register', methods=['get', 'post'])
def register():
    # form = LoginForm()
    # if request.method == "POST" and form.validate():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        # sex = request.form['sex']
        age = request.form['age']
        user = User(
            username=username,
            password=password,
            # sex=sex,
            age=age
        )
        db.session.add(user)
        db.session.commit()
        print(username, password)
    return render_template('index/register.html')


@app.route("/userlist", methods=['get', 'post'])
def userList():
    if request.method == "POST":
        input_username = request.form['username']
        condition = {request.form['field']: input_username}
        # filter_by
        users = User.query.filter_by(**condition).all()
        # filter
        # if request.form['field'] == "id":
        #     condition = User.id.like('%%%s%%' % input_username)
        # elif request.form['field'] == "username":
        #     condition = User.username.like('%%%s%%' % input_username)
        # elif request.form['field'] == "age":
        #     condition = User.age.like('%%%s%%' % input_username)

        # if request.form['order'] == "1":
        #     order = User.id.asc()
        # else:
        #     order = User.id.desc()

        # users = User.query.filter(condition).order_by(order).all()
        # users = User.query.filter(condition).all()

    else:
        # paginate分页设置
        # page = request.args.get('page')
        # users = User.query.paginate(int(page), 10)
        users = User.query.all()

    return render_template("user/user_list.html", users=users)
    # return render_template("user/user_list.html", users=users.items,
    #                        pages=users.pages,  # 总页数
    #                        total=users.total,  # 总条数
    #                        pageList=users.iter_pages()  # 自动分页
    #                        )


@app.route("/user_delete/<int:user_id>")
def deleteUser(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("userList"))


@app.route("/editedit/<int:user_id>", methods=['get', 'post'])
def editUser(user_id):
    user = User.query.get(user_id)
    if request.method == "POST":
        user.username = request.form['username']
        user.password = request.form['password']
        # sex = request.form['sex']
        user.age = request.form['age']
        # db.session.add(user)
        db.session.commit()
        return redirect(url_for("userList"))
    return render_template("user/edit_user.html", user=user)


@app.route('/hello', methods=('GET',))
def hello():
    # print("hello")
    # name = request.args.get('name', 'Flask')
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


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
