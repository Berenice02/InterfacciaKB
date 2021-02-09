# Import flask and template operators
from flask import Flask, render_template

# Define the application
app = Flask(__name__)

# Configurations
app.config.from_object('config')

#initial general page
@app.route('/')
def main():
    return render_template("index.html")

# Import the modules using their blueprint handler variable
from app.mod_process.controllers import mod_process as process
from app.mod_shopfloor.controllers import mod_shopfloor as sf
from app.mod_products.controllers import mod_products as products

# Register blueprint
app.register_blueprint(process)
app.register_blueprint(sf)
app.register_blueprint(products)