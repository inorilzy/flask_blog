from flask import Flask, session, render_template
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

    # 注册blog蓝图
    from apps.blog import blog_blueprint
    app.register_blueprint(blog_blueprint, )
    Migrate(app, db)
    # 关联模型文件
    import apps.blog.database
    # 全文搜索
    flask_whooshalchemyplus.init_app(app)

    # flask_whooshalchemyplus.index_all(app)
    # 捕获异常
    @app.errorhandler(404)
    def not_found(error):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        return render_template('500.html'), 500

    # 全站提示信息
    @app.context_processor
    def prompt_message():
        info_msg = None
        if session.get('info_message') is not None:
            info_msg = session.get('info_message')
            session['info_message'] = None
        err_msg = None
        if session.get('error_message') is not None:
            err_msg = session.get('error_message')
            session['error_message'] = None

        toastr_info_msg = None
        if session.get('toastr_info_message') is not None:
            toastr_info_msg = session.get('toastr_info_message')
            session['toastr_info_message'] = None
        toastr_err_msg = None
        if session.get('toastr_error_message') is not None:
            toastr_err_msg = session.get('toastr_error_message')
            session['toastr_error_message'] = None
        return dict(info_msg=info_msg, err_msg=err_msg, toastr_info_msg=toastr_info_msg, toastr_err_msg=toastr_err_msg)

    return app
