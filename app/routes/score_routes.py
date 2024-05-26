#Defines routes related to managing user scores.

from flask import render_template, request, redirect, url_for, flash
from . import score_bp
from ..models import Score
from ..extensions import db

@score_bp.route('/scores', methods=['GET'])
def view_scores():
    scores = Score.query.all()
    return render_template('scores.html', scores=scores)