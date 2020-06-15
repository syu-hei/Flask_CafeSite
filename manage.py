from flask_script import Manager
from cafe_site import app

from cafe_site.scripts.db import InitDB


if __name__ == "__main__":
    manager = Manager(app)
    manager.add_command('init_db', InitDB())
    manager.run()
