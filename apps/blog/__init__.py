from flask import Blueprint

blog_blueprint = Blueprint('blog', __name__, template_folder='blog_templates', static_folder='static',)

from .blog_view import *
