from flask import Blueprint, render_template, request
from pokemon.models import Pokemon, Type, User
from pokemon.extension import db

core_bp = Blueprint('core', 
                    __name__,
                    template_folder='templates')

@core_bp.route('/')
def index():
    page = request.args.get('page', type=int)
    query = db.select(Pokemon)
    pokemons = db.paginate(query, page=page,per_page=4)
    return render_template('core/index.html',
                           title='Home Page',
                           pokemons=pokemons)