#Defines the routes related to user profiles and rankings.

from flask import render_template, request, redirect, url_for, flash
from . import user_bp
from ..models import User
from ..extensions import db

@user_bp.route('/profile', methods=['GET'])
def view_profile():
    # Retrieve the user profile details
    return render_template('profile.html')

@user_bp.route('/rankings', methods=['GET'])
def view_rankings():
    # Retrieve and display user rankings
    return render_template('rankings.html')