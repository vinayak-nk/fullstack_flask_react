from flask import Flask, request
from flask_restx import Api, Resource, fields

# from routes import init_app_route
from config import DevConfig
from models import Recipe
from exts import db

app = Flask(__name__)
app.config.from_object(DevConfig)
# init_app_route(app)

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

@api.route('/recipes')
class RecipeResource(Resource):
  @api.marshal_list_with(recipe_model)
  def get(self):
    """ get all recipes"""
    recipes = Recipe.query.all()
    return recipes

  @api.marshal_with(recipe_model)
  def post(self):
    """ post a recipe"""
    data = request.get_json()
    new_recipe = Recipe(
      title=data.get('title'),
      description=data.get('description')
    )
    
    new_recipe.save()
    
    return new_recipe, 201

@api.route('/recipe/<int:id>')
class RecipeResource(Resource):
  @api.marshal_with(recipe_model)
  def get(self,id):
    """get recipe by id"""
    recipe_to_get = Recipe.query.get_or_404(id)
    return recipe_to_get

  @api.marshal_with(recipe_model)
  def put(self,id):
    """set recipe by id"""
    recipe_to_update = Recipe.query.get_or_404(id)
    data = request.get_json()
    recipe_to_update.update(data.get('title'), data.get('description'))
    
    return recipe_to_update, 201

  @api.marshal_with(recipe_model)
  def delete(self,id):
    """set recipe by id"""
    recipe_to_delete = Recipe.query.get_or_404(id)
    recipe_to_delete.delete()
    return recipe_to_delete



@app.shell_context_processor
def make_shell_context():
  return {
    'db': db,
    'Recipe': Recipe,
  }

if __name__ == '__main__':
  app.run()