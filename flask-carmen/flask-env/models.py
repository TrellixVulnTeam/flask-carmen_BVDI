from datetime import datetime

from libs import db


# 创建数据库Model结构
class User(db.Model):
    # db.Column()为创建字段，第一个参数为字段数据类型
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    sex = db.Column(db.String)
    age = db.Column(db.Integer)


class Author(db.Model):
    # db.Column()为创建字段，第一个参数为字段数据类型
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), unique=True)
    phone = db.Column(db.String(20))
    nickname = db.Column(db.String(20))
    like = db.Column(db.String(20))

    articles = db.relationship('Article')


class Article(db.Model):
    # db.Column()为创建字段，第一个参数为字段数据类型
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), index=True)
    body = db.Column(db.Text)

    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))


class Message(db.Model):
    # db.Column()为创建字段，第一个参数为字段数据类型
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(20))
    author_text = db.Column(db.String(200))

    timestamp = db.Column(db.DateTime, default=datetime.now, index=True)


class Post(db.Model):
    # db.Column()为创建字段，第一个参数为字段数据类型
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), index=True)
    category = db.Column(db.String(20))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)


class Category(db.Model):
    # db.Column()为创建字段，第一个参数为字段数据类型
    category_id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(20))


class Link(db.Model):
    link_id = db.Column(db.Integer, primary_key=True)
    link_name = db.Column(db.String(30))
    link_url = db.Column(db.String(255))