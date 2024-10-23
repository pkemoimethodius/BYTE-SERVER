from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_cors import CORS  # Import CORS
from config import Config
from db import db
import routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize CORS
    CORS(app)  # Enable CORS for all routes

    db.init_app(app)
    jwt = JWTManager(app)
    migrate = Migrate(app, db)

    # Define a route for the root URL
    @app.route('/')
    def home():
        return jsonify(message="Hello, World!")

    # Create all tables within the application context
    with app.app_context():
        db.create_all()

        # Register the routes with the app instance
        routes.register_routes(app)

        # Print all registered routes for debugging
        print("Registered routes:")
        for rule in app.url_map.iter_rules():
            print(rule)

    return app

# This part ensures the app factory is callable
if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', debug=False)
