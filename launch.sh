export FLASK_APP=app
export FLASK_DEBUG=1
export FLASK_SECRET_KEY=lol
export DATABASE_URL2=sqlite:///db.sqlite
python3 createdb.py
flask run
