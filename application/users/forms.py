from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, SubmitField

class LoginForm(FlaskForm):
	
	username = StringField('username', validators=[validators.DataRequired()])

	password = PasswordField('password', validators=[validators.DataRequired(),
													 validators.Length(min=6)])

	submit =  SubmitField('submit', validators=[validators.DataRequired()])

