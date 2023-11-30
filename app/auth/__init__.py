
from flask import Blueprint

bp = Blueprint('auth', __name__)


def init():
    from app.auth import routes


init()
