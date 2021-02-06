# Run a test server.
from app import app
from flask import render_template

@app.route('/')
def main():
    return render_template("menu.html")

app.run(host='0.0.0.0', port=8080, debug=True)
