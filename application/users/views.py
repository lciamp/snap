from flask import Blueprint, flash, render_template, url_for, redirect, g
from flask_login import login_user, logout_user, current_user

from forms import LoginForm

from models import User
from application import flask_bcrypt

users = Blueprint('users', __name__, template_folder='templates')


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

