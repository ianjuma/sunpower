from sunpower import api
from distributors.views import DistributorDetail, DistributorList

api.add_resource(DistributorDetail, '/distributors/<string:_id>')
api.add_resource(DistributorList, '/distributors')
