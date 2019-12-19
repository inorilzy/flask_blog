from . import blog_blueprint
from flask import render_template


@blog_blueprint.route('/')
def blog_list():
    return render_template('blog_list.html')
