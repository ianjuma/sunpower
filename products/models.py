from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from sunpower.database import Base


class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship('Category', backref=backref('category', lazy='dynamic'))

    type = Column(String(120), unique=False)

    def __init__(self, name, category):
        self.name = name
        self.category = category

    def __repr__(self):
        return '<Product %r>' % self.username


class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name