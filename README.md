# poc-desktop

Create the db (initialization) in python console
   
from app import db, create_app
db.create_all(app=create_app())

#pytest

python3 -m pytest -v
