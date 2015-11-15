from flask_restful import Resource, reqparse
from flask import jsonify
from sunpower import db
from agents.models import Agent
parser = reqparse.RequestParser()


class AgentDetail(Resource):
    @staticmethod
    def get(_id):
        agent = Agent.query.filter_by(id=_id).first()

        if agent is None:
            return jsonify({})
        else:
            return jsonify(agent)

    @staticmethod
    def put(_id):
        data = parser.parse_args()
        agent = Agent.query.filter_by(id=_id).first()
        if agent is not None:
            agent.email = data.get('email', None)
            agent.phone_number = data.get('phone_number', None)
            agent.username = data.get('username', None)

            db.commit()

        return jsonify(agent)

    @staticmethod
    def delete(_id):
        Agent.query.filter_by(id=_id).delete()
        return jsonify({'OK': 'Deleted'})


class AgentList(Resource):
    @staticmethod
    def get():
        agents = Agent.query.filter_by().all()
        return jsonify(agents)

    @staticmethod
    def post():
        data = parser.parse_args()
        agent = Agent(email=data.email, username=data.username, phone_number=data.phone_nubmer)
        with agent:
            db.session.add(agent)
            db.commit()

        return jsonify(agent)