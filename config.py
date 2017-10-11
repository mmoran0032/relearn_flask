#!/usr/bin/env python3


import json
from pathlib import Path

base_dir = Path(__file__).parent
with (base_dir / 'secret_key.txt').open() as f:
    secret_key = f.read().strip()
with (base_dir / 'email_secret.json').open() as f:
    email_config = json.load(f)


class Config:
    SECRET_KEY = secret_key
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = email_config['MAIL_SERVER']
    MAIL_PORT = email_config['MAIL_PORT']
    MAIL_USE_TSL = email_config['MAIL_USE_TSL']
    FLASK_MAIL_SUBJECT_PREFIX = email_config['FLASK_MAIL_SUBJECT_PREFIX']
    FLASK_MAIL_SENDER = email_config['FLASK_MAIL_SENDER']

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{base_dir}/data-dev.sqlite'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{base_dir}/data-test.sqlite'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{base_dir}/data-test.sqlite'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
