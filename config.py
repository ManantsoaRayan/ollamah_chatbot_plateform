import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_recycle": 200,
        "pool_size": 10,
        "max_overflow": 20,
    }

class DevConfig(Config):
    DEBUG = True

class ProdConfig(Config):
    DEBUG = False