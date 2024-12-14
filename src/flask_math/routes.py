from flask import Blueprint

routes = Blueprint('routes', __name__)
@routes.route('/hello')
def hello():
    return 'Hello!'

@routes.route("/square/<number>")
def square(number):
    try:
        number = float(number)
    except ValueError:
        return f"Numbers are expected, you provided the following: {number}"
    return "{:g}".format(number ** 2)