from flask import render_template, flash

from app import app, db
from app.forms import LoginForm
from app.models import User

# from user_management import manage_users


users = set( str(username) for username in User.query.all() )


@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        manage_user(form.username.data.strip())

    return render_template('login.html', form=form)


@app.route('/all_users')
def all_users():
    return render_template('all_users.html', users=users)


def manage_user(username):
    if username not in users:
        flash(f"Hello {username}!")
        users.add(username)

        user = User(username=username)
        db.session.add(user)
        db.session.commit()
    else:
        flash(f"Already seen, {username}!")
