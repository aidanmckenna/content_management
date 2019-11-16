

import os


class Config:
    TESTING = os.environ.get('TESTING')
    DEBUG = os.environ.get('DEBUG')

class ProdConfig(Config):
    TESTING = False
    DEBUG = False
    DB_URL = os.environ.get('PROD_RTDB_URL')
    STORAGE_URL = os.environ.get('PROD_CLOUDSTORAGE_URL')

class TestConfig(Config):
    TESTING = True
    DEBUG = False
    DB_URL = os.environ.get('DEV_RTDB_URL')
    STORAGE_URL = os.environ.get('DEV_CLOUDSTORAGE_URL')


class DebugConfig(Config):
    TESTING = True
    DEBUG = True
    DB_URL = os.environ.get('DEV_RTDB_URL')
    STORAGE_URL = os.environ.get('DEV_CLOUDSTORAGE_URL')
