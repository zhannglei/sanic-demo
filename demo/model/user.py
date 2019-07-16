from .util import Base
from sqlalchemy import Column, Integer, String
from flask_restful import fields


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))


user_fields = {
    'name': fields.String
}
