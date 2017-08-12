from application.users.models import User
new_user = User(email='lou2@me.com', username='me2')

from application import db
db.session.add(new_user)
db.session.commit()

print new_user.email