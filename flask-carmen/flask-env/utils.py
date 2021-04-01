# import app
import click
# from flask import app
from app import app
from libs import db
from models import User, Message
import random


def createBatchUsers():
    words = list("abcdefghijklmnopqrstuvwxyz")

    for i in range(30):
        username = "".join(words[:6])
        random.shuffle(username)
        password = "123456"
        random.shuffle(password)
        sex = random.randint(0, 1)
        age = random.randint(15, 50)
        user = User(
            username=username,
            password=password,
            sex=sex,
            age=age
        )
        db.session.add(user)
    db.session.commit()
