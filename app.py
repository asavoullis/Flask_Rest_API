from flask import Flask
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

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)