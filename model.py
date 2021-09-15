import db
from sqlalchemy import Column, Integer, String, Float

class Product(db.Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    price = Column(Float)

    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __repr__(self):
        return f'Product({self.name}, {self.price})'
    
    def __str__(self):
        return self.name