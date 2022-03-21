from flask import Flask
from flask_restx import Api
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from models import Recipe, User
from exts import db
from auth import auth_ns
from services import recipe_ns
# from config import DevConfig
# from routes import init_app_route

def create_app(config):
  app = Flask(__name__)
  app.config.from_object(config)
  # init_app_route(app)

  db.init_app(app)
  migrate=Migrate(app, db)
  JWTManager(app)

  api = Api(app, doc='/docs')
  api.add_namespace(recipe_ns)
  api.add_namespace(auth_ns)
  
  @app.shell_context_processor
  def make_shell_context():
    return {
      'db': db,
      'Recipe': Recipe,
      'user': User,
    }

  return app

if __name__ == '__main__':
  app.run()
  # app.run(debug = False, host='0.0.0.0', port= '9090')
