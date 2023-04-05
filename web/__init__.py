from flask import Flask
from .views import views
from .db import db

def create_app():
  app = Flask(__name__)

  app.config['SECRET_KEY'] = 'mysecretkey'
  print(app.root_path)
  app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{app.root_path}/database.db"
  db.init_app(app)

  app.register_blueprint(views, url_prefix='/')

  from . import models
  
  create_db(app)

  return app


def create_db(app):
  with app.app_context():
    db.create_all()
    print('[+] Database created')