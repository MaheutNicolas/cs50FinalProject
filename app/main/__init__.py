
from flask import Blueprint

bp = Blueprint('main', __name__)


def init():
    from app.main import routes


init()
