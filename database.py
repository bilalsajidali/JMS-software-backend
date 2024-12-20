# database.py
from flask_pymongo import PyMongo
from flask import current_app
from werkzeug.local import LocalProxy

mongo = PyMongo()

# Use LocalProxy to get db when it's actually needed
db = LocalProxy(lambda: mongo.db)

def init_db(app):
    mongo.init_app(app)