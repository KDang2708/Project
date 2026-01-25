from flask import Blueprint
from services.todo_service import TodoService

def create_todo_blueprint(todo_service: TodoService):
    bp = Blueprint('todo', __name__, url_prefix='/todos')

    @bp.route('/', methods=['GET'])
    def get_todos():
        return "OK"

    return bp