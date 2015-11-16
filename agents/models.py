from sqlalchemy import Column, Integer, String, Sequence
# from sqlalchemy.schema import CreateSequence
from sunpower.database import Base

# Base.execute(CreateSequence(Sequence('agent_id_sequence')))


class Agent(Base):
    __tablename__ = 'agent'
    id = Column(Integer, Sequence('agent_id_sequence'), primary_key=True)
    username = Column(String(80), unique=True)
    email = Column(String(120), unique=True)
    phone_number = Column(String(120), unique=True)

    def __init__(self, username, email, phone_number):
        self.username = username
        self.email = email
        self.phone_number = phone_number

    def __repr__(self):
        return '<Agent %r>' % self.username