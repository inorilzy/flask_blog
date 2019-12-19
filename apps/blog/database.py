from apps import db


class Article(db.Model):
    '''文章'''
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.String(32))
    content = db.Column(db.Text)