from flask_restx import Api, Resource
from app import api
from flask_restx import Resource, fields

#model (serialiser)
recipe_model = api.model(
  "Recipe",
    {
      'id': fields.Integer(),
      'title': fields.String(),
      'description': fields.String()
    }
)

class RecipeResource(Resource):
  @api.marshal_list_with(recipe_model)
  def get(self):
    """ get all recipes"""
    return 'hello'

  def post(self):
    """ get all recipes"""
    pass
  
  def get_by_id(self,id):
    """get recipe by id"""
    pass

  def put_by_id(self,id):
    """set recipe by id"""
    pass

  def delete_by_id(self,id):
    """set recipe by id"""
    pass
