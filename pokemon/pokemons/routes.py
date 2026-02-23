from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from flask_sqlalchemy import query
from pokemon.models import Pokemon, Type, User
from pokemon.models import db

pokemon_db = Blueprint('pokemon_db', __name__, 
                       template_folder='templates')

@pokemon_db.route('/')
def index():
    query = db.select(Pokemon).where(Pokemon.user == current_user)
    pokemon = db.session.scalars(query).all()
    return render_template('pokemons/index.html',
                           title='Pokemon Page',
                           pokemons=pokemon)

@pokemon_db.route('/new', methods=['GET', 'POST'])
def new_pokemon():
    qury = db.select(Type)
    types = db.session.scalars(qury).all()
    if request.method == 'POST':
        name = request.form.get('name')
        height = request.form.get('height')
        weight = request.form.get('weight')
        description = request.form.get('description')
        img_url = request.form.get('img_url')
        user_id = current_user.id
        pokemon_types = request.form.getlist('pokemon_types')

        query = db.select(Pokemon).where(Pokemon.name==name)
        pokemon = db.session.scalar(query)
        if pokemon:
            flash(f'Pokemon :{pokemon.name} is already exists!', 'warning')
            return redirect(url_for('pokemon.new_pokemon'))
        else:
            P_types = []
            for id in pokemon_types:
                P_types.append(db.session.get(Type, id))
            pokemon = Pokemon(
                name = name,
                height = height,
                weight = weight,
                description = description,
                img_url = img_url,
                user_id = user_id,
                types=P_types

            )    
            db.session.add(pokemon)
            db.session.commit()
            flash('Add new pokemon successful!', 'success')
            return redirect(url_for('pokemon_db.index'))

    return render_template('pokemons/new_pokemon.html',
                           title='New Pokemon Page',
                           types=types)
