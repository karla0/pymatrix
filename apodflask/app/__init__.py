from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)

# this is where we define bootstrap enables
# bootstrap/base.html
bootstrap = Bootstrap(app)

from app import routes