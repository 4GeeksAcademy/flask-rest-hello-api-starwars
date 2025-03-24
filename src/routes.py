from flask import Blueprint, jsonify
from models import db, Usuario, Personaje, Planeta, PersonajeFavorito, PlanetaFavorito

api = Blueprint('api', __name__)

@api.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    return {'usuarios': [usuario.to_dict() for usuario in usuarios]}

# GET /people
@api.route('/people', methods=['GET'])
def get_people():
    characters = db.session.query(Personaje).all()
    return jsonify([char.to_dict() for char in characters]), 200

# GET /people/<int:id>
@api.route('/people/<int:personaje_id>', methods=['GET'])
def get_single_personaje(personaje_id):
    personaje = db.session.get(Personaje, personaje_id)
    if personaje is None:
        return jsonify({"msg": "Personaje no encontrado"}), 404
    return jsonify(personaje.to_dict()), 200

# GET /planets
@api.route('/planets', methods=['GET'])
def get_planets():
    planets = db.session.query(Planeta).all()
    return jsonify([planet.to_dict() for planet in planets]), 200

# GET /planets/<int:id>
@api.route('/planets/<int:planeta_id>', methods=['GET'])
def get_single_planet(planeta_id):
    planeta = db.session.get(Planeta, planeta_id)
    if planeta is None:
        return jsonify({"msg": "Planeta no encontrado"}), 404
    return jsonify(planeta.to_dict()), 200

@api.route('/usuarios/favorites', methods=['GET'])
def get_Usuario_favorites():
    Usuario_id = 1  # Simulación de Usuario logueado
    Usuario = Usuario.query.get(Usuario_id)

    if not Usuario:
        return jsonify({"msg": "Usuario no encontrado"}), 404

    personajes = [fav.personaje.to_dict() for fav in Usuario.personajes_favoritos]
    planetas = [fav.planeta.to_dict() for fav in Usuario.planetas_favoritos]

    return jsonify({
        "personajes_favoritos": personajes,
        "planetas_favoritos": planetas
    }), 200

@api.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def add_fav_planet(planet_id):
    Usuario_id = 1
    planeta = Planeta.query.get(planet_id)
    if not planeta:
        return jsonify({"msg": "Planeta no encontrado"}), 404

    nuevo_fav = PlanetaFavorito(Usuario_id=Usuario_id, planeta_id=planet_id)
    db.session.add(nuevo_fav)
    db.session.commit()
    return jsonify({"msg": "Planeta añadido a favoritos"}), 201

@api.route('/favorite/people/<int:people_id>', methods=['POST'])
def add_fav_people(people_id):
    Usuario_id = 1
    personaje = Personaje.query.get(people_id)
    if not personaje:
        return jsonify({"msg": "Personaje no encontrado"}), 404

    nuevo_fav = PersonajeFavorito(Usuario_id=Usuario_id, personaje_id=people_id)
    db.session.add(nuevo_fav)
    db.session.commit()
    return jsonify({"msg": "Personaje añadido a favoritos"}), 201

@api.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def delete_fav_planet(planet_id):
    Usuario_id = 1
    favorito = PlanetaFavorito.query.filter_by(Usuario_id=Usuario_id, planeta_id=planet_id).first()
    if not favorito:
        return jsonify({"msg": "Favorito no encontrado"}), 404

    db.session.delete(favorito)
    db.session.commit()
    return jsonify({"msg": "Planeta eliminado de favoritos"}), 200

@api.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def delete_fav_people(people_id):
    Usuario_id = 1
    favorito = PersonajeFavorito.query.filter_by(Usuario_id=Usuario_id, personaje_id=people_id).first()
    if not favorito:
        return jsonify({"msg": "Favorito no encontrado"}), 404

    db.session.delete(favorito)
    db.session.commit()
    return jsonify({"msg": "Personaje eliminado de favoritos"}), 200


