from flask import Flask, request, redirect, url_for, abort, jsonify, make_response
from flask import render_template
from jinja2 import escape

# app是一个符合wsgi接口协议的python程序对象
# 服务器可以将用户的访问请求数据发送给这个app
app = Flask(__name__)


@app.route('/home', methods=('GET',))
def home():
    lists = [
        {"title": "头条新闻", "intro": "XXXXXXXXX"},
        {"title": "头条新闻", "intro": "XXXXXXXXX"},
        {"title": "头条新闻", "intro": "XXXXXXXXX"},
    ]
    return render_template("index/home.html", newsLists=lists)


@app.route('/', methods=('GET',))
def index():
    # print("hello")
    return render_template("index/index.html")


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


@app.route('/hello', methods=('GET',))
def hello():
    # print("hello")
    # name = request.args.get('name', 'Flask')
    name = request.args.get('name')
    if name is None:
        name = request.cookies.get('name','Human')
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

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
