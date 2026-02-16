types = [
    'Grass', 'Ice', 'Poison', 'Rock', 'Fire',
    'Dragon', 'Dark', 'Electric', 'Ground', 'Water',
    'Flying', 'Fairy', 'Steel', 'Normal', 'Ghost',
    'Bug', 'Fighting', 'Psychic'
]

from pokemon.models import Type
from pokemon.extension import db
def create_pokemon_types():
    for type in types:
        pt = Type(name = type)
        db.session.add(pt)
    db.session.commit()