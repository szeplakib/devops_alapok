from flask import Blueprint

routes = Blueprint('routes', __name__)
@routes.route('/complex')
def complex():
    return 'This is the result of a computationally intensive task!'

@routes.route("/complex2")
def complex2():
    return 'This is the result of another computationally intensive task!'
