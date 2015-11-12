from sqlalchemy import Column, Integer, String
from sunpower.database import Base


class Distributor(Base):
    __tablename__ = "distributor"
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True)
    email = Column(String(120), unique=True)
    phone_number = Column(String(120), unique=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<Distributor %r>' % self.username