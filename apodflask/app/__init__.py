from flask import Flask
from flask_bootstrap import Bootstrap
from flask_fontawesome import FontAwesome

app = Flask(__name__)

# this is where we define bootstrap enables
# bootstrap/base.html
bootstrap = Bootstrap(app)
fa = FontAwesome(app)

from app import routes