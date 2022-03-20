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

