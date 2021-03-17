# Run a test server.
from app import app
from app import db

app.debug = True
db.create_all()
app.run(host='0.0.0.0', port=8080, debug=True)
