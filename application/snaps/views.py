from flask import Blueprint
from flask_login import login_required
from forms import SnapsForm
from models import Snap

snaps = Blueprint('snaps', __name__, template_folder='templates')

@snaps.route("/", methods=['GET'])
def listing():
	snaps = Snap.query.order_by(Snap.created_on.desc()).limit(20).all()
	return render_template('snaps/index.html', snaps=snaps)


@snaps.route("/add", methods=['GET', 'POST'])
@login_required
def add():
	form = SnapsForm()

	if form.validate_on_submit():
		user_id = current_user.id

		snap = Snap(user_id = user_id,
                    name = form.name.data,
                    content = form.content.data,
                    extension = form.extension.data)

		db.session.add(snap)

		try:
			db.session.commit()
		except exc.SQLAlchemyError:
			current_app.exception("Could not save new Snap")
			flash("Something went wrong while saving your Snap")

	else:
		return render_template('snaps/add.html', form=form)

	return redirect(url_for('snaps.listing'))