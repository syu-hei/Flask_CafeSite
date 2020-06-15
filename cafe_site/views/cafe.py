from flask import render_template
from flask import Blueprint

cafe = Blueprint('cafe', __name__)

@cafe.route('/')
def index():
     return render_template('cafe_site/index.html', id="home")



@cafe.route('/menu')
def menu():
     return render_template('cafe_site/menu.html', id="menu")



@cafe.route('/news')
def news():
     return render_template('cafe_site/news.html', id="news")



@cafe.route('/contact')
def contact():
     return render_template('cafe_site/contact.html', id="contact")