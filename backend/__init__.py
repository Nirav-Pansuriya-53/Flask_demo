from backend.user import function_base_user
from backend.user.class_base_user_apis import class_base_user
from flask import Flask

from .extensions import db, migrate


def create_app():
    # Flask app
    app = Flask(__name__)

    # Load configuration
    app.config.from_object("config.Config")

    # Initialize extensions (database, migrate)
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    app.register_blueprint(class_base_user, url_prefix="/class_base_user")
    app.register_blueprint(function_base_user, url_prefix="/function_base_user")
    return app
