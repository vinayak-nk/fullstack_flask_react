from flask_restx import Namespace, Resource, Api, fields
# from os import access
from flask import request
# from flask_migrate import Migrate
from flask_jwt_extended import jwt_required, JWTManager

from models import Blog


blog_ns = Namespace('api', description="A namespace for Blogs Model")

#model (serialiser)
recipe_model = blog_ns.model(
  "Blog",
    {
      'id': fields.Integer(),
      'title': fields.String(),
      'description': fields.String()
    }
)

@blog_ns.route('/hello')
class HellowResorce(Resource):
  def get(self):
    return {'msg': 'hellowwwwww'}   

@blog_ns.route('/blogs')
class BlogResource(Resource):
  @blog_ns.marshal_list_with(recipe_model)
  def get(self):
    """ get all blogs"""
    blogs = Blog.query.all()
    return blogs

  @blog_ns.marshal_with(recipe_model)
  @blog_ns.expect(recipe_model)
  @jwt_required()
  def post(self):
    """ post a blog"""
    data = request.get_json()
    new_recipe = Blog(
      title=data.get('title'),
      description=data.get('description')
    )
    
    new_recipe.save()
    
    return new_recipe, 201

@blog_ns.route('/blog/<int:id>')
class BlogResource(Resource):
  @blog_ns.marshal_with(recipe_model)
  @jwt_required()
  def get(self,id):
    """get blog by id"""
    recipe_to_get = Blog.query.get_or_404(id)
    return recipe_to_get

  @blog_ns.marshal_with(recipe_model)
  @jwt_required()
  def put(self,id):
    """set blog by id"""
    recipe_to_update = Blog.query.get_or_404(id)
    data = request.get_json()
    recipe_to_update.update(data.get('title'), data.get('description'))
    
    return recipe_to_update, 201

  @blog_ns.marshal_with(recipe_model)
  @jwt_required()
  def delete(self,id):
    """set blog by id"""
    recipe_to_delete = Blog.query.get_or_404(id)
    recipe_to_delete.delete()
    return recipe_to_delete




# from flask_restx import Api, Resource
# from app import blog_ns
# from flask_restx import Resource, fields

# #model (serialiser)
# recipe_model = blog_ns.model(
#   "Blog",
#     {
#       'id': fields.Integer(),
#       'title': fields.String(),
#       'description': fields.String()
#     }
# )

# class BlogResource(Resource):
#   @blog_ns.marshal_list_with(recipe_model)
#   def get(self):
#     """ get all blogs"""
#     return 'hello'

#   def post(self):
#     """ get all blogs"""
#     pass
  
#   def get_by_id(self,id):
#     """get blog by id"""
#     pass

#   def put_by_id(self,id):
#     """set blog by id"""
#     pass

#   def delete_by_id(self,id):
#     """set blog by id"""
#     pass
