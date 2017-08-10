import os
class DevelopmentConfig(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://ubuntu:thinkful@localhost:5432/draft"
    DEBUG = True
    
class TestingConfig(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://ubuntu:thinkful@localhost:5432/draft-test"
    DEBUG = False