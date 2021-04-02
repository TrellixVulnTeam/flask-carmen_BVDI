from flask import request, redirect, url_for
from flask import render_template, flash
from libs import db
from models import Message
from flask import Blueprint

message_app = Blueprint("message_app", __name__)


@message_app.route("/sayhello", methods=['get', 'post'])
def sayHello():
    if request.method == "POST":
        author = request.form['author']  # 承接前端author字段传参过来的数据
        author_text = request.form['author-text']
        print(author, author_text)
        message = Message(
            author=author,
            author_text=author_text
        )
        db.session.add(message)  # 将数据提交到缓冲区
        db.session.commit()  # 提交到数据库
        flash("提交成功了~~~你的话全世界都知道啦")
        #     # sex = request.form['sex']
        #     user.age = request.form['age']
        #     # db.session.add(user)
        #     db.session.commit()
        return redirect(url_for("message_app.messageList"))  # 重定向到message展示页
    return render_template("board-item/say-hello.html")  # 确定使用的前端模版


@message_app.route("/messagelist", methods=['get', 'post'])
def messageList():
    # 加载所有的记录，这里使用逆序排列
    messages = Message.query.order_by(Message.timestamp.desc()).all()

    return render_template("board-item/say-hello.html", messages=messages)