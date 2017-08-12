from flask import Blueprint, flash, render_template, url_for, redirect, g
from flask_login import login_user, logout_user, current_user

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, SubmitField

from models import User
from application import flask_bcrypt

users = Blueprint('users', __name__, template_folder='templates')

class LoginForm(FlaskForm):
	
	username = StringField('username', validators=[validators.DataRequired()])

	password = PasswordField('password', validators=[validators.DataRequired(),
													 validators.Length(min=6)])

	submit =  SubmitField('submit', validators=[validators.DataRequired()])

@users.route("/login", methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated():
		redirect(urls_for('snaps.listing'))

	form = LoginForm()

	if form.validate():
		user = User.query.filter_by(username=form.username.data).first()

		if not user or not flask_bcrypt.check_password_hash(user.password, form.password.data):
			flash("No such user exists.")
			return render_template('users/login.html', form=form)

		login_user(user, remember=True)
		return redirect(url_for('snaps.listing'))

	return render_template('users/login.html', form=form)



@users.route("/logout", methods=["GET"])
def logout():
	logout_user()
	return redirect(url_for('snaps.listing'))

