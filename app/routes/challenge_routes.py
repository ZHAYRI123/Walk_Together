#Defines the routes related to challenges.

from flask import render_template, request, redirect, url_for, flash
from . import challenge_bp
from ..models import Challenge
from ..extensions import db

@challenge_bp.route('/challenges', methods=['GET'])
def view_challenges():
    challenges = Challenge.query.all()
    return render_template('challenges.html', challenges=challenges)

@challenge_bp.route('/challenge/add', methods=['GET', 'POST'])
def add_challenge():
    if request.method == 'POST':
        # Handle adding a new challenge
        pass
    return render_template('add_challenge.html')