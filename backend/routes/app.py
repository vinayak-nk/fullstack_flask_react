from flask import Blueprint

from services import RecipeResource

my_app = Blueprint('my_app', __name__)

my_app.route('/recipe', methods=['GET', 'POST'])(RecipeResource.get)
my_app.route('/recipe/<int:id>', methods=['GET'])(RecipeResource.get_by_id)


