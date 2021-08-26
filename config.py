import os

class Config:
    SECRET_KEY = 'this is secret'
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:Access@localhost/pitchcollections'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}