# Import flask dependencies
from flask import Blueprint, render_template

# Define the blueprint: 'shopfloor', set its url prefix: app.url/process
mod_shopfloor = Blueprint('sf', __name__, url_prefix='/sf')

@mod_shopfloor.route('/')
def hello():
    return render_template("shopfloor/index.html")

@mod_shopfloor.route('/new/')
def new():
    return render_template("shopfloor/new.html")

@mod_shopfloor.route('/mod/')
def mod():
    return render_template("shopfloor/mod.html")

@mod_shopfloor.route('/newAggr/')
def newAggr():
    return render_template("shopfloor/newAggr.html")

@mod_shopfloor.route('/modAggr/')
def modAggr():
    return render_template("shopfloor/modAggr.html")
