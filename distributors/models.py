from sqlalchemy import Column, Integer, String, Sequence
from sunpower.database import Base


class Distributor(Base):
    __tablename__ = "distributor"
    id = Column(Integer, Sequence('distributor_id_sequence'), primary_key=True)
    username = Column(String(80), unique=True)
    email = Column(String(120), unique=True)
    phone_number = Column(String(120), unique=False)

    def __init__(self, username, email, phone_number):
        self.username = username
        self.email = email
        self.phone_number = phone_number

    def __repr__(self):
        return '<Distributor %r>' % self.username