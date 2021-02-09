# Import flask dependencies
from flask import Blueprint, render_template

#from InterfacciaKB.app.mod_shopfloor.models import Resource, AggregateResource

#lista di risorse
risorse = []
#lista di risorse aggregate
aggregate = []

# Define the blueprint: 'shopfloor', set its url prefix: app.url/process
mod_shopfloor = Blueprint('sf', __name__, url_prefix='/sf')

@mod_shopfloor.route('/')
def hello():
    return render_template("shopfloor/indexSF.html")

@mod_shopfloor.route('/newRes/')
def new():
    return render_template("shopfloor/newRes.html")

@mod_shopfloor.route('/modRes/')
def mod():
    return render_template("shopfloor/modRes.html")

@mod_shopfloor.route('/newAggr/')
def newAggr():
    return render_template("shopfloor/newAggr.html")

@mod_shopfloor.route('/modAggr/')
def modAggr():
    return render_template("shopfloor/modAggr.html")
