# importing and registering the blueprints defined in the other route files

from flask import Blueprint

# Define blueprints for different parts of the application
auth_bp = Blueprint('auth', __name__)
task_bp = Blueprint('task', __name__)
challenge_bp = Blueprint('challenge', __name__)
user_bp = Blueprint('user', __name__)
score_bp = Blueprint('score', __name__)

# Import routes to associate them with the blueprints
from . import auth_routes, task_routes, challenge_routes, user_routes

def register_blueprints(app):
    # Register blueprints with the Flask application
    app.register_blueprint(auth_bp)
    app.register_blueprint(task_bp)
    app.register_blueprint(challenge_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(score_bp)