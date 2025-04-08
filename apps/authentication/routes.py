# THIS IS apps/authentication/routes.py

from flask import render_template, redirect, request, url_for, Response
from flask_login import current_user, login_user, logout_user
from flask_dance.contrib.github import github

from apps import db, login_manager
from apps.authentication import blueprint  # This blueprint = Blueprint("authentication_blueprint", __name__, url_prefix="/auth")
from apps.authentication.forms import LoginForm, CreateAccountForm
from apps.authentication.models import Users
from apps.authentication.util import verify_pass

# Redirect "/" under /auth to the home page
@blueprint.route('/')
def route_default():
    # Goes to /home/index or wherever your home blueprint's main page is
    return redirect(url_for('home_blueprint.index'))

# Example GitHub OAuth route
@blueprint.route('/github')
def login_github():
    """ Github login """
    if not github.authorized:
        return redirect(url_for("github.login"))
    res = github.get("/user")
    return redirect(url_for('home_blueprint.index'))

# -----------------------------
#   LOGIN & REGISTRATION
# -----------------------------

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    """
    URL: /auth/login
    """
    login_form = LoginForm(request.form)
    if 'login' in request.form:
        username = request.form['username']
        password = request.form['password']

        # Locate user
        user = Users.query.filter_by(username=username).first()

        # Check the password
        if user and verify_pass(password, user.password):
            login_user(user)
            return redirect(url_for('home_blueprint.index'))  # or /home/index

        # If user/pass is invalid
        return render_template('accounts/login.html',
                               msg='Wrong user or password',
                               form=login_form)

    # If GET request or no form submission
    if not current_user.is_authenticated:
        return render_template('accounts/login.html', form=login_form)

    # If already authenticated
    return redirect(url_for('home_blueprint.index'))

@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    """
    URL: /auth/register
    """
    create_account_form = CreateAccountForm(request.form)
    if 'register' in request.form:
        username = request.form['username']
        email = request.form['email']

        # Check if username exists
        user = Users.query.filter_by(username=username).first()
        if user:
            return render_template('accounts/register.html',
                                   msg='Username already registered',
                                   success=False,
                                   form=create_account_form)

        # Check if email exists
        user = Users.query.filter_by(email=email).first()
        if user:
            return render_template('accounts/register.html',
                                   msg='Email already registered',
                                   success=False,
                                   form=create_account_form)

        # Create the new user
        user = Users(**request.form)
        db.session.add(user)
        db.session.commit()

        # Log out any active user
        logout_user()
        
        return render_template('accounts/register.html',
                               msg='Account created successfully.',
                               success=True,
                               form=create_account_form)

    # If GET request or no form submission
    return render_template('accounts/register.html', form=create_account_form)

@blueprint.route('/logout')
def logout():
    """
    URL: /auth/logout
    """
    logout_user()
    # After logout, go back to login page
    return redirect(url_for('authentication_blueprint.login'))

# -----------------------------
#   ERROR HANDLERS
# -----------------------------

@login_manager.unauthorized_handler
def unauthorized_handler():
    return render_template('home/page-403.html'), 403

@blueprint.errorhandler(403)
def access_forbidden(error):
    return render_template('home/page-403.html'), 403

@blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('home/page-404.html'), 404

@blueprint.errorhandler(500)
def internal_error(error):
    return render_template('home/page-500.html'), 500

# -----------------------------
#   ANY EXTRA IMPORTS FOR GRAPHS (if needed)
# -----------------------------
import matplotlib.pyplot as plt
import io
import base64
import pandas as pd
import numpy as np
import requests
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.arima.model import ARIMA
# etc. as needed


