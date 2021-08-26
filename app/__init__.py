from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

    #creating app configurations
    app.config.from_object(config_options[config_name])

    #initializing flask extensions
    db.init_app(app)

    #registering blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #setting config
    #from .requests import configure_request
    #configure_request(app)

    return app