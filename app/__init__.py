from flask import Flask
from .config import Config

# Create the Flask application instance
app = Flask(__name__)

# Load configuration from config.py
app.config.from_object(Config)

# Import blueprints
from .routes import main_bp

# Register blueprints
app.register_blueprint(main_bp)

if __name__ == "__main__":
    app.run()
