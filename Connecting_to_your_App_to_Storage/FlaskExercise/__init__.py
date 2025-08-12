from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Import after app and db are ready, then register the blueprint
    from FlaskExercise.views import bp as main_bp
    app.register_blueprint(main_bp)

    return app
