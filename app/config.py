import os


class Configuration(object):
    APP_DIR = os.path.dirname(os.path.realpath(__file__))
    DEBUG = True  # need no reload server to applying changes
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:pass@localhost/test1'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////%s/bloggy.db' % APP_DIR
    SECRET_KEY = 'nobodyknowsthiskey'

    ### Flask-Security
    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'
