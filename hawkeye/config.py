class Config(object):
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    DEBUG = False
    MYSQL_DATABASE_USER = 'root'
    MYSQL_DATABASE_PASSWORD = ''# Put your MySQL root password here
    MYSQL_DATABASE_DB = 'HawkeyeWithData'
    MYSQL_DATABASE_HOST = 'localhost'
    
class DevelopmentConfig(Config):
    DEBUG = True
    TEMPLATES_AUTO_RELOAD=True
    MYSQL_DATABASE_USER = 'root'
    MYSQL_DATABASE_PASSWORD = ''# Put your MySQL root password here
    MYSQL_DATABASE_DB = 'HawkeyeWithData'
    MYSQL_DATABASE_HOST = 'localhost'
    CACHE_TYPE = "null"

class TestingConfig(Config):
    TESTING = True
