import datetime
from application import db, flask_bcrypt
from sqlalchemy.ext.hybrid import hybrid_property

class User(db.Model):

	id = db.Column(db.Integer, primary_key=True)

	email = db.Column(db.String(255), unique=True)

	username = db.Column(db.String(40), unique=True)

	#password = db.Column(db.String(60))

	created_on = db.Column(db.DateTime, default=datetime.datetime.utcnow)

	# hashed password for the user
	_password = db.Column('password', db.String(60))

	@hybrid_property
	def password(self):
		#bcrypted password of given user
		return self._password

	@password.setter
	def password(self, password):
		self._password = flask_bcrypt.generate_password_hash(password)


	def __repr__(self):
		return '<User {!r}>'.format(self.username)

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymoous(self):
		return False

	def get_id(self):
		return unicode(self.id)