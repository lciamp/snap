# application __init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../snap.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

login_manager = LoginManager(app)
flask_bcrypt = Bcrypt(app)

from applications.users import models as user_models
from application.users.views import users

@login_manager
def load_user(user_id):
	return application.user_models.query.get(int(user_id))

