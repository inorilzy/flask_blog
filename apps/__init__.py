from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from settings import config_dict


db = None

def create_app(config_type):
    app = Flask(__name__)
    app.config.from_object(config_dict[config_type])
    global db
    db = SQLAlchemy(app)

    # 注册蓝图
    from apps.auth import auth_blueprint
    app.register_blueprint(auth_blueprint)
    from apps.bio import bio_blueprint
    app.register_blueprint(bio_blueprint)
    from apps.blog import blog_blueprint
    app.register_blueprint(blog_blueprint)
    Migrate(app, db)
    # 关联模型文件
    import apps.blog.database
    return app