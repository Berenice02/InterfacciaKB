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