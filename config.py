import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = '57094c2b56ecea04715fa1cfe8ae1f6c21299e152a570b41'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(basedir, 'cardGame.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
