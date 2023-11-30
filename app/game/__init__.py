
from flask import Blueprint

bp = Blueprint('game', __name__)


def init():
    from app.game import routes


init()
