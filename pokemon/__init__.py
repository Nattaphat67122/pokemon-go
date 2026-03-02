import os
from flask import Flask 
from pokemon.extension import db, login_manager, bcrypt
from pokemon.models import User, Type, Pokemon
from pokemon.core.routes import core_bp
from pokemon.users.routes import users_bp
from pokemon.pokemons.routes import pokemon_db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'users.login'
    login_manager.login_message = 'Please login to access this page.'
    login_manager.login_message_category = 'warning'

    app.register_blueprint(core_bp, url_prefix='/')
    app.register_blueprint(users_bp, url_prefix='/users')
    app.register_blueprint(pokemon_db, url_prefix='/pokemons')

    return app
