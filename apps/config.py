import os

class Config(object):
    basedir = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = os.getenv('SECRET_KEY', 'S#perS3crEt_007')

    # Use SQLite as default DB for both dev and production
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False 

    # Assets
    ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets')    

    # Github login toggle
    SOCIAL_AUTH_GITHUB = False
    GITHUB_ID = os.getenv('GITHUB_ID')
    GITHUB_SECRET = os.getenv('GITHUB_SECRET')

    if GITHUB_ID and GITHUB_SECRET:
        SOCIAL_AUTH_GITHUB = True


class ProductionConfig(Config):
    DEBUG = False

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

    # Use same SQLite DB
    SQLALCHEMY_DATABASE_URI = Config.SQLALCHEMY_DATABASE_URI


class DebugConfig(Config):
    DEBUG = True


# Load all possible configurations
config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig
}

