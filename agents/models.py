from sqlalchemy import Column, Integer, String
from sunpower.database import Base


class Agent(Base):
    __tablename__ = "agent"
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True)
    email = Column(String(120), unique=True)
    phone_number = Column(String(120), unique=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<Agent %r>' % self.username