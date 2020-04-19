from flask import Flask, render_template


app = Flask(__name__)



@app.route('/')
def index():
     return render_template('index.html', id="home")



@app.route('/menu')
def menu():
     return render_template('menu.html', id="menu")



@app.route('/news')
def news():
     return render_template('news.html', id="news")



@app.route('/contact')
def contact():
     return render_template('contact.html', id="contact")






if __name__ == '__main__':
    app.debug = True
    app.run()