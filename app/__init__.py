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
from app.mod_products.controllers import mod_process as process

# Register blueprint
app.register_blueprint(process)