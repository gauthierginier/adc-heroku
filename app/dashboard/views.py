from operator import ipow
from app.models import Skills
from flask_login import login_required, current_user
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login.utils import login_user
from app import dashboard, db

dashboard = Blueprint('dashboard', __name__, template_folder='templates')

@dashboard.route('/')
def index():
    return render_template('index.html')

@dashboard.route('/profile', methods=['POST','GET'])
@login_required
def profile():
    skills = Skills.query.filter_by(person_id=current_user.id).all()
    return render_template('profile.html', firstname=current_user.firstname, skills=skills)

# @dashboard.route('/create')
# @login_required
# def create():
#     return render_template('create_address.html')

# @dashboard.route('/create', methods=['POST'])
# @login_required
# def create_post():
#     name = request.form.get('name')
#     lat = request.form.get('lat')
#     lng = request.form.get('lng')
#     city = request.form.get('city')
#     zip = request.form.get('zip')
#     country = request.form.get('country')
#     qrcode_data=keygen.generate_key()

#     name_check = Address.query.filter_by(
#         name=name,
#         person_id=current_user.id
#     ).all() # if this returns a user, then the email already exists in database

#     print(name_check)
#     if name_check:
#         flash(f'vous avez déjà une addresse à ce mon : {name}')
#         return redirect(url_for('dashboard.create'))
#     # create a new user with the form data. Hash the password so the plaintext version isn't saved.
#     new_address = Address(name=name, person_id=current_user.id, lat=lat, qrcode_data=qrcode_data, lng=lng, city=city, zip=zip, country=country)

#     # add the new user to the database
#     db.session.add(new_address)
#     db.session.commit()

#     return redirect(url_for('dashboard.profile'))
