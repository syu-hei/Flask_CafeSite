from cafe_site import db
from datetime import datetime

class Review(db.Model):
    __tablename__ = 'Reviews'
    id = db.Column(db.Integer, primary_key=True)
    star = db.Column(db.Integer)
    title = db.Column(db.String(50), unique=True)
    text = db.Column(db.Text)
    created_at = db.Column(db.DateTime)

    def __init__(self, star=None, title=None, text=None):
        self.star = star
        self.title = title
        self.text = text
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return '<Review id:{} star:{} title:{} text:{}>'.format(self.id, self.star, self.title, self.text)
