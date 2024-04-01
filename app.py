#app.py
import logging
from flask import Flask, jsonify
from config import Config
from models.extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Create the database
    with app.app_context():
        db.create_all()

    # Import blueprints
    from controllers.account_controller import account_bp
    from controllers.user_controller import user_bp

    # Register blueprints
    app.register_blueprint(account_bp, url_prefix='/accounts')
    app.register_blueprint(user_bp, url_prefix='/users')

    @app.route('/')
    def hello():
        return jsonify(message="Hello, welcome to the Bank API!")

    # Error handling
    @app.errorhandler(404)
    def page_not_found(e):
        return jsonify(error="Resource not found"), 404

    @app.errorhandler(Exception)
    def internal_server_error(e):
        app.logger.error('An error occurred during a request.')
        return jsonify(error="Internal server error"), 500

    return app

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app = create_app()
    app.run(debug=True)