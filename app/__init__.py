

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
# from flask_migrate import Migrate, MigrateCommand
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

from config import config


bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    return app


# sqlalchemy processing
# base_dir = Path(__file__).parent
# app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{base_dir}/data.sqlite'
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# migrate = Migrate(app, db)
# manager.add_command('db', MigrateCommand)
#
# from .models import Role, User
#
#
# def make_shell_context():
#     return dict(app=app, db=db, Role=Role, User=User)
#
#
# manager.add_command('shell', Shell(make_context=make_shell_context))
