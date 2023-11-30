
from flask import Blueprint

bp = Blueprint('deck', __name__)


def init():
    from app.deck import routes


init()
