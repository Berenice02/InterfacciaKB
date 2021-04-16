# Run a test server.
from app import app
from app import db

<<<<<<< HEAD
#app.run(host='0.0.0.0', port=8080, debug=True)
app.run()
=======
app.debug = True
db.create_all()
app.run(host='0.0.0.0', port=8080, debug=True)
>>>>>>> 6c72045c898d174287873ab8cf19a7c0b4703342
