from flask_restful import Resource


class ProductDetail(Resource):
    def get(self, _id):
        return {_id: "1"}, 200

    def put(self, _id):
        return {_id: "2"}, 200

    def delete(self, _id):
        return {self, _id}, 200


class ProductList(Resource):
    def get(self):
        return {}, 200

    def post(self):
        return {'task': 'Hello world'}, 201