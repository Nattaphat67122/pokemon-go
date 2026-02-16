from pokemon.extension import db, login_manager, bcrypt
from sqlalchemy import String, Integer, Table,Column, ForeignKey,func,Text, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import List
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id : Mapped[int] = mapped_column(primary_key=True)
    username : Mapped[str] = mapped_column(String(25), unique=True, nullable=False)
    email : Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    password : Mapped[str] = mapped_column(String(255), nullable=False)
    frist_name : Mapped[str] = mapped_column(String(25), nullable=True)
    last_name : Mapped[str] = mapped_column(String(25), nullable=True)
    avatar : Mapped[str] = mapped_column(String(255), nullable=True, default='avatar.png')
    created_at : Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at : Mapped[datetime] = mapped_column(DateTime(timezone=True), onupdate=func.now(), nullable=True, server_default=func.now())

    pokemons : Mapped[List['Pokemon']] = relationship(back_populates='user')
    def __repr__(self) -> str:
        return f'<User {self.username}>'
    
pokedex = Table(
         'pokedex',
         db.metadata,
         Column('type_id', Integer, ForeignKey('type.id'), primary_key=True),
         Column('pokemon_id', Integer, ForeignKey('pokemon.id'), primary_key=True)     
    )
    
class Type(db.Model):
    __tablename__ = 'type'
    id : Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column(String(25), nullable=False, unique=True)

    pokemons : Mapped[list['Pokemon']] = relationship(back_populates='types',
                                                        secondary=pokedex)
    def __repr__(self) -> str:
            return f'<Type {self.name}>'
        
class Pokemon(db.Model):
    __tablename__ = 'pokemon'
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    name : Mapped[str] = mapped_column(String(25), nullable=False, unique=True)
    height : Mapped[str] = mapped_column(String(25), nullable=False, )
    weight : Mapped[str] = mapped_column(String(25), nullable=False, )
    description : Mapped[str] = mapped_column(Text, nullable=False, )
    img_url : Mapped[str] = mapped_column(Text, nullable=False, )
    user_id : Mapped[int] = mapped_column(Integer, ForeignKey('user.id'))
    created_at : Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    user : Mapped[User] = relationship(back_populates='pokemons')
    types : Mapped[List['Type']] = relationship(back_populates='pokemons',
                                                        secondary=pokedex)
    def __repr__(self) -> str:
        return f'<Pokemon {self.name}>'