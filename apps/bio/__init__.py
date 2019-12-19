from flask import Blueprint

bio_blueprint = Blueprint('bio', __name__, url_prefix='/bio', template_folder='templates', static_folder='static')

from .bio_view import *
