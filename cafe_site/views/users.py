from flask import request, redirect, url_for, render_template, flash, session
from cafe_site import app
from cafe_site import db
from cafe_site.models.users import User
from cafe_site.views.loging import login_required
from flask import Blueprint


user = Blueprint('user', __name__)


@user.route('/users', methods=['POST'])
def add_user():
    user = User(
            username=request.form['username'],
            password=request.form['password']
            )
    db.session.add(user)
    db.session.commit()
    flash('新規ユーザ登録が完了しました。ログインしてください。')
    return redirect(url_for('loging.login'))


@user.route('/users/new', methods=['GET'])
def new_user():
    return render_template('users/new.html', id='user')