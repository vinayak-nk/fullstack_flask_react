from flask import request, jsonify, make_response
from flask_restx import Resource, Namespace, fields
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required, JWTManager

from models import User

auth_ns = Namespace('auth', description="A namespace for Authentication")


signup_model = auth_ns.model(
  "signUp",
  {
    "username": fields.String(),
    "email": fields.String(),
    "password": fields.String(),
    "date": fields.Date()
  }
)

login_model = auth_ns.model(
  "Login", 
  {
    "username": fields.String(),
    "password": fields.String()    
  }
)

@auth_ns.route('/signup')
class Signup(Resource):
  @auth_ns.expect(signup_model)
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
    return make_response(jsonify({ 'message': f'User {username} created Successfully' }), 201)


@auth_ns.route('/login')
class Login(Resource):
  @auth_ns.expect(login_model)
  def post(self):
    data= request.get_json()
    username = data.get('username')
    password =  data.get('password'),
    db_user = User.query.filter_by(username=username).first()
    # if db_user and check_password_hash(db_user.password, password):
    access_token = create_access_token(identity=db_user.username)
    refresh_token = create_refresh_token(identity=db_user.username)
      
    return jsonify({ 'access_token': access_token, 'refresh_token': refresh_token })
      
