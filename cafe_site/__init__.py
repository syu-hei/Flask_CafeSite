from flask import Flask

app = Flask(__name__)
app.config.from_object('cafe_site.config')

import cafe_site.views
