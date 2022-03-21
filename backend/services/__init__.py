from flask_restx import Namespace, Resource, Api, fields
# from os import access
from flask import request
# from flask_migrate import Migrate
from flask_jwt_extended import jwt_required, JWTManager

from models import Recipe


recipe_ns = Namespace('api', description="A namespace for Recipes Model")

#model (serialiser)
recipe_model = recipe_ns.model(
  "Recipe",
    {
      'id': fields.Integer(),
      'title': fields.String(),
      'description': fields.String()
    }
)

@recipe_ns.route('/hello')
class HellowResorce(Resource):
  def get(self):
    return {'msg': 'hellowwwwww'}   

@recipe_ns.route('/recipes')
class RecipeResource(Resource):
  @recipe_ns.marshal_list_with(recipe_model)
  def get(self):
    """ get all recipes"""
    recipes = Recipe.query.all()
    return recipes

  @recipe_ns.marshal_with(recipe_model)
  @recipe_ns.expect(recipe_model)
  @jwt_required()
  def post(self):
    """ post a recipe"""
    data = request.get_json()
    new_recipe = Recipe(
      title=data.get('title'),
      description=data.get('description')
    )
    
    new_recipe.save()
    
    return new_recipe, 201

@recipe_ns.route('/recipe/<int:id>')
class RecipeResource(Resource):
  @recipe_ns.marshal_with(recipe_model)
  @jwt_required()
  def get(self,id):
    """get recipe by id"""
    recipe_to_get = Recipe.query.get_or_404(id)
    return recipe_to_get

  @recipe_ns.marshal_with(recipe_model)
  @jwt_required()
  def put(self,id):
    """set recipe by id"""
    recipe_to_update = Recipe.query.get_or_404(id)
    data = request.get_json()
    recipe_to_update.update(data.get('title'), data.get('description'))
    
    return recipe_to_update, 201

  @recipe_ns.marshal_with(recipe_model)
  @jwt_required()
  def delete(self,id):
    """set recipe by id"""
    recipe_to_delete = Recipe.query.get_or_404(id)
    recipe_to_delete.delete()
    return recipe_to_delete




# from flask_restx import Api, Resource
# from app import recipe_ns
# from flask_restx import Resource, fields

# #model (serialiser)
# recipe_model = recipe_ns.model(
#   "Recipe",
#     {
#       'id': fields.Integer(),
#       'title': fields.String(),
#       'description': fields.String()
#     }
# )

# class RecipeResource(Resource):
#   @recipe_ns.marshal_list_with(recipe_model)
#   def get(self):
#     """ get all recipes"""
#     return 'hello'

#   def post(self):
#     """ get all recipes"""
#     pass
  
#   def get_by_id(self,id):
#     """get recipe by id"""
#     pass

#   def put_by_id(self,id):
#     """set recipe by id"""
#     pass

#   def delete_by_id(self,id):
#     """set recipe by id"""
#     pass
