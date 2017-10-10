#!/usr/bin/env python3


from pathlib import Path

base_dir = Path(__file__).parent
with (base_dir / 'secret_key.txt').open() as f:
    secret_key = f.read().strip()


class Config:
    SECRET_KEY = secret_key
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

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
