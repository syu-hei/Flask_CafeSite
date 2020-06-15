from flask import request, redirect, url_for, render_template, flash, session
from cafe_site import app
from functools import wraps
from flask import Blueprint

loging = Blueprint('loging', __name__)

def login_required(loging):
    @wraps(loging)
    def inner(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('loging.login'))
        return loging(*args, **kwargs)
    return inner


@loging.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            flash('ユーザ名が異なります')
        elif request.form['password'] != app.config['PASSWORD']:
            flash('パスワードが異なります')
        else:
            session['logged_in'] = True
            flash('ログインしました')
            return redirect(url_for('review.show_reviews'))
    return render_template('login.html', id="login")



@loging.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('ログアウトしました')
    return redirect(url_for('review.show_reviews'))

@loging.app_errorhandler(404)
def non_existant_route(error):
    return redirect(url_for('loging.login'))