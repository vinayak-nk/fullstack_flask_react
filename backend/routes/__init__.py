from .app import my_app

def init_app_route(app):
  app.register_blueprint(my_app)
