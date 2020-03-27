from . import blog_blueprint
from flask import render_template, url_for, request, jsonify, redirect
from ..blog.database import Article, Tag, Classify, auto_commit
from apps import db
import flask_whooshalchemyplus


@blog_blueprint.route('/')
@blog_blueprint.route('/blog_list')
def blog_list():
    '''博客列表'''
    blog_query = db.session.query(Article).all()
    blog_list = []
    for blog in blog_query:
        blog_tmp = {}
        blog_tmp['id'] = blog.id
        blog_tmp['title'] = blog.title
        blog_tmp['author'] = blog.author
        blog_tmp['content'] = blog.content
        blog_list.append(blog_tmp)

    return render_template('blog/blog_list.html', blog_list=blog_list)


@blog_blueprint.route('/blog_detail/<int:id>')
def blog_detail(id):
    blog = {'id': id}
    return render_template('blog/blog_detail.html', blog=blog)


@blog_blueprint.route('/blog_detail_json/<int:id>')
def blog_detail_json(id):
    blog_query = db.session.query(Article).filter(Article.id == id).first()
    blog_dict = {'blogtitle': blog_query.title, 'blogcontent': blog_query.content}
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
        temp_article.title = title_name
        db.session.add(temp_article)
        db.session.commit()

        flask_whooshalchemyplus.index_one_model(Article)
        return jsonify({'status': True})


@blog_blueprint.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query_arcitle_name = request.form['search_param']
        results = Article.query.whoosh_search(query_arcitle_name).all()

        blog_list = []
        for blog in results:
            blog_tmp = {}
            blog_tmp['id'] = blog.id
            blog_tmp['title'] = blog.title
            blog_tmp['author'] = blog.author
            blog_tmp['content'] = blog.content
            blog_list.append(blog_tmp)

        return render_template('blog/blog_list.html', blog_list=blog_list)
    return render_template('blog/search.html')


@blog_blueprint.route('/remove/<int:id>')
def remove_arcitle(id):
    cur_article = db.session.query(Article).filter(Article.id == id).first()
    if cur_article is None:
        return {'status': -1}
    db.session.delete(cur_article)
    status = auto_commit()
    return status


@blog_blueprint.route('/tags')
def tags():
    tags = db.session.query(Tag).filter(Tag.tag_name != None).all()
    tags_list = []
    for tag in tags:
        tag_d = {}
        tag_d['id'] = tag.id
        tag_d['name'] = tag.tag_name
        tags_list.append(tag_d)
    return jsonify(tags_list)


@blog_blueprint.route('/tag/<int:id>')
def tag(id):
    blog_query = db.session.query(Tag).filter(Tag.id == id).first().articles
    blog_list = []
    for blog in blog_query:
        blog_tmp = {}
        blog_tmp['id'] = blog.id
        blog_tmp['title'] = blog.title
        blog_tmp['author'] = blog.author
        blog_tmp['content'] = blog.content
        blog_list.append(blog_tmp)
    return render_template('blog/blog_list.html', blog_list=blog_list)


@blog_blueprint.route('/classifies')
def classifies():
    base_query = db.session.query(Classify).filter(Classify.name != None).all()
    classifies_list = []
    for classify in base_query:
        t = {}
        t['id'] = classify.id
        t['name'] = classify.name
        classifies_list.append(t)
    return jsonify(classifies_list)


@blog_blueprint.route('/classify/<int:id>')
def classify(id):
    articles_query = db.session.query(Classify).filter(Classify.id == id).first().articles
    blog_list = []
    for blog in articles_query:
        blog_tmp = {}
        blog_tmp['id'] = blog.id
        blog_tmp['title'] = blog.title
        blog_tmp['author'] = blog.author
        blog_tmp['content'] = blog.content
        blog_list.append(blog_tmp)
    return render_template('blog/blog_list.html', blog_list=blog_list)


@blog_blueprint.route('/about')
def about():
    return render_template('blog/about.html')
