#------------------------------------------------------------------------------
# From: https://www.airpair.com/python/posts/django-flask-pyramid
#  In this approach, you create bind the instance specifically to the Flask
#  application called "app"
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
# We'll just use SQLite here so we don't need an external database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


#------------------------------------------------------------------------------
# From Purna's repo
#   In this approach, you create the object once and the configure the app
#   to use it via db.init_app(app)
# Note: methods like create_all() and drop_all() will one work if
#   flask.Flask.app_context() exists; they work all the time for method above

# database.py
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# app.py
from flask import Flask
from database import db
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["SQLALCHEMY_DATABASE_URI"]
db.init_app(app)