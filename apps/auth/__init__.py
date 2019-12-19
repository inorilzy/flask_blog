from flask import Blueprint

auth_blueprint = Blueprint('auth', __name__, static_folder='static', url_prefix='/auth',template_folder='templates')

from .auth_view import *
