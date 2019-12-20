from . import blog_blueprint
from flask import render_template, url_for



@blog_blueprint.route('/blog_list')
def blog_list():
    return render_template('blog_list.html')

@blog_blueprint.route('/blog_detail')
def blog_detail():
    url_for()
    return render_template('blog_detail.html')

@blog_blueprint.route('/')
@blog_blueprint.route('/blog_create')
def blog_create():
    return render_template('blog_create.html', info='blog_create_info')

