from app import db
from flask import flash


def manage_users(username):
    if username not in users:
        flash(f"Hello { username }!")
        users.add(username)

        user = User(username=username)
        db.session.add(user)
        db.session.commit()
    else:
        flash(f"Already seen, { username }!")
