from distutils.debug import DEBUG


class Config(object):
    DEBUG = False
    TESTING = False

    SECRET_KEY = 'AKDFJAS;DF'

    DB_NAME = 'prod-db'
    DB_USERNAME = 'root'
    DB_PASSWORD = 'example'

    UPLOADING = '/home/username/app/'

    SESSION_COOKIE_SECURE = True


class ProductionConfig(Config):
    pass



class DevelopmentConfig(Config):
    DEBUG = True 

    DB_NAME = 'develop-db'
    DB_USERNAME = 'root'
    DB_PASSED = 'exampl'

    UPLAODS = '/home/username/projects'

    SESSION_COOKIE_SECURE = False

class TestingConfig(Config):
    TESTING = True

    DB_NAME = 'dev-db'
    DB_USERNAME = 'root'
    DB_PASSWORD = 'dfldf'

    SESSION_COOKIE_SECURE = False