from operator import ipow
from app.models import Skills
from flask_login import login_required, current_user
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login.utils import login_user
from app import dashboard, db
from statistics import mean

dashboard = Blueprint('dashboard', __name__, template_folder='templates')

@dashboard.route('/')
def index():
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
    moyennedevops = []
    moyennedevcloud = []
    for skill in skills_devops:
        skill = Skills.query.filter_by(name=skill).all()
        # print([(int(i.points),i.name) for i in skill])
        moyennedevops.append(mean([int(i.points) for i in skill]))
    moyennedevops = dict(zip(skills_devcloud, moyennedevops))
    # print("moyenne devops",moyennedevops)
    for skill in skills_devcloud:
        skill = Skills.query.filter_by(name=skill).all()
        # print([(int(i.points),i.name) for i in skill])
        moyennedevcloud.append(mean([int(i.points) for i in skill]))
    moyennedevcloud = dict(zip(skills_devcloud, moyennedevcloud))
    # print("moyenne devcloud",moyennedevcloud)
    return render_template('index.html', skills_devcloud=skills_devcloud, skills_devops=skills_devops, devopspoints=moyennedevops, devcloudpoints=moyennedevcloud)

@dashboard.route('/profile', methods=['GET'])
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
    skillpoints = [i.points for i in skills]
    devopspoints = skillpoints[:8]
    devcloudpoints = skillpoints[8:]
    # print(devopspoints, devcloudpoints)
    devopspoints = dict(zip(skills_devops, devopspoints))
    devcloudpoints = dict(zip(skills_devcloud, devcloudpoints))
    print(devcloudpoints, devopspoints, sep="\n")
    return render_template('profile.html', firstname=current_user.firstname, devopspoints=devopspoints, devcloudpoints=devcloudpoints, skills_devcloud=skills_devcloud, skills_devops=skills_devops)


@dashboard.route('/profile', methods=['POST'])
def profile_post():
    present_skills = Skills.query.filter_by(person_id=current_user.id).all()
    for i in present_skills:
        db.session.delete(i)
    db.session.commit()
    # print("skills : ",present_skills)
    future_skills = dict(request.form)
    # print(future_skills)
    for i in future_skills:
        # print(i, future_skills.get(i))
        new_skill = Skills(name=i.split("/")[0], person_id = current_user.id, ref=i.split("/")[-1], points=future_skills.get(i))
        db.session.add(new_skill)
    db.session.commit()
    # password = request.form.get('password')
    # firstname = request.form.get('firstname')
    # surname = request.form.get('surname')
    

    # email_check = Users.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database
    # data_to_validate = [(email_check, email)]

    # for data in data_to_validate:
    #     if data[0]:
    #         flash(f'{data[1]} is not available')
    #         return redirect(url_for('auth.signup'))
    # # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    # new_user = Users(email=email,password=generate_password_hash(password, method='sha256'), firstname=firstname, surname=surname)

    # # add the new user to the database
    # db.session.add(new_user)
    # db.session.commit()

    flash(f'Vous compétences ont bien été modifiées')
    return redirect(url_for('dashboard.profile'))



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
