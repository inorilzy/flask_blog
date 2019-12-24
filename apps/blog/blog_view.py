from . import blog_blueprint
from flask import render_template, url_for, request, jsonify
from ..blog.database import Article
from apps import db


@blog_blueprint.route('/')
def index():
    return render_template('blog/base.html')


@blog_blueprint.route('/blog_list')
def blog_list():
    return render_template('blog/blog_list.html')


@blog_blueprint.route('/blog_detail')
def blog_detail():
    # blog = db.session.query(Article).first()
    # blog_dict = {'blogcontent': blog.content}
    return render_template('blog/blog_detail.html')


@blog_blueprint.route('/blog_detail_json')
def blog_detail_json():
    blog = db.session.query(Article).first()
    blog_dict = {'blogcontent': blog.content}
    return jsonify(blog_dict)


@blog_blueprint.route('/blog_create', methods=['GET', 'POST'])
def blog_create():
    if request.method == 'GET':
        return render_template('blog/blog_create.html')
    elif request.method == 'POST':
        markdown_str = request.form.get('text')
        temp_article = Article()
        temp_article.author = 'liuzhiyu'
        temp_article.content = markdown_str
        db.session.add(temp_article)
        db.session.commit()
        return jsonify({'status':True})
