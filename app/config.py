class Config:
    pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    degug = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SQLALCHEMY_ECHO = True
