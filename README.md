# fullstack_flask_react

# python
flask flask_restx Flask-SQLAlchemy flask_jwt_extended 


steps
-------
mkdir backend
cd backend
py -m venv venv
flask flask_restx Flask-SQLAlchemy flask_jwt_extended
------------

1. config.py
2. pip install python-decouple
3. .env
4. exts.py
5. models.py
6. app.py

      from flask import Flask, request
      from flask_restx import Api, Resource, fields
      from config import DevConfig
      from models import Recipe
      from exts import db

      app = Flask(__name__)
      app.config.from_object(DevConfig)
      db.init_app(app)
      api = Api(app, doc='/docs')

      @api.route('/hello')
      class HellowResorce(Resource):
        def get(self):
          return {'msg': 'hellowwwwww'}

      @app.shell_context_processor
      def make_shell_context():
        return {
          'db': db,
          'Recipe': Recipe,
        }

      if __name__ == '__main__':
        app.run()


7. export FLASK_APP=main.py
8. flask shell
    db.create_all()

9. model serialiser
recipe_model = api.model(
  "Recipe",
    {
      'id': fields.Integer(),
      'title': fields.String(),
      'description': fields.String()
    }
)
10. creare routes

==========================================================
login

1. create User Model
2. pip install flask_migrate
3. app.py
  from flask_migrate import Migrate

  migrate=Migrate(app, db)
  flask shell

  flask db init --> generate migrations folder
  flask db migrate -m "added user table"
  flask db upgrade

=========================================================
JWT Authentication
=========================================================

1. pip install flask_jwt_extended
2. 
  @api.route('/signup')
  class Signup(Resource):
    def post(self):
      pass

  @api.route('/login')
  class Login(Resource):
    def post(self):
      pass
3. from models import User
4. sign up

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


  #model serializer
  signup_model = api.model(
    "signUp",
    {
      "username": fields.String(),
      "email": fields.String(),
      "password": fields.String()
    }
  )