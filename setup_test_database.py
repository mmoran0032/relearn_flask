#!/usr/bin/env python3


from test_app import db, Role, User


db.drop_all()
db.create_all()

admin = Role(name='admin')
mod = Role(name='moderator')
user = Role(name='user')
john = User(username='john', role=admin)
susan = User(username='susan', role=user)
david = User(username='david', role=user)

db.session.add_all([admin, mod, user, john, susan, david])
db.session.commit()
