import os
from flask import Flask 
from pokemon.extension import db, login_manager, bcrypt
from pokemon.models import User, Type, Pokemon

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['SECRET_KEY'] = os.environ.get('MY_SECRET_KEY')
    
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    return app
