from flask import Flask  # all is clear
from config import Configuration  # tut tozhe
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from flask_security import SQLAlchemyUserDatastore, Security


app = Flask(__name__)  # init of app
app.config.from_object(Configuration)  # applying config of app from class Configuration

db = SQLAlchemy(app)

from models import *

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

### ADMIN ###

admin = Admin(app)
admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(Tag, db.session))

### Flask-Security ###

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)