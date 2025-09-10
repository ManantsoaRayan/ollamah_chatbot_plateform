from flask import Flask
from .extensions import db, migrate
from .routes import register_blueprints
from . import models

def create_app(config_class="config.DevConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)

    print(app)

    db.init_app(app)
    migrate.init_app(app, db)

    # complete the blueprint
    register_blueprints(app)

    return app
