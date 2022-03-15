from flask import Flask
from flask_restx import Api, Resource, fields

from routes import init_app_route
from config import DevConfig
from models import Recipe
from exts import db

app = Flask(__name__)
app.config.from_object(DevConfig)
init_app_route(app)

db.init_app(app)

api = Api(app, doc='/docs')

#model (serialiser)
recipe_model = api.model(
  "Recipe",
    {
      'id': fields.Integer(),
      'title': fields.String(),
      'description': fields.String()
    }
)


@api.route('/hello')
class HellowResorce(Resource):
  def get(self):
    return {'msg': 'hellowwwwww'}


# @api.route('/recipes')
# class RecipeResource(Resource):
#   def get(self):
#     """ get all recipes"""
#     pass



@app.shell_context_processor
def make_shell_context():
  return {
    'db': db,
    'Recipe': Recipe,
  }

if __name__ == '__main__':
  app.run()