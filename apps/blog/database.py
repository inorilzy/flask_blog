from apps import db
from jieba.analyse.analyzer import ChineseAnalyzer


article_to_tag = db.Table('article_to_tag',
               db.Column('article_id', db.Integer, db.ForeignKey('article.id')),
               db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
               )


class Article(db.Model):
    __tablename__ = 'article'
    __searchable__ = ['content', 'title']
    __analyzer__ = ChineseAnalyzer()

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.String(32))
    title = db.Column(db.String(32))
    content = db.Column(db.Text)
    tag = db.relationship('Tag', secondary='article_to_tag', backref=db.backref('articles'), lazy='dynamic')


class Tag(db.Model):
    __tablename__ = 'tag'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tag_name = db.Column(db.String(32))


def auto_commit():
    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        return {'status': -1}
    else:
        return {'status': 1}
