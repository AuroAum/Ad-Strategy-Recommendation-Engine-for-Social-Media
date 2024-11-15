from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create an instance of SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configure the app and initialize extensions
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'  # Update with your database path
    db.init_app(app)

    with app.app_context():
        # Import routes and models to register with the app context
        from . import routes, models  # Ensure models is being imported here
        db.create_all()  # Create tables if not already created

        # Register the Blueprint to make the routes accessible
        app.register_blueprint(routes.main)  # This is where you add the line

    return app
