import os
from decouple import config

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
class Config:
  SECRET_KEY = config('SECRET_KEY')
  SQLALCHEMY_TRACK_MODIFICATIONS=config('SQLALCHEMY_TRACK_MODIFICATIONS', cast=bool)
  
class DevConfig(Config):
  SQLALCHEMY_DATABASE_URI= 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'dev.db'))
  SQLALCHEMY_ECHO=True
  DEBUG=True

class ProdConfig(Config):
  pass

class TestConfig(Config):
  pass

  