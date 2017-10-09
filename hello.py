#!/usr/bin/env python3


from datetime import datetime

from flask import (
    flash, Flask, redirect, render_template, request, session, url_for
)
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_script import Manager
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required


class NameForm(FlaskForm):
    name = StringField('Name:', validators=[Required()])
    submit = SubmitField('Submit')


app = Flask(__name__)
with open('secret_key.txt', 'r') as f:
    app.config['SECRET_KEY'] = f.read().strip()

bootstrap = Bootstrap(app)
manager = Manager(app)
moment = Moment(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name and old_name != form.name.data:
            flash(f'Name changed to {form.name.data}')
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    user_agent = request.headers.get('User-Agent')
    return render_template('index.html',
                           user_agent=user_agent,
                           current_time=datetime.utcnow(),
                           form=form,
                           name=session.get('name'))


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


# error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    manager.run()
