# Import flask dependencies
from flask import Blueprint, render_template

from app.mod_products.models import Task, Function, Constraint

#costanti
IND = "Independent"
SYN = "Synchronous"
SIM = "Simultaneous"
SUPP = "Supportive"

#lista di task
lista = []
#lista di vincoli di precedenza sui task
vincoli = []

# Define the blueprint: 'process', set its url prefix: app.url/process
mod_process = Blueprint('process', __name__, url_prefix='/process')

@mod_process.route('/')
def hello():
    return render_template("process/process.html", lista=lista)

