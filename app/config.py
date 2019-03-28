class Config:
    pass


class ProdConfig(Config):
    SECRET_KEY = '\xa8\xcc\xeaP+\xb3\xe8|\xad\xdb\xea\xd0\xd4\xe8\xac\xee\xfaW\x072@O3'


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SQLALCHEMY_ECHO = True
    SECRET_KEY = '\xa8\xcc\xeaP+\xb3\xe8|\xad\xdb\xea\xd0\xd4\xe8\xac\xee\xfaW\x072@O3'
