import os
from secrets import token_urlsafe

basedir = os.path.abspath(os.path.join(os.path.dirname(__file__),'database'))

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or token_urlsafe(10)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or f"sqlite:///{os.path.join(basedir,'app.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False