from flask import Blueprint

routes = Blueprint('routes', __name__)
@routes.route('/complex_task')
def complex_task():
    return 'This is the result of a computationally intensive task!'

@routes.route("/complex_task2")
def complex_task2():
    return 'This is the result of another computationally intensive task!'
