from os import access
from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash

from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required, JWTManager

# from routes import init_app_route
from config import DevConfig
from models import Recipe, User
from exts import db

app = Flask(__name__)
app.config.from_object(DevConfig)
# init_app_route(app)

db.init_app(app)
migrate=Migrate(app, db)
JWTManager(app)

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

signup_model = api.model(
  "signUp",
  {
    "username": fields.String(),
    "email": fields.String(),
    "password": fields.String(),
    "date": fields.Date()
  }
)
@api.route('/hello')
class HellowResorce(Resource):
  def get(self):
    return {'msg': 'hellowwwwww'}
  
@api.route('/signup')
class Signup(Resource):
  # @api.marshal_with(signup_model)
  @api.expect(signup_model)
  def post(self):
    signup_data = request.get_json()
    username = signup_data.get('username')
    db_user = User.query.filter_by(username=username).first()
    
    if db_user is not None:
      return jsonify({'message': f'User with username {username} already exist'})
    
    
    new_user = User (
      username = username,
      email = signup_data.get('email'),
      password =  generate_password_hash(signup_data.get('password')),
    )
    new_user.save()
    
    # return new_user, 201
    return jsonify({ 'message': f'User {username} created Successfully' })

login_model = api.model(
  "Login", 
  {
    "username": fields.String(),
    "password": fields.String()    
  }
)

@api.route('/login')
class Login(Resource):
  @api.expect(login_model)
  def post(self):
    data= request.get_json()
    username = data.get('username')
    password =  data.get('password'),
    db_user = User.query.filter_by(username=username).first()
    # if db_user and check_password_hash(db_user.password, password):
    access_token = create_access_token(identity=db_user.username)
    refresh_token = create_refresh_token(identity=db_user.username)
      
    return jsonify({ 'access_token': access_token, 'refresh_token': refresh_token })
      
    


@api.route('/recipes')
class RecipeResource(Resource):
  @api.marshal_list_with(recipe_model)
  def get(self):
    """ get all recipes"""
    recipes = Recipe.query.all()
    return recipes

  @api.marshal_with(recipe_model)
  @api.expect(recipe_model)
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

@api.route('/recipe/<int:id>')
class RecipeResource(Resource):
  @api.marshal_with(recipe_model)
  @jwt_required()
  def get(self,id):
    """get recipe by id"""
    recipe_to_get = Recipe.query.get_or_404(id)
    return recipe_to_get

  @api.marshal_with(recipe_model)
  @jwt_required()
  def put(self,id):
    """set recipe by id"""
    recipe_to_update = Recipe.query.get_or_404(id)
    data = request.get_json()
    recipe_to_update.update(data.get('title'), data.get('description'))
    
    return recipe_to_update, 201

  @api.marshal_with(recipe_model)
  @jwt_required()
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
  # app.run(debug = False, host='0.0.0.0', port= '9090')
