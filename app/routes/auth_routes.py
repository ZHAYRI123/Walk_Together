#Defines the authentication-related routes, such as login and registration

from flask import render_template, request, redirect, url_for, flash
from . import auth_bp
from ..models import User
from ..extensions import db

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic here
        pass
    return render_template('login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Handle registration logic here
        pass
    return render_template('register.html')