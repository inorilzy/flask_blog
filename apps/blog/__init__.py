from flask import Blueprint

blog_blueprint = Blueprint('blog', __name__, url_prefix='/blog', template_folder='blog_templates', static_folder='static',)

from .blog_view import *
