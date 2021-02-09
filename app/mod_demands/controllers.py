# Import flask dependencies
from flask import Blueprint, render_template

# Define the blueprint: 'shopfloor', set its url prefix: app.url/process
mod_demands = Blueprint('demands', __name__, url_prefix='/demands')

@mod_demands.route('/')
def hello():
    return render_template("demands/indexDem.html")

@mod_demands.route('/newDem/')
def new():
    return render_template("demands/newDem.html")

@mod_demands.route('/modDem/')
def mod():
    return render_template("demands/modDem.html")
