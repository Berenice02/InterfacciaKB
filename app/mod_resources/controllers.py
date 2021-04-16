# Import flask dependencies
from flask import Blueprint, render_template, redirect, flash, url_for

from app import db

from app.mod_resources.forms import ResourceForm
from app.mod_resources.models import Resource

# Define the blueprint: 'resource', set its url prefix: app.url/resource
mod_resource = Blueprint('resource', __name__, url_prefix='/resource')

@mod_resource.route('/')
def hello():
    form = ResourceForm()
    return render_template("resource/indexRes.html", form = form)

@mod_resource.route('/', methods=("POST", ))
def add_res():
    form = ResourceForm()
    if form.validate_on_submit():
        resource = Resource()
        form.populate_obj(resource)
        db.session.add(resource)
        db.session.commit()
        flash("Added resource!")
        return redirect(url_for("indexRes"))
    return render_template("resource/indexRes.html", form = form)


@mod_resource.route('/newDem/')
def new():
    return render_template("resource/newDem.html")

@mod_resource.route('/modDem/')
def mod():
    return render_template("resource/modDem.html")
