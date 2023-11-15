from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

# Create a SQLAlchemy database instance
db = SQLAlchemy()

def create_app():
    # Create and configure the Flask app
    app = Flask(__name__)

    # Load configuration from a separate Config class
    app.config.from_object(Config)

    # Initialize the database with the Flask app
    db.init_app(app)

    # Import and register blueprints
    from .routes import main_bp, import_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(import_bp)

    return app