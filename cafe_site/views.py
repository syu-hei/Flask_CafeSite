from flask import request, redirect, url_for, render_template, flash, session
from cafe_site import app




@app.route('/')
def index():
     return render_template('cafe_site/index.html', id="home")



@app.route('/menu')
def menu():
     return render_template('cafe_site/menu.html', id="menu")



@app.route('/news')
def news():
     return render_template('cafe_site/news.html', id="news")



@app.route('/contact')
def contact():
     return render_template('cafe_site/contact.html', id="contact")



@app.route('/review', methods=['GET'])
def review():
     return render_template('cafe_site/review.html', id="review")



@app.route('/review', methods=['POST'])
def view_board():
     if request.form['star'] and request.form['title'] and request.form['review']:
          return render_template('cafe_site/review.html',  name=app.config['USERNAME'], star=request.form['star'], title=request.form['title'], review=request.form['review'])



@app.route('/review')
def show_entries():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('cafe_site/review.html')


@app.route('/login', methods=['GET', 'POST'])
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
            return redirect(url_for('show_entries'))
    return render_template('login.html')



@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('ログアウトしました')
    return redirect(url_for('show_entries'))