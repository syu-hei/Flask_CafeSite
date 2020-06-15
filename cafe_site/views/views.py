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