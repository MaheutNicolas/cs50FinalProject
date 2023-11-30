from flask import Flask
from config import Config
import language.text as text
import gameBoard
import service.askService as askService


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Configure session to use filesystem (instead of signed cookies)
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"

    # Initialize Flask extensions here
    text.init()
    app.jinja_env.globals.update(text=text.get)

    gameBoard.init()

    askService.init()

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.game import bp as game_bp
    app.register_blueprint(game_bp, url_prefix='/game')

    from app.deck import bp as deck_bp
    app.register_blueprint(deck_bp, url_prefix='/deck')

    from app.ask import bp as ask_bp
    app.register_blueprint(ask_bp, url_prefix='/ask')

    return app
