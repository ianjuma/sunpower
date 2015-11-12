from sunpower import api
from agents.views import AgentDetail, AgentList

api.add_resource(AgentDetail, '/agents/<string:todo_id>')
api.add_resource(AgentList, '/agents')