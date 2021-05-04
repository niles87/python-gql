import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


class Config(object):
    TESTING = False


class Development(Config):
    ENV = os.getenv("ENV")
    DEVELOPMENT = True
    SECRET_KEY = os.getenv("DEV_SECRET")
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
    MONGO_URI = os.getenv("DB_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
