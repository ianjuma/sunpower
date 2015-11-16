from flask import Flask
import logging
import settings
from flask.ext.sqlalchemy import SQLAlchemy
from flask_restful import Api

from sunpower.views import Index
from sunpower.database import db_session

app = Flask('app')
api = Api(app)

app.config.from_pyfile('settings.py', silent=True)

db = SQLAlchemy(app)
db.init_app(app)

from sunpower import urls
from agents import urls
from distributors import urls
from products import urls
"""
api.add_resource(DistributorDetail, '/distributors/<string:_id>')
api.add_resource(DistributorList, '/distributors')

api.add_resource(ProductDetail, '/products/<string:_id>')
api.add_resource(ProductList, '/products')
api.add_resource(Index, '/')
"""

logging.basicConfig(filename='SunPower.log', level=logging.DEBUG)