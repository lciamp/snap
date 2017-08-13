# application __init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


app = Flask(__name__)
# cat /dev/urandom | base64 | head -c 30; echo
app.secret_key = 'nix/xkxN6SVgVu4ddNVelmaRC8/4TN'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../snap.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
flask_bcrypt = Bcrypt(app)

from application.users import models as user_models
from application.users.views import users
from application.snaps.views import snaps
app.register_blueprint(users, url_prefix='/users')
app.register_blueprint(snaps, url_prefix='')

@login_manager.user_loader
def load_user(user_id):
    return user_models.User.query.get(int(user_id))

