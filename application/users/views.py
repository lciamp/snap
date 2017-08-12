from flask import Blueprint
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, SubmitField

users = Blueprint('users', __name__, template_folder='templates')


