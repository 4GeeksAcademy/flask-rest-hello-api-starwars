import os
from typing import List
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column, relationship
from eralchemy2 import render_er
from sqlalchemy import ForeignKey, String, Integer

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'Usuarios'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(80), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    nombre: Mapped[str] = mapped_column(nullable=False)
    apellidos: Mapped[str] = mapped_column(nullable=False)
    ciudad: Mapped[str] = mapped_column(nullable=False)

    personajes_favoritos: Mapped[List["PersonajeFavorito"]] = relationship("PersonajeFavorito", back_populates="Usuario")
    planetas_favoritos: Mapped[List["PlanetaFavorito"]] = relationship("PlanetaFavorito", back_populates="Usuario")

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "nombre": self.nombre,
            "apellidos": self.apellidos,
            "ciudad": self.ciudad
        }

class Personaje(db.Model):
    __tablename__ = 'personaje'

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(nullable=False)
    genero: Mapped[str] = mapped_column(nullable=False)
    edad: Mapped[int] = mapped_column(nullable=False)
    altura: Mapped[int] = mapped_column(nullable=False)
    color_ojos: Mapped[str] = mapped_column(nullable=False)
    color_pelo: Mapped[str] = mapped_column(nullable=False)

    favoritos: Mapped[List["PersonajeFavorito"]] = relationship("PersonajeFavorito", back_populates="personaje")

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "genero": self.genero,
            "edad": self.edad,
            "altura": self.altura,
            "color_ojos": self.color_ojos,
            "color_pelo": self.color_pelo
        }

class Planeta(db.Model):
    __tablename__ = 'planeta'

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(nullable=False, unique=True)
    clima: Mapped[str] = mapped_column(nullable=False)
    gravedad: Mapped[int] = mapped_column(nullable=False)
    terreno: Mapped[str] = mapped_column(nullable=False)

    favoritos: Mapped[List["PlanetaFavorito"]] = relationship("PlanetaFavorito", back_populates="planeta")

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "clima": self.clima,
            "gravedad": self.gravedad,
            "terreno": self.terreno
        }

class PersonajeFavorito(db.Model):
    __tablename__ = 'personaje_favorito'

    id: Mapped[int] = mapped_column(primary_key=True)
    Usuarios_id: Mapped[int] = mapped_column(ForeignKey("Usuarios.id"))
    personaje_id: Mapped[int] = mapped_column(ForeignKey("personaje.id"))

    Usuario: Mapped["Usuario"] = relationship("Usuario", back_populates="personajes_favoritos")
    personaje: Mapped["Personaje"] = relationship("Personaje", back_populates="favoritos")

    def to_dict(self):
        return {
            "id": self.id,
            "Usuarios_id": self.Usuarios_id,
            "personaje_id": self.personaje_id
        }

class PlanetaFavorito(db.Model):
    __tablename__ = 'planeta_favorito'

    id: Mapped[int] = mapped_column(primary_key=True)
    Usuarios_id: Mapped[int] = mapped_column(ForeignKey("Usuarios.id"))
    planeta_id: Mapped[int] = mapped_column(ForeignKey("planeta.id"))

    Usuario: Mapped["Usuario"] = relationship("Usuario", back_populates="planetas_favoritos")
    planeta: Mapped["Planeta"] = relationship("Planeta", back_populates="favoritos")

    def to_dict(self):
        return {
            "id": self.id,
            "Usuarios_id": self.Usuarios_id,
            "planeta_id": self.planeta_id
        }

# Generar el diagrama ER automáticamente
render_er(db.Model, 'diagram.png')
