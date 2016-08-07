from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os 
from config import basedir

app = Flask(__name__, static_url_path='', static_folder='static')
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models