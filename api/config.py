from datetime import timedelta
from decouple import config

class Config(object):
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
  JWT_COOKIE_SECURE = False
  JWT_TOKEN_LOCATION = ["cookies","headers"]
  JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)
  JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  CORS_HEADER = "Content-Type"

class DevelopmentConfig(Config):
  DEVELOPMENT = True
  DEBUG = True

class TestingConfig(Config):
  TESTING = True
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = "sqlite:///testdb.db"
  
class ProductionConfig(Config):
  DEBUG = False
  DEBUG_TB_ENABLED = False
  JWT_COOKIE_SECURE = True
