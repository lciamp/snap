import datetime, hashlib
from application import db

class Snap(db.Model):
	
	id = db.Column(db.Integer, primary_key=True)

	name = db.Column(db.String(128))

	extension = db.Column(db.String(12))

	content = db.Column(db.Text())

	def content_hash(context):
		content = context.current_parameters['content']
		created_on = context.current_parameters['created_on']
		return hashlib.sha1(content + str(created_on)).hexdigest()

	hash_key = db.Column(db.String(40), unique=True, default=content_hash)

	created_on = db.Column(db.DateTime, default=datetime.datetime.utcnow, index=True)

	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	user = db.relationship('User', backref=db.backref('snaps', lazy='dynamic'))

	def __repr__(self):
		return '<Snap {!r}>'.format(self.id)

"""
	def __init__(self, user_id, name, content, extension):
		self.user_id = user_id
		self.name = name
		self.content = content
		self.extension = extension
		self.created_on = datetime.datetime.utcnow()
		self.hash_key = hashlib.sha1(self.content + str(self.created_on)).hexdigest()

"""
	
