import os
from utils import generate_sitemap
from utils import APIException
from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from admin import setup_admin
from models import db
from routes import api

def create_app():
    """
    This function creates and configures the Flask app.
    """
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    # Configure the database URL
    db_url = os.getenv("DATABASE_URL")
    if db_url is not None:
        app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    Migrate(app, db)
    CORS(app)
    setup_admin(app)

    # Register routes (blueprints)
    app.register_blueprint(api, url_prefix='/')

    # Handle errors like a JSON object
    @app.errorhandler(APIException)
    def handle_invalid_usage(error):
        return jsonify(error.to_dict()), error.status_code

    # Generate sitemap with all your endpoints
    @app.route('/')
    def sitemap():
        return generate_sitemap(app)

    # Simple Hello endpoint
    @app.route('/Usuario', methods=['GET'])
    def handle_hello():
        response_body = {
            "msg": "Hello, this is your GET /Usuario response"
        }
        return jsonify(response_body), 200

    return app


# This only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    app = create_app()
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
