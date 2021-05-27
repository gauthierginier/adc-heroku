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
    skills_devops=[
        "Concevoir un système de veille technologique permettant de collecter, classifier et analyser l’information afin d’améliorer la prise de décisions techniques.",
        "Assurer le versionnement d’un code source d’une application organisée en fonctionnalités et lots à l’aide d’un logiciel de contrôle de version de manière à garantir la fiabilité du code source dans un environnement multi-contributeurs",
        "Contrôler l'exécution du code source à l’aide de tests et d’outils d’analyses statiques* du code source afin de minimiser le risque d’erreur dans un contexte de livraison continue",
        "Automatiser les phases de tests unitaires et d’analyses statiques du code source lors du partage des sources à l’aide d’un outil d’intégration continue* de manière à prévenir les erreurs potentielles",
        "Concevoir un processus de livraison continue à l’aide d’outils d’automatisation de manière à l’intégrer au processus de développement",
        "Développer l’architecture d’une application en micro-services à l’aide d’outils et de bibliothèques logicielles adaptées afin de réduire la complexité globale du système",
        "Concevoir un système de veille technologique permettant la collecte, la classification, l’analyse et la diffusion de l’information aux différents acteurs de l’organisation afin d’améliorer la prise de décisions techniques",
        "Accompagner les collaborateurs au sein de l’équipe projet dans la sensibilisation et l’acculturation des méthodes d’organisation et de production DevOps de manière à optimiser le cycle de livraison d’un projet"
    ]
    skills_devcloud=[
        "Développer des programmes et scripts simples",
        "Analyser une infrastructure réseau simple",
        "Utiliser les machines virtuelles (serveurs web, de base de données…)",
        "Développer une application simple pour le cloud en exploitant les outils de développement de la plateforme (PaaS et SaaS)",
        "Déployer une application sur le cloud",
        "Analyser un besoin en développement d’application cloud",
        "Développer une application cloud native",
        "Sécuriser une applications à tous les niveaux en environnement cloud",
        "Optimiser une application cloud native"
    ]
    skills = Skills.query.filter_by(person_id=current_user.id).all()
    return render_template('profile.html', firstname=current_user.firstname, skills=skills, skills_devcloud=skills_devcloud, skills_devops=skills_devops)

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
