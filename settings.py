import os
from datetime import timedelta


class Config(object):
    DEBUG = False
    TESTING = False
    # 私钥设置
    SECRET_KEY = '8rfZwtdo-3oig-3Urj-ajUp-DPq9RfWBVVJp'
    # 密码前缀设置
    PASSWORD_PREFIX = "v61baB7o-LpnT-COeG-Tvhr-08UgSc78msQV"

    # 服务器本地配置
    HOST = '127.0.0.1'
    PORT = 3306
    USERNAME = 'root'
    PASSWORD = 'liuzhiyu'
    DATABASE = 'flask_blog'

    # SQLALCHEMY配置
    DIALECT = 'mysql'
    DRIVER = 'pymysql'
    SQLALCHEMY_DATABASE_URI = f"{DIALECT}+{DRIVER}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}?charset=utf8"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE = 100


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True


config_dict = {
    'pro': ProductionConfig,
    'dev': DevelopmentConfig,
    'test': TestingConfig
}
