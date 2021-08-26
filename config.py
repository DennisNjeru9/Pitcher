import os

class Config:
    SECRET_KEY = 'thisissecret'
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:Access@localhost/pitchcollections'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}