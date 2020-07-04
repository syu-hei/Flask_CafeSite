from cafe_site import db
from datetime import datetime
import bcrypt
<<<<<<< HEAD
import pdb
=======
>>>>>>> future/database

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
<<<<<<< HEAD
    password = db.Column(db.String(50))
=======
    password = db.Column(db.String(100))
>>>>>>> future/database
    salt = db.Column(db.String(50))
    created_at = db.Column(db.DateTime)

    def __init__(self, username=None, password=None):
        self.username = username
        self.salt = bcrypt.gensalt().decode()
        self.password = bcrypt.hashpw(password.encode(), self.salt.encode()).decode()
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return '<Entry id:{} username:{}>'.format(self.id, self.username)