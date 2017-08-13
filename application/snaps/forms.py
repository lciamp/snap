from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField
from wtforms.widgets import TextArea

class SnapsForm(FlaskForm):

	name = StringField('name', validators=[validators.DataRequired()])

	extension = StringField('extension', validators=[validators.DataRequired()])

	content = StringField('content', widget=TextArea(), validators=[validators.DataRequired()])

	submit = SubmitField('submit', validators=[validators.DataRequired()])