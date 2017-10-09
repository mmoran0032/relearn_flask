

from pathlib import Path

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate, MigrateCommand
from flask_moment import Moment
from flask_script import Manager, Shell
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
with open('secret_key.txt', 'r') as f:
    app.config['SECRET_KEY'] = f.read().strip()

bootstrap = Bootstrap(app)
manager = Manager(app)
moment = Moment(app)

# sqlalchemy processing
base_dir = Path(__file__).parent
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{base_dir}/data.sqlite'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

from .models import Role, User


def make_shell_context():
    return dict(app=app, db=db, Role=Role, User=User)


manager.add_command('shell', Shell(make_context=make_shell_context))
