from flask import Blueprint

from services import RecipeResource

my_app = Blueprint('my_app', __name__)

my_app.route('/blog', methods=['GET', 'POST'])(RecipeResource.get)
my_app.route('/blog/<int:id>', methods=['GET'])(RecipeResource.get_by_id)


