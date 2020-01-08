from . import blog_blueprint
from flask import render_template, url_for, request, jsonify, redirect
from ..blog.database import Article
from apps import db
import flask_whooshalchemyplus



@blog_blueprint.route('/')
def index():
    return render_template('blog/base.html')


@blog_blueprint.route('/blog_list')
def blog_list():
    blog_query = db.session.query(Article).all()
    blog_list = []
    for blog in blog_query:
        blog_tmp = {}
        blog_tmp['id'] = blog.id
        blog_tmp['author'] = blog.author
        blog_tmp['content'] = blog.content
        blog_list.append(blog_tmp)

    return render_template('blog/blog_list.html', blog_list=blog_list)


@blog_blueprint.route('/blog_detail')
def blog_detail():
    # blog = db.session.query(Article).first()
    # blog_dict = {'blogcontent': blog.content}
    return render_template('blog/blog_detail.html')


@blog_blueprint.route('/blog_detail_json')
def blog_detail_json():
    blog = db.session.query(Article).all()[-1]
    blog_dict = {'blogcontent': blog.content}
    return jsonify(blog_dict)


@blog_blueprint.route('/blog_create', methods=['GET', 'POST'])
def blog_create():
    if request.method == 'GET':
        return render_template('blog/blog_create.html')
    elif request.method == 'POST':
        title_name = request.form.get('title')
        markdown_str = request.form.get('text')
        temp_article = Article()
        temp_article.author = 'liuzhiyu'
        temp_article.content = markdown_str
        db.session.add(temp_article)
        db.session.commit()

        flask_whooshalchemyplus.index_one_model(Article)
        return jsonify({'status':True})

@blog_blueprint.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['search']
        results = Article.query.whoosh_search(query).all()

    return render_template('blog/search.html')
#     if not request.form['search']:
#         return redirect(url_for('index'))
#
#     return redirect(url_for('search',query=request.form['search']))
#
# @blog_blueprint.route('/search_results/<query>')
# def search_resutls(query):
#     results = Article.query.whoosh_search(query).all()
#     return render_template()


@blog_blueprint.route('/about')
def about():
    return render_template('blog/about.html')