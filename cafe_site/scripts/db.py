from flask_script import Command
from cafe_site import db


class InitDB(Command):
    "create database"

    def run(self):
        db.create_all()
