

from datetime import datetime

from flask import (
    flash, redirect, render_template, request, session, url_for
)

from . import main
from .forms import NameForm
from .. import db
from ..models import User


@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data.lower()).first()
        if not user:
            user = User(username=form.name.data.lower())
            db.session.add(user)
            session['known'] = False
            flash(f'User {form.name.data} added')
        else:
            session['known'] = True

        old_name = session.get('name')
        if old_name and old_name != form.name.data:
            flash(f'Name changed to {form.name.data}')
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('.index'))
    user_agent = request.headers.get('User-Agent')
    return render_template('index.html',
                           user_agent=user_agent,
                           current_time=datetime.utcnow(),
                           form=form,
                           name=session.get('name'),
                           known=session.get('known', False))
