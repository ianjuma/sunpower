from flask import Flask
import logging
import settings
from flask.ext.sqlalchemy import SQLAlchemy
from flask_restful import Api

# from agents.views import AgentDetail, AgentList
from distributors.views import DistributorDetail, DistributorList
from products.views import ProductDetail, ProductList
from sunpower.views import Index

app = Flask('app')
api = Api(app)

app.config.from_pyfile('settings.py', silent=True)

db = SQLAlchemy(app)
db.init_app(app)

# 3 methods - pick one
# from agents import urls
# vs
from sunpower import urls
# vs
# urls
# api.add_resource(AgentDetail, '/agents/<string:_id>')
# api.add_resource(AgentList, '/agents')

api.add_resource(DistributorDetail, '/distributors/<string:_id>')
api.add_resource(DistributorList, '/distributors')

api.add_resource(ProductDetail, '/products/<string:_id>')
api.add_resource(ProductList, '/products')
api.add_resource(Index, '/')

logging.basicConfig(filename='SunPower.log', level=logging.DEBUG)