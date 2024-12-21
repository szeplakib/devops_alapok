import requests
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
    return f"{number ** 2:g}"


@routes.route("/complex_task")
async def complex_task():
    data = requests.get(url = 'http://172.32.0.3:5000/complex_task')
    return data.text

@routes.route("/complex_task2")
async def complex_task2():
    data = requests.get(url = 'http://172.32.0.3:5000/complex_task2')
    return data.text