from flask import Blueprint

bp = Blueprint('ask', __name__)


def init():
    from app.ask import routes


init()
