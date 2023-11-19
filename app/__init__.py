from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_apscheduler import APScheduler

from .config import Config

# Create a SQLAlchemy database instance
db = SQLAlchemy()
scheduler = APScheduler()
csrf = CSRFProtect()


def create_app():
    from updatedata.updateScheduler import scheduled_job

    # Create and configure the Flask app
    app = Flask(__name__)

    # Load configuration from a separate Config class
    app.config.from_object(Config)

    # Initialize the database with the Flask app
    db.init_app(app)

    # Set the secret key for CSRF protection
    csrf.init_app(app)
    app.config['WTF_CSRF_SECRET_KEY'] = app.config['SECRET_KEY']

    # Import and register blueprints
    from .routes import main_bp, import_bp, search_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(import_bp)
    app.register_blueprint(search_bp)

    # Start the scheduler when the Flask application starts
    app.config["SCHEDULER_API_ENABLED"] = True
    scheduler.init_app(app)
    scheduler.start()

    return app
