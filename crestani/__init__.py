from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'c1444b3dc88d5bb19c4d917edb7d780d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crestani.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from crestani import routes