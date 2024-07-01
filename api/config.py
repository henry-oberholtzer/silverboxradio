from decouple import config

class Config(object):
  PROPAGATE_EXCEPTIONS = True
  API_TITLE = "Silver Box Radio"
  API_VERSION = "v1"
  OPENAPI_VERSION = "3.0.3"
  OPENAPI_URL_PREFIX = "/"
  OPENAPI_SWAGGER_UI_PATH = "/swagger-ui"
  OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
  DEBUG = False
  TESTING = False
  CSRF_ENABLED = True
  SQLALCHEMY_DATABASE_URI = config("DATABASE_URL")
  JWT_SECRET_KEY = config("SECRET_KEY")
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  CORS_HEADER = "Content-Type"

class DevelopmentConfig(object):
  DEVELOPMENT = True
  DEBUG = True

class TestingConfig(Config):
  TESTING = True
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = "sqlite:///testdb.db"
  BCRYPT_LOG_ROUNDS = 1
  WTF_CSRF_ENABLED = False

class ProductionConfig(Config):
  DEBUG = False
  DEBUG_TB_ENABLED = False
