from flask import Flask, jsonify, request, render_template, Blueprint
import json, time
from methods import *

routes = Blueprint('routes', __name__)

# shows the calculator at flask default port
@routes.route('/')
def home():
    return render_template('calculator.html', title="home")

# shows the calculator at /calculator if preferred
@routes.route('/calculator')
def calculator():
    return render_template('calculator.html', title="calc")

# handles the json data from frontend
@routes.route('/data', methods=["POST"])
def calc_data():
    data = json.loads(request.data, strict=False)
    arr = data['arr']
    display_string = calc(arr)

    return json.dumps(display_string)

    