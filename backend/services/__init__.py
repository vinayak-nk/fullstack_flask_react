from flask_restx import Api, Resource

class RecipeResource(Resource):
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
