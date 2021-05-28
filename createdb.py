import os 

from app import db, create_app
if not os.path.exists("app/db.sqlite"):
    db.create_all(app=create_app())
