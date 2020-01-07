from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from settings import config_dict
import flask_whooshalchemyplus
from flask_whooshalchemyplus import index_all

db = None


def create_app(config_type):
    app = Flask(__name__)
    app.config.from_object(config_dict[config_type])


    global db
    db = SQLAlchemy(app)



    # 注册蓝图
    from apps.auth import auth_blueprint
    app.register_blueprint(auth_blueprint)
    # 注册简历蓝图
    from apps.bio import bio_blueprint
    app.register_blueprint(bio_blueprint, url_prefix='/bio')
    # 注册blog蓝图
    from apps.blog import blog_blueprint
    app.register_blueprint(blog_blueprint, url_prefix='/blog')
    Migrate(app, db)
    # 关联模型文件
    import apps.blog.database
    # 全文搜索
    flask_whooshalchemyplus.init_app(app)

    # flask_whooshalchemyplus.index_all(app)
    return app
