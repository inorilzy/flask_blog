from apps import db
from jieba.analyse.analyzer import ChineseAnalyzer



class Article(db.Model):
    '''文章'''
    __tablename__ = 'article'
    __searchable__ = ['content', 'title']
    __analyzer__ = ChineseAnalyzer()


    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.String(32))
    title = db.Column(db.String(32))
    content = db.Column(db.Text)

