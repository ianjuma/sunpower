from sunpower import api
from products.views import ProductDetail, ProductList

api.add_resource(ProductDetail, '/products/<string:_id>')
api.add_resource(ProductList, '/products')