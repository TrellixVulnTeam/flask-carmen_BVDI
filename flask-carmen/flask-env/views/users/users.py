from flask import request, redirect, url_for
from flask import render_template
from libs import db
from flask import Blueprint
from models import User


user_app = Blueprint("user_app", __name__)


@user_app.route('/register', methods=['get', 'post'])
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


@user_app.route("/userlist", methods=['get', 'post'])
def userList():
    if request.method == "POST":
        input_username = request.form['username']
        # if not input_username:
        condition = {request.form['field']: input_username}
        print(condition)
        # filter_by
        users = User.query.filter_by(**condition).all()
        if not input_username:
            users = User.query.all()
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
        page = request.args.get('page')
        if page is not None:
            # users = User.query.paginate(1, 10)
            users = User.query.paginate(int(page), 10)
        else:
            users = User.query.paginate(1, 10)
        # users = User.query.all()

    # return render_template("user/user_list.html", users=users)
    return render_template("user/user_list.html", users=users.items,
                           pages=users.pages,  # 总页数
                           total=users.total,  # 总条数
                           pageList=users.iter_pages(),  # 自动分页
                           next_num=users.next_num,  # 下一页
                           prev_num=users.prev_num  # 上一页
                           )


@user_app.route("/user_delete/<int:user_id>")
def deleteUser(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("user_app.userList"))


@user_app.route("/edituser/<int:user_id>", methods=['get', 'post'])
def editUser(user_id):
    user = User.query.get(user_id)
    if request.method == "POST":
        user.username = request.form['username']
        user.password = request.form['password']
        # sex = request.form['sex']
        user.age = request.form['age']
        # db.session.add(user)
        db.session.commit()
        return redirect(url_for("user_app.userList"))
    return render_template("user/edit_user.html", user=user)