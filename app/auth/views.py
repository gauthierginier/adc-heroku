from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import Users
from app import db
import logging

auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/login')
def login():
    """ Login page 
    
    :returns: template file
    """
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = Users.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page
    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('dashboard.profile'))

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    password = request.form.get('password')
    firstname = request.form.get('firstname')
    surname = request.form.get('surname')
    

    email_check = Users.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database
    data_to_validate = [(email_check, email)]

    for data in data_to_validate:
        if data[0]:
            flash(f'{data[1]} is not available')
            return redirect(url_for('auth.signup'))
    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = Users(email=email,password=generate_password_hash(password, method='sha256'), firstname=firstname, surname=surname)

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('dashboard.index'))