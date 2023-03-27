from flask import Flask
from models import  db
from Controller import simple_page

# Initializing Flask
# Initialising db connection
# Registering Blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:1234@localhost/mock'
app.register_blueprint(simple_page)
db.init_app(app)






