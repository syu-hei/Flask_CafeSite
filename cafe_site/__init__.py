from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('cafe_site.config')

db = SQLAlchemy(app)

from cafe_site.views.cafe import cafe
app.register_blueprint(cafe)

from cafe_site.views.loging import loging
app.register_blueprint(loging)

from cafe_site.views.reviews import review
app.register_blueprint(review, url_prefix='/users')
